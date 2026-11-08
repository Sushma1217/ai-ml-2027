import re #(regular expression)

###########Part A — Basic text cleaning###################
text = "I LOVE Machine Learning!!! NLP is interesting."
text = text.lower()
text = re.sub(r"[^a-z0-9\s]", "", text)
print(text)

############Part B — Tokenization##############
tokens = text.split()
print(tokens)

# models cannot directly process ordinary sentences as humans do. We need to represent text in a numerical form.

#################Part C — Create a vocabulary - TOKEN IDS###################
vocabulary = {}

for token in tokens:
    if token not in vocabulary:
        vocabulary[token] = len(vocabulary)+1
print(vocabulary)
# We want each unique word to have one ID, rather than assigning a new ID every time the word appears.


###########Part D — Convert text into token IDs#############
token_ids = [vocabulary[token] for token in tokens] #list comprehension

########Part E — Handle unknown words##########
new_text = "I love deep learning"
# The word deep is not in our vocabulary. so 
#  we need an unknown-token strategy. One simple approach is an UNK token.

vocabulary["<UNK>"] = len(vocabulary)+1
new_tokens = new_text.lower().split()
new_ids = [vocabulary.get(token, vocabulary["<UNK>"]) for token in new_tokens]
print(new_ids)
text
# [ vocabulary.get( token , vocabulary["<UNK>"] ) for token in new_tokens ]
#   └────┬───────┘  └──┬──┘ └─────────┬────────┘  └──────────┬───────────┘
#        │             │              │                      │
#    Look up this      │        If not found,          Loop through each
#        word      Separates   use the ID stored       word in your list
#                   arguments    under "<UNK>"