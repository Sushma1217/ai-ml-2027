documents = [
    "I love machine learning",
    "I love deep learning",
    "Machine learning is interesting"
]

# Normalize text
documents = [doc.lower() for doc in documents]

# Build vocabulary
vocabulary = sorted(set (word for doc in documents for word in doc.split()))
print("Vocabulary:", vocabulary)

# Part B — Generate word-count vectors
bow_vectors = []

for document in documents:
    words = document.split()
    vector = []
    for word in vocabulary:
        vector.append(words.count(word)) #It counts how many times a vocabulary word appears in the current document.
    bow_vectors.append(vector)
print(bow_vectors)

# Part C — Use Scikit-learn

# sentences = [
#     "I love this movie",
#     "I do not love this movie"
# ]

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
X= vectorizer.fit_transform(documents)

print(vectorizer.get_feature_names_out())
print(X.toarray())


# Understand:
# - fit() learns the vocabulary.
# - transform() converts documents into numerical vectors.
# - fit_transform() performs both.
# - toarray() displays the sparse matrix as a regular array.
# The output should represent the same word counts as your manual implementation, though the vocabulary ordering and default preprocessing may differ.

# Part D — Understand the limitation
sentences = [
    "I love this movie",
    "I do not love this movie"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

print(vectorizer.get_feature_names_out())
print(X.toarray())