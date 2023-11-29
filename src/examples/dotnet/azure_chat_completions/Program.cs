// Chat completions example
using System.Xml.Serialization;
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

var chatCompletionsOptions = new ChatCompletionsOptions()
{
    DeploymentName = "gpt-3.5-turbo",
    Messages =
                {
                    new ChatMessage(ChatRole.System, "You are a helpful assistant. You will talk like a pirate."),
                    new ChatMessage(ChatRole.User, "Can you help me?"),
                    new ChatMessage(ChatRole.Assistant, "Arrrr! Of course, me hearty! What can I do for ye?"),
                    new ChatMessage(ChatRole.User, "What's the best way to train a parrot?"),
                }
};

Azure.Response<ChatCompletions> completionsResponse = client.GetChatCompletions(chatCompletionsOptions);

var completion = completionsResponse.Value.Choices[0].Message.Content;
Console.WriteLine(completion);
