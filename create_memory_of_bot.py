# Import necessary modules for environment variable management and image processing
import os
from dotenv import load_dotenv
import base64

# Step 1: Setup GROQ API Key
load_dotenv()

# Retrieve the GROQ API key from environment variables
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')


# Step 2: Convert image to required format
def encode_image(image_path):   
    image_file=open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')


# Step 3: Setup Multimodal LLM
from groq import Groq

model = "llama-3.2-90b-vision-preview"

def analyze_image_with_query(query, model, encoded_image):
    """
    Analyze an image with a text query using a multimodal language model.

    :param query: The text query to analyze alongside the image
    :param model: The model identifier to use for the analysis
    :param encoded_image: The base64-encoded image data
    :return: The content of the model's response
    """
    # Initialize the Groq client
    client = Groq()
    
    # Construct the message payload with text and image data
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }
    ]

    # Create a chat completion request with the specified model and messages
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    # Return the content of the first choice's message
    return chat_completion.choices[0].message.content

# # Example usage
# query = "Is there something wrong with my face?"
# response = analyze_image_with_query(query, model, encoded_image)
# print(response)