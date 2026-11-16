from  sklearn.model_selection  import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

texts = [
    "Win a free prize now",
    "Claim your free cash reward",
    "Congratulations you won a lottery",
    "Hey are we meeting today",
    "Can we have lunch tomorrow",
    "Are you coming to the meeting",
    "Free entry in a competition",
    "Let's catch up this weekend",
    "You have won a free gift",
    "Please send me the project update"
]

labels = [
    1, 1, 1, 0, 0, 0, 1, 0, 1, 0
]
# 1 = spam, 0 = not spam

# Split the texts and labels into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(texts,labels,test_size=.2, random_state=42)

# Use TfidfVectorizer to convert the text into numerical features.
vectorizer = TfidfVectorizer()

#training the data
X_train_vec = vectorizer.fit_transform(X_train)

#testing 
X_test_vec = vectorizer.transform(X_test) 

# Train a Logistic Regression classifier.
model = LogisticRegression()
model.fit(X_train_vec,y_train)

# 5. Predict labels for the test data
y_pred = model.predict(X_test_vec)

print("Predicted labels:", y_pred)
print("Actual labels:   ", y_test)

# Predicted labels: [0 0]
# Actual labels:    [1, 1]

#my notes
# Think of training a model like studying for an exam:

# * **`X_train_vec` (Questions) & `y_train` (Answers):** When you call `model.fit(X_train_vec, y_train)`, you are giving the model both the training texts (`X_train_vec`) and their actual labels (`y_train`). This is the study phase where the model learns the patterns—it needs to know the correct answers so it can figure out what makes a text spam or not spam.
# * **`y_test` (The Final Exam Answer Key):** `y_test` contains the correct labels for your test set, but **we hide this from the model**. If you passed `y_test` during training or prediction, the model would essentially be cheating by looking at the answer key beforehand.
# * **`model.predict(X_test_vec)`:** Here, you only pass the test features (`X_test_vec`) because you want to test if the model can figure out the answers *on its own* without peeking.

# Once you get `y_pred` (the model's guesses), you then compare `y_pred` against the hidden `y_test` at the very end to see how well it performed.

#Evaluate the model using metrics
print(accuracy_score(y_test, y_pred))  #0.0
print(confusion_matrix(y_test, y_pred)) #[[0 0]
 #[2 0]]
print(classification_report(y_test, y_pred)) #got 0 for all 
