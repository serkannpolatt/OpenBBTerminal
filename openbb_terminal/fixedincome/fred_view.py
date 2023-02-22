""" FRED view """
__docformat__ = "numpy"

import logging
import os
import pathlib
from itertools import cycle
from typing import List, Optional

import pandas as pd
from matplotlib import pyplot as plt

from openbb_terminal.config_plot import PLOT_DPI
from openbb_terminal.config_terminal import theme
from openbb_terminal.decorators import check_api_key, log_start_end
from openbb_terminal.fixedincome import fred_model
from openbb_terminal.helper_funcs import (
    export_data,
    is_valid_axes_count,
    plot_autoscale,
    print_rich_table,
)
from openbb_terminal.rich_config import console

logger = logging.getLogger(__name__)

# pylint: disable=too-many-lines

ice_bofa_path = pathlib.Path(__file__).parent / "ice_bofa_indices.xlsx"
commercial_paper_path = pathlib.Path(__file__).parent / "commercial_paper.xlsx"
spot_rates_path = pathlib.Path(__file__).parent / "corporate_spot_rates.xlsx"

ID_TO_NAME_ESTR = {
    "ECBESTRVOLWGTTRMDMNRT": "Euro Short-Term Rate: Volume-Weighted Trimmed Mean Rate",
    "ECBESTRTOTVOL": "Euro Short-Term Rate: Total Volume",
    "ECBESTRNUMTRANS": "Euro Short-Term Rate: Number of Transactions",
    "ECBESTRRT75THPCTVOL": "Euro Short-Term Rate: Rate at 75th Percentile of Volume",
    "ECBESTRNUMACTBANKS": "Euro Short-Term Rate: Number of Active Banks",
    "ECBESTRSHRVOL5LRGACTBNK": "Euro Short-Term Rate: Share of Volume of the 5 Largest Active Bank",
    "ECBESTRRT25THPCTVOL": "Euro Short-Term Rate: Rate at 25th Percentile of Volume",
}
ID_TO_NAME_SOFR = {
    "SOFR": "Secured Overnight Financing Rate (SOFR)",
    "SOFR30DAYAVG": "30-Day Average SOFR",
    "SOFR90DAYAVG": "90-Day Average SOFR",
    "SOFR180DAYAVG": "180-Day Average SOFR",
    "SOFRINDEX": "SOFR Index",
}
ID_TO_NAME_SONIA = {
    "IUDSOIA": "Daily Sterling Overnight Index Average (SONIA) Rate",
    "IUDZOS2": "SONIA Compounded Index",
    "IUDZLS6": "SONIA Rate: 10th percentile",
    "IUDZLS7": "SONIA Rate: 25th percentile",
    "IUDZLS8": "SONIA Rate: 75th percentile",
    "IUDZLS9": "SONIA Rate: 90th percentile",
    "IUDZLT2": "SONIA Rate Total Nominal Value",
}
ID_TO_NAME_AMERIBOR = {
    "AMERIBOR": "Overnight Unsecured AMERIBOR Benchmark Interest Rate",
    "AMBOR30T": "AMERIBOR Term-30 Derived Interest Rate Index",
    "AMBOR90T": "AMERIBOR Term-90 Derived Interest Rate Index",
    "AMBOR1W": "1-Week AMERIBOR Term Structure of Interest Rates",
    "AMBOR1M": "1-Month AMERIBOR Term Structure of Interest Rates",
    "AMBOR3M": "3-Month AMERIBOR Term Structure of Interest Rates",
    "AMBOR6M": "6-Month AMERIBOR Term Structure of Interest Rates",
    "AMBOR1Y": "1-Year AMERIBOR Term Structure of Interest Rates",
    "AMBOR2Y": "2-Year AMERIBOR Term Structure of Interest Rates",
    "AMBOR30": "30-Day Moving Average AMERIBOR Benchmark Interest Rate",
    "AMBOR90": "90-Day Moving Average AMERIBOR Benchmark Interest Rate",
}
ID_TO_NAME_FED = {
    "FEDFUNDS": "Monthly Effective Federal Funds Rate",
    "EFFR": "Daily Effective Federal Funds Rate",
    "DFF": "Daily Effective Federal Funds Rate",
    "OBFR": "Daily Overnight Bank Funding Rate",
    "FF": "Weekly Effective Federal Funds Rate",
    "RIFSPFFNB": "Daily (Excl. Weekends) Effective Federal Funds Rate",
    "RIFSPFFNA": "Annual Effective Federal Funds Rate",
    "RIFSPFFNBWAW": "Biweekly Effective Federal Funds Rate",
    "EFFRVOL": "Effective Federal Funds Volume",
    "OBFRVOL": "Overnight Bank Funding Volume",
}

ID_TO_NAME_DWPCR = {
    "MPCREDIT": "Monthly",
    "RIFSRPF02ND": "Daily (incl. Weekends)",
    "WPCREDIT": "Weekly",
    "DPCREDIT": "Daily (excl. Weekends)",
    "RIFSRPF02NA": "Annual",
}
ID_TO_NAME_TMC = {
    "T10Y3M": "3-Month",
    "T10Y2Y": "2-Year",
}
ID_TO_NAME_FFRMC = {
    "T10YFF": "10-Year",
    "T5YFF": "5-Year",
    "T1YFF": "1-Year",
    "T6MFF": "6-Month",
    "T3MFF": "3-Month",
}
ID_TO_NAME_SECONDARY = {
    "TB3MS": "3-Month",
    "DTB4WK": "4-Week",
    "DTB1YR": "1-Year",
    "DTB6": "6-Month",
}
ID_TO_NAME_TIPS = {
    "DFII5": "5-Year",
    "DFII7": "7-Year",
    "DFII10": "10-Year",
    "DFII20": "20-Year",
    "DFII30": "30-Year",
}
ID_TO_NAME_CMN = {
    "DGS1MO": "1 Month",
    "DGS3MO": "3 Month",
    "DGS6MO": "6 Month",
    "DGS1": "1 Year",
    "DGS2": "2 Year",
    "DGS3": "3 Year",
    "DGS5": "5 Year",
    "DGS7": "7 Year",
    "DGS10": "10 Year",
    "DGS20": "20 Year",
    "DGS30": "30 Year",
}
ID_TO_NAME_TBFFR = {
    "TB3SMFFM": "3 Month",
    "TB6SMFFM": "6 Month",
}

NAME_TO_ID_PROJECTION = {
    "Range High": ["FEDTARRH", "FEDTARRHLR"],
    "Central tendency High": ["FEDTARCTH", "FEDTARCTHLR"],
    "Median": ["FEDTARMD", "FEDTARMDLR"],
    "Range Midpoint": ["FEDTARRM", "FEDTARRMLR"],
    "Central tendency Midpoint": ["FEDTARCTM", "FEDTARCTMLR"],
    "Range Low": ["FEDTARRL", "FEDTARRLLR"],
    "Central tendency Low": ["FEDTARCTL", "FEDTARCTLLR"],
}

NAME_TO_ID_ECB = {"deposit": "ECBDFR", "lending": "ECBMLFR", "refinancing": "ECBMRRFR"}

