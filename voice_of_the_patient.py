
# Step 1: Setup Audio recorder(ffmpeg & portaudio)

import os
import wave
import pyaudio
import keyboard
from datetime import datetime
from pydub import AudioSegment

def record_audio(sample_rate=16000, channels=1, chunk=1024):
    """
    Record audio from the microphone while the SPACE button is held down.
    """
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=channels,
        rate=sample_rate,
        input=True,
        frames_per_buffer=chunk,
    )

    print("Press and hold the SPACE button to start recording...")
    frames = []

    keyboard.wait("space")  # Wait for SPACE button to be pressed
    print("Recording... (Release SPACE to stop)")

    while keyboard.is_pressed("space"):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording finished.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Return frames, sample rate, and sample width
    return frames, sample_rate, p.get_sample_size(pyaudio.paInt16)

def save_audio(frames, sample_rate, sample_width):
    """
    Save recorded audio to a WAV file and convert it to MP3 in the current directory.
    """
    # Create a unique filename using the current timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    wav_filename = f"recording_{timestamp}.wav"
    mp3_filename = f"recording_{timestamp}.mp3"
    wav_filepath = os.path.join(os.getcwd(), wav_filename)
    mp3_filepath = os.path.join(os.getcwd(), mp3_filename)

    # Save the WAV file
    with wave.open(wav_filepath, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(sample_width)
        wf.setframerate(sample_rate)
        wf.writeframes(b"".join(frames))

    # Convert WAV to MP3
    audio = AudioSegment.from_wav(wav_filepath)
    audio.export(mp3_filepath, format="mp3")

    # Optionally, remove the WAV file after conversion
    os.remove(wav_filepath)

    return mp3_filepath

def get_audio_filepath():
    try:
        # Record audio
        frames, sample_rate, sample_width = record_audio()
        # Save audio to a file in the current directory
        audio_path = save_audio(frames, sample_rate, sample_width)
        print(f"Audio saved to {audio_path}")
        return audio_path
    except KeyboardInterrupt:
        print("\nRecording stopped by user.")

audio_path = get_audio_filepath()
print(f"Audio file path: {audio_path}")



# Step 2: Setup Speech to text-SST-model for transcription

import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
stt_model="whisper-large-v3"

def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    client=Groq(api_key=GROQ_API_KEY)
    
    audio_file=open(audio_filepath, "rb")
    transcription=client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en"
    )
    return transcription.text

response=transcribe_with_groq(stt_model,audio_path,GROQ_API_KEY)
print(response)



