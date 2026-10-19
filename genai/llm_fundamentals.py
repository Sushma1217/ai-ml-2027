text = "AI makes software smarter."
print("original text",text)
print("Character count:", len(text))
print("Word count:", len(text.split()))

# Note:
# Word count is not the same as an LLM token count.
# Actual tokenization depends on the model.


prompt_a = "Explain AI."

prompt_b = """
Explain artificial intelligence to a beginner.
Use three simple bullet points and include
one everyday example.
"""

print("\nPrompt A:")
print(prompt_a)

print("\nPrompt B:")
print(prompt_b)

# Concept: In a chat-based LLM application, a system instruction defines the assistant's general behavior, while a user message contains the user's specific request. 
# The model uses both as context when generating a response.
system_instruction = (
    "You are a patient teacher. "
    "Explain technical concepts simply."
)

user_message = (
    "Explain neural networks to a beginner."
)

print("\nSystem instruction:")
print(system_instruction)

print("\nUser message:")
print(user_message)

temperature_for_factual_task = 0.2
temperature_for_creative_task = 0.8