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

9. Why are Transformers useful for LLMs?
   it helps to understand or rank how each words is important or related to a particular word so that we can establish the connection between them .

# Interview questions

Try answering these in your own words:

1. What problem does attention solve?
2. Explain Query, Key and Value with an example.
3. What is self-attention?
4. What is the role of softmax in attention?
5. What is the difference between RNN and Transformer?
6. What is positional encoding?
7. What is multi-head attention?
   google:
   Multi-head attention runs multiple attention mechanisms in parallel, splitting the model's capacity to focus on different aspects of the text simultaneousl
