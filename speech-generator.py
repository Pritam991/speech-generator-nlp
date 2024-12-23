import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for recording
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 8
WAVE_OUTPUT_FILENAME = "output.wav"

def record_speech():
    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open the stream
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Recording...")

    # Record the speech signal
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording finished")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded speech signal to a file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def read_recorded_speech_signal():
    # Open the recorded speech signal file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'rb')

    # Read the audio data from the file
    data = wf.readframes(wf.getnframes())

    # Convert the audio data to a numpy array
    audio_data = np.frombuffer(data, dtype=np.int16)

    # Print the audio data
    print("Audio Data:")
    print(audio_data)

    # Plot the audio data
    plt.plot(audio_data)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Audio Signal')
    plt.show()

    # Close the file
    wf.close()

def generate_speech_pattern():
    # Read the recorded speech signal from the file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'rb')
    data = wf.readframes(wf.getnframes())

    # Convert the data to a numpy array
    data = np.frombuffer(data, dtype=np.int16)

    # Generate the speech pattern using FFT
    speech_pattern = np.fft.fft(data)

    # Print the speech pattern
    print("Speech pattern:")
    print(speech_pattern)

def main():
    while True:
        print("Menu:")
        print("1. Record speech signal")
        print("2. Read recorded speech signal")
        print("3. Generate speech pattern")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            record_speech()
        elif choice == "2":
            read_recorded_speech_signal()
        elif choice == "3":
            generate_speech_pattern()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()