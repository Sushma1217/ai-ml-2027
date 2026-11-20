What is a Transformer block?

So far, you've learned attention, multiple attention heads and positional embeddings. A Transformer block brings several components together: attention, residual connections, normalization and a feed-forward network.

Why do we need it? Attention helps tokens exchange information, while the other components help the model transform and stabilize those representations.

Where does it fit? LLMs such as GPT use stacks of Transformer blocks to process text and predict the next token.
Task 1 — Understand the components
READ & UNDERSTAND
A simplified Transformer block contains:
Component Purpose
Multi-head attention Connects information across tokens
Residual connection Adds the original input back to the transformed output
Layer normalization Helps stabilize the values during training
Feed-forward network Further transforms each token's representation

You don't need to implement all these components manually. PyTorch already provides a Transformer layer.

# causal masking

This is particularly important for GPT-style models.

Imagine the sentence:
"The child reads a book."

When predicting the next word after "The child", the model should not be allowed to look ahead at "reads a book".

Causal masking prevents a token from accessing future tokens.

Visual example: allowed attention positions
The child reads book

Token The child reads book
The ✓ — — —
child ✓ ✓ — —
reads ✓ ✓ ✓ —
book ✓ ✓ ✓ ✓

✓ = allowed to attend to; — = future token is blocked.

1. What is a Transformer block?
   transformer block brings several concepts together like feed forward network, normalization, attention, residual connections

2. What are the four components we discussed?
   normalization, rersidual connection, feed forward network, attension

3. What is a residual connection?
   a shortcut connection in nn that add layer's input directly to its output.

4. What is layer normalization?
   Layer normalization (LayerNorm) normalizes activations across all features within a single sample (token or data point) so they have zero mean and unit variance.

5. What is causal masking?
   its about preventing a token from accessing the future token

6. Why does GPT need causal masking?
   because GPT model usually predicts the next word or token using previous token so casual masking helps in preventing access to the future tokens.

7. What is the difference between an encoder and a decoder?
   An encoder processes the input sequence and produces contextual representations using self-attention. A decoder generates output tokens. In the original Transformer, the decoder also attends to encoder outputs. GPT is decoder-only and uses causal self-attention to predict the next token.

8. Why does the output shape remain [1, 4, 8]?
   this is because the transformer change the representation not their embedding dimension or number of tokens thats why output shape as input shape.

# interview

What are the main components of a Transformer block?
Hide model answerMODEL ANSWER
A Transformer block typically includes multi-head attention, residual connections, layer normalization and a feed-forward network. Together, they allow the model to exchange information between tokens and transform their representations.

2. What is causal masking?
   Hide model answerMODEL ANSWER
   Causal masking prevents a token from attending to future tokens. It ensures that when GPT predicts the next token, it can only use the current and preceding tokens.

3. Why does GPT use a decoder-style Transformer?
   Hide model answerMODEL ANSWER
   GPT is an autoregressive language model. It generates text one token at a time, using previously available tokens to predict the next one. Decoder-style blocks with causal self-attention support this behavior.

4. What is the purpose of a residual connection?
   Hide model answerMODEL ANSWER
   A residual connection adds a block's input to its output. It helps information and gradients flow through deeper networks, making them easier to train.

5. What is the difference between an encoder and a decoder?
   Hide model answerMODEL ANSWER
   A standard Transformer encoder uses self-attention to build contextual representations of the input. A decoder generates output and, in autoregressive models such as GPT, uses causal masking so it cannot attend to future tokens.
