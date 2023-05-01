import openai
openai.api_key = "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"

audio_file = open("audio/german1.mp3", "rb")
result = openai.Audio.translate("whisper-1", audio_file)

print(result)