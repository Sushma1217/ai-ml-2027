1. What are word embeddings?
   Until now, we have converted words into numbers using BoW and TF-IDF.

   For example:
   - BoW tells us how many times a word appears.
   - TF-IDF tells us how important a word is in a document.
   - Word embeddings represent a word as a list of numbers (a vector) that captures aspects of its meaning and usage.
     Think of it this way: words used in similar contexts tend to have similar vector representations.

   For example, king and queen may have more similar vectors than king and banana.Why do we need them?

   Because a machine-learning model needs numbers, but simple word counts don't capture semantic relationships between words.

2. What is Word2Vec?
   Word2Vec is a technique that learns word embeddings by looking at how words appear together in sentences.

   The basic idea is:
   Words that appear in similar contexts often have related meanings.
   For example:
   "The king lives in the palace."
   "The queen lives in the palace."
   The model learns from surrounding words and adjusts the word vectors during training.

3. CBOW vs Skip-gram
   These are two approaches used by Word2Vec.
   CBOW — Continuous Bag of Words
   Predicts the missing or target word using the surrounding words.
   CONTEXT WORDS
   The,lives,in,palace
   |
   king ----> Predicted target word

   Skip-gram: Predicts the surrounding words using the target word.
   ex: king--->Input target word
   The, lives, in, palace---> Predicted context words

Remember this simple distinction:

- CBOW: Context → Target word.
- Skip-gram: Target word → Context.

4. What are vector size and context window?
   Vector size (embedding dimension)
   This is the number of values used to represent one word.
   For example, if vector size is 100, every word gets a vector containing 100 numbers.
   A larger vector can represent more patterns, but it also needs more training data and computation. Bigger isn't automatically better.

   Context window
   This controls how many nearby words the model considers when learning relationships.
   For example:
   The king lives in the palace
   If the context window is 2, the model looks at up to two words on either side of a target word.

5. Why does a small dataset produce poor embeddings?
   Imagine learning the meaning of English words after reading only five sentences.

   You would see only a tiny number of word combinations and wouldn't understand how words are used in different contexts.

   Word2Vec has the same limitation. It needs many examples of words appearing in different contexts to learn useful representations.

   Our small dataset is only for learning how to use the library, not for producing meaningful embeddings.

   Topic Short answer to remember
   Word embeddings: Numerical vectors representing words and their semantic relationships
   Word2Vec: Learns word vectors using surrounding context
   CBOW :Predicts target word from context
   Skip-gram : Predicts context from target word
   Vector size : Number of dimensions in a word vector
   Context : window Number of nearby words considered
   Small: dataset Not enough examples to learn reliable word relationships

6. What is Gensim?
7. What does most_similar() do?
   it finds the top n most similar words in a vector.

8. What is cosine similarity?
   it measures how similar two vectors based on the angle between them.
   closer direction = higher similarity
   more different direction = lower similarity

9. Why does a small dataset produce poor embeddings?
   because the model gets fewer examples or dataset to learn the pattern, analyse the parameters so when it faces new data it might fail to work on

# actual implementation with gensim

Gensim is a Python library used to work with text data. It provides implementations of algorithms such as Word2Vec that learn numerical representations (vectors) of words.

Gensim's Word2Vec expects tokenized sentences in this format:
[
["i", "love", "learning"],
["i", "love", "python"]
]

| Parameter        | Meaning                                  |
| ---------------- | ---------------------------------------- |
| `sentences`      | Our tokenized training data              |
| `vector_size=50` | Each word gets a vector of 50 numbers    |
| `window=2`       | Looks at up to two surrounding words     |
| `min_count=1`    | Includes words appearing at least once   |
| `workers=1`      | Uses one worker for training             |
| `sg=1`           | Uses Skip-gram                           |
| `epochs=100`     | Goes through the training data 100 times |

Important: sg=1 means Skip-gram. If you use sg=0, it uses CBOW.

What does training actually mean?
The model repeatedly examines the words and their surrounding context. It adjusts its internal numerical representations to improve its ability to predict context words.

model.wv provides access to the learned word vectors.
index_to_key gives us the list of words included in the model's vocabulary.

What is cosine similarity?
It measures how similar two vectors are based on the angle between them.
Closer direction → higher similarity.
More different direction → lower similarity.

# interview questions

Q1. What is the difference between TF-IDF and Word2Vec?

TF-IDF represents words using importance scores based on document frequency. Word2Vec learns dense numerical vectors based on surrounding word contexts.

Q2. What is the difference between CBOW and Skip-gram?

CBOW predicts a target word using surrounding words. Skip-gram predicts surrounding words using a target word.

Q3. What does vector_size mean?

It specifies the number of dimensions in the vector representing each word.

Q4. Does Word2Vec understand the meaning of a sentence?

No. Traditional Word2Vec learns static word representations. It does not understand sentence-level context in the way modern contextual language models do.

Q5. What is the limitation of Word2Vec?

A word gets the same vector regardless of its context. For example, the word "bank" in a river context and a financial context receives the same embedding.
