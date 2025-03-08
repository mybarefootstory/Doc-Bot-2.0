# Doc-Bot-2.0

## Description
Doc-Bot-2.0 is an advanced medical chatbot that integrates voice and vision capabilities to facilitate interactive healthcare communication. Utilizing state-of-the-art language models and speech processing technologies, Doc-Bot-2.0 simulates a doctor-patient interaction, analyzing both text and image inputs to provide medical insights and suggestions.

## Table of Contents
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Workflow](#workflow)
- [Environment Variables](#environment-variables)
- [Future Scope and Improvements](#future-scope-and-improvements)
- [Use Cases in Healthcare](#use-cases-in-healthcare)
- [Contact](#contact)

## Technology Stack
Doc-Bot-2.0 leverages a variety of technologies to deliver its functionalities:

- **Python**: The core programming language used for development.
- **Gradio**: Provides a user-friendly web interface for interacting with the chatbot.
- **SpeechRecognition**: Captures and processes audio input from users.
- **PyDub**: Handles audio file conversions and manipulations.
- **PyAudio**: Facilitates audio recording from the microphone.
- **gTTS**: Converts text responses into speech using Google's Text-to-Speech API.
- **ElevenLabs**: Provides advanced text-to-speech capabilities.
- **Groq**: Utilized for multimodal language model processing.
- **dotenv**: Manages environment variables securely.
- **FFmpeg**: Required for audio processing tasks.

## Installation
To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mybarefootstory/Doc-Bot-2.0.git
   cd Doc-Bot-2.0
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Install FFmpeg**:
   Ensure `ffmpeg` is installed and accessible from your system's PATH for audio processing.

## Usage
To run the Gradio interface for Doc-Bot-2.0, execute the following command:

```bash
python gradio_app.py
```

This will launch a web interface where you can interact with the chatbot using voice and image inputs.

## Features
- **Voice Input**: Record audio queries using your microphone.
- **Image Analysis**: Upload images for medical analysis.
- **Text-to-Speech**: Receive audio responses from the chatbot.
- **Multimodal Interaction**: Combines text and image data for comprehensive analysis.

## Workflow
1. **Voice Input**: Users can record their queries using a microphone. The audio is captured and processed to extract text using the SpeechRecognition library.
2. **Image Analysis**: Users can upload images for analysis. The image is encoded and analyzed using the Groq multimodal language model.
3. **Text Processing**: The extracted text and image analysis results are processed to generate a response using predefined prompts.
4. **Text-to-Speech**: The response is converted into speech using either gTTS or ElevenLabs, providing an audio output to the user.
5. **User Interface**: The Gradio interface facilitates seamless interaction, displaying text responses and playing audio outputs.

## Environment Variables
The project requires the following environment variables, which should be set in a `.env` file:

- `GROQ_API_KEY`: Your API key for the Groq service.
- `ELEVENLABS_API_KEY`: Your API key for the ElevenLabs service.

Example `.env` file:
```
GROQ_API_KEY="your_groq_api_key"
ELEVENLABS_API_KEY="your_elevenlabs_api_key"
```

## Future Scope and Improvements
- **Integration with EHR Systems**: Enhance the chatbot's capabilities by integrating with Electronic Health Record (EHR) systems for personalized patient data analysis.
- **Natural Language Understanding**: Improve the chatbot's natural language understanding to handle more complex queries and provide more accurate responses.
- **Multilingual Support**: Expand the chatbot's language capabilities to support multiple languages, making it accessible to a broader audience.
- **Real-time Monitoring**: Implement real-time health monitoring features using wearable devices to provide instant feedback and recommendations.
- **AI Model Enhancements**: Continuously update and train the underlying AI models to improve accuracy and reliability.

## Use Cases in Healthcare
- **Patient Triage**: Assist in preliminary patient assessment by analyzing symptoms and providing initial recommendations.
- **Remote Consultations**: Facilitate remote consultations by providing a platform for patients to interact with healthcare professionals.
- **Health Education**: Educate patients on various health topics and preventive measures through interactive sessions.
- **Chronic Disease Management**: Support chronic disease management by providing personalized advice and monitoring patient progress.

## Contact
For questions or inquiries, please contact the project maintainer:

- Your Name - [Akash Kumar Swarnkar](mailto:akashkumarswarnkar7172@gmail.com)

Project Link: [https://github.com/mybarefootstory/Doc-Bot-2.0](https://github.com/mybarefootstory/Doc-Bot-2.0)