USARATES_TO_FRED_ID = {
    "4_week": {"tbill": "DTB4WK"},
    "1_month": {"cmn": "DGS1MO"},
    "3_month": {"tbill": "TB3MS", "cmn": "DGS3MO"},
    "6_month": {"tbill": "DTB6", "cmn": "DGS6MO"},
    "1_year": {"tbill": "DTB1YR", "cmn": "DGS1"},
    "2_year": {"cmn": "DGS2"},
    "3_year": {"cmn": "DGS3"},
    "5_year": {"tips": "DFII5", "cmn": "DGS5"},
    "7_year": {"tips": "DFII7", "cmn": "DGS7"},
    "10_year": {"tips": "DFII10", "cmn": "DGS10"},
    "20_year": {"tips": "DFII20", "cmn": "DGS20"},
    "30_year": {"tips": "DFII30", "cmn": "DGS30"},
}

ICE_BOFA_TO_OPTIONS = {
    "Type": ["total_return", "yield", "yield_to_worst"],
    "Category": ["all", "duration", "eur", "usd"],
    "Area": ["asia", "emea", "eu", "ex_g10", "latin_america", "us"],
    "Grade": [
        "a",
        "aa",
        "aaa",
        "b",
        "bb",
        "bbb",
        "ccc",
        "crossover",
        "high_grade",
        "high_yield",
        "non_financial",
        "non_sovereign",
        "private_sector",
        "public_sector",
    ],
}

MOODY_TO_OPTIONS = {
    "Type": {
        "aaa": {
            "index": {
                "id": "DAAA",
                "name": "Moody's Seasoned Aaa Corporate Bond Yield",
            },
            "treasury": {
                "id": "AAA10Y",
                "name": "Moody's Seasoned Aaa Corporate Bond Yield Relative to Yield "
                "on 10-Year Treasury Constant Maturity",
            },
            "fed_funds": {
                "id": "AAAFF",
                "name": "Moody's Seasoned Aaa Corporate Bond Minus Federal Funds Rate",
            },
        },
        "baa": {
            "index": {
                "id": "DBAA",
                "name": "Moody's Seasoned Baa Corporate Bond Yield",
            },
            "treasury": {
                "id": "BAA10Y",
                "name": "Moody's Seasoned Baa Corporate Bond Yield Relative "
                "to Yield on 10-Year Treasury Constant Maturity",
            },
            "fed_funds": {
                "id": "BAAFF",
                "name": "Moody's Seasoned Baa Corporate Bond Minus Federal Funds Rate",
            },
        },
    },
    "Spread": ["treasury", "fed_funds"],
}

CP_TO_OPTIONS = {
    "Maturity": ["15d", "30d", "60d", "7d", "90d", "overnight"],
    "Category": ["asset_backed", "financial", "non_financial", "spread"],
    "Grade": ["a2_p2", "aa"],
}

SPOT_TO_OPTIONS = {
    "Maturity": [
        "1y",
        "1.5y",
        "2y",
        "2.5y",
        "3y",
        "3.5y",
        "4y",
        "4.5y",
        "5y",
        "5.5y",
        "6 y",
        "6y",
        "6.5y",
        "7y",
        "7.5y",
        "8y",
        "8.5y",
        "9y",
        "9.5y",
        "10y",
        "10.5y",
        "11y",
        "11.5y",
        "12y",
        "12.5y",
        "13y",
        "13.5y",
        "14y",
        "14.5y",
        "15y",
        "15.5y",
        "16y",
        "16.5y",
        "17y",
        "17.5y",
        "18y",
        "18.5y",
        "19y",
        "19.5y",
        "20y",
        "20.5y",
        "21y",
        "21.5y",
        "22y",
        "22.5y",
        "23y",
        "23.5y",
        "24y",
        "24.5y",
        "25y",
        "25.5y",
        "26y",
        "26.5y",
        "27y",
        "27.5y",
        "28y",
        "28.5y",
        "29y",
        "29.5y",
        "30y",
        "30.5y",
        "31y",
        "31.5y",
        "32y",
        "32.5y",
        "33y",
        "33.5y",
        "34y",
        "34.5y",
        "35y",
        "35.5y",
        "36y",
        "36.5y",
        "37y",
        "37.5y",
        "38y",
        "38.5y",
        "39y",
        "39.5y",
        "40y",
        "40.5y",
        "41y",
        "41.5y",
        "42y",
        "42.5y",
        "43y",
        "43.5y",
        "44y",
        "44.5y",
        "45y",
        "45.5y",
        "46y",
        "46.5y",
        "47y",
        "47.5y",
        "48y",
        "48.5y",
        "49y",
        "49.5y",
        "50y",
        "50.5y",
        "51y",
        "51.5y",
        "52y",
        "52.5y",
        "53y",
        "53.5y",
        "54y",
        "54.5y",
        "55y",
        "55.5y",
        "56y",
        "56.5y",
        "57y",
        "57.5y",
        "58y",
        "58.5y",
        "59y",
        "59.5y",
        "60y",
        "60.5y",
        "61y",
        "61.5y",
        "62y",
        "62.5y",
        "63y",
        "63.5y",
        "64y",
        "64.5y",
        "65y",
        "65.5y",
        "66y",
        "66.5y",
        "67y",
        "67.5y",
        "68y",
        "68.5y",
        "69y",
        "69.5y",
        "70y",
        "70.5y",
        "71y",
        "71.5y",
        "72y",
        "72.5y",
        "73y",
        "73.5y",
        "74y",
        "74.5y",
        "75y",
        "75.5y",
        "76y",
        "76.5y",
        "77y",
        "77.5y",
        "78y",
        "78.5y",
        "79y",
        "79.5y",
        "80y",
        "80.5y",
        "81y",
        "81.5y",
        "82y",
        "82.5y",
        "83y",
        "83.5y",
        "84y",
        "84.5y",
        "85y",
        "85.5y",
        "86y",
        "86.5y",
        "87y",
        "87.5y",
        "88y",
        "88.5y",
        "89y",
        "89.5y",
        "90y",
        "90.5y",
        "91y",
        "91.5y",
        "92y",
        "92.5y",
        "93y",
        "93.5y",
        "94y",
        "94.5y",
        "95y",
        "95.5y",
        "96y",
        "96.5y",
        "97y",
        "97.5y",
        "98y",
        "98.5y",
        "99y",
        "99.5y",
        "100y",
    ],
    "Category": ["spot_rate", "par_yield"],
}

ESTR_PARAMETER_TO_ECB_ID = {
    "volume_weighted_trimmed_mean_rate": "ECBESTRVOLWGTTRMDMNRT",
    "number_of_transactions": "ECBESTRNUMTRANS",
    "number_of_active_banks": "ECBESTRNUMACTBANKS",
    "total_volume": "ECBESTRTOTVOL",
    "share_of_volume_of_the_5_largest_active_banks": "ECBESTRSHRVOL5LRGACTBNK",
    "rate_at_75th_percentile_of_volume": "ECBESTRRT75THPCTVOL",
    "rate_at_25th_percentile_of_volume": "ECBESTRRT25THPCTVOL",
}

