// OpenAI Chat Completions Streaming Your Data Example

// https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/openai/Azure.AI.OpenAI/tests/Samples/Sample08_UseYourOwnData.cs
// # Create a new Azure Cognitive Search index and load an index with Azure content
// # https://microsoftlearning.github.io/mslearn-knowledge-mining/Instructions/Labs/10-vector-search-exercise.html


using Azure.AI.OpenAI;
using DotNetEnv;


Env.Load();

// Get the key from the environment variables
string? key = Environment.GetEnvironmentVariable("OPENAI_API_KEY");
string? endpoint = Environment.GetEnvironmentVariable("OPENAI_ENDPOINT_URL");

string? searchEndpoint = Environment.GetEnvironmentVariable("AZURE_AI_SEARCH_ENDPOINT");
string? indexName = Environment.GetEnvironmentVariable("AZURE_AI_SEARCH_INDEX_NAME");
string? searchKey = Environment.GetEnvironmentVariable("AZURE_AI_SEARCH_KEY");

if (key == null || endpoint == null || searchEndpoint == null || indexName == null || searchKey == null)
{
    Console.WriteLine("Please set the OPENAI_API_KEY, OPENAI_ENDPOINT_URL, AZURE_AI_SEARCH_ENDPOINT, AZURE_AI_SEARCH_INDEX_NAME, and AZURE_AI_SEARCH_KEY environment variables.");
    return;
}

var client = new OpenAIClient(new Uri(endpoint), new Azure.AzureKeyCredential(key));

AzureCognitiveSearchChatExtensionConfiguration contosoExtensionConfig = new()
{
    SearchEndpoint = new Uri(searchEndpoint),
    IndexName = indexName,
};

contosoExtensionConfig.SetSearchKey(searchKey);

var chatCompletionsOptions = new ChatCompletionsOptions()
{
    DeploymentName = "gpt-3.5-turbo", // Use DeploymentName for "model" with non-Azure clients
    Messages =
    {
        new ChatMessage(ChatRole.User, "What are the differences between Azure Machine Learning and Azure AI services?"),

    },
    AzureExtensionsOptions = new AzureChatExtensionsOptions()
    {
        Extensions = { contosoExtensionConfig }
    }
};

await foreach (StreamingChatCompletionsUpdate chatUpdate in client.GetChatCompletionsStreaming(chatCompletionsOptions))
{
    if (chatUpdate.Role.HasValue)
    {
        Console.Write($"{chatUpdate.Role.Value.ToString().ToUpperInvariant()}: ");
    }
    if (!string.IsNullOrEmpty(chatUpdate.ContentUpdate))
    {
        Console.Write(chatUpdate.ContentUpdate);
        Console.Out.Flush(); // Force flush to console for streaming output in debug mode
    }
    await Task.Delay(50);
}
