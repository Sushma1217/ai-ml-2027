So far, we've learned how to clean text and convert words into IDs.

But token IDs alone don't tell a traditional ML model how frequently words appear in a document.

Bag of Words represents text using word counts.
Example:

Two sentences:

- "I love machine learning"
- "I love deep learning"
  Vocabulary:

["i", "love", "machine", "deep", "learning"]

Their Bag of Words representations:
Vocabulary
i
love
machine
deep
learning

Sentence 1
[1, 1, 1, 0, 1]
Sentence 2
[1, 1, 0, 1, 1]

The key limitation: Bag of Words ignores word order and context.

Include:

1. What is Bag of Words?
   it represent the words along with their occurence count.

2. How does it convert text into numbers?
   it converts text into numbers by simply counting how many times the words apprears.

3. What is vocabulary?
   the collection or mapping of known tokens

4. What is a document-term matrix?
   A document-term matrix (DTM) is a grid where rows represent individual documents and columns represent unique words, with each cell storing that word's frequency in a specific document. It essentially translates an entire text corpus into a numerical table that machine learning algorithms can analyze.

5. What is the difference between manual BoW and CountVectorizer?
   Manual BoW: We create the vocabulary and count word occurrences ourselves.
   CountVectorizer: Scikit-learn automates vocabulary creation and word counting, returning a document-term matrix.
6. What are the limitations of BoW?
   the limitation of bow is that it ignores the order of the word and its context.

7. Why does BoW ignore context and word order?
   because its counts their frequency not the position and sequence.
   google answer:
   Bag of Words treats text like a literal grocery bag of loose items, counting only word frequencies while completely throwing away positions and sequences. Because it ignores where words appear relative to each other, sentences with completely opposite meanings (like "dog bites man" vs. "man bites dog") end up looking identical to the computer.

Interview questions

- What is Bag of Words?
- What is a document-term matrix?
- What is the difference between tokenization and BoW?
  Tokenization: Splitting text into individual tokens.
  BoW: Converting those tokens into numerical word-count vectors.

- What are the limitations of BoW?
- Why does CountVectorizer return a sparse matrix?
  CountVectorizer returns a sparse matrix because the resulting document-term grid is mostly filled with zeros.
