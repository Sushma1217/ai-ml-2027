temperature
is a generation setting that influence how a llm select its next token. Lower values generally make outputs more predictable; higher values generally allow more variation. Exact behavior depends on the model and API.

For example:

- Lower temperature: useful when you want relatively consistent answers.
- Higher temperature: can be useful for brainstorming and creative writing.
  Temperature does not guarantee factual accuracy. A low-temperature answer can still be wrong.

Concept: A hallucination occurs when an LLM produces an incorrect or unsupported answer, sometimes presenting it confidently.

For example, a model might invent a research paper or give an incorrect Python function name.

In a real application, we reduce risk by verifying claims against trusted sources, testing generated code, and using retrieved documents when appropriate.

# questions

What is an LLM?
its a model that is trained on huge amount of data generates the output by analysing the relationship, applying learned patterns, predicting next word(token)
application- chat assistant, writing code, creative writing.

How does next-token generation work?
Next-token generation is the core mechanism LLMs use to write text. It happens in an automated loop:

- **1. Tokenization:** Your input text is broken down into smaller chunks called tokens (words, parts of words, or punctuation).
- **2. Scoring Probabilities:** The model passes these tokens through its neural network layers to calculate a probability score for every single token in its vocabulary as the _next_ potential piece.
- **3. Selection:** One token is chosen based on those probabilities (often influenced by settings like temperature).
- **4. Autoregressive Loop:** That new token is added to your original input, and the entire process repeats instantly to generate the next word, continuing until a complete sentence or stop token is reached.

Token
a basic chunk of the text that LLM process, it can we a word, piece of word, punctuation.

What is a prompt?
a ask made by user or query that we give to llm

System instruction vs. user message
user message- what to answer. consist of user specific request
system ins- how to respond. defines general behaviour

What is temperature?
a general setting that influence how llm selects its next token. higher temperature- more creative, variant ans
lower temp- most consistance ans

What is an LLM hallucination?
Concept: A hallucination occurs when an LLM produces an incorrect or unsupported answer, sometimes presenting it confidently.

How LLMs differ from traditional ML models.
traditional ml models- they perform one task, no token based mechanism
llm- multi task, token based

Where these concepts fit in a GenAI application
llm fits in generating text or response for user reponse in real life- chat bot assistance, writing code etc
