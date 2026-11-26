import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("api key is missing")

client = Groq(api_key=api_key)

MODEL_NAME = "openai/gpt-oss-20b"

def generate_response(prompt,temperature,max_tokens):
    reponse = client.chat.completions.create(
        model= MODEL_NAME,
        messages=[{
            "role":"user",
            "content": prompt
        }],
        temperature=temperature,
        max_completion_tokens=max_tokens
    )
    return reponse.choices[0].message.content

# temperature=0.1: Lower randomness.
# temperature=1.2: Higher randomness.
# max_completion_tokens=100: Limits the generated response length.

# . Experiment with temperature

prompt = "Explain artificial intelligence using a real-world example."

print("LOW TEMPERATURE",generate_response(prompt,0.1,200))
print("LOW TEMPERATURE",generate_response(prompt,1.2,200))


# 3. Experiment with response length
prompt = "Explain how a recommendation system works."

print("SHORT RESPONSE")
print(generate_response(prompt, 0.3, 40))

print("\nLONGER RESPONSE")
print(generate_response(prompt, 0.3, 200))
