import whisper
import warnings
warnings.simplefilter("ignore")

model = whisper.load_model("tiny")

result = model.transcribe(audio="./sample2.mp3")

print(result["text"])