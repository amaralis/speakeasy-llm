import whisper, warnings

warnings.simplefilter("ignore")

model = whisper.load_model("tiny")

result = model.transcribe(audio="./audio-files/recordedSample.wav")

speechCapture = result["text"]

print(speechCapture)

with open('./transcriptions/transcription.txt', mode="wt") as file:
    file.write(speechCapture)