from LLMConnector import LLMConnector
from protocols.promptable import Promptable
from llms.LMStudio import LMStudio
from record import record
from stt import speechToText
from tts import play

llm: Promptable = LMStudio()

def startPrompting(model=llm):
    connector = LLMConnector(model)
    print('Press space bar to start recording your prompt.')
    
    # Start and stop recording with space bar
    record('space', './audio-files/recordedSample.wav')


    prompt = speechToText("./audio-files/recordedSample.wav", './transcriptions/transcription.txt')
    print("Recorded speech: ", prompt)

    # Send the prompt converted to text to the LLM
    response = connector.sendPrompt(model, prompt)
    print(response)

    # Run text to speech on the text response
    play(response)