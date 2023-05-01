import openai
openai.api_key = "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"

resultado = openai.Image.create(
    prompt = "Draw a realistic art of Goku boxing with Broly",
    n = 1,
    size = "1024x1024"
)

print(resultado)