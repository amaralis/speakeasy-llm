import asyncio
from LLMConnector import LLMConnector
from promptable import Promptable
from LMStudio import LMStudio
from record import record
from stt import speechToText
from llmClient import submitPrompt
from tts import play

llm: Promptable = LMStudio()
connector = LLMConnector(llm)

# Start and stop recording with space bar
record('space', './audio-files/recordedSample.wav')


prompt = speechToText("./audio-files/recordedSample.wav", './transcriptions/transcription.txt')
print("Speech: ", prompt)

# Send the prompt converted to text to the LLM
response = submitPrompt(prompt)
print(response)

# Run text to speech on the text response
play(response)