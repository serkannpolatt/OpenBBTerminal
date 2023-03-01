"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[11386],{3905:(e,t,n)=>{n.d(t,{Zo:()=>p,kt:()=>h});var a=n(67294);function l(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function r(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){l(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function i(e,t){if(null==e)return{};var n,a,l=function(e,t){if(null==e)return{};var n,a,l={},o=Object.keys(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||(l[n]=e[n]);return l}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(l[n]=e[n])}return l}var s=a.createContext({}),u=function(e){var t=a.useContext(s),n=t;return e&&(n="function"==typeof e?e(t):r(r({},t),e)),n},p=function(e){var t=u(e.components);return a.createElement(s.Provider,{value:t},e.children)},c="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},m=a.forwardRef((function(e,t){var n=e.components,l=e.mdxType,o=e.originalType,s=e.parentName,p=i(e,["components","mdxType","originalType","parentName"]),c=u(n),m=l,h=c["".concat(s,".").concat(m)]||c[m]||d[m]||o;return n?a.createElement(h,r(r({ref:t},p),{},{components:n})):a.createElement(h,r({ref:t},p))}));function h(e,t){var n=arguments,l=t&&t.mdxType;if("string"==typeof e||l){var o=n.length,r=new Array(o);r[0]=m;var i={};for(var s in t)hasOwnProperty.call(t,s)&&(i[s]=t[s]);i.originalType=e,i[c]="string"==typeof e?e:l,r[1]=i;for(var u=2;u<o;u++)r[u]=n[u];return a.createElement.apply(null,r)}return a.createElement.apply(null,n)}m.displayName="MDXCreateElement"},8412:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>s,contentTitle:()=>r,default:()=>d,frontMatter:()=>o,metadata:()=>i,toc:()=>u});var a=n(87462),l=(n(67294),n(3905));const o={title:"Troubleshooting",sidebar_position:4,keywords:["faq","questions","openbb","terminal","troubleshooting","errors","bugs","issues","problems","installation","contributors","developers","github","pip"]},r=void 0,i={unversionedId:"quickstart/troubleshooting",id:"quickstart/troubleshooting",title:"Troubleshooting",description:"Still experiencing trouble after consulting this page? Reach us on Discord or visit our contact page.",source:"@site/content/terminal/quickstart/troubleshooting.md",sourceDirName:"quickstart",slug:"/quickstart/troubleshooting",permalink:"/terminal/quickstart/troubleshooting",draft:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/terminal/quickstart/troubleshooting.md",tags:[],version:"current",sidebarPosition:4,frontMatter:{title:"Troubleshooting",sidebar_position:4,keywords:["faq","questions","openbb","terminal","troubleshooting","errors","bugs","issues","problems","installation","contributors","developers","github","pip"]},sidebar:"tutorialSidebar",previous:{title:"Settings API Keys",permalink:"/terminal/quickstart/api-keys"},next:{title:"Basics",permalink:"/terminal/guides/basics/"}},s={},u=[{value:"Installation and Updates",id:"installation-and-updates",level:2},{value:"Launching",id:"launching",level:2},{value:"General Operation",id:"general-operation",level:2},{value:"Data and Sources",id:"data-and-sources",level:2},{value:"General Troubleshooting",id:"general-troubleshooting",level:2},{value:"Bugs, Support, and Feedback",id:"bugs-support-and-feedback",level:2},{value:"Developer Issues",id:"developer-issues",level:2}],p={toc:u},c="wrapper";function d(e){let{components:t,...n}=e;return(0,l.kt)(c,(0,a.Z)({},p,n,{components:t,mdxType:"MDXLayout"}),(0,l.kt)("p",null,"Still experiencing trouble after consulting this page? Reach us on ",(0,l.kt)("a",{parentName:"p",href:"https://openbb.co/discord"},"Discord")," or visit our ",(0,l.kt)("a",{parentName:"p",href:"https://openbb.co/contact"},"contact page"),"."),(0,l.kt)("h2",{id:"installation-and-updates"},"Installation and Updates"),(0,l.kt)("details",null,(0,l.kt)("summary",null,"How much hard drive space is required?"),(0,l.kt)("p",null,"An installation will use approximately 4GB of space.")),(0,l.kt)("details",null,(0,l.kt)("summary",null,"What is the minimum version of Windows or MacOS required to install the OpenBB Terminal?"),(0,l.kt)("p",null,"The OpenBB Terminal installation packages are compatible with:"),(0,l.kt)("ul",null,(0,l.kt)("li",{parentName:"ul"},"Windows 10 or later."),(0,l.kt)("li",{parentName:"ul"},"MacOS Monterey or later.")),(0,l.kt)("p",null,(0,l.kt)("strong",{parentName:"p"},"Note:")," Machines which are not compatible with the installer packages may be able to install from the source code.")),(0,l.kt)("details",null,(0,l.kt)("summary",null,"How do I update my installation to the latest version?"),(0,l.kt)("p",null,"The terminal is constantly being updated with new features and bug fixes. The process for updating will vary by the installation type:"),(0,l.kt)("ul",null,(0,l.kt)("li",{parentName:"ul"},"As of version 2.4.1, the Windows installer has an option for uninstalling the existing prior to updating."),(0,l.kt)("li",{parentName:"ul"},"For other installer versions, uninstall the previous version (uninstall.exe for Windows, delete the Application folder on MacOS); then, download the latest version and reinstall. User settings and data will remain."),(0,l.kt)("li",{parentName:"ul"},"For a ",(0,l.kt)("inlineCode",{parentName:"li"},"pip")," installation, when a new version is published: ",(0,l.kt)("inlineCode",{parentName:"li"},"pip install -U openbb[all]")),(0,l.kt)("li",{parentName:"ul"},"Upgrade a cloned version of the GitHub repo with:")),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-console"},"git fetch\ngit pull\npoetry install -E all\n")),(0,l.kt)("p",null,(0,l.kt)("strong",{parentName:"p"},"Notes:")," If the cloned repository is a fork, pull from: ",(0,l.kt)("inlineCode",{parentName:"p"},"git pull origin main")," or ",(0,l.kt)("inlineCode",{parentName:"p"},"git pull origin develop"),". If there are changes locally to the files that conflict with the incoming changes from GitHub, stash them before pulling from main with ",(0,l.kt)("inlineCode",{parentName:"p"},"git stash"),".")),(0,l.kt)("details",null,(0,l.kt)("summary",null,'"Microsoft Visual C++ 14.0 or greater is required"'),(0,l.kt)("p",null,"Download and install ",(0,l.kt)("a",{parentName:"p",href:"https://visualstudio.microsoft.com/visual-cpp-build-tools/"},"C++ Build Tools"),", restart the machine, then try again.")),(0,l.kt)("details",null,(0,l.kt)("summary",null,"Error: failed building wheel for bt"),(0,l.kt)("p",null,'There may be an additional message that is printed from this error, stating: "Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools".'),(0,l.kt)("p",null,"Download and install it. ",(0,l.kt)("a",{parentName:"p",href:"https://visualstudio.microsoft.com/visual-cpp-build-tools/"},"https://visualstudio.microsoft.com/visual-cpp-build-tools/")),(0,l.kt)("p",null,"Mac and Linux users may also encounter a similar error because a C++ compiler is not installed. Install Homebrew:"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-console"},'/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"\n')),(0,l.kt)("p",null,"Then run:"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-console"},"brew install gcc\nbrew install cmake\n"))),(0,l.kt)("details",null,(0,l.kt)("summary",null,"Miniconda3 will not install on ARM/Linux Raspberry Pi machines."),(0,l.kt)("p",null,"Refer to this issue on the Conda ",(0,l.kt)("a",{parentName:"p",href:"https://github.com/conda/conda/issues/10723"},"GitHub")," page.")),(0,l.kt)("h2",{id:"launching"},"Launching"),(0,l.kt)("details",null,(0,l.kt)("summary",null,"Mac: Invalid CPU Type - Terminal fails to launch."),(0,l.kt)("p",null,"This error is usually the result of a Mac M1/M2 machine which does not have Rosetta installed. Install from the system Terminal command line:"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-console"},"softwareupdate --install-rosetta\n")),(0,l.kt)("details",null,(0,l.kt)("summary",null,"Terminal app does not launch: Failed to execute script 'terminal' due to unhandled exception!"),(0,l.kt)("p",null,"When an installer-packaged version of the OpenBB Terminal fails to launch, because of this message, the machine may have an obsolete CPU-type or operating system. Please try installing via the source code, and if problems persist, reach out to us on ",(0,l.kt)("a",{parentName:"p",href:"https://discord.gg/xPHTuHCmuV"},"Discord")," or fill out a support request form on our ",(0,l.kt)("a",{parentName:"p",href:"https://openbb.co/support"},"website"),".")),(0,l.kt)("details",null,(0,l.kt)("summary",null,"ModuleNotFoundError: No module named '______'"),(0,l.kt)("p",null,"Before troubleshooting please verify that the recommended installation instructions were followed. These errors often can occur when the virtual environment has not been activated, or the ",(0,l.kt)("inlineCode",{parentName:"p"},"poetry install")," command was skipped. Activate the OpenBB virtual environment created during the installation process prior to launching or importing the SDK."),(0,l.kt)("p",null,(0,l.kt)("strong",{parentName:"p"},"Terminal"),":"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-console"},"conda activate obb\npython terminal.py\n")),(0,l.kt)("p",null,(0,l.kt)("strong",{parentName:"p"},"SDK"),":"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-console"},"conda activate obb\nipython\nfrom openbb_terminal.sdk import openbb\n")),(0,l.kt)("p",null,(0,l.kt)("strong",{parentName:"p"},"Jupyter"),":"),(0,l.kt)("p",null,"Check that the kernel selected for the session is the OpenBB virtual environment created during the installation process and then re-run the cell."),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-console"},"from openbb_terminal.sdk import openbb\n")),(0,l.kt)("p",null,"There is also a possibility that a new dependency has been added to the code and it has not yet been installed in the environment. This may happen after updating the code from GitHub, but before running the ",(0,l.kt)("inlineCode",{parentName:"p"},"poetry install")," install command."),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-console"},"poetry install -E all\n"))),(0,l.kt)("details",null,(0,l.kt)("summary",null,"Fontconfig warning: ignoring UTF-8: not a valid region tag"),(0,l.kt)("p",null,"In the OS default terminal shell profile, check for a variable similar to, \u201cset locale environment variables at startup\u201d, then also, set text encoding to UTF-8.")),(0,l.kt)("details",null,(0,l.kt)("summary",null,"SSL certificates fail to authorize"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-console"},"SSL: CERTIFICATE_VERIFY_FAILED\n")),(0,l.kt)("p",null,"An error message, similar to above, is usually encountered while attempting to use the OpenBB Platform from behind a firewall.  A workplace environment is typically the most common occurrence.  Try connecting to the internet directly through a home network to test the connection. If using a work computer and/or network,  we recommend speaking with the company's IT department prior to installing or running any software."),(0,l.kt)("p",null,"A potential solution is to try:"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-console"},"pip install pip-system-certs\n"))),(0,l.kt)("details",null,(0,l.kt)("summary",null,"Cannot connect due to proxy connection."),(0,l.kt)("p",null,"Find the ",(0,l.kt)("inlineCode",{parentName:"p"},".env")," file (located at the root of the user account folder: (",(0,l.kt)("inlineCode",{parentName:"p"},"~/.openbb_terminal/.env"),"), and add a line at the bottom of the file with:"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-console"},'HTTP_PROXY="<ADDRESS>" or HTTPS_PROXY="<ADDRESS>\u201d \n'))),(0,l.kt)("details",null,(0,l.kt)("summary",null," Linux Ubuntu installation was successful but now hangs on launch."),(0,l.kt)("p",null,"Check that VcXsvr - or an equivalent X-host - is running and configured prior to launch.")),(0,l.kt)("h2",{id:"general-operation"},"General Operation"),(0,l.kt)("details",null,(0,l.kt)("summary",null,"Charts do not display on Linux/WSL or Docker installation."),(0,l.kt)("p",null,"Check that X-11, or similar, is installed, open, and configured. Follow the instructions pertaining to the system here: ",(0,l.kt)("a",{parentName:"p",href:"https://docs.openbb.co/terminal/quickstart/installation#3-configuring-your-x-server-to-show-plots"},"https://docs.openbb.co/terminal/quickstart/installation#3-configuring-your-x-server-to-show-plots"))),(0,l.kt)("details",null,(0,l.kt)("summary",null,"How do I retrieve more results than is returned by default?"),(0,l.kt)("p",null,"Most functions will have either, ",(0,l.kt)("inlineCode",{parentName:"p"},"--start")," and ",(0,l.kt)("inlineCode",{parentName:"p"},"--end")," flags, or a ",(0,l.kt)("inlineCode",{parentName:"p"},"--limit")," argument. Print the help dialogue for any command by attaching, ",(0,l.kt)("inlineCode",{parentName:"p"},"--help")," or ",(0,l.kt)("inlineCode",{parentName:"p"},"-h"),".")),(0,l.kt)("details",null,(0,l.kt)("summary",null,"Does the portfolio menu allow for dividends, interest, or other distributions?"),(0,l.kt)("p",null,"Currently, this is only possible by manually updating the portfolio file.")),(0,l.kt)("details",null,(0,l.kt)("summary",null,"Why does my Portfolio file fail to load?"),(0,l.kt)("p",null,"This can be the result of a formatting error, check the file in a simple text editor to observe any abnormalities in the formatting; or, it could be a bug - check the ",(0,l.kt)("a",{parentName:"p",href:"https://github.com/OpenBB-finance/OpenBBTerminal/issues"},"GitHub issues page")," for similar errors."),(0,l.kt)("ul",null,(0,l.kt)("li",{parentName:"ul"},"Check that all the necessary column titles are present."),(0,l.kt)("li",{parentName:"ul"},"Inspect the file to see if cells left blank have been filled unintentionally with 0 or NaN values."),(0,l.kt)("li",{parentName:"ul"},"A particular asset may not be able to load data. Check for valid historical data from the Stocks menu."),(0,l.kt)("li",{parentName:"ul"},"Format ticker symbols according to yFinance naming convention."),(0,l.kt)("li",{parentName:"ul"},"All dates must be entered as YYYY-MM-DD."),(0,l.kt)("li",{parentName:"ul"},"Transactions dated for today will fail to load historical data."),(0,l.kt)("li",{parentName:"ul"},"MacOS users should attempt to avoid using the Numbers application as it has a habit of changing the formatting while saving.")),(0,l.kt)("p",null,"Files can be formatted as either ",(0,l.kt)("inlineCode",{parentName:"p"},".csv")," or ",(0,l.kt)("inlineCode",{parentName:"p"},".xlsx")," files, and the required column headers are:"),(0,l.kt)("p",null,(0,l.kt)("inlineCode",{parentName:"p"},"[Date,Type,Ticker,Side,Price,Quantity,Fees,Investment,Currency,Sector,Industry,Country,Region]")),(0,l.kt)("p",null,"See the guide ",(0,l.kt)("a",{parentName:"p",href:"https://docs.openbb.co/sdk/guides/intros/portfolio"},"here")," for more information.")),(0,l.kt)("details",null,(0,l.kt)("summary",null,"How do I change the chart styles?"),(0,l.kt)("p",null,"Place style sheets in this folder: ",(0,l.kt)("inlineCode",{parentName:"p"},"OpenBBUserData/styles/user")),(0,l.kt)("p",null,"SDK users can refer to the documentation ",(0,l.kt)("a",{parentName:"p",href:"https://docs.openbb.co/sdk/guides/advanced/chart-styling"},"here")," for syntax. A sample Matplotlib configuration file can be copied from ",(0,l.kt)("a",{parentName:"p",href:"https://matplotlib.org/stable/tutorials/introductory/customizing.html#the-default-matplotlibrc-file"},"here"),".")),(0,l.kt)("details",null,(0,l.kt)("summary",null,"Can I change the colors of the text in the Terminal?"),(0,l.kt)("p",null,"Yes, follow the directions on this page: ",(0,l.kt)("a",{parentName:"p",href:"https://openbb.co/products/terminal?customizeMenu=true#terminal"},"https://openbb.co/products/terminal?customizeMenu=true#terminal"))),(0,l.kt)("details",null,(0,l.kt)("summary",null,"After setting the preset in the stocks screener, nothing happens."),(0,l.kt)("p",null,"Print the current screen again with by entering, ",(0,l.kt)("inlineCode",{parentName:"p"},"?"),". Does the name of the selected preset display? With a preset loaded, run the screener by entering one of the commands below:"),(0,l.kt)("ul",null,(0,l.kt)("li",{parentName:"ul"},"Financial"),(0,l.kt)("li",{parentName:"ul"},"Ownership"),(0,l.kt)("li",{parentName:"ul"},"Overview"),(0,l.kt)("li",{parentName:"ul"},"Performance"),(0,l.kt)("li",{parentName:"ul"},"Technical"),(0,l.kt)("li",{parentName:"ul"},"Valuation"))),(0,l.kt)("details",null,(0,l.kt)("summary",null,"Forecast functions say to enter a valid data set"),(0,l.kt)("p",null,"Because an unlimited number of data sets can be loaded into the Forecast menu, each function requires defining the specific data set to be used. Add the ",(0,l.kt)("inlineCode",{parentName:"p"},"-d")," or ",(0,l.kt)("inlineCode",{parentName:"p"},"--dataset")," argument to the command, along with the name of the desired data set."),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-console"},"rnn -d SPY\n"))),(0,l.kt)("h2",{id:"data-and-sources"},"Data and Sources"),(0,l.kt)("p",null,"Please note that OpenBB does not provide any data, it is an aggregator which provides users access to data from a variety of sources. OpenBB does not maintain or have any control over the raw data supplied. If there is a specific problem with the output from a data provider, please consider contacting them first."),(0,l.kt)("details",null,(0,l.kt)("summary",null,"Data from today is missing."),(0,l.kt)("p",null,"By default, the load function requests end-of-day daily data and is not included until the EOD summary has been published. The current day's data is considered intraday and is loaded when the ",(0,l.kt)("inlineCode",{parentName:"p"},"interval")," argument is present."),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-console"},"load SPY -i 60\n"))),(0,l.kt)("details",null,(0,l.kt)("summary",null,"Can I stream live prices and news feeds?"),(0,l.kt)("p",null,"The OpenBB Terminal is not currently capable of streaming live feeds through websocket connections.")),(0,l.kt)("details",null,(0,l.kt)("summary",null,'"Pair BTC/USDT not found in binance"'),(0,l.kt)("p",null,"US-based users are currently unable to access the Binance API. Please try loading the pair from a different source, for example:"),(0,l.kt)("p",null,(0,l.kt)("inlineCode",{parentName:"p"},"load btc --source CCXT --exchange kraken"))),(0,l.kt)("h2",{id:"general-troubleshooting"},"General Troubleshooting"),(0,l.kt)("p",null,'Both Windows and MacOS provide a "developer mode", and enabling it may help.'),(0,l.kt)("p",null,(0,l.kt)("strong",{parentName:"p"},"MacOS"),': Go to the System Settings, and under the "Privacy and Security" tab, scroll to the bottom and select the option to "Allow applications downloaded from App Store and identified developers". Then, scroll up to click on, "Developer Tools", and add ',(0,l.kt)("inlineCode",{parentName:"p"},"Terminal.app")," and ",(0,l.kt)("inlineCode",{parentName:"p"},"Visual Studio Code")," (or the preferred code editor) to the list of applications allowed to run software locally that does not meet the system's security policy."),(0,l.kt)("p",null,(0,l.kt)("strong",{parentName:"p"},"Windows"),': Go to the Control Panel, and under the "Privacy & Security" tab, click on, "For developers". Under this menu, turn "Developer Mode" on.'),(0,l.kt)("p",null,'From the Windows Security menu, click on the Firewall & Network Protection tab, then click on "Allow an app through firewall". If the applications below are not allowed to communicate through Windows Defender Firewall, change the settings to allow.'),(0,l.kt)("ul",null,(0,l.kt)("li",{parentName:"ul"},"BranchCache"),(0,l.kt)("li",{parentName:"ul"},"Hyper-V"),(0,l.kt)("li",{parentName:"ul"},"VcXsrv"),(0,l.kt)("li",{parentName:"ul"},"Windows Terminal"))),(0,l.kt)("details",null,(0,l.kt)("summary",null,"Why does a specific menu or command not exist?"),(0,l.kt)("p",null,"It could be that you are running an outdated version in which the menu or command is not yet available. Please check the ",(0,l.kt)("a",{parentName:"p",href:"https://docs.openbb.co/terminal/quickstart/installation"},"installation guide")," to download the most recent release."),(0,l.kt)("p",null,"Do note that it is also possible that the menu or command has been deprecated. If this is oversight, please reach out to us ",(0,l.kt)("a",{parentName:"p",href:"https://openbb.co/support"},"here"),".")),(0,l.kt)("h2",{id:"bugs-support-and-feedback"},"Bugs, Support, and Feedback"),(0,l.kt)("p",null,"When an error is encountered, it is always a good idea to check the open issues on ",(0,l.kt)("a",{parentName:"p",href:"https://github.com/OpenBB-finance/OpenBBTerminal/issues"},"GitHub"),". There may be a workaround solution for the specific problem until a patch is released."),(0,l.kt)("details",null,(0,l.kt)("summary",null,"How often are patches for bugs released?"),(0,l.kt)("p",null,"The installer versions are packaged approximately every two-weeks. Those working with a cloned GitHub version can checkout the Develop branch to get the latest fixes and releases before they are pushed to the main branch."),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-console"},"git checkout develop\n"))),(0,l.kt)("details",null,(0,l.kt)("summary",null,"How do I report a bug?"),(0,l.kt)("p",null,"First, search the open issues for another report. If one already exists, attach any relevant information and screenshots as a comment. If one does not exist, start one with this ",(0,l.kt)("a",{parentName:"p",href:"https://github.com/OpenBB-finance/OpenBBTerminal/issues/new?assignees=&labels=type%3Abug&template=bug_report.md&title=%5BBug%5D"},"link"))),(0,l.kt)("details",null,(0,l.kt)("summary",null,"How can I get help with OpenBB Terminal?"),(0,l.kt)("p",null,"You can get help with OpenBB Terminal by joining our ",(0,l.kt)("a",{parentName:"p",href:"https://openbb.co/discord"},"Discord server")," or contact us in our support form ",(0,l.kt)("a",{parentName:"p",href:"https://openbb.co/support"},"here"),".")),(0,l.kt)("details",null,(0,l.kt)("summary",null,"How can I give feedback about the OpenBB Terminal, or request specific functionality?"),(0,l.kt)("p",null,"Being an open source platform that wishes to tailor to the needs of any type of investor, we highly encourage anyone to share with us their experience and/or how we can further improve the OpenBB Terminal. This can be anything from a very small bug, a new feature, or the implementation of a highly advanced Machine Learning model."),(0,l.kt)("p",null,"You are able to directly send us information about a bug or a question/suggestion from inside the terminal by using the ",(0,l.kt)("inlineCode",{parentName:"p"},"support")," command which is available everywhere in the terminal. Here you can select which command you want to report a bug on, ask a question or make a suggestion. After entering ",(0,l.kt)("inlineCode",{parentName:"p"},"support"),", when you press ",(0,l.kt)("inlineCode",{parentName:"p"},"ENTER")," (\u23ce), you are taken to the Support form which is automatically filled with your input. You are only required to include the type (e.g. bug, suggestion or question) and message in the form, although this can also be set directly from inside the terminal (see ",(0,l.kt)("inlineCode",{parentName:"p"},"support -h"),")."),(0,l.kt)("p",null,"Alternatively, you can contact us via the following routes:"),(0,l.kt)("ul",null,(0,l.kt)("li",{parentName:"ul"},"If you notice that a feature is missing inside the terminal, please fill in the ",(0,l.kt)("a",{parentName:"li",href:"https://openbb.co/request-a-feature"},"Request a Feature")," form."),(0,l.kt)("li",{parentName:"ul"},"If you wish to report a bug, have a question/suggestion or anything else, please fill in the ",(0,l.kt)("a",{parentName:"li",href:"https://openbb.co/support"},"Support")," form."),(0,l.kt)("li",{parentName:"ul"},"If you wish to speak to us directly, please contact us on ",(0,l.kt)("a",{parentName:"li",href:"https://openbb.co/discord"},"Discord"),"."))),(0,l.kt)("h2",{id:"developer-issues"},"Developer Issues"),(0,l.kt)("details",null,(0,l.kt)("summary",null,'Error: "git pull" fails because of a hot fix: cannot lock ref'),(0,l.kt)("p",null,"If the error message looks something like:"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-console"},"cannot lock ref: 'refs/remotes/origin/hotfix' exists; cannot create\n")),(0,l.kt)("p",null,"Try:"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-console"},"git remote prune origin\ngit pull\n"))),(0,l.kt)("details",null,(0,l.kt)("summary",null,"What does it mean if it says wheel is missing?"),(0,l.kt)("p",null,"If you receive any notifications regarding ",(0,l.kt)("inlineCode",{parentName:"p"},"wheel")," missing, this could be due to this dependency missing."),(0,l.kt)("p",null,(0,l.kt)("inlineCode",{parentName:"p"},"conda install -c conda-forge wheel")," or ",(0,l.kt)("inlineCode",{parentName:"p"},"pip install wheel"))),(0,l.kt)("details",null,(0,l.kt)("summary",null,"Why do these .whl files not exist?"),(0,l.kt)("p",null,"If you get errors about .whl files not existing (usually on Windows) you have to reinitialize the following folder.\nJust removing the 'artifacts' folder could also be enough:"),(0,l.kt)("table",null,(0,l.kt)("thead",{parentName:"table"},(0,l.kt)("tr",{parentName:"thead"},(0,l.kt)("th",{parentName:"tr",align:null},"Platform"),(0,l.kt)("th",{parentName:"tr",align:null},"Location"))),(0,l.kt)("tbody",{parentName:"table"},(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"Linux"),(0,l.kt)("td",{parentName:"tr",align:null},'"~/.cache/pypoetry"')),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"Mac"),(0,l.kt)("td",{parentName:"tr",align:null},'"~/Library/Caches/pypoetry"')),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"Windows"),(0,l.kt)("td",{parentName:"tr",align:null},'"%localappdata%/pypoetry/cache"')))),(0,l.kt)("p",null,"When you try to add a package to Poetry it is possible that it causes a similar issue. Here you can remove the\n'artifacts' folder again to reinitialize Poetry."),(0,l.kt)("p",null,"If you run into trouble with Poetry, and the advice above did not help, your best bet is to try"),(0,l.kt)("ul",null,(0,l.kt)("li",{parentName:"ul"},(0,l.kt)("inlineCode",{parentName:"li"},"poetry update --lock")),(0,l.kt)("li",{parentName:"ul"},(0,l.kt)("inlineCode",{parentName:"li"},"conda deactivate")," -> ",(0,l.kt)("inlineCode",{parentName:"li"},"conda activate obb"),", then try again"),(0,l.kt)("li",{parentName:"ul"},"Track down the offensive package and purge it from your anaconda ",(0,l.kt)("inlineCode",{parentName:"li"},"<environment_name>")," folder, then try again")),(0,l.kt)("table",null,(0,l.kt)("thead",{parentName:"table"},(0,l.kt)("tr",{parentName:"thead"},(0,l.kt)("th",{parentName:"tr",align:null},"Platform"),(0,l.kt)("th",{parentName:"tr",align:null},"Location"))),(0,l.kt)("tbody",{parentName:"table"},(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"Linux/Mac"),(0,l.kt)("td",{parentName:"tr",align:null},"~/anaconda3/envs, or , ~/opt/anaconda3/envs")),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"Windows"),(0,l.kt)("td",{parentName:"tr",align:null},"%userprofile%/anaconda3/envs")))),(0,l.kt)("ul",null,(0,l.kt)("li",{parentName:"ul"},(0,l.kt)("p",{parentName:"li"},"Completely nuke your conda environment folder and make a new environment from scratch"),(0,l.kt)("ul",{parentName:"li"},(0,l.kt)("li",{parentName:"ul"},(0,l.kt)("inlineCode",{parentName:"li"},"conda deactivate")),(0,l.kt)("li",{parentName:"ul"},(0,l.kt)("inlineCode",{parentName:"li"},"conda env remove -n obb")),(0,l.kt)("li",{parentName:"ul"},(0,l.kt)("inlineCode",{parentName:"li"},"conda clean -a")),(0,l.kt)("li",{parentName:"ul"},"Make a new environment and install dependencies again."))),(0,l.kt)("li",{parentName:"ul"},(0,l.kt)("p",{parentName:"li"},"Reboot your computer and try again")),(0,l.kt)("li",{parentName:"ul"},(0,l.kt)("p",{parentName:"li"},"Submit a ticket on GitHub")))),(0,l.kt)("details",null,(0,l.kt)("summary",null,"What does the JSONDecodeError mean during poetry install?"),(0,l.kt)("p",null,"Sometimes poetry can throw a ",(0,l.kt)("inlineCode",{parentName:"p"},"JSONDecodeError")," on random packages while running ",(0,l.kt)("inlineCode",{parentName:"p"},"poetry install"),". This can be observed on macOS 10.14+ running python 3.8+. This is because of the use of an experimental installer that can be switched off to avoid the mentioned error. Run the code below as advised ",(0,l.kt)("a",{parentName:"p",href:"https://github.com/python-poetry/poetry/issues/4210"},"here")," and it should fix the installation process."),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-bash"},"poetry config experimental.new-installer false\n")),(0,l.kt)("p",null,(0,l.kt)("em",{parentName:"p"},"Commands that may help you in case of an error:")),(0,l.kt)("ul",null,(0,l.kt)("li",{parentName:"ul"},(0,l.kt)("inlineCode",{parentName:"li"},"python -m pip install --upgrade pip")),(0,l.kt)("li",{parentName:"ul"},(0,l.kt)("inlineCode",{parentName:"li"},"poetry update --lock")),(0,l.kt)("li",{parentName:"ul"},(0,l.kt)("inlineCode",{parentName:"li"},"poetry install")))),(0,l.kt)("details",null,(0,l.kt)("summary",null,"How do I deal with errors regarding CRLF?"),(0,l.kt)("p",null,"When trying to commit code changes, pylint will prevent you from doing so if your line break settings are set to\nCRLF (default for Windows).\nThis is because the entire package uses LF (default for Linux/Mac), and it is therefore\nimportant that you change this setting to LF ",(0,l.kt)("em",{parentName:"p"},"before")," you make any changes to the code."),(0,l.kt)("p",null,"It is possible that CRLF automatically turns back on, you can correct this with:"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-bash"},"git config --global core.autocrlf false\n")),(0,l.kt)("p",null,"In case you already made coding adjustments, you have to reset your cache, and the changes you made to the code with\nthe following:"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-bash"},"git rm --cached -r .\ngit reset --hard\n"))),(0,l.kt)("details",null,(0,l.kt)("summary",null,"Why can't I run OpenBB via the VS Code integrated terminal?"),(0,l.kt)("p",null,"This occurs when VS Code terminal python version/path is different from the terminal version."),(0,l.kt)("p",null,"To fix it add this to vscode JSON settings (",(0,l.kt)("a",{parentName:"p",href:"https://stackoverflow.com/questions/54582361/vscode-terminal-shows-incorrect-python-version-and-path-launching-terminal-from"},"ref"),"):"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-bash"},'    "terminal.integrated.inheritEnv": false,\n'))))}d.isMDXComponent=!0}}]);