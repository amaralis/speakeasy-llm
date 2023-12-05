def prompt():
    with open('./transcriptions/transcription.txt', mode='r') as file:
        text = file.read()
        print('This is the prompt: ', text)
        return text