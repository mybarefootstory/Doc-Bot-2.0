
# Step 1a: Setup Text to Speech-TTS-model with gTTS 
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

input_text = "Hi This is Akash, An aspiring AI Engineer."
# text_to_speech_with_gtts_old(input_text=input_text,output_filepath="gtts_testing.mp3")

# Step 1b: Setup Text to Speech-TTS-model with ElevenLabs 
import elevenlabs
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
load_dotenv()

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")
def text_to_speech_with_elevenlabs_old(input_text,output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio,output_filepath)

# text_to_speech_with_elevenlabs_old(input_text,output_filepath="elevenlabs_testing.mp3")


# Step 2: Use Model for text output to Voice
import subprocess
import platform
from pydub import AudioSegment


def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    # Generate MP3 file
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

    # Convert MP3 to WAV
    mp3_audio = AudioSegment.from_mp3(output_filepath)
    wav_filepath = output_filepath.replace(".mp3", ".wav")
    mp3_audio.export(wav_filepath, format="wav")

    # Play the WAV file
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', wav_filepath])

        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', wav_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

input_text = "Hi This is Akash, An aspiring AI Engineer."
# text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

    # Convert MP3 to WAV
    mp3_audio = AudioSegment.from_mp3(output_filepath)
    wav_filepath = output_filepath.replace(".mp3", ".wav")
    mp3_audio.export(wav_filepath, format="wav")

    # Play the WAV file
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', wav_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', wav_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

input_text = "Hi This is Akash, An aspiring AI Engineer."
text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")

