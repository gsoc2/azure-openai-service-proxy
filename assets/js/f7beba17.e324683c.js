"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[692],{4137:(e,n,t)=>{t.d(n,{Zo:()=>l,kt:()=>d});var r=t(7294);function a(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function o(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function i(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?o(Object(t),!0).forEach((function(n){a(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):o(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function p(e,n){if(null==e)return{};var t,r,a=function(e,n){if(null==e)return{};var t,r,a={},o=Object.keys(e);for(r=0;r<o.length;r++)t=o[r],n.indexOf(t)>=0||(a[t]=e[t]);return a}(e,n);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)t=o[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(a[t]=e[t])}return a}var s=r.createContext({}),c=function(e){var n=r.useContext(s),t=n;return e&&(t="function"==typeof e?e(n):i(i({},n),e)),t},l=function(e){var n=c(e.components);return r.createElement(s.Provider,{value:n},e.children)},u="mdxType",h={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},m=r.forwardRef((function(e,n){var t=e.components,a=e.mdxType,o=e.originalType,s=e.parentName,l=p(e,["components","mdxType","originalType","parentName"]),u=c(t),m=a,d=u["".concat(s,".").concat(m)]||u[m]||h[m]||o;return t?r.createElement(d,i(i({ref:n},l),{},{components:t})):r.createElement(d,i({ref:n},l))}));function d(e,n){var t=arguments,a=n&&n.mdxType;if("string"==typeof e||a){var o=t.length,i=new Array(o);i[0]=m;var p={};for(var s in n)hasOwnProperty.call(n,s)&&(p[s]=n[s]);p.originalType=e,p[u]="string"==typeof e?e:a,i[1]=p;for(var c=2;c<o;c++)i[c]=t[c];return r.createElement.apply(null,i)}return r.createElement.apply(null,t)}m.displayName="MDXCreateElement"},1667:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>s,contentTitle:()=>i,default:()=>h,frontMatter:()=>o,metadata:()=>p,toc:()=>c});var r=t(7462),a=(t(7294),t(4137));const o={},i="OpenAI API access",p={unversionedId:"raw-openai-api-access",id:"raw-openai-api-access",title:"OpenAI API access",description:"The Azure OpenAI proxy service provides access to the Azure OpenAI APIs for developers to build applications, again using a time bound event code. Initially, there are two REST endpoints available via the proxy service, chat completion, and embeddings.",source:"@site/docs/80-raw-openai-api-access.md",sourceDirName:".",slug:"/raw-openai-api-access",permalink:"/azure-openai-service-proxy/raw-openai-api-access",draft:!1,editUrl:"https://github.com/gloveboxes/azure-openai-service-proxy/tree/master/docs/docs/80-raw-openai-api-access.md",tags:[],version:"current",sidebarPosition:80,frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Using the Playground",permalink:"/azure-openai-service-proxy/playground"}},s={},c=[{value:"Authentication",id:"authentication",level:2},{value:"Chat completion with Curl",id:"chat-completion-with-curl",level:2},{value:"Chat completion with Python and httpx",id:"chat-completion-with-python-and-httpx",level:2},{value:"The Python OpenAI Proxy SDK",id:"the-python-openai-proxy-sdk",level:2}],l={toc:c},u="wrapper";function h(e){let{components:n,...t}=e;return(0,a.kt)(u,(0,r.Z)({},l,t,{components:n,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"openai-api-access"},"OpenAI API access"),(0,a.kt)("p",null,"The Azure OpenAI proxy service provides access to the Azure OpenAI APIs for developers to build applications, again using a time bound event code. Initially, there are two REST endpoints available via the proxy service, ",(0,a.kt)("inlineCode",{parentName:"p"},"chat completion"),", and ",(0,a.kt)("inlineCode",{parentName:"p"},"embeddings"),"."),(0,a.kt)("h2",{id:"authentication"},"Authentication"),(0,a.kt)("p",null,"The authorization token is made up of the event code and a user id. The user id can be any string, it's recommended to use a GitHub user name. For eample, ",(0,a.kt)("inlineCode",{parentName:"p"},"hackathon/githubuser"),"."),(0,a.kt)("p",null,"The authorization token is passed in the ",(0,a.kt)("inlineCode",{parentName:"p"},"openai-event-code")," header of the REST Post request."),(0,a.kt)("h2",{id:"chat-completion-with-curl"},"Chat completion with Curl"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-shell"},'curl -X POST \\\n-H "openai-event-code: hackathon/githubuser" \\\n-H "Content-Type: application/json" \\\n-d \'{\n    "max_tokens": 256,\n    "temperature": 1,\n    "messages": [\n        {\n            "role": "system",\n            "content": "You are an AI assistant that writes poems in the style of William Shakespeare."\n        },\n        {\n            "role": "user",\n            "content": "Write a poem about indian elephants"\n        }\n    ]\n}\' \\\nhttps://YOUR_OPENAI_PROXY_ENDPOINT/api/v1/chat/completions\n')),(0,a.kt)("p",null,"or pretty print the JSON response with ",(0,a.kt)("inlineCode",{parentName:"p"},"jq")),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-shell"},'curl -X POST \\\n-H "openai-event-code: hackathon/githubuser" \\\n-H "Content-Type: application/json" \\\n-d \'{\n    "max_tokens": 256,\n    "temperature": 1,\n    "messages": [\n        {\n            "role": "system",\n            "content": "You are an AI assistant that writes poems in the style of William Shakespeare."\n        },\n        {\n            "role": "user",\n            "content": "Write a poem about indian elephants"\n        }\n    ]\n}\' \\\nhttps://YOUR_OPENAI_PROXY_ENDPOINT/api/v1/chat/completions | jq\n')),(0,a.kt)("h2",{id:"chat-completion-with-python-and-httpx"},"Chat completion with Python and httpx"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},'\nrequest = {\n    "max_tokens": 256,\n    "temperature": 1,\n    "messages": [\n        {\n            "role": "system",\n            "content": "You are an AI assistant that writes poems in the style of William Shakespeare."\n        },\n        {\n            "role": "user",\n            "content": "Write a poem about indian elephants"\n        }\n    ]\n}\n\nurl = "https://YOUR_OPENAI_PROXY_ENDPOINT/api/v1/chat/completions"\n\nheaders = {"openai-event-code": hackathon/githubuser}\n\nresponse = httpx.post(url=url, headers=headers, json=request, timeout=30)\n\nif response.status_code == 200:\n    print(response.json())\n')),(0,a.kt)("h2",{id:"the-python-openai-proxy-sdk"},"The Python OpenAI Proxy SDK"),(0,a.kt)("p",null,"The Python OpenAI Proxy SDK wraps the REST API calls to the proxy service. The wrapper is designed to be a drop in replacement for the official OpenAI Chat Completion Python API."),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},'\'\'\' Example of using the OpenAI Proxy Python SDK \'\'\'\n\nimport json\nimport openai.error\nimport openai_proxy\n\nopenai_proxy.api_key = "hackathon/githubuser"\nopenai_proxy.api_base = "https://YOUR_OPENAI_PROXY_ENDPOINT"\nopenai_proxy.api_version = "2023-07-01-preview"\nopenai_proxy.api_type = "azure"\n\npoem_messages = [\n    {\n        "role": "system",\n        "content": "You are an AI assistant that writes poems in the style of William Shakespeare.",\n    },\n    {"role": "user", "content": "Write a poem about indian elephants"},\n]\n\ntry:\n    response = openai_proxy.ChatCompletion.create(\n        messages=poem_messages,\n        max_tokens=256,\n        temperature=1.0,\n    )\n\n    print(json.dumps(response, indent=4, sort_keys=True))\n\nexcept openai.error.InvalidRequestError as invalid_request_error:\n    print(invalid_request_error)\n\nexcept openai.error.AuthenticationError as authentication_error:\n    print(authentication_error)\n\nexcept openai.error.PermissionError as permission_error:\n    print(permission_error)\n\nexcept openai.error.TryAgain as try_again:\n    print(try_again)\n\nexcept openai.error.RateLimitError as rate_limit_error:\n    print(rate_limit_error)\n\nexcept openai.error.APIError as api_error:\n    print(api_error)\n\nexcept Exception as exception:\n    print(exception)\n')),(0,a.kt)("p",null,"A complete working example can be found in the ",(0,a.kt)("a",{parentName:"p",href:"https://github.com/gloveboxes/azure-openai-service-proxy/tree/main/src/sdk/python"},"Python OpenAI Proxy SDK")," folder."))}h.isMDXComponent=!0}}]);