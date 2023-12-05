from record import record
from stt import speechToText
from prompt import prompt
from llmClient import sendPromptToLLM

# Start and stop recording with space bar
record('space', './audio-files/recordedSample.wav')
speechToText("./audio-files/recordedSample.wav", './transcriptions/transcription.txt')

sendPromptToLLM(prompt())