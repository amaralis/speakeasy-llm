import asyncio
from record import record
from stt import speechToText
from llmClient import sendPromptToLLM
from tts import play

# Start and stop recording with space bar
record('space', './audio-files/recordedSample.wav')

prompt = speechToText("./audio-files/recordedSample.wav", './transcriptions/transcription.txt')
print("Speech: ", prompt)

# Send the prompt converted to text to the LLM
response = sendPromptToLLM(prompt)
print(response)

# Run text to speech on the text response
play(response)