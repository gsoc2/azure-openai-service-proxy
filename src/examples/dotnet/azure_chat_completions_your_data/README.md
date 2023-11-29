# Notes

## Nuget Packages

```shell
dotnet add package Azure.AI.OpenAI --prerelease
dotnet add package DotNetEnv
```

## Environment variables

| Name | Description |
| --- | --- |
| OPENAI_API_KEY | The API key and consists of your EVENT_ID/USER_ID |
| OPENAI_ENDPOINT_URL | The endpoint URL for the Azure OpenAI proxy |
| YOUR_AZURE_SEARCH_ENDPOINT | The endpoint URL for the Azure Search service |
| YOUR_AZURE_SEARCH_INDEX_NAME | The name of the Azure Search index |
| YOUR_AZURE_SEARCH_KEY | The API key for the Azure Search service |

## Azure AI Search

To learn about and create an Azure AI Search service, see:

1. [Create an Azure AI Search service in the portal](https://learn.microsoft.com/azure/search/search-create-service-portal).

1. [Create an Azure AI Search Index for this example](https://microsoftlearning.github.io/mslearn-knowledge-mining/Instructions/Labs/10-vector-search-exercise.html).
