import openai
openai.api_key = "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"

result = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [{"role": "user", "content": "What is the distance between the earth and mars?"}]
)

print(result)