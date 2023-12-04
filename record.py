import pyaudio
# import wave

# chunk = 1024  # Record in chunks of 1024 samples
# sample_format = pyaudio.paInt16  # 16 bits per sample
# channels = 1
# sampleRate = 44100  # Record at 44100 samples per second
# seconds = 3
# filename = "./audio-files/output.wav"

# audioInterface = pyaudio.PyAudio()  # Create an interface to PortAudio

# stream = audioInterface.open(input=True, channels=1, frames_per_buffer=chunk, rate=sampleRate, format=sample_format)

# frames = [] # Initialize frame array

# print('Recording')




# print('Finished recording')

# Sure! Here's an example of how you could do this using the `pyaudio` library:

import keyboard, time, math, wave

chunkSize = 1024  # Record in chunks of 1024 samples
sampleRate = 44100 # Record at 44100 samples per second
sampleFormat = pyaudio.paInt16
numChannels = 1
filename = './audio-files/recordedSample.wav'

# Set up the PyAudio object
audioInterface = pyaudio.PyAudio() # Access the PortAudio resources

def startRecording():
    # Open the audio stream
    stream = audioInterface.open(format=sampleFormat, channels=numChannels, rate=sampleRate, input=True) 

    # Start recording
    stream.start_stream()
    startTime = time.time() # Start recording timer in seconds
    print('Start time:', startTime) 
    stopTime = time.time() # Safety

    frames = []  # Initialize array to store frames

    while True:
        # Continuous read from data stream, in chunks
        data = stream.read(chunkSize)
        frames.append(data)

        if keyboard.is_pressed(' '):
            stopTime = time.time()
            print('Stop time:', stopTime)
            print('Recording stopped') 
            break    

    print('Duration:', stopTime - startTime)
 
    # Stop recording and close the stream
    stream.stop_stream()
    stream.close()

    # Terminate the PortAudio interface
    audioInterface.terminate()

    # Save the recorded data as a WAV file
    dataWriter = wave.open(filename, 'wb')
    dataWriter.setnchannels(numChannels)
    dataWriter.setsampwidth(audioInterface.get_sample_size(sampleFormat))
    dataWriter.setframerate(sampleRate)
    dataWriter.writeframes(b''.join(frames))
    dataWriter.close()

# Wait for the spacebar key to be pressed
while True:
    if keyboard.is_pressed(' '):
        time.sleep(0.2)
        print('Recording started')
        startRecording()
        break