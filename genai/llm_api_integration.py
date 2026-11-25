
import os
from dotenv import load_dotenv
from groq import Groq

# Step 1: Load environment variables
load_dotenv()

# Step 2: Read API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Groq API key not found")

# Step 3: Create Groq client
client = Groq(api_key=api_key)

# Step 4: Send prompt to LLM
# response = client.chat.completions.create(
#     model="openai/gpt-oss-20b",
#     messages=[
#         {
#             "role": "user",
#             "content": "Explain Generative AI in simple terms with one example."
#         }
#     ]
# )

# # Step 5: Display response
# print("Groq Response:", response.choices[0].message.content)


#Make the integration reusable
# In real applications, users provide different prompts. So let's create a reusable function.


def generate_response(prompt):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as error:
        print("API request failed:", error)
        return None





# # Test 1
answer1 = generate_response(
    "Explain RAG in simple terms."
)
print("Response 1:")
print(answer1)
# Test 2
answer2 = generate_response(
    "What is the difference between AI and ML?"
)
print("Response 2:")
print(answer2)