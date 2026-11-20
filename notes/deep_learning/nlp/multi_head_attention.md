we implemented one attention operation. But a Transformer uses multiple attention heads so it can learn different relationships between tokens simultaneously. It also needs positional information to understand word order.

We'll now extend what you've already built.

Part A — Multi-head attention
Imagine this sentence:

"The child reads a book."

Different attention heads may learn different relationships:

- One head may focus on subject and verb.
- Another may focus on relationships between nearby words.
- Another may focus on other contextual patterns.
  These are illustrative examples; the model learns the patterns rather than being explicitly instructed to identify grammatical roles.

What happens?

1. Input vectors are passed into multiple attention heads.
2. Each head calculates its own attention output.
3. The outputs are combined.
4. A final learned transformation produces the combined representation.

Part C — Positional encoding
What problem does it solve?

Attention can relate tokens, but the model also needs to know their positions.

Compare:

- "Dog bites man."
- "Man bites dog."
  The words are almost the same, but their order changes the meaning.

Positional encoding adds information about where each token occurs in the sequence.

1. What is multi-head attention?
   multi-head attenstion runs multiple attenstions in parellel, each head can learn different relationship or pattern bewtween the token.

2. Why do we use multiple heads?
   because it can learn the relationship between tokesn simultaneously.

3. What is an embedding dimension?
   the number of values used to represent one word.

4. Why must the embedding dimension be divisible by the number of heads?

5. What is positional encoding?
   it adds the information about where each token occurs in the sequence

6. Why does a Transformer need positional information?
   because it positional holds the information about the order of the token in the sequence which helps to understand the relationship since the process happens parellely

7. What is the difference between token embeddings and positional embeddings?

# interview questions

. Why does a Transformer use multiple attention heads?
MODEL ANSWER
Multiple heads allow the model to learn different relationships between tokens in parallel. Their outputs are combined to produce a richer representation.

2. What is the embedding dimension?
   It is the number of numerical values used to represent each token in the model's embedding space.

3. Why must embed_dim be divisible by num_heads in standard multi-head attention?
   The embedding dimension is split across the attention heads. Divisibility ensures each head receives an equal-sized portion.

4. What is positional encoding?
   It adds information about token positions to token representations so the model can account for sequence order.

5. What is the difference between token embeddings and positional embeddings?
   Token embeddings represent the token's learned numerical representation. Positional embeddings represent where the token occurs in the sequence. They are combined before further Transformer processing.
