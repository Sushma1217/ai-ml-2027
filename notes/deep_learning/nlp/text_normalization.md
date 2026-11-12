Objective: Learn how to clean text beyond basic punctuation removal, and understand why different NLP preprocessing techniques are used.

This is the next logical step before TF-IDF and embeddings.
Part A — Understand the concepts (20 minutes)

1. Stop words
   Stop words are common words that may carry little useful information for a particular NLP task.

Example:
I am learning machine learning

After removing common stop words:
learning machine learning

Examples include is, am, the, a, and.

Important: Don't remove stop words blindly. Words such as "not" can change sentiment and meaning.

2. Stemming
   Stemming cuts words down to a root-like form, often using simple rules.

Examples:
playing → play
played → play
studies → studi

Notice that studi isn't a proper English word. Stemming doesn't always produce dictionary words.

3. Lemmatization
   Lemmatization converts words into their meaningful dictionary base form.

Examples:
studies → study
better → good
running → run

1. What are stop words?
   words that are common and carry little information for nlp task. for example a, the, and, of

2. Why should stop words not always be removed?
   beccause some stop words like not, under, but etc might carry some information or express the tone of the sentences

3. What is stemming?
   cuts the word into root-like form.

4. What is lemmatization?
   Lemmatization converts words into their meaningful dictionary base form.

5. Difference between stemming and lemmatization.
   stemming- cutting the word and transforming into its room form
   lemmatization- converting the word into meaningful form

6. Why does lemmatization use part-of-speech information?
   without pos lemmatization may not convert the word into expected base form for example playing- without pos - playing
   with pos- v - play
   so it wil give the context to convert the word

Interview questions:

- What is the difference between stemming and lemmatization?
- Can removing stop words affect sentiment analysis?
- Why is text normalization important?
  Text normalization is the foundational preprocessing step that transforms raw, messy text into a clean, uniform format so a machine learning model can actually understand the underlying patterns.

- Does every NLP project need stemming or lemmatization?
  No. but im not sure about the reason
