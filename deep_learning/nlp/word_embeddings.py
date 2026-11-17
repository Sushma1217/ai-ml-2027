from gensim.models import Word2Vec

sentences_array = [
    ["king", "queen", "royal", "kingdom"],
    ["man", "woman", "boy", "girl"],
    ["machine", "learning", "deep", "neural"],
    ["deep", "learning", "model", "training"],
    ["queen", "woman", "royal", "king"]
]

# Create and train the model
model = Word2Vec(sentences=sentences_array, vector_size=50,window=2,min_count=1,workers=1, sg=1,epochs=100)
# | Parameter | Meaning |
# |--------|--------|
# | `sentences` | Our tokenized training data |
# | `vector_size=50` | Each word gets a vector of 50 numbers |
# | `window=2` | Looks at up to two surrounding words |
# | `min_count=1` | Includes words appearing at least once |
# | `workers=1` | Uses one worker for training |
# | `sg=1` | Uses Skip-gram |
# | `epochs=100` | Goes through the training data 100 times |


print("Vocabulary:",model.wv.index_to_key)

# model.wv provides access to the learned word vectors.
# index_to_key gives us the list of words included in the model's vocabulary.

#Get the vector for a word
king_vector = model.wv["king"]
print("King vector:",king_vector) 
print("Vector shape:",king_vector.shape) #50

# Why 50?
# Because we selected vector_size=50.
# The word king is now represented by 50 numerical values instead of a text string.

# Step 7 — Find similar words
similar_words = model.wv.most_similar("king",topn=3)
print("Words similar to king:")
for word, score in similar_words:
        print(word, score)
# Words similar to king:
# kingdom 0.30768024921417236
# machine 0.2254999727010727
# boy 0.19931486248970032

