
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
import os
import subprocess
import platform
from gtts import gTTS
from pydub import AudioSegment
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    # Generate MP3 file
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

    # Play the MP3 file
    os_name = platform.system()
    try:
        if os_name == "Darwin" or os_name == "Linux" or os_name == "Windows":  # macOS, Linux, Windows
            subprocess.run(['ffplay', '-nodisp', '-autoexit', output_filepath], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

    # Play the MP3 file
    os_name = platform.system()
    try:
        if os_name == "Darwin" or os_name == "Linux" or os_name == "Windows":  # macOS, Linux, Windows
            subprocess.run(['ffplay', '-nodisp', '-autoexit', output_filepath], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# input_text = "Hi This is Akash, An aspiring AI Engineer. autoplay."
# text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")

