# refer my python notes for more explanantion

Include:

1. Why do we need attention?
   while processing text we might end up in finding how the particular word is related to other words. Attenstion solves this problem it helps to findout how a particular word is relevant to other words.

2. What is self-attention?
   its the tech where the model can consider and assign the weight to other words while processing a particular or target word.

3. What are Query, Key and Value?
   Query- the information that im looking for
   Key - the info that each item represent
   value- the info that each item contain

4. What is the purpose of softmax?
   Softmax converts scores into weights

5. Why do we scale attention scores?
   sclaing helps to keep the scores in managable range before applying the softmax.

6. What is a Transformer?
   transformer is the neural network architecture that uses attension mechanism to process the sequence.

7. What is positional encoding?
   Positional encoding is a technique used in Transformer architectures to give the model an awareness of the order of words in a sequence.

8. Difference between RNN and Transformer.
   RNN - process the words sequentially, reading one word at a time so it might fail to captiure the relationship between the words
   transofmer- process entire sequence in parallel using self attension and capture the relationship

   better ans
   RNNs process sequences sequentially, passing information through a hidden state. Transformers use attention to establish relationships between tokens and can process the input sequence in parallel during training.

9. Why are Transformers useful for LLMs?
   it helps to understand or rank how each words is important or related to a particular word so that we can establish the connection between them .
   attention allows the model to build contextual representations using relationships between tokens, which helps it process language and generate relevant text.

# Interview questions

Try answering these in your own words:

1. What problem does attention solve?
   Attention helps a model identify relationships between different tokens in a sequence. It allows the model to combine information from relevant tokens rather than relying only on a fixed sequential hidden state.

2. Explain Query, Key and Value with an example.
   Query represents what information a token is looking for. Key represents what information each token offers for matching. Value contains the information that gets combined. The Query is compared with Keys to calculate attention weights, which are then applied to Values.

3. What is self-attention?
   Self-attention is a mechanism where tokens in the same input sequence interact with one another. Each token uses Queries, Keys and Values to calculate how much information to take from other tokens.
4. What is the role of softmax in attention?
   Softmax converts attention scores into normalized weights. These weights indicate how much information a token receives from other tokens, and they are used to combine the Value vectors.
5. What is the difference between RNN and Transformer?
   RNNs process sequence elements step by step and maintain a hidden state. Transformers use attention to model relationships between tokens and allow parallel processing of input tokens during training.
6. What is positional encoding?
   Positional encoding adds information about token positions to their embeddings. This helps Transformers understand word order because attention alone does not inherently represent sequence position.
7. What is multi-head attention?
   google:
   Multi-head attention runs multiple attention mechanisms in parallel, splitting the model's capacity to focus on different aspects of the text simultaneously.

   better ans:
   Multi-head attention runs multiple attention operations in parallel. Each head can learn different relationships or patterns between tokens. Their outputs are combined to form a richer representation.
