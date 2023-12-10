import pyaudio, keyboard, time, wave

chunkSize = 1024  # Record in chunks of 1024 samples
sampleRate = 44100 # Record at 44100 samples per second  
sampleFormat = pyaudio.paInt16
numChannels = 1

# Set up the PyAudio object
audioInterface = pyaudio.PyAudio() # Access the PortAudio resources

def record(key, filename):
    keyboard.wait(key)
    time.sleep(0.2)
    print('Recording started. Press space bar to stop recording and send your prompt to the LLM.')

    # Open the audio stream
    stream = audioInterface.open(format=sampleFormat, channels=numChannels, rate=sampleRate, input=True) 

    # Start recording
    stream.start_stream()
    startTime = time.time() # Start recording timer in seconds
    print('Start time:', startTime) 
    stopTime = time.time() # Default stop time

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