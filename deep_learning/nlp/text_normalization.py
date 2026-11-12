text = "I am learning NLP and I am enjoying machine learning"
tokens = text.lower().split()
stop_words = {"i","am","and"}

filtered_words = [word for word in tokens if word not in stop_words]
print(filtered_words)

# Stemming with NLTK
from nltk.stem import PorterStemmer
import nltk


stemmer = PorterStemmer()
words = ["playing", "played", "plays", "studies"]

for word in words:
    print(word,"->", stemmer.stem(word))

# Part D — Lemmatization with NLTK
nltk.download("wordnet")
nltk.download("omw-1.4")

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
words = ["playing", "played", "studies", "better"]

for word in words:
    print(word,"->",lemmatizer.lemmatize(word))

# Important: Without the correct part-of-speech information, the default lemmatizer may not convert every word to the expected base form. For example, "playing" may remain "playing" when treated as a noun.

print(lemmatizer.lemmatize("playing", pos="v")) #pos is part of speech so v - verb
print(lemmatizer.lemmatize("better", pos="a")) #a- adjective, n- noun