"""
Basic example of edge_tts usage.
"""

import asyncio, edge_tts
from playsound import playsound

VOICE = "en-US-SteffanNeural"
OUTPUT_FILE = "./voice-reply/reply-1.mp3"

async def convertTextToSpeech(text):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(OUTPUT_FILE)
    playsound(OUTPUT_FILE)

def play(text):
    asyncio.run(convertTextToSpeech(text))
