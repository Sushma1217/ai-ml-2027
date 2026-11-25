import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("api key is missing")

client = Groq(api_key=api_key)

MODEL_NAME = "openai/gpt-oss-20b"

messages = [
    {
        "role": "system",
        "content": """
        You are a helpful AI tutor.

        Explain technical concepts in simple English.
        Use practical examples.
        Keep answers concise.
        """
    }
]


# Create the chat function
def chat(user_input):
     # Add user message to history
     messages.append({
          "role":"user",
          "content":user_input
     })
      # Send complete conversation to Groq
     response = client.chat.completions.create(model=MODEL_NAME,messages=messages)

      # Extract assistant response
     assistant_response = response.choices[0].message.content

     # Add assistant response to history
     messages.append({
          "role":"assistant",
          "content":assistant_response
     })

     return assistant_response

# Understand the most important logic:
# 1. User asks a question.
# 2. We append that question to messages.
# 3. We send the entire message list to Groq.
# 4. Groq generates a response using the available conversation context.
# 5. We append the assistant response to the same list.
# 6. The next request includes both previous messages.
    
# Step D — Test the conversation
print("User: What is RAG?")
print("Assistant:", chat("What is RAG?"))

print("\nUser: Give me a real-world example.")
print("Assistant:", chat("Give me a real-world example."))

print("\nUser: What are its main components?")
print("Assistant:", chat("What are its main components?"))

# Step E — Inspect conversation history
print("\nComplete Conversation History:")
for msg in messages:
     print(msg["role"],":",msg["content"])

# Remove conversation history
def chat_without_history(user_input):
     response = client.chat.completions.create(
          model = MODEL_NAME,
          messages=[
               {
                "role": "user",
                "content": user_input
            }
          ]
     )
     return response.choices[0].message.content

print(
    chat_without_history(
        "Give me a real-world example of it."
    )
)