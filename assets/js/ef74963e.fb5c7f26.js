"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[5138],{3905:(e,t,r)=>{r.d(t,{Zo:()=>u,kt:()=>f});var n=r(67294);function a(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function l(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function i(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?l(Object(r),!0).forEach((function(t){a(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):l(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function o(e,t){if(null==e)return{};var r,n,a=function(e,t){if(null==e)return{};var r,n,a={},l=Object.keys(e);for(n=0;n<l.length;n++)r=l[n],t.indexOf(r)>=0||(a[r]=e[r]);return a}(e,t);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(e);for(n=0;n<l.length;n++)r=l[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}var c=n.createContext({}),m=function(e){var t=n.useContext(c),r=t;return e&&(r="function"==typeof e?e(t):i(i({},t),e)),r},u=function(e){var t=m(e.components);return n.createElement(c.Provider,{value:t},e.children)},p="mdxType",s={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},d=n.forwardRef((function(e,t){var r=e.components,a=e.mdxType,l=e.originalType,c=e.parentName,u=o(e,["components","mdxType","originalType","parentName"]),p=m(r),d=a,f=p["".concat(c,".").concat(d)]||p[d]||s[d]||l;return r?n.createElement(f,i(i({ref:t},u),{},{components:r})):n.createElement(f,i({ref:t},u))}));function f(e,t){var r=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var l=r.length,i=new Array(l);i[0]=d;var o={};for(var c in t)hasOwnProperty.call(t,c)&&(o[c]=t[c]);o.originalType=e,o[p]="string"==typeof e?e:a,i[1]=o;for(var m=2;m<l;m++)i[m]=r[m];return n.createElement.apply(null,i)}return n.createElement.apply(null,r)}d.displayName="MDXCreateElement"},81088:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>c,contentTitle:()=>i,default:()=>s,frontMatter:()=>l,metadata:()=>o,toc:()=>m});var n=r(87462),a=(r(67294),r(3905));const l={title:"estr",description:"OpenBB Terminal Function"},i="estr",o={unversionedId:"reference/fixedincome/estr",id:"reference/fixedincome/estr",title:"estr",description:"OpenBB Terminal Function",source:"@site/content/terminal/reference/fixedincome/estr.md",sourceDirName:"reference/fixedincome",slug:"/reference/fixedincome/estr",permalink:"/terminal/reference/fixedincome/estr",draft:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/terminal/reference/fixedincome/estr.md",tags:[],version:"current",frontMatter:{title:"estr",description:"OpenBB Terminal Function"},sidebar:"tutorialSidebar",previous:{title:"ecbycrv",permalink:"/terminal/reference/fixedincome/ecbycrv"},next:{title:"fed",permalink:"/terminal/reference/fixedincome/fed"}},c={},m=[{value:"Usage",id:"usage",level:3},{value:"Parameters",id:"parameters",level:2}],u={toc:m},p="wrapper";function s(e){let{components:t,...r}=e;return(0,a.kt)(p,(0,n.Z)({},u,r,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"estr"},"estr"),(0,a.kt)("p",null,"The euro short-term rate (\u20acSTR) reflects the wholesale euro unsecured overnight borrowing costs of banks located in the euro area. The \u20acSTR is published on each TARGET2 business day based on transactions conducted and settled on the previous TARGET2 business day (the reporting date \u201cT\u201d) with a maturity date of T+1 which are deemed to have been executed at arm\u2019s length and thus reflect market rates in an unbiased way."),(0,a.kt)("h3",{id:"usage"},"Usage"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python",metastring:"wordwrap",wordwrap:!0},"estr [-p {volume_weighted_trimmed_mean_rate,number_of_transactions,number_of_active_banks,total_volume,share_of_volume_of_the_5_largest_active_banks,rate_at_75th_percentile_of_volume,rate_at_25th_percentile_of_volume}] [-s START_DATE] [-e END_DATE]\n")),(0,a.kt)("hr",null),(0,a.kt)("h2",{id:"parameters"},"Parameters"),(0,a.kt)("table",null,(0,a.kt)("thead",{parentName:"table"},(0,a.kt)("tr",{parentName:"thead"},(0,a.kt)("th",{parentName:"tr",align:null},"Name"),(0,a.kt)("th",{parentName:"tr",align:null},"Parameter"),(0,a.kt)("th",{parentName:"tr",align:null},"Description"),(0,a.kt)("th",{parentName:"tr",align:null},"Default"),(0,a.kt)("th",{parentName:"tr",align:null},"Optional"),(0,a.kt)("th",{parentName:"tr",align:null},"Choices"))),(0,a.kt)("tbody",{parentName:"table"},(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"parameter"),(0,a.kt)("td",{parentName:"tr",align:null},"-p  --parameter"),(0,a.kt)("td",{parentName:"tr",align:null},"Specific Euro Short-Term Rate data to retrieve"),(0,a.kt)("td",{parentName:"tr",align:null},"volume_weighted_trimmed_mean_rate"),(0,a.kt)("td",{parentName:"tr",align:null},"True"),(0,a.kt)("td",{parentName:"tr",align:null},"volume_weighted_trimmed_mean_rate, number_of_transactions, number_of_active_banks, total_volume, share_of_volume_of_the_5_largest_active_banks, rate_at_75th_percentile_of_volume, rate_at_25th_percentile_of_volume")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"start_date"),(0,a.kt)("td",{parentName:"tr",align:null},"-s  --start"),(0,a.kt)("td",{parentName:"tr",align:null},"Starting date (YYYY-MM-DD) of data"),(0,a.kt)("td",{parentName:"tr",align:null},"None"),(0,a.kt)("td",{parentName:"tr",align:null},"True"),(0,a.kt)("td",{parentName:"tr",align:null},"None")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"end_date"),(0,a.kt)("td",{parentName:"tr",align:null},"-e  --end"),(0,a.kt)("td",{parentName:"tr",align:null},"Ending date (YYYY-MM-DD) of data"),(0,a.kt)("td",{parentName:"tr",align:null},"None"),(0,a.kt)("td",{parentName:"tr",align:null},"True"),(0,a.kt)("td",{parentName:"tr",align:null},"None")))),(0,a.kt)("hr",null))}s.isMDXComponent=!0}}]);