"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[41569],{3905:(t,e,n)=>{n.d(e,{Zo:()=>u,kt:()=>g});var r=n(67294);function a(t,e,n){return e in t?Object.defineProperty(t,e,{value:n,enumerable:!0,configurable:!0,writable:!0}):t[e]=n,t}function l(t,e){var n=Object.keys(t);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(t);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),n.push.apply(n,r)}return n}function o(t){for(var e=1;e<arguments.length;e++){var n=null!=arguments[e]?arguments[e]:{};e%2?l(Object(n),!0).forEach((function(e){a(t,e,n[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(n)):l(Object(n)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(n,e))}))}return t}function i(t,e){if(null==t)return{};var n,r,a=function(t,e){if(null==t)return{};var n,r,a={},l=Object.keys(t);for(r=0;r<l.length;r++)n=l[r],e.indexOf(n)>=0||(a[n]=t[n]);return a}(t,e);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(t);for(r=0;r<l.length;r++)n=l[r],e.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(t,n)&&(a[n]=t[n])}return a}var p=r.createContext({}),m=function(t){var e=r.useContext(p),n=e;return t&&(n="function"==typeof t?t(e):o(o({},e),t)),n},u=function(t){var e=m(t.components);return r.createElement(p.Provider,{value:e},t.children)},c="mdxType",d={inlineCode:"code",wrapper:function(t){var e=t.children;return r.createElement(r.Fragment,{},e)}},s=r.forwardRef((function(t,e){var n=t.components,a=t.mdxType,l=t.originalType,p=t.parentName,u=i(t,["components","mdxType","originalType","parentName"]),c=m(n),s=a,g=c["".concat(p,".").concat(s)]||c[s]||d[s]||l;return n?r.createElement(g,o(o({ref:e},u),{},{components:n})):r.createElement(g,o({ref:e},u))}));function g(t,e){var n=arguments,a=e&&e.mdxType;if("string"==typeof t||a){var l=n.length,o=new Array(l);o[0]=s;var i={};for(var p in e)hasOwnProperty.call(e,p)&&(i[p]=e[p]);i.originalType=t,i[c]="string"==typeof t?t:a,o[1]=i;for(var m=2;m<l;m++)o[m]=n[m];return r.createElement.apply(null,o)}return r.createElement.apply(null,n)}s.displayName="MDXCreateElement"},17980:(t,e,n)=>{n.r(e),n.d(e,{assets:()=>p,contentTitle:()=>o,default:()=>d,frontMatter:()=>l,metadata:()=>i,toc:()=>m});var r=n(87462),a=(n(67294),n(3905));const l={title:"anom",description:"OpenBB Terminal Function"},o="anom",i={unversionedId:"reference/forecast/anom",id:"reference/forecast/anom",title:"anom",description:"OpenBB Terminal Function",source:"@site/content/terminal/reference/forecast/anom.md",sourceDirName:"reference/forecast",slug:"/reference/forecast/anom",permalink:"/terminal/reference/forecast/anom",draft:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/terminal/reference/forecast/anom.md",tags:[],version:"current",frontMatter:{title:"anom",description:"OpenBB Terminal Function"},sidebar:"tutorialSidebar",previous:{title:"ycrv",permalink:"/terminal/reference/fixedincome/ycrv"},next:{title:"atr",permalink:"/terminal/reference/forecast/atr"}},p={},m=[{value:"Usage",id:"usage",level:3},{value:"Parameters",id:"parameters",level:2}],u={toc:m},c="wrapper";function d(t){let{components:e,...n}=t;return(0,a.kt)(c,(0,r.Z)({},u,n,{components:e,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"anom"},"anom"),(0,a.kt)("p",null,"Perform a Quantile Anomaly detection on a given dataset: ",(0,a.kt)("a",{parentName:"p",href:"https://unit8co.github.io/darts/generated_api/darts.ad.detectors.quantile_detector.html"},"https://unit8co.github.io/darts/generated_api/darts.ad.detectors.quantile_detector.html")),(0,a.kt)("h3",{id:"usage"},"Usage"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python",metastring:"wordwrap",wordwrap:!0},"anom [-d {}] [-c TARGET_COLUMN] [-t TRAIN_SPLIT] [--end S_END_DATE] [--start S_START_DATE] [--forecast-only]\n")),(0,a.kt)("hr",null),(0,a.kt)("h2",{id:"parameters"},"Parameters"),(0,a.kt)("table",null,(0,a.kt)("thead",{parentName:"table"},(0,a.kt)("tr",{parentName:"thead"},(0,a.kt)("th",{parentName:"tr",align:null},"Name"),(0,a.kt)("th",{parentName:"tr",align:null},"Parameter"),(0,a.kt)("th",{parentName:"tr",align:null},"Description"),(0,a.kt)("th",{parentName:"tr",align:null},"Default"),(0,a.kt)("th",{parentName:"tr",align:null},"Optional"),(0,a.kt)("th",{parentName:"tr",align:null},"Choices"))),(0,a.kt)("tbody",{parentName:"table"},(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"target_dataset"),(0,a.kt)("td",{parentName:"tr",align:null},"-d  --dataset"),(0,a.kt)("td",{parentName:"tr",align:null},"The name of the dataset you want to select"),(0,a.kt)("td",{parentName:"tr",align:null},"None"),(0,a.kt)("td",{parentName:"tr",align:null},"True"),(0,a.kt)("td",{parentName:"tr",align:null},"None")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"target_column"),(0,a.kt)("td",{parentName:"tr",align:null},"-c  --target-column"),(0,a.kt)("td",{parentName:"tr",align:null},"The name of the specific column you want to use"),(0,a.kt)("td",{parentName:"tr",align:null},"close"),(0,a.kt)("td",{parentName:"tr",align:null},"True"),(0,a.kt)("td",{parentName:"tr",align:null},"None")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"train_split"),(0,a.kt)("td",{parentName:"tr",align:null},"-t  --train-split"),(0,a.kt)("td",{parentName:"tr",align:null},"Start point for rolling training and forecast window. 0.0-1.0"),(0,a.kt)("td",{parentName:"tr",align:null},"0.85"),(0,a.kt)("td",{parentName:"tr",align:null},"True"),(0,a.kt)("td",{parentName:"tr",align:null},"None")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"s_end_date"),(0,a.kt)("td",{parentName:"tr",align:null},"--end"),(0,a.kt)("td",{parentName:"tr",align:null},"The end date (format YYYY-MM-DD) to select for testing"),(0,a.kt)("td",{parentName:"tr",align:null},"None"),(0,a.kt)("td",{parentName:"tr",align:null},"True"),(0,a.kt)("td",{parentName:"tr",align:null},"None")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"s_start_date"),(0,a.kt)("td",{parentName:"tr",align:null},"--start"),(0,a.kt)("td",{parentName:"tr",align:null},"The start date (format YYYY-MM-DD) to select for testing"),(0,a.kt)("td",{parentName:"tr",align:null},"None"),(0,a.kt)("td",{parentName:"tr",align:null},"True"),(0,a.kt)("td",{parentName:"tr",align:null},"None")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"forecast_only"),(0,a.kt)("td",{parentName:"tr",align:null},"--forecast-only"),(0,a.kt)("td",{parentName:"tr",align:null},"Do not plot the historical data without forecasts."),(0,a.kt)("td",{parentName:"tr",align:null},"False"),(0,a.kt)("td",{parentName:"tr",align:null},"True"),(0,a.kt)("td",{parentName:"tr",align:null},"None")))),(0,a.kt)("hr",null))}d.isMDXComponent=!0}}]);