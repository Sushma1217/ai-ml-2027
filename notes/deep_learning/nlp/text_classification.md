stratify=labels = This keeps the proportion of spam and non-spam examples approximately balanced in both sets.

- Accuracy: How many predictions were correct overall?
- Precision: Of the messages predicted as spam, how many were actually spam?
- Recall: Of all actual spam messages, how many did the model identify?
- Confusion matrix: Shows correct and incorrect predictions for each class.

What is text classification?
analysing the words or sentences or text and classifying into the correct category.

Why do we convert text into numerical features?
because machine can understand the numbers

Why use TF-IDF?
because TF-IDF gives more importance to the words that appear frequently and not common across the entire collection(or uncommon) which helps to distinguish between the categories.

Why use Logistic Regression?
because its a categorical problem or classification problem and Logistic regressed is most used for classification problem between two values(true or false, 0 or 1).
better answer:
Logistic Regression is a supervised classification algorithm that learns from numerical features and predicts the probability of a category. It can be used for binary classification, such as spam or not spam.

Why must we fit TF-IDF only on training data?
to avoid the data leakage so the model can learn the pattern instead of memorizing the params and apply them to predict on the new data. the vocabulary and IDF weights must be learned from training data alone, so the test data remains unseen.

What are accuracy, precision, recall and a confusion matrix?
accuracy - how much the model was able to predict correctly overall.
precision - out of all the prediction, how much the model was able to predict corretly.
Problem related: Of all messages predicted as spam, how many were actually spam?
recall - out the all positive prediction how much model was able to predict correctly
Problem related: Of all actual spam messages, how many did the model correctly identify?
confusion matrix - shows correct and incorrect prediction for each class

Interview questions

1. What is text classification?
2. Why is TF-IDF used before training a classifier?
3. Why is Logistic Regression suitable for text classification?
4. What is the difference between precision and recall?
5. What is data leakage in NLP?
   In NLP, this most commonly occurs during preprocessing—such as running fit_transform with a vectorizer on the entire dataset before splitting it. This allows your training set to "learn" the vocabulary, word frequencies, or IDF scores of the test data ahead of time.
