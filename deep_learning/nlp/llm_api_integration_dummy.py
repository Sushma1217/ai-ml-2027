import os 
from dotenv import load_dotenv
from google import genai
import time
from google.genai import errors

# # Step 1: Load environment variables
load_dotenv()

# # Step 2: Read the API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found")

# # Step 3: Create Gemini client
client = genai.Client(api_key=api_key)

# # Step 4: Send prompt to Gemini
# response = client.interactions.create(model = "gemini-3.8-flash",input="Explain Generative AI in simple terms with one example.")
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain Generative AI in simple terms with one example."
)

print(response.text)

# # Step 5: Display the model response
print("Gemini Response:",response.output_text)


# for attempt in range(3):
#     try:
#         response = client.interactions.create(
#             model="gemini-3.8-flash",
#             input="Explain Generative AI in simple terms with one example."
#         )
#         print("Gemini Response:", response.output_text)
#         break

#     except errors.APIError as e:
#         if e.code == 503 and attempt < 2:
#             print("Gemini server is busy. Retrying...")
#             time.sleep(5)
#         else:
#             raise

# load_dotenv()	Loads your .env variables
# os.getenv()	Reads the API key
# genai.Client()	Creates a client to communicate with Gemini
# interactions.create()	Sends a request to the model
# model	Specifies which LLM to use
# input	Contains the prompt
# response.output_text	Extracts the generated text


# Make the integration reusable
# Right now, your prompt is hardcoded.
# In real applications, users provide different prompts. So let's create a reusable function.


##############NOT WORKING SO SWTICEHD TO GROQ##############

