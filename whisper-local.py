import whisper

# model = whisper.load_model("base")
model = whisper.load_model("medium")
result = model.transcribe("./audio/vinny.mp3")
print(result["text"])