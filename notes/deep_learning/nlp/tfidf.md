TF (Term Frequency): How often a word appears in one document.

IDF (Inverse Document Frequency): How uncommon that word is across all documents.

TF-IDF: Combines both to give a word an importance score.

Compare BoW and TF-IDF.

Use the same documents with CountVectorizer and TfidfVectorizer.

Print both matrices and answer:

tfidf
vocabulary = ['deep' 'interesting' 'is' 'learning' 'love' 'machine']
matrix=
[[0.         0.         0.         0.48133417 0.61980538 0.61980538]
 [0.72033345 0.         0.         0.42544054 0.54783215 0.        ]
 [0.         0.5844829  0.5844829  0.34520502 0.         0.44451431]]

bow
Vocabulary: ['deep', 'i', 'interesting', 'is', 'learning', 'love', 'machine']
[[0, 1, 0, 0, 1, 1, 1], 
[1, 1, 0, 0, 1, 1, 0], 
[0, 0, 1, 1, 1, 0, 1]]

1. Why are the values different?
   bow - Bag of Words treats every word count equally.
   tfidf- consideres the frequence and how that is uncommon across the document

2. Which representation uses raw word counts?
   bow

3. Which representation uses weighted scores?
   tfidf

4. Why might TF-IDF be useful for text classification?
   TF-IDF gives higher importance to words that appear frequently in a particular document but are relatively uncommon across the entire collection. These words can help a classifier distinguish between categories.

- What is TF-IDF?
  a metric that measures how important the word is in the doc

- What are TF and IDF?
  TF (Term Frequency): How often a word appears in one document.
  IDF (Inverse Document Frequency): How uncommon that word is across all documents.

- Difference between BoW and TF-IDF.
  bow - Bag of Words treats every word count equally.
  tfidf- consideres the frequence and how that is uncommon across the document

- Why are common words given lower importance?
  Words appearing in almost every document are less useful for distinguishing one document from another, so IDF reduces their weight.

- Where is TF-IDF used?
  TF-IDF is widely used across search engines, text analytics, and machine learning pipelines whenever systems need to quickly rank, categorize, or extract meaning from large collections of text.

  Interview questions

1. What is TF-IDF?
2. How is it different from Bag of Words?
3. Why does IDF reduce the importance of common words?
4. Can TF-IDF understand the meaning of a sentence?
   No.It does not understand context, word order, or semantic relationships. For example, it cannot reliably understand that "good" and "excellent" have similar meanings.

5. Can TF-IDF be used for spam classification?
   yes
