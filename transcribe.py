import json
import whisper

model = whisper.load_model("turbo")
result = model.transcribe("/Users/tyler/Recording.mp3")

with open("/Users/tyler/transcript.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)