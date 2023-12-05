import whisper, warnings

def speechToText(sourceAudioFile, targetTextFile):
    warnings.simplefilter("ignore")
    model = whisper.load_model("tiny")
    result = model.transcribe(audio=sourceAudioFile)
    speechCapture = result["text"]
    print(speechCapture)
    with open(targetTextFile, mode="wt") as file:
        file.write(speechCapture)
    return speechCapture