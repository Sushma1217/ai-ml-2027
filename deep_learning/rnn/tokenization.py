import tiktoken

# Step 1: Load a tokenizer
encoding = tiktoken.get_encoding("cl100k_base")

# Step 2: Provide some text
text = "Artificial Intelligence is transforming software development."

# Step 3: Convert text into token IDs
token_ids = encoding.encode(text)

# Step 4: Display token IDs
print("Token IDs:", token_ids)

# Step 5: Display individual token pieces
tokens= [encoding.decode_single_token_bytes(token).decode("utf-8", errors="replace")
         for token in token_ids]
print("Tokens:", tokens)

# Step 6: Count the tokens
print("Number of tokens:", len(token_ids))

# Step 7: Convert token IDs back into text
decoded_text = encoding.decode(token_ids)
print("Decoded text:", decoded_text)

# Code	What it does
# get_encoding()	Loads the tokenizer
# encode()	Converts text into token IDs
# decode_single_token_bytes()	Helps display individual token pieces
# len(token_ids)	Counts tokens
# decode()	Converts token IDs back into text

# Calculate a token budget
# Context window example
context_window = 8000
input_tokens = 6000
requested_output_tokens = 2500

remaining_tokens = context_window - input_tokens

allowed_output_tokens = min(requested_output_tokens,remaining_tokens)
print("Remaining tokens:", remaining_tokens)
print("Allowed output tokens:", allowed_output_tokens)


# Remaining tokens: 2000
# Allowed output tokens: 2000
# This is a simplified budget calculation. Real APIs may also have separate input and output limits.