SOFR_PARAMETER_TO_FRED_ID = {
    "overnight": "SOFR",
    "30_day_average": "SOFR30DAYAVG",
    "90_day_average": "SOFR90DAYAVG",
    "180_day_average": "SOFR180DAYAVG",
    "index": "SOFRINDEX",
}
SONIA_PARAMETER_TO_FRED_ID = {
    "rate": "IUDSOIA",
    "index": "IUDZOS2",
    "10th_percentile": "IUDZLS6",
    "25th_percentile": "IUDZLS7",
    "75th_percentile": "IUDZLS8",
    "90th_percentile": "IUDZLS9",
    "total_nominal_value": "IUDZLT2",
}
AMERIBOR_PARAMETER_TO_FRED_ID = {
    "overnight": "AMERIBOR",
    "term_30": "AMBOR30T",
    "term_90": "AMBOR90T",
    "1_week_term_structure": "AMBOR1W",
    "1_month_term_structure": "AMBOR1M",
    "3_month_term_structure": "AMBOR3M",
    "6_month_term_structure": "AMBOR6M",
    "1_year_term_structure": "AMBOR1Y",
    "2_year_term_structure": "AMBOR2Y",
    "30_day_ma": "AMBOR30",
    "90_day_ma": "AMBOR90",
}

FED_PARAMETER_TO_FRED_ID = {
    "monthly": "FEDFUNDS",
    "daily": "DFF",
    "weekly": "FF",
    "daily_excl_weekend": "RIFSPFFNB",
    "annual": "RIFSPFFNA",
    "biweekly": "RIFSPFFNBWAW",
    "volume": "EFFRVOL",
}

OBFR_PARAMETER_TO_FRED_ID = {
    "daily": "OBFR",
    "volume": "OBFRVOL",
}

DWPCR_PARAMETER_TO_FRED_ID = {
    "daily_excl_weekend": "DPCREDIT",
    "monthly": "MPCREDIT",
    "weekly": "WPCREDIT",
    "daily": "RIFSRPF02ND",
    "annual": "RIFSRPF02NA",
}
TMC_PARAMETER_TO_FRED_ID = {
    "3_month": "T10Y3M",
    "2_year": "T10Y2Y",
}
FFRMC_PARAMETER_TO_FRED_ID = {
    "10_year": "T10YFF",
    "5_year": "T5YFF",
    "1_year": "T1YFF",
    "6_month": "T6MFF",
    "3_month": "T3MFF",
}

TBFFR_PARAMETER_TO_FRED_ID = {
    "3_month": "TB3SMFFM",
    "6_month": "TB6SMFFM",
}


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_estr(
    series_id: str = "ECBESTRVOLWGTTRMDMNRT",
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plot Euro Short-Term Rate (ESTR)

    Parameters
    ----------
    series_id: str
        FRED ID of ESTR data to plot, options: ['ECBESTRVOLWGTTRMDMNRT',
        'ECBESTRTOTVOL', 'ECBESTRNUMTRANS', 'ECBESTRRT75THPCTVOL',
        'ECBESTRNUMACTBANKS', 'ECBESTRSHRVOL5LRGACTBNK', 'ECBESTRRT25THPCTVOL']
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    export: str
        Export data to csv or excel file
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    if series_id in ESTR_PARAMETER_TO_ECB_ID:
        series_id = ESTR_PARAMETER_TO_ECB_ID[series_id]

    df = fred_model.get_series_data(
        series_id=series_id, start_date=start_date, end_date=end_date
    )

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    colors = cycle(theme.get_colors())
    ax.plot(
        df.index,
        df.values,
        color=next(colors, "#FCED00"),
    )
    ax.set_title(ID_TO_NAME_ESTR[series_id], fontsize=15)
    theme.style_primary_axis(ax)

    if series_id == "ECBESTRTOTVOL":
        ylabel = "Millions in EUR"
    elif series_id == "ECBESTRNUMACTBANKS":
        ylabel = "Number of Banks"
    elif series_id == "ECBESTRNUMTRANS":
        ylabel = "Number of Transactions"
    else:
        ylabel = "Yield (%)"

    ax.set_ylabel(ylabel)

    if external_axes is None:
        theme.visualize_output()

    if export:
        if series_id not in ["ECBESTRTOTVOL", "ECBESTRNUMACTBANKS", "ECBESTRNUMTRANS"]:
            # Check whether it is a percentage, relevant for exporting
            df_transformed = pd.DataFrame(df, columns=[series_id]) / 100
        else:
            df_transformed = pd.DataFrame(df, columns=[series_id])

        export_data(
            export,
            os.path.dirname(os.path.abspath(__file__)),
            series_id,
            df_transformed,
            sheet_name,
        )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_sofr(
    series_id: str = "SOFR",
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plot Secured Overnight Financing Rate (SOFR)

    Parameters
    ----------
    series_id: str
        FRED ID of SOFR data to plot, options: ['SOFR', 'SOFR30DAYAVG', 'SOFR90DAYAVG', 'SOFR180DAYAVG', 'SOFRINDEX']
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    export: str
        Export data to csv or excel file
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    if series_id in SOFR_PARAMETER_TO_FRED_ID:
        series_id = SOFR_PARAMETER_TO_FRED_ID[series_id]

    df = fred_model.get_series_data(
        series_id=series_id, start_date=start_date, end_date=end_date
    )

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    colors = cycle(theme.get_colors())
    ax.plot(
        df.index,
        df.values,
        color=next(colors, "#FCED00"),
    )
    ax.set_title(ID_TO_NAME_SOFR[series_id], fontsize=15)
    ax.set_ylabel("Yield (%)" if series_id != "SOFRINDEX" else "Index [Base = 04-2018]")

    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    if export:
        if series_id != "SOFRINDEX":
            # Check whether it is a percentage, relevant for exporting
            df_transformed = pd.DataFrame(df, columns=[series_id]) / 100
        else:
            df_transformed = pd.DataFrame(df, columns=[series_id])

        export_data(
            export,
            os.path.dirname(os.path.abspath(__file__)),
            series_id,
            df_transformed,
            sheet_name,
        )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_sonia(
    series_id: str = "IUDSOIA",
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plot Sterling Overnight Index Average (SONIA)

    Parameters
    ----------
    series_id: str
        FRED ID of SONIA data to plot, options: ['IUDSOIA', 'IUDZOS2',
        'IUDZLS6', 'IUDZLS7', 'IUDZLS8', 'IUDZLS9', 'IUDZLT2']
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    export: str
        Export data to csv or excel file
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    if series_id in SONIA_PARAMETER_TO_FRED_ID:
        series_id = SONIA_PARAMETER_TO_FRED_ID[series_id]

    df = fred_model.get_series_data(
        series_id=series_id, start_date=start_date, end_date=end_date
    )

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    colors = cycle(theme.get_colors())
    ax.plot(
        df.index,
        df.values,
        color=next(colors, "#FCED00"),
    )

    if series_id == "IUDZLT2":
        ylabel = "Millions of GDP"
    elif series_id == "IUDZOS2":
        ylabel = "Index [Base = 04-2018]"
    else:
        ylabel = "Yield (%)"

    ax.set_title(ID_TO_NAME_SONIA[series_id], fontsize=15)
    ax.set_ylabel(ylabel)
    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    if export:
        if series_id not in ["IUDZOS2", "IUDZLT2"]:
            # Check whether it is a percentage, relevant for exporting
            df_transformed = pd.DataFrame(df, columns=[series_id]) / 100
        else:
            df_transformed = pd.DataFrame(df, columns=[series_id])

        export_data(
            export,
            os.path.dirname(os.path.abspath(__file__)),
            series_id,
            df_transformed,
            sheet_name,
        )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_ameribor(
    series_id: str = "AMERIBOR",
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plot American Interbank Offered Rate (AMERIBOR)

    Parameters
    ----------
    series_id: str
        FRED ID of AMERIBOR data to plot, options: ['AMERIBOR', 'AMBOR30T',
        'AMBOR90T', 'AMBOR1W', 'AMBOR1M', 'AMBOR3M', 'AMBOR6M', 'AMBOR1Y',
        'AMBOR2Y', 'AMBOR30', 'AMBOR90']
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    export: str
        Export data to csv or excel file
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    if series_id in AMERIBOR_PARAMETER_TO_FRED_ID:
        series_id = AMERIBOR_PARAMETER_TO_FRED_ID[series_id]

    df = fred_model.get_series_data(
        series_id=series_id, start_date=start_date, end_date=end_date
    )

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    colors = cycle(theme.get_colors())
    ax.plot(
        df.index,
        df.values,
        color=next(colors, "#FCED00"),
    )

    ylabel = "Index" if series_id in ["AMBOR30T", "AMBOR90T"] else "Yield (%)"

    ax.set_title(ID_TO_NAME_AMERIBOR[series_id], fontsize=15)
    ax.set_ylabel(ylabel)
    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    if export:
        if series_id not in ["AMBOR30T", "AMBOR90T"]:
            # Check whether it is a percentage, relevant for exporting
            df_transformed = pd.DataFrame(df, columns=[series_id]) / 100
        else:
            df_transformed = pd.DataFrame(df, columns=[series_id])

        export_data(
            export,
            os.path.dirname(os.path.abspath(__file__)),
            series_id,
            df_transformed,
            sheet_name,
        )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_fftr(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plot Federal Funds Target Range.

    A bank rate is the interest rate a nation's central bank charges to its domestic banks to borrow money. The rates
    central banks charge are set to stabilize the economy. In the United States, the Federal Reserve System's Board
    of Governors set the bank rate, also known as the discount rate.

    Parameters
    ----------
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    export: str
        Export data to csv or excel file
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    df_upper = fred_model.get_series_data(
        series_id="DFEDTARU", start_date=start_date, end_date=end_date
    )
    df_lower = fred_model.get_series_data(
        series_id="DFEDTARL", start_date=start_date, end_date=end_date
    )
    df = pd.DataFrame([df_upper, df_lower]).transpose()

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    ax.plot(
        df.index,
        df.values,
    )
    ax.set_title("Federal Funds Target Range")
    ax.legend(["Upper limit", "Lower limit"])
    ax.set_ylabel("Yield (%)")
    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "fftr",
        pd.DataFrame(df, columns=["FFTR"]) / 100,
        sheet_name,
    )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_fed(
    series_id: str = "FEDFUNDS",
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    overnight: bool = False,
    quantiles: bool = False,
    target: bool = False,
    raw: bool = False,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plot Effective Federal Funds Rate.

    A bank rate is the interest rate a nation's central bank charges to its domestic banks to borrow money. The rates
    central banks charge are set to stabilize the economy. In the United States, the Federal Reserve System's Board
    of Governors set the bank rate, also known as the discount rate.

    Parameters
    ----------
    series_id: str
        FRED ID of EFFER data to plot, options: ['EFFR', 'EFFRVOL', 'EFFR1', 'EFFR25', 'EFFR75', 'EFFR99']
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    overnight: bool
        Whether you want to plot the Overnight Banking Federal Rate
    quantiles: bool
        Whether you want to see the 1, 25, 75 and 99 percentiles
    target: bool
        Whether you want to see the high and low target range
    raw : bool
        Show raw data
    export: str
        Export data to csv or excel file
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    if series_id in FED_PARAMETER_TO_FRED_ID:
        series_id = FED_PARAMETER_TO_FRED_ID[series_id]

    if overnight:
        # This piece of code adjusts the series id when the user wants to plot the overnight rate
        if series_id == "DFF":
            series_id = "OBFR"
        elif series_id == "EFFRVOL":
            series_id = "OBFRVOL"
        else:
            console.print(
                "The Overnight Banking Federal Rate only supports Daily data."
            )
            series_id = "OBFR"

    if quantiles or target and not overnight:
        data_series = [series_id if series_id != "EFFRVOL" else "EFFR"]
        series_id = series_id if series_id != "EFFRVOL" else "EFFR"

        if quantiles:
            data_series.extend(["EFFR1", "EFFR25", "EFFR75", "EFFR99"])
        if target:
            data_series.extend(["DFEDTARU", "DFEDTARL"])

        df = pd.DataFrame()

        for series in data_series:
            data = pd.DataFrame(
                fred_model.get_series_data(
                    series_id=series, start_date=start_date, end_date=end_date
                ),
                columns=[series],
            )
            df = data if series == series_id else pd.concat([df, data], axis=1)

        df = df.dropna()

        # This plot has 1 axis
        if not external_axes:
            _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
        elif is_valid_axes_count(external_axes, 1):
            (ax,) = external_axes
        else:
            return

        colors = cycle(theme.get_colors())
        for column in df.columns:
            ax.plot(
                df[column],
                linewidth=3 if column == series_id else 1,
                color=next(colors),
            )
        ax.set_title(ID_TO_NAME_FED[series_id])
        ax.legend(data_series)
        ax.set_ylabel("Yield (%)")
        theme.style_primary_axis(ax)

        if external_axes is None:
            theme.visualize_output()
    else:
        df = fred_model.get_series_data(
            series_id=series_id, start_date=start_date, end_date=end_date
        )

        # This plot has 1 axis
        if not external_axes:
            _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
        elif is_valid_axes_count(external_axes, 1):
            (ax,) = external_axes
        else:
            return

        colors = cycle(theme.get_colors())
        ax.plot(
            df.index,
            df.values,
            linewidth=2,
            color=next(colors),
        )
        ax.set_title(ID_TO_NAME_FED[series_id])
        ax.set_ylabel(
            "Yield (%)"
            if series_id not in ["EFFRVOL", "OBFRVOL"]
            else "Billions in USD"
        )
        theme.style_primary_axis(ax)

        if external_axes is None:
            theme.visualize_output()

    if export or raw:
        if not quantiles and not target:
            if series_id != "EFFRVOL":
                # Check whether it is a percentage, relevant for exporting
                df_transformed = pd.DataFrame(df, columns=[series_id]) / 100
            else:
                df_transformed = pd.DataFrame(df, columns=[series_id])
        else:
            df_transformed = df / 100

    if raw:
        print_rich_table(
            df_transformed.iloc[-10:],
            headers=list(df_transformed.columns),
            show_index=True,
            title=ID_TO_NAME_FED[series_id],
            floatfmt=".3f",
        )

    if export:
        export_data(
            export,
            os.path.dirname(os.path.abspath(__file__)),
            series_id,
            df_transformed,
            sheet_name,
        )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_iorb(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plot Interest Rate on Reserve Balances.

    A bank rate is the interest rate a nation's central bank charges to its domestic banks to borrow money. The rates
    central banks charge are set to stabilize the economy. In the United States, the Federal Reserve System's Board
    of Governors set the bank rate, also known as the discount rate.

    Parameters
    ----------
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    export: str
        Export data to csv or excel file
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    df = fred_model.get_series_data(
        series_id="IORB", start_date=start_date, end_date=end_date
    )

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    colors = cycle(theme.get_colors())
    ax.plot(
        df.index,
        df.values,
        color=next(colors, "#FCED00"),
    )
    ax.set_title("Interest Rate on Reserve Balances")
    ax.set_ylabel("Yield (%)")
    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "iorb",
        pd.DataFrame(df, columns=["IORB"]) / 100,
        sheet_name,
    )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_projection(
    long_run: bool = False,
    raw: bool = False,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plot the Federal Reserve's projection of the federal funds rate.

    Parameters
    ----------
    long_run: str
        Whether to plot the long run projection.
    export: str
        Export data to csv or excel file
    raw : bool
        Show raw data
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    data_series = {}

    for projection, values in NAME_TO_ID_PROJECTION.items():
        data_series[projection] = fred_model.get_series_data(series_id=values[long_run])

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    data_series_df = pd.DataFrame.from_dict(data_series).dropna()
    data_series_df.index = pd.to_datetime(data_series_df.index).date

    for legend, df in data_series_df.items():
        ax.plot(
            df.index,
            df.values,
            linestyle="dashed" if legend != "Median" else "solid",
            linewidth=1 if legend != "Median" else 2,
            label=legend,
        )

    ax.set_title(
        f"FOMC {'Long Run ' if long_run else ''}Summary of Economic Projections\nfor the Federal Funds Rate"
    )
    ax.legend(prop={"size": 8}, loc="lower left")
    ax.set_ylabel("Yield (%)")

    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    if raw:
        print_rich_table(
            data_series_df,
            headers=list(data_series_df.columns),
            show_index=True,
            title=f"FOMC {'Long Run ' if long_run else ''}Summary of "
            "Economic Projections for the Federal Funds Rate",
        )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "projection",
        data_series_df,
        sheet_name,
    )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_dwpcr(
    series_id: str = "DPCREDIT",
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plot Discount Window Primary Credit Rate.

    A bank rate is the interest rate a nation's central bank charges to its domestic banks to borrow money. The rates
    central banks charge are set to stabilize the economy. In the United States, the Federal Reserve System's Board
    of Governors set the bank rate, also known as the discount rate.

    Parameters
    ----------
    series_id: str
        FRED ID of DWPCR data to plot, options: ['MPCREDIT', 'RIFSRPF02ND', 'WPCREDIT', 'DPCREDIT', 'RIFSRPF02NA']
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    export: str
        Export data to csv or excel file
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    if series_id in DWPCR_PARAMETER_TO_FRED_ID:
        series_id = DWPCR_PARAMETER_TO_FRED_ID[series_id]

    df = fred_model.get_series_data(
        series_id=series_id, start_date=start_date, end_date=end_date
    )

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    colors = cycle(theme.get_colors())
    ax.plot(
        df.index,
        df.values,
        color=next(colors, "#FCED00"),
    )
    ax.set_title(
        "Discount Window Primary Credit Rate " + ID_TO_NAME_DWPCR[series_id],
        fontsize=10,
    )
    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        series_id,
        pd.DataFrame(df, columns=[series_id]) / 100,
        sheet_name,
    )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_ecb(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    interest_type: Optional[str] = None,
    raw: bool = False,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plot the key ECB interest rates.

    The Governing Council of the ECB sets the key interest rates for the euro area:

    - The interest rate on the main refinancing operations (MRO), which provide
     the bulk of liquidity to the banking system.
    - The rate on the deposit facility, which banks may use to make overnight deposits with the Eurosystem.
    - The rate on the marginal lending facility, which offers overnight credit to banks from the Eurosystem.

    Parameters
    ----------
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    export: str
        Export data to csv or excel file
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """

    if interest_type:
        df = pd.DataFrame(
            fred_model.get_series_data(
                series_id=NAME_TO_ID_ECB[interest_type],
                start_date=start_date,
                end_date=end_date,
            ),
            columns=[interest_type],
        )

    else:
        series_dictionary = {}

        for interest_name, value in NAME_TO_ID_ECB.items():
            series_dictionary[interest_name.title()] = fred_model.get_series_data(
                series_id=value, start_date=start_date, end_date=end_date
            )

        df = pd.DataFrame.from_dict(series_dictionary)
        df.index = pd.to_datetime(df.index).date

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    colors = cycle(theme.get_colors())

    for series in df:
        ax.plot(
            df.index,
            df[series],
            color=next(colors, "#FCED00"),
            label=series.title(),
        )

    title = (
        f"ECB {interest_type.title()} Rate for Euro Area"
        if interest_type
        else "ECB Interest Rates for Euro Area"
    )
    ax.set_title(title)
    ax.legend(loc="lower left")
    ax.set_ylabel("Yield (%)")
    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    if raw:
        print_rich_table(
            df.iloc[-10:],
            headers=list(df.columns),
            show_index=True,
            title=title,
            floatfmt=".3f",
        )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "ecbdfr",
        pd.DataFrame(df, columns=["ECBDFR"]) / 100,
        sheet_name,
    )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_ecbmlfr(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plot ECB Marginal Lending Facility Rate for Euro Area.

    A standing facility of the Euro-system which counterparties may use to receive overnight credit from a national
    central bank at a pre-specified interest rate against eligible assets.

    A bank rate is the interest rate a nation's central bank charges to its domestic banks to borrow money. The rates
    central banks charge are set to stabilize the economy.

    Parameters
    ----------
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    export: str
        Export data to csv or excel file
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    df = fred_model.get_series_data(
        series_id="ECBMLFR", start_date=start_date, end_date=end_date
    )

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    colors = cycle(theme.get_colors())
    ax.plot(
        df.index,
        df.values,
        color=next(colors, "#FCED00"),
    )
    ax.set_title("ECB Marginal Lending Facility Rate for Euro Area")
    ax.set_ylabel("Yield (%)")
    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    export_data(
        export, os.path.dirname(os.path.abspath(__file__)), "ecbmlfr", df, sheet_name
    )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_ecbmrofr(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plot ECB Marginal Lending Facility Rate for Euro Area.

    A regular open market operation executed by the Euro-system (in the form of a reverse transaction) for the purpose
    of providing the banking system with the amount of liquidity that the former deems to be appropriate. Main
    refinancing operations are conducted through weekly standard tenders (in which banks can bid for liquidity) and
    normally have a maturity of one week.

    A bank rate is the interest rate a nation's central bank charges to its domestic banks to borrow money. The rates
    central banks charge are set to stabilize the economy.

    Parameters
    ----------
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    export: str
        Export data to csv or excel file
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    df = fred_model.get_series_data(
        series_id="ECBMRRFR", start_date=start_date, end_date=end_date
    )

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    colors = cycle(theme.get_colors())
    ax.plot(
        df.index,
        df.values,
        color=next(colors, "#FCED00"),
    )
    ax.set_title(
        "ECB Main Refinancing Operations Rate: Fixed Rate Tenders for Euro Area"
    )
    ax.set_ylabel("Yield (%)")
    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "ecbmrofr",
        pd.DataFrame(df, columns=["ECBMROFR"]) / 100,
        sheet_name,
    )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_tmc(
    series_id: str = "T10Y3M",
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plot 10-Year Treasury Constant Maturity Minus Selected Treasury Constant Maturity data.

    Constant maturity is the theoretical value of a U.S. Treasury that is based on recent values of auctioned U.S.
    Treasuries. The value is obtained by the U.S. Treasury on a daily basis through interpolation of the Treasury
    yield curve which, in turn, is based on closing bid-yields of actively-traded Treasury securities.

    Parameters
    ----------
    series_id: str
        FRED ID of TMC data to plot, options: ['T10Y3M', 'T10Y3M']
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    export: str
        Export data to csv or excel file
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    if series_id in TMC_PARAMETER_TO_FRED_ID:
        series_id = TMC_PARAMETER_TO_FRED_ID[series_id]

    df = fred_model.get_series_data(
        series_id=series_id, start_date=start_date, end_date=end_date
    )

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    colors = cycle(theme.get_colors())
    ax.plot(
        df.index,
        df.values,
        color=next(colors, "#FCED00"),
    )
    ax.set_title(
        "10-Year Treasury Constant Maturity Minus "
        + ID_TO_NAME_TMC[series_id]
        + " Treasury Constant Maturity",
        fontsize=10,
    )

    ax.set_ylabel("Yield (%)")
    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        series_id,
        pd.DataFrame(df, columns=[series_id]) / 100,
        sheet_name,
    )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_ffrmc(
    series_id: str = "T10YFF",
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plot Selected Treasury Constant Maturity Minus Federal Funds Rate data.

    Constant maturity is the theoretical value of a U.S. Treasury that is based on recent values of auctioned U.S.
    Treasuries. The value is obtained by the U.S. Treasury on a daily basis through interpolation of the Treasury
    yield curve which, in turn, is based on closing bid-yields of actively-traded Treasury securities.

    Parameters
    ----------
    series_id: str
        FRED ID of FFRMC data to plot, options: ['T10YFF', 'T5YFF', 'T1YFF', 'T6MFF', 'T3MFF']
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    export: str
        Export data to csv or excel file
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    if series_id in FFRMC_PARAMETER_TO_FRED_ID:
        series_id = FFRMC_PARAMETER_TO_FRED_ID[series_id]

    df = fred_model.get_series_data(
        series_id=series_id, start_date=start_date, end_date=end_date
    )

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    colors = cycle(theme.get_colors())
    ax.plot(
        df.index,
        df.values,
        color=next(colors, "#FCED00"),
    )
    ax.set_title(
        ID_TO_NAME_FFRMC[series_id]
        + " Treasury Constant Maturity Minus Federal Funds Rate",
        fontsize=10,
    )
    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        series_id,
        pd.DataFrame(df, columns=[series_id]) / 100,
        sheet_name,
    )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def display_yield_curve(
    date: str = "",
    inflation_adjusted: bool = False,
    raw: bool = False,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Display yield curve based on US Treasury rates for a specified date.

    The graphic depiction of the relationship between the yield on bonds of the same credit quality but different
    maturities is known as the yield curve. In the past, most market participants have constructed yield curves from
    the observations of prices and yields in the Treasury market. Two reasons account for this tendency. First,
    Treasury securities are viewed as free of default risk, and differences in creditworthiness do not affect yield
    estimates. Second, as the most active bond market, the Treasury market offers the fewest problems of illiquidity
    or infrequent trading. The key function of the Treasury yield curve is to serve as a benchmark for pricing bonds
    and setting yields in other sectors of the debt market.

    It is clear that the market’s expectations of future rate changes are one important determinant of the
    yield-curve shape. For example, a steeply upward-sloping curve may indicate market expectations of near-term Fed
    tightening or of rising inflation. However, it may be too restrictive to assume that the yield differences across
    bonds with different maturities only reflect the market’s rate expectations. The well-known pure expectations
    hypothesis has such an extreme implication. The pure expectations hypothesis asserts that all government bonds
    have the same near-term expected return (as the nominally riskless short-term bond) because the return-seeking
    activity of risk-neutral traders removes all expected return differentials across bonds.

    Parameters
    ----------
    date: str
        Date to get curve for. If None, gets most recent date (format yyyy-mm-dd)
    external_axes : Optional[List[plt.Axes]], optional
        External axes (1 axis is expected in the list), by default None
    raw : bool
        Output only raw data
    export : str
        Export data to csv,json,xlsx or png,jpg,pdf,svg file
    """
    rates, date_of_yield = fred_model.get_yield_curve(date, True, inflation_adjusted)
    if rates.empty:
        console.print(f"[red]Yield data not found for {date_of_yield}.[/red]\n")
        return
    if external_axes is None:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    ax.plot(rates["Maturity"], rates["Rate"], "-o")
    ax.set_xlabel("Maturity")
    ax.set_ylabel("Yield (%)")
    theme.style_primary_axis(ax)
    if external_axes is None:
        ax.set_title(
            f"US {'Real' if inflation_adjusted else 'Nominal'} Yield Curve for {date_of_yield} "
        )
        theme.visualize_output()

    if raw:
        print_rich_table(
            rates,
            headers=list(rates.columns),
            show_index=False,
            title=f"United States {'Real' if inflation_adjusted else 'Nominal'} Yield Curve for {date_of_yield}",
            floatfmt=".3f",
        )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "ycrv",
        rates.set_index("Maturity") / 100,
        sheet_name,
    )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_usrates(
    parameter: str = "tbills",
    maturity: str = "3_months",
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    raw: bool = False,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plot various treasury rates from the United States

    A Treasury Bill (T-Bill) is a short-term U.S. government debt obligation backed by the Treasury Department with a
    maturity of one year or less. Treasury bills are usually sold in denominations of $1,000. However, some can reach
    a maximum denomination of $5 million in non-competitive bids. These securities are widely regarded as low-risk
    and secure investments.

    Yields on Treasury nominal securities at “constant maturity” are interpolated by the U.S. Treasury from the daily
    yield curve for non-inflation-indexed Treasury securities. This curve, which relates the yield on a security to
    its time to maturity, is based on the closing market bid yields on actively traded Treasury securities in the
    over-the-counter market. These market yields are calculated from composites of quotations obtained by the Federal
    Reserve Bank of New York. The constant maturity yield values are read from the yield curve at fixed maturities,
    currently 1, 3, and 6 months and 1, 2, 3, 5, 7, 10, 20, and 30 years. This method provides a yield for a 10-year
    maturity, for example, even if no outstanding security has exactly 10 years remaining to maturity. Similarly,
    yields on inflation-indexed securities at “constant maturity” are interpolated from the daily yield curve for
    Treasury inflation protected securities in the over-the-counter market. The inflation-indexed constant maturity
    yields are read from this yield curve at fixed maturities, currently 5, 7, 10, 20, and 30 years.

    Parameters
    ----------
    parameter: str
        Either "tbills", "cmn", or "tips".
    maturity: str
        Depending on the chosen parameter, a set of maturities is available.
    series_id: str
        FRED ID of Treasury Bill Secondary Market Rate data to plot, options: ['TB3MS', 'DTB4WK', 'DTB1YR', 'DTB6']
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    export: str
        Export data to csv or excel file
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    series_id = USARATES_TO_FRED_ID[maturity][parameter]
    df = fred_model.get_series_data(
        series_id=series_id, start_date=start_date, end_date=end_date
    )

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    colors = cycle(theme.get_colors())
    ax.plot(
        df.index,
        df.values,
        color=next(colors, "#FCED00"),
    )

    if parameter == "tbill":
        title = f"{maturity.replace('_', ' ').title()} Treasury Bill Secondary Market Rate, Discount Basis"
    elif parameter == "cmn":
        title = f"{maturity.replace('_', ' ').title()} Treasury Constant Maturity Nominal Market Yield"
    elif parameter == "tips":
        title = f"{maturity.replace('_', ' ').title()} Yields on Treasury inflation protected securities "
        "(TIPS) adjusted to constant maturities"

    ax.set_title(title, fontsize=15)
    ax.set_ylabel("Yield (%)")
    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    if raw:
        print_rich_table(
            pd.DataFrame(df, columns=[parameter]).iloc[-10:],
            title=title,
            show_index=True,
            floatfmt=".3f",
        )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        series_id,
        pd.DataFrame(df, columns=[parameter]) / 100,
        sheet_name,
    )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_tbffr(
    series_id: str = "TB3SMFFM",
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plot Selected Treasury Bill Minus Federal Funds Rate data.

    Parameters
    ----------
    series_id: str
        FRED ID of TBFFR data to plot, options: ['TB3SMFFM', 'TB6SMFFM']
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    export: str
        Export data to csv or excel file
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    if series_id in TBFFR_PARAMETER_TO_FRED_ID:
        series_id = TBFFR_PARAMETER_TO_FRED_ID[series_id]

    df = fred_model.get_series_data(
        series_id=series_id, start_date=start_date, end_date=end_date
    )

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    colors = cycle(theme.get_colors())
    ax.plot(
        df.index,
        df.values,
        color=next(colors, "#FCED00"),
    )
    ax.set_title(
        ID_TO_NAME_TBFFR[series_id] + " Treasury Bill Minus Federal Funds Rate"
    )
    theme.style_primary_axis(ax)

    ax.set_ylabel("Yield (%)")
    if external_axes is None:
        theme.visualize_output()

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        series_id,
        pd.DataFrame(df, columns=["TBFFR"]) / 100,
        sheet_name,
    )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_icebofa(
    data_type: str = "yield",
    category: str = "all",
    area: str = "us",
    grade: str = "non_sovereign",
    options: bool = False,
    description: bool = False,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    raw: bool = False,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plot ICE BofA US Corporate Bond Index data.

    Parameters
    ----------
    data_type: str
        The type of data you want to see, either "yield", "yield_to_worst", "total_return", or "spread"
    category: str
        The type of category you want to see, either "all", "duration", "eur" or "usd".
    area: str
        The type of area you want to see, either "asia", "emea", "eu", "ex_g10", "latin_america" or "us"
    grade: str
        The type of grade you want to see, either "a", "aa", "aaa", "b", "bb", "bbb", "ccc", "crossover",
        "high_grade", "high_yield", "non_financial", "non_sovereign", "private_sector", "public_sector"
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    raw: bool
        Show raw data
    export: str
        Export data to csv or excel file
    sheet_name: str
        Name of the sheet to export to
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    if data_type == "total_return":
        units = "index"
    elif data_type in ["yield", "yield_to_worst", "spread"]:
        units = "percent"

    series = pd.read_excel(ice_bofa_path)

    if options:
        return print_rich_table(
            series.drop(
                ["Frequency", "Units", "Asset Class", "FRED Series ID", "Description"],
                axis=1,
            )[
                series["Type"].isin(
                    ["yield", "yield_to_worst", "total_return"]
                    if data_type != "spread"
                    else ["spread"]
                )
            ]
        )

    series = series[
        (series["Type"] == data_type)
        & (series["Units"] == units)
        & (series["Frequency"] == "daily")
        & (series["Asset Class"] == "bonds")
        & (series["Category"] == category)
        & (series["Area"] == area)
        & (series["Grade"] == grade)
    ]

    if series.empty:
        console.print("The combination of parameters does not result in any data.")
        return pd.DataFrame()

    series_dictionary = {}

    for series_id, title in series[["FRED Series ID", "Title"]].values:
        series_dictionary[title] = fred_model.get_series_data(
            series_id=series_id, start_date=start_date, end_date=end_date
        )

    df = pd.DataFrame.from_dict(series_dictionary)
    df.index = pd.to_datetime(df.index).date

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    colors = cycle(theme.get_colors())

    for column in df.columns:
        ax.plot(
            df.index,
            df[column].values,
            color=next(colors, "#FCED00"),
            label=column,
        )

    if len(df.columns) > 1:
        title = "ICE BofA Bond Benchmark Indices"
        ax.set_title(title, fontsize=15)
        ax.legend(prop={"size": 8})
    else:
        ax.set_title(title, fontsize=10)

    ax.set_ylabel("Yield (%)" if units == "percent" else "Index")
    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    if raw:
        print_rich_table(
            df.iloc[-10:],
            title=title,
            show_index=True,
            floatfmt=".3f",
        )

    if description:
        for title, description_text in series[["Title", "Description"]].values:
            console.print(f"\n[bold]{title}[/bold]")
            console.print(description_text)

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "ICEBOFA",
        df / 100,
        sheet_name,
    )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_moody(
    data_type: str = "aaa",
    spread: str = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    raw: bool = False,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plot ICE BofA US Corporate Bond Index data.

    Parameters
    ----------
    data_type: str
        The type of data you want to see, either "yield", "yield_to_worst", "total_return", or "spread"
    category: str
        The type of category you want to see, either "all", "duration", "eur" or "usd".
    area: str
        The type of area you want to see, either "asia", "emea", "eu", "ex_g10", "latin_america" or "us"
    grade: str
        The type of grade you want to see, either "a", "aa", "aaa", "b", "bb", "bbb", "ccc", "crossover",
        "high_grade", "high_yield", "non_financial", "non_sovereign", "private_sector", "public_sector"
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    raw: bool
        Show raw data
    export: str
        Export data to csv or excel file
    sheet_name: str
        Name of the sheet to export to
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    series_id = MOODY_TO_OPTIONS["Type"][data_type][spread if spread else "index"]["id"]
    name = MOODY_TO_OPTIONS["Type"][data_type][spread if spread else "index"]["name"]

    series = fred_model.get_series_data(
        series_id=series_id, start_date=start_date, end_date=end_date
    )

    df = pd.DataFrame(series, columns=[f"{data_type}_{spread if spread else 'index'}"])
    df.index = pd.to_datetime(df.index).date

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    colors = cycle(theme.get_colors())

    ax.plot(
        df.index,
        df.values,
        color=next(colors, "#FCED00"),
    )

    ax.set_title(name, fontsize=10)
    ax.set_ylabel("Yield (%)")
    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    if raw:
        print_rich_table(
            df.iloc[-10:],
            title=name,
            show_index=True,
            floatfmt=".3f",
        )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "MOODY",
        df / 100,
        sheet_name,
    )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_cp(
    maturity: str = "30d",
    category: str = "financial",
    grade: str = "aa",
    options: bool = False,
    description: bool = False,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    raw: bool = False,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plot ICE BofA US Corporate Bond Index data.

    Parameters
    ----------
    maturity: str
        The maturity you want to see, either "overnight", "7d", "15d", "30d", "60d" or "90d"
    category: str
        The category you want to see, either "asset_backed", "financial" or "non_financial"
    grade: str
        The type of grade you want to see, either "a2_p2" or "aa"
    description: bool
        Whether you wish to obtain a description of the data.
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    raw: bool
        Show raw data
    export: str
        Export data to csv or excel file
    sheet_name: str
        Name of the sheet to export to
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    if grade == "a2_p2" and category != "non_financial":
        console.print(
            "Setting category to 'non_financial' given "
            f"the chosen {grade} grade only has data for 'non_financial'."
        )
        category = "non_financial"

    series = pd.read_excel(commercial_paper_path)

    if options:
        return print_rich_table(series.drop(["Description", "FRED Series ID"], axis=1))

    series = series[
        (series["Maturity"] == maturity)
        & (series["Category"] == category)
        & (series["Grade"] == grade)
    ]

    if series.empty:
        console.print("The combination of parameters does not result in any data.")
        return pd.DataFrame()

    series_dictionary = {}

    for series_id, title in series[["FRED Series ID", "Title"]].values:
        series_dictionary[title] = fred_model.get_series_data(
            series_id=series_id, start_date=start_date, end_date=end_date
        )

    df = pd.DataFrame.from_dict(series_dictionary)
    df.index = pd.to_datetime(df.index).date

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    colors = cycle(theme.get_colors())

    for column in df.columns:
        ax.plot(
            df.index,
            df[column].values,
            color=next(colors, "#FCED00"),
            label=column,
        )

    if len(df.columns) > 1:
        title = "Commercial Paper Interest Rates"
        ax.set_title(title, fontsize=15)
        ax.legend(prop={"size": 8})
    else:
        ax.set_title(title, fontsize=10)

    ax.set_ylabel("Yield (%)")
    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    if raw:
        print_rich_table(
            df.iloc[-10:],
            title=title,
            show_index=True,
            floatfmt=".3f",
        )

    if description:
        for title, description_text in series[["Title", "Description"]].values:
            console.print(f"\n[bold]{title}[/bold]")
            console.print(description_text)

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "CP",
        df / 100,
        sheet_name,
    )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_spot(
    maturity: List = ["10y"],
    category: List = ["spot_rate"],
    description: bool = False,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    raw: bool = False,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """
    The spot rate for any maturity is the yield on a bond that provides
    a single payment at that maturity. This is a zero coupon bond. Because each
    spot rate pertains to a single cashflow, it is the relevant interest rate
    concept for discounting a pension liability at the same maturity.

    Parameters
    ----------
    maturity: str
        The maturity you want to see, either "overnight", "7d", "15d", "30d", "60d" or "90d"
    category: str
        The category you want to see, either "asset_backed", "financial" or "non_financial"
    grade: str
        The type of grade you want to see, either "a2_p2" or "aa"
    description: bool
        Whether you wish to obtain a description of the data.
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    raw: bool
        Show raw data
    export: str
        Export data to csv or excel file
    sheet_name: str
        Name of the sheet to export to
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    series = pd.read_excel(spot_rates_path)

    series = series[
        (series["Maturity"].isin(maturity)) & (series["Category"].isin(category))
    ]

    if "par_yield" in category and "par_yield" not in series["Category"].values:
        console.print(
            "No Par Yield data available for (some of) the selected maturities. "
            "Only 2y, 5y, 10y and 30y is available."
        )

    series_dictionary = {}

    for series_id, title in series[["FRED Series ID", "Title"]].values:
        series_dictionary[title] = fred_model.get_series_data(
            series_id=series_id, start_date=start_date, end_date=end_date
        )

    df = pd.DataFrame.from_dict(series_dictionary)
    df.index = pd.to_datetime(df.index).date

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    colors = cycle(theme.get_colors())

    for column in df.columns:
        ax.plot(
            df.index,
            df[column].values,
            color=next(colors, "#FCED00"),
            label=column,
        )

    if len(df.columns) > 1:
        title = "High Quality Market (HQM) Corporate Bond Rates"
        ax.set_title(title, fontsize=15)
        ax.legend(prop={"size": 8})
    else:
        ax.set_title(title, fontsize=10)

    ax.set_ylabel("Yield (%)")
    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    if raw:
        print_rich_table(
            df.iloc[-10:],
            title=title,
            show_index=True,
            floatfmt=".3f",
        )

    if description:
        for title, description_text in series[["Title", "Description"]].values:
            console.print(f"\n[bold]{title}[/bold]")
            console.print(description_text)

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "SPOT",
        df / 100,
        sheet_name,
    )


@log_start_end(log=logger)
@check_api_key(["API_FRED_KEY"])
def plot_hqm(
    date: Optional[str] = None,
    par: bool = False,
    raw: bool = False,
    export: str = "",
    sheet_name: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """
    The HQM yield curve represents the high quality corporate bond market, i.e.,
    corporate bonds rated AAA, AA, or A.  The HQM curve contains two regression terms. These
    terms are adjustment factors that blend AAA, AA, and A bonds into a single HQM yield curve
    that is the market-weighted average (MWA) quality of high quality bonds.

    Parameters
    ----------
    date: str
        The date of the yield curve you wish to plot
    par: bool
        Whether you wish to plot the par yield curve as well
    raw: bool
        Show raw data
    export: str
        Export data to csv or excel file
    sheet_name: str
        Name of the sheet to export to
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list)
    """
    df = pd.DataFrame()
    data_types = ["spot", "par"] if par else ["spot"]

    for types in data_types:
        subset, date_of_yield = fred_model.get_yield_curve(
            date, True, spot_or_par=types
        )
        subset.set_index("Maturity", inplace=True)
        subset.columns = [types]

        df = pd.concat([df, subset], axis=1)

    if par:
        # Drop NaNs because of length mismatch
        df = df.dropna()

    if df.empty:
        console.print(f"[red]Yield data not found at {date_of_yield}.[/red]\n")

    # This plot has 1 axis
    if not external_axes:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    for types in data_types:
        ax.plot(df.index, df[types], label=f"{types.title()} Yield")

    ax.set_title(f"Spot{'and Par' if par else ''} Yield Curve for {date_of_yield}")
    ax.set_xlabel("Maturity")
    ax.set_ylabel("Yield (%)")
    ax.legend() if par else None
    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    if raw:
        print_rich_table(
            df,
            headers=list(df.columns),
            show_index=True,
            index_name="Maturity",
            title=f"Spot {'and Par' if par else ''} Yield Curve for {date_of_yield}",
            floatfmt=".3f",
        )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "cycrv",
        df / 100,
        sheet_name,
    )
