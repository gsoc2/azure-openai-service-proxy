"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[686],{4137:(e,t,n)=>{n.d(t,{Zo:()=>l,kt:()=>g});var r=n(7294);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,r,a=function(e,t){if(null==e)return{};var n,r,a={},o=Object.keys(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||(a[n]=e[n]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var p=r.createContext({}),c=function(e){var t=r.useContext(p),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},l=function(e){var t=c(e.components);return r.createElement(p.Provider,{value:t},e.children)},u="mdxType",m={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},d=r.forwardRef((function(e,t){var n=e.components,a=e.mdxType,o=e.originalType,p=e.parentName,l=s(e,["components","mdxType","originalType","parentName"]),u=c(n),d=a,g=u["".concat(p,".").concat(d)]||u[d]||m[d]||o;return n?r.createElement(g,i(i({ref:t},l),{},{components:n})):r.createElement(g,i({ref:t},l))}));function g(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=n.length,i=new Array(o);i[0]=d;var s={};for(var p in t)hasOwnProperty.call(t,p)&&(s[p]=t[p]);s.originalType=e,s[u]="string"==typeof e?e:a,i[1]=s;for(var c=2;c<o;c++)i[c]=n[c];return r.createElement.apply(null,i)}return r.createElement.apply(null,n)}d.displayName="MDXCreateElement"},841:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>p,contentTitle:()=>i,default:()=>m,frontMatter:()=>o,metadata:()=>s,toc:()=>c});var r=n(7462),a=(n(7294),n(4137));const o={},i="Image Generation API",s={unversionedId:"raw-api-access/images-generations",id:"raw-api-access/images-generations",title:"Image Generation API",description:"The Azure OpenAI proxy service supports the Azure OpenAI Image Generation API, as of November 2023, the OpenAI Dall-e 2 model is supported. Requests are forwarded to the Azure OpenAI service and the response is returned to the caller.",source:"@site/docs/80-raw-api-access/40-images-generations.md",sourceDirName:"80-raw-api-access",slug:"/raw-api-access/images-generations",permalink:"/azure-openai-service-proxy/raw-api-access/images-generations",draft:!1,editUrl:"https://github.com/gloveboxes/azure-openai-service-proxy/tree/master/docs/docs/80-raw-api-access/40-images-generations.md",tags:[],version:"current",sidebarPosition:40,frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Embeddings API",permalink:"/azure-openai-service-proxy/raw-api-access/embedding"}},p={},c=[{value:"Python Example",id:"python-example",level:2},{value:"Using cURL to access the Image Generation API",id:"using-curl-to-access-the-image-generation-api",level:2}],l={toc:c},u="wrapper";function m(e){let{components:t,...n}=e;return(0,a.kt)(u,(0,r.Z)({},l,n,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"image-generation-api"},"Image Generation API"),(0,a.kt)("p",null,"The Azure OpenAI proxy service supports the Azure OpenAI Image Generation API, as of November 2023, the OpenAI ",(0,a.kt)("inlineCode",{parentName:"p"},"Dall-e 2")," model is supported. Requests are forwarded to the Azure OpenAI service and the response is returned to the caller."),(0,a.kt)("p",null,"The is no SDK for the Image Generation API, so, using your preferred programming language, make REST calls to the proxy service Image Generation API endpoint."),(0,a.kt)("p",null,"The following example is from the ",(0,a.kt)("inlineCode",{parentName:"p"},"src/examples")," folder and demonstrates how to use httpx to access the images generations API."),(0,a.kt)("h2",{id:"python-example"},"Python Example"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},'""" generate images from OpenAI Dall-e model"""\n\nimport os\nimport json\nfrom dotenv import load_dotenv\nimport httpx\n\nload_dotenv()\n\nENDPOINT_URL = os.environ.get("ENDPOINT_URL")\nAPI_KEY = os.environ.get("API_KEY")\n\n\ndef generate_images(prompt):\n    """post the prompt to the OpenAI API and return the response"""\n    url = ENDPOINT_URL + "/images/generations"\n    headers = {\n        "Content-Type": "application/json",\n        "api-key": API_KEY,\n    }\n\n    data = {\n        "prompt": prompt,\n        "n": 5,\n        "size": "512x512",\n    }\n\n    response = httpx.post(url, headers=headers, json=data, timeout=30)\n    return response\n\n\nresult = generate_images("cute picture of a cat")\nresult = result.json()\nprint(json.dumps(result, indent=4, sort_keys=True))\n')),(0,a.kt)("h2",{id:"using-curl-to-access-the-image-generation-api"},"Using cURL to access the Image Generation API"),(0,a.kt)("p",null,"The following example demonstrates how to use ",(0,a.kt)("inlineCode",{parentName:"p"},"cURL")," to access the Image Generation API. Remember, the ",(0,a.kt)("inlineCode",{parentName:"p"},"EVENT_TOKEN")," is the EventCode/GitHubUserName, eg ",(0,a.kt)("inlineCode",{parentName:"p"},"hackathon/gloveboxes"),", and the ",(0,a.kt)("inlineCode",{parentName:"p"},"PROXY_ENDPOINT_URL")," is proxy url provided by the event administrator."),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-shell"},'curl -X POST -H "Content-Type: application/json" -H "api-key: API_KEY" -d \'{\n  "prompt": "cute picture of a cat",\n  "size": "1024x1024",\n  "n": 2\n}\' https://PROXY_ENDPOINT_URL/v1/api/images/generations | jq\n')))}m.isMDXComponent=!0}}]);