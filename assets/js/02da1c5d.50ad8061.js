"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[15597],{3905:(e,t,a)=>{a.d(t,{Zo:()=>m,kt:()=>g});var n=a(67294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function i(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function l(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?i(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function s(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},i=Object.keys(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var o=n.createContext({}),c=function(e){var t=n.useContext(o),a=t;return e&&(a="function"==typeof e?e(t):l(l({},t),e)),a},m=function(e){var t=c(e.components);return n.createElement(o.Provider,{value:t},e.children)},u="mdxType",p={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},d=n.forwardRef((function(e,t){var a=e.components,r=e.mdxType,i=e.originalType,o=e.parentName,m=s(e,["components","mdxType","originalType","parentName"]),u=c(a),d=r,g=u["".concat(o,".").concat(d)]||u[d]||p[d]||i;return a?n.createElement(g,l(l({ref:t},m),{},{components:a})):n.createElement(g,l({ref:t},m))}));function g(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var i=a.length,l=new Array(i);l[0]=d;var s={};for(var o in t)hasOwnProperty.call(t,o)&&(s[o]=t[o]);s.originalType=e,s[u]="string"==typeof e?e:r,l[1]=s;for(var c=2;c<i;c++)l[c]=a[c];return n.createElement.apply(null,l)}return n.createElement.apply(null,a)}d.displayName="MDXCreateElement"},61853:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>o,contentTitle:()=>l,default:()=>p,frontMatter:()=>i,metadata:()=>s,toc:()=>c});var n=a(87462),r=(a(67294),a(3905));const i={title:"search",description:"OpenBB Terminal Function"},l="search",s={unversionedId:"reference/stocks/search",id:"reference/stocks/search",title:"search",description:"OpenBB Terminal Function",source:"@site/content/terminal/reference/stocks/search.md",sourceDirName:"reference/stocks",slug:"/reference/stocks/search",permalink:"/terminal/reference/stocks/search",draft:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/terminal/reference/stocks/search.md",tags:[],version:"current",frontMatter:{title:"search",description:"OpenBB Terminal Function"},sidebar:"tutorialSidebar",previous:{title:"view",permalink:"/terminal/reference/stocks/screener/view"},next:{title:"country",permalink:"/terminal/reference/stocks/sia/country"}},o={},c=[{value:"Usage",id:"usage",level:3},{value:"Parameters",id:"parameters",level:2}],m={toc:c},u="wrapper";function p(e){let{components:t,...a}=e;return(0,r.kt)(u,(0,n.Z)({},m,a,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"search"},"search"),(0,r.kt)("p",null,"Show companies matching the search query, country, sector, industry and/or exchange. Note that by default only the United States exchanges are searched which tend to contain the most extensive data for each company. To search all exchanges use the --all-exchanges flag."),(0,r.kt)("h3",{id:"usage"},"Usage"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python",metastring:"wordwrap",wordwrap:!0},"search [-q QUERY [QUERY ...]] [-c country] [-s sector] [-g industry_group] [-i industry] [-e exchange] [-a]\n")),(0,r.kt)("hr",null),(0,r.kt)("h2",{id:"parameters"},"Parameters"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},"Name"),(0,r.kt)("th",{parentName:"tr",align:null},"Parameter"),(0,r.kt)("th",{parentName:"tr",align:null},"Description"),(0,r.kt)("th",{parentName:"tr",align:null},"Default"),(0,r.kt)("th",{parentName:"tr",align:null},"Optional"),(0,r.kt)("th",{parentName:"tr",align:null},"Choices"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"query"),(0,r.kt)("td",{parentName:"tr",align:null},"-q  --query"),(0,r.kt)("td",{parentName:"tr",align:null},"The search term used to find company tickers"),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"None")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"country"),(0,r.kt)("td",{parentName:"tr",align:null},"-c  --country"),(0,r.kt)("td",{parentName:"tr",align:null},"Search by country to find stocks matching the criteria"),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"afghanistan, anguilla, argentina, australia, austria, azerbaijan, bahamas, bangladesh, barbados, belgium, belize, bermuda, botswana, brazil, british_virgin_islands, cambodia, canada, cayman_islands, chile, china, colombia, costa_rica, cyprus, czech_republic, denmark, dominican_republic, egypt, estonia, falkland_islands, finland, france, french_guiana, gabon, georgia, germany, ghana, gibraltar, greece, greenland, guernsey, hong_kong, hungary, iceland, india, indonesia, ireland, isle_of_man, israel, italy, ivory_coast, japan, jersey, jordan, kazakhstan, kyrgyzstan, latvia, liechtenstein, lithuania, luxembourg, macau, macedonia, malaysia, malta, mauritius, mexico, monaco, mongolia, montenegro, morocco, mozambique, myanmar, namibia, netherlands, netherlands_antilles, new_zealand, nigeria, norway, panama, papua_new_guinea, peru, philippines, poland, portugal, qatar, reunion, romania, russia, saudi_arabia, senegal, singapore, slovakia, slovenia, south_africa, south_korea, spain, suriname, sweden, switzerland, taiwan, tanzania, thailand, turkey, ukraine, united_arab_emirates, united_kingdom, united_states, uruguay, vietnam, zambia")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"sector"),(0,r.kt)("td",{parentName:"tr",align:null},"-s  --sector"),(0,r.kt)("td",{parentName:"tr",align:null},"Search by sector to find stocks matching the criteria"),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"communication_services, consumer_discretionary, consumer_staples, energy, financials, health_care, industrials, information_technology, materials, real_estate, utilities")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"industry_group"),(0,r.kt)("td",{parentName:"tr",align:null},"-g  --industrygroup"),(0,r.kt)("td",{parentName:"tr",align:null},"Search by industry group to find stocks matching the criteria"),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"automobiles",(0,r.kt)("em",{parentName:"td"},"&_components, banks, capital_goods, commercial"),"&",(0,r.kt)("em",{parentName:"td"},"professional_services, consumer_durables"),"&",(0,r.kt)("em",{parentName:"td"},"apparel, consumer_services, diversified_financials, energy, food"),"&",(0,r.kt)("em",{parentName:"td"},"staples_retailing, food,_beverage"),"&",(0,r.kt)("em",{parentName:"td"},"tobacco, health_care_equipment"),"&",(0,r.kt)("em",{parentName:"td"},"services, household"),"&",(0,r.kt)("em",{parentName:"td"},"personal_products, insurance, materials, media"),"&",(0,r.kt)("em",{parentName:"td"},"entertainment, pharmaceuticals,_biotechnology"),"&",(0,r.kt)("em",{parentName:"td"},"life_sciences, real_estate, retailing, semiconductors"),"&",(0,r.kt)("em",{parentName:"td"},"semiconductor_equipment, software"),"&",(0,r.kt)("em",{parentName:"td"},"services, technology_hardware"),"&_equipment, telecommunication_services, transportation, utilities")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"industry"),(0,r.kt)("td",{parentName:"tr",align:null},"-i  --industry"),(0,r.kt)("td",{parentName:"tr",align:null},"Search by industry to find stocks matching the criteria"),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"aerospace",(0,r.kt)("em",{parentName:"td"},"&_defense, air_freight"),"&",(0,r.kt)("em",{parentName:"td"},"logistics, airlines, auto_components, automobiles, banks, beverages, biotechnology, building_products, capital_markets, chemicals, commercial_services"),"&",(0,r.kt)("em",{parentName:"td"},"supplies, communications_equipment, construction"),"&",(0,r.kt)("em",{parentName:"td"},"engineering, construction_materials, consumer_finance, distributors, diversified_consumer_services, diversified_financial_services, diversified_telecommunication_services, electric_utilities, electrical_equipment, electronic_equipment,_instruments"),"&",(0,r.kt)("em",{parentName:"td"},"components, energy_equipment"),"&",(0,r.kt)("em",{parentName:"td"},"services, entertainment, equity_real_estate_investment_trusts"),"(reits), food",(0,r.kt)("em",{parentName:"td"},"&_staples_retailing, gas_utilities, health_care_equipment"),"&",(0,r.kt)("em",{parentName:"td"},"supplies, health_care_providers"),"&",(0,r.kt)("em",{parentName:"td"},"services, health_care_technology, hotels,_restaurants"),"&",(0,r.kt)("em",{parentName:"td"},"leisure, household_durables, household_products, it_services, independent_power_and_renewable_electricity_producers, industrial_conglomerates, insurance, interactive_media"),"&",(0,r.kt)("em",{parentName:"td"},"services, internet"),"&",(0,r.kt)("em",{parentName:"td"},"direct_marketing_retail, machinery, marine, media, metals"),"&",(0,r.kt)("em",{parentName:"td"},"mining, multi-utilities, oil,_gas"),"&",(0,r.kt)("em",{parentName:"td"},"consumable_fuels, paper"),"&",(0,r.kt)("em",{parentName:"td"},"forest_products, pharmaceuticals, professional_services, real_estate_management"),"&",(0,r.kt)("em",{parentName:"td"},"development, road"),"&",(0,r.kt)("em",{parentName:"td"},"rail, semiconductors"),"&",(0,r.kt)("em",{parentName:"td"},"semiconductor_equipment, software, specialty_retail, technology_hardware,_storage"),"&",(0,r.kt)("em",{parentName:"td"},"peripherals, textiles,_apparel"),"&",(0,r.kt)("em",{parentName:"td"},"luxury_goods, thrifts"),"&",(0,r.kt)("em",{parentName:"td"},"mortgage_finance, tobacco, trading_companies"),"&_distributors, transportation_infrastructure, water_utilities")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"exchange_country"),(0,r.kt)("td",{parentName:"tr",align:null},"-e  --exchange"),(0,r.kt)("td",{parentName:"tr",align:null},"Search by a specific exchange country to find stocks matching the criteria"),(0,r.kt)("td",{parentName:"tr",align:null}),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"united_states, argentina, austria, australia, belgium, brazil, canada, chile, china, czech_republic, denmark, egypt, estonia, europe, finland, france, germany, greece, hong_kong, hungary, iceland, india, indonesia, ireland, israel, italy, japan, latvia, lithuania, malaysia, mexico, netherlands, new_zealand, norway, portugal, qatar, russia, singapore, south_africa, south_korea, spain, saudi_arabia, sweden, switzerland, taiwan, thailand, turkey, united_kingdom, venezuela")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"all_exchanges"),(0,r.kt)("td",{parentName:"tr",align:null},"-a  --all-exchanges"),(0,r.kt)("td",{parentName:"tr",align:null},"Whether to search all exchanges, without this option only the United States market is searched."),(0,r.kt)("td",{parentName:"tr",align:null},"False"),(0,r.kt)("td",{parentName:"tr",align:null},"True"),(0,r.kt)("td",{parentName:"tr",align:null},"None")))),(0,r.kt)("hr",null))}p.isMDXComponent=!0}}]);