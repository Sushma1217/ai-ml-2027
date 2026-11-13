from sklearn.feature_extraction.text import TfidfVectorizer


documents = [
    "I love machine learning",
    "I love deep learning",
    "Machine learning is interesting"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)
print(vectorizer.get_feature_names_out())
print(X.toarray())
