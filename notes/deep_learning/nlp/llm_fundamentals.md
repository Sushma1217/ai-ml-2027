for more details-
refer my notes

What is a token?
text or sentences broken into small pieces its called token, it can be punctuation, word, a part of word etc.

What is tokenization?
the process of breaking the text into small unit is called tokenization

Why do LLMs use token IDs?
because comupter can understand only the numbers, so for each token an unique id will be assinged and it present that token

What is a context window?
the amount of information it consider to predict the next token.

What information consumes context tokens?

What is next-token prediction?
it is the process of predicting the next token based on the past or previous token.

What are logits and probabilities?
logits are weight or score assigned to the token so while predicting the next token a model can consider it.
probabilities - scores or logits are converted into the probability represent the chances of relating to the previous token.

Important interview point: Context window is not the same as memory. A model's context window describes what it can process within a request. It does not mean the model permanently remembers everything from previous conversations.

What is the difference between context window and memory?
context window is about what amoutn of information it can consider or process while processing. not rembering
memory - model remembers everything from previous conversations
