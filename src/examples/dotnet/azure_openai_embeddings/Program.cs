using Azure.AI.OpenAI;
using DotNetEnv;

Env.Load();

// Get the key from the environment variables
string? key = Environment.GetEnvironmentVariable("OPENAI_API_KEY");
string? endpoint = Environment.GetEnvironmentVariable("OPENAI_ENDPOINT_URL");

if (key == null || endpoint == null)
{
    Console.WriteLine("Please set the OPENAI_API_KEY and OPENAI_ENDPOINT_URL environment variables.");
    return;
}

var client = new OpenAIClient(new Uri(endpoint), new Azure.AzureKeyCredential(key));

EmbeddingsOptions embeddingsOptions = new()
{
    DeploymentName = "text-embedding-ada-002",
    Input = { "Your text string goes here" },
};
Azure.Response<Embeddings> response = await client.GetEmbeddingsAsync(embeddingsOptions);


EmbeddingItem item = response.Value.Data[0];
ReadOnlyMemory<float> embedding = item.Embedding;
Console.WriteLine($"Embedding vector length: {embedding.Length}");
Console.WriteLine($"Embedding vector: {string.Join(", ", embedding.ToArray())}");
