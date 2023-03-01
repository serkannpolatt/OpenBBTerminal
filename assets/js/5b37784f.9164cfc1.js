"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[45658],{3905:(e,t,r)=>{r.d(t,{Zo:()=>s,kt:()=>f});var n=r(67294);function a(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function l(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function i(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?l(Object(r),!0).forEach((function(t){a(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):l(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function o(e,t){if(null==e)return{};var r,n,a=function(e,t){if(null==e)return{};var r,n,a={},l=Object.keys(e);for(n=0;n<l.length;n++)r=l[n],t.indexOf(r)>=0||(a[r]=e[r]);return a}(e,t);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(e);for(n=0;n<l.length;n++)r=l[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}var u=n.createContext({}),p=function(e){var t=n.useContext(u),r=t;return e&&(r="function"==typeof e?e(t):i(i({},t),e)),r},s=function(e){var t=p(e.components);return n.createElement(u.Provider,{value:t},e.children)},c="mdxType",m={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},d=n.forwardRef((function(e,t){var r=e.components,a=e.mdxType,l=e.originalType,u=e.parentName,s=o(e,["components","mdxType","originalType","parentName"]),c=p(r),d=a,f=c["".concat(u,".").concat(d)]||c[d]||m[d]||l;return r?n.createElement(f,i(i({ref:t},s),{},{components:r})):n.createElement(f,i({ref:t},s))}));function f(e,t){var r=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var l=r.length,i=new Array(l);i[0]=d;var o={};for(var u in t)hasOwnProperty.call(t,u)&&(o[u]=t[u]);o.originalType=e,o[c]="string"==typeof e?e:a,i[1]=o;for(var p=2;p<l;p++)i[p]=r[p];return n.createElement.apply(null,i)}return n.createElement.apply(null,r)}d.displayName="MDXCreateElement"},14299:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>u,contentTitle:()=>i,default:()=>m,frontMatter:()=>l,metadata:()=>o,toc:()=>p});var n=r(87462),a=(r(67294),r(3905));const l={title:"usrates",description:"OpenBB SDK Function"},i="usrates",o={unversionedId:"reference/fixedincome/usrates",id:"reference/fixedincome/usrates",title:"usrates",description:"OpenBB SDK Function",source:"@site/content/sdk/reference/fixedincome/usrates.md",sourceDirName:"reference/fixedincome",slug:"/reference/fixedincome/usrates",permalink:"/sdk/reference/fixedincome/usrates",draft:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/sdk/reference/fixedincome/usrates.md",tags:[],version:"current",frontMatter:{title:"usrates",description:"OpenBB SDK Function"},sidebar:"tutorialSidebar",previous:{title:"treasury",permalink:"/sdk/reference/fixedincome/treasury"},next:{title:"ycrv",permalink:"/sdk/reference/fixedincome/ycrv"}},u={},p=[{value:"Parameters",id:"parameters",level:2},{value:"Returns",id:"returns",level:2}],s={toc:p},c="wrapper";function m(e){let{components:t,...r}=e;return(0,a.kt)(c,(0,n.Z)({},s,r,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"usrates"},"usrates"),(0,a.kt)("p",null,"Plot various treasury rates from the United States"),(0,a.kt)("p",null,"Source Code: [",(0,a.kt)("a",{parentName:"p",href:"https://github.com/OpenBB-finance/OpenBBTerminal/tree/main/openbb_terminal/fixedincome/fred_model.py#L927"},"link"),"]"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python",metastring:"wordwrap",wordwrap:!0},'openbb.fixedincome.usrates(parameter: str = "tbills", maturity: str = "3_months", start_date: Optional[str] = None, end_date: Optional[str] = None)\n')),(0,a.kt)("hr",null),(0,a.kt)("h2",{id:"parameters"},"Parameters"),(0,a.kt)("table",null,(0,a.kt)("thead",{parentName:"table"},(0,a.kt)("tr",{parentName:"thead"},(0,a.kt)("th",{parentName:"tr",align:null},"Name"),(0,a.kt)("th",{parentName:"tr",align:null},"Type"),(0,a.kt)("th",{parentName:"tr",align:null},"Description"),(0,a.kt)("th",{parentName:"tr",align:null},"Default"),(0,a.kt)("th",{parentName:"tr",align:null},"Optional"))),(0,a.kt)("tbody",{parentName:"table"},(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"parameter"),(0,a.kt)("td",{parentName:"tr",align:null},"str"),(0,a.kt)("td",{parentName:"tr",align:null},'Either "tbills", "cmn", or "tips".'),(0,a.kt)("td",{parentName:"tr",align:null},"tbills"),(0,a.kt)("td",{parentName:"tr",align:null},"True")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"maturity"),(0,a.kt)("td",{parentName:"tr",align:null},"str"),(0,a.kt)("td",{parentName:"tr",align:null},"Depending on the chosen parameter, a set of maturities is available.",(0,a.kt)("br",null),'    "4_week": {"tbill": "DTB4WK"},',(0,a.kt)("br",null),'    "1_month": {"cmn": "DGS1MO"},',(0,a.kt)("br",null),'    "3_month": {"tbill": "TB3MS", "cmn": "DGS3MO"},',(0,a.kt)("br",null),'    "6_month": {"tbill": "DTB6", "cmn": "DGS6MO"},',(0,a.kt)("br",null),'    "1_year": {"tbill": "DTB1YR", "cmn": "DGS1"},',(0,a.kt)("br",null),'    "2_year": {"cmn": "DGS2"},',(0,a.kt)("br",null),'    "3_year": {"cmn": "DGS3"},',(0,a.kt)("br",null),'    "5_year": {"tips": "DFII5", "cmn": "DGS5"},',(0,a.kt)("br",null),'    "7_year": {"tips": "DFII7", "cmn": "DGS7"},',(0,a.kt)("br",null),'    "10_year": {"tips": "DFII10", "cmn": "DGS10"},',(0,a.kt)("br",null),'    "20_year": {"tips": "DFII20", "cmn": "DGS20"},',(0,a.kt)("br",null),'    "30_year": {"tips": "DFII30", "cmn": "DGS30"},'),(0,a.kt)("td",{parentName:"tr",align:null},"3_months"),(0,a.kt)("td",{parentName:"tr",align:null},"True")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"start_date"),(0,a.kt)("td",{parentName:"tr",align:null},"Optional","[str]"),(0,a.kt)("td",{parentName:"tr",align:null},"Start date, formatted YYYY-MM-DD"),(0,a.kt)("td",{parentName:"tr",align:null},"None"),(0,a.kt)("td",{parentName:"tr",align:null},"True")),(0,a.kt)("tr",{parentName:"tbody"},(0,a.kt)("td",{parentName:"tr",align:null},"end_date"),(0,a.kt)("td",{parentName:"tr",align:null},"Optional","[str]"),(0,a.kt)("td",{parentName:"tr",align:null},"End date, formatted YYYY-MM-DD"),(0,a.kt)("td",{parentName:"tr",align:null},"None"),(0,a.kt)("td",{parentName:"tr",align:null},"True")))),(0,a.kt)("hr",null),(0,a.kt)("h2",{id:"returns"},"Returns"),(0,a.kt)("p",null,"This function does not return anything"),(0,a.kt)("hr",null))}m.isMDXComponent=!0}}]);