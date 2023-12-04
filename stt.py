import whisper
import warnings
warnings.simplefilter("ignore")

model = whisper.load_model("tiny")

result = model.transcribe(audio="./audio-files/output.wav")

print(result["text"])

speechCapture = result["text"]