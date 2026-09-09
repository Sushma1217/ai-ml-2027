
import pandas as pd
from  sklearn.model_selection  import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.model_selection import cross_val_score
from sklearn.metrics import make_scorer, precision_score, recall_score

# load data
df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"],errors="coerce")

df = df.dropna()
df= df.drop(columns="customerID")

# identify and segregating the column
numerical_columns = ["MonthlyCharges","TotalCharges","tenure"]
categorical_columns = ["gender","Partner","Dependents","PhoneService","MultipleLines","InternetService","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport",
                       "StreamingTV","StreamingMovies","Contract","PaperlessBilling","PaymentMethod","SeniorCitizen"]

# Separate features and target
X= df.drop(columns="Churn")
y= df["Churn"]

# train, test and split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.2, random_state=42)

# Preprocessing
# create the transoformers
numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown="ignore",drop="first")

# Part 5 — Create the ColumnTransformer
preprocessor = ColumnTransformer(transformers=[("num",numeric_transformer,numerical_columns),("cat",categorical_transformer,categorical_columns)])


model = LogisticRegression(max_iter=1000, class_weight="balanced")


# Part 3 — Put preprocessing + model together ⭐
model_pipeline = Pipeline([("processing",preprocessor),("model",model)])

# Part 4 — Train the model
model_pipeline.fit(X_train,y_train)

# Part 5 — Make predictions
y_pred = model_pipeline.predict(X_test)

# print(y_pred[:20])

# Part 6 — Compare prediction vs reality
# print("test data",y_test.head(20))
# print("predicted data",y_pred[:20])

# Manual challenge
# Count roughly how many predictions appear correct in those 20.
# around 4 or 5

# Part 7 — Your first metric: Accuracy
accuracy = accuracy_score(y_test, y_pred)
accuracy_percentage = round(accuracy*100,2)
print("accuracy_percentage,",accuracy_percentage) 

# Part 8 — Check the model's training accuracy too
train_pred = model_pipeline.predict(X_train)
train_accuracy = accuracy_score(y_train,train_pred)
train_accuracy_percentage = round(train_accuracy*100,2)

print("accuracy_percentage,",accuracy_percentage)  #78.68
print("train_accuracy_percentage,",train_accuracy_percentage) #80.91

cm = confusion_matrix(y_test, y_pred)
print(cm)

print("classification_report", classification_report(y_test,y_pred))

# Part 4 — Check class distribution
print(y.value_counts())

print(y.value_counts(normalize=True))

 # 🔴🔴🔴🔴🔴🔴🔴🔴 cross validation


# 1. Define a custom scorer that sets pos_label='Yes'
f1_yes_scorer = make_scorer(f1_score, pos_label="Yes")

f1__scores = cross_val_score(
    model_pipeline,
    X_train,
    y_train,
    cv=5,
    scoring=f1_yes_scorer
)
print("f1__scores",f1__scores)
print("f1__scores", f1__scores.mean())
print("f1__scores", f1__scores.std())

# Part 6 — Compare metrics
# accuracy
scores_accuracy = cross_val_score(model_pipeline,
    X_train,
    y_train,
    cv=5,
    scoring="accuracy")
print("scores_accuracy",scores_accuracy.mean())
print("scores_accuracy",scores_accuracy.std())

# precision
precision_yes_scorer = make_scorer(precision_score, pos_label="Yes")
scores_precision = cross_val_score(model_pipeline,
    X_train,
    y_train,
    cv=5,
    scoring=precision_yes_scorer)
print("scores_precision",scores_precision.mean())
print("scores_precision",scores_precision.std())

# recall
recall_yes_scorer = make_scorer(recall_score, pos_label="Yes")
scores_recall = cross_val_score(model_pipeline,
    X_train,
    y_train,
    cv=5,
    scoring=recall_yes_scorer)
print("scores_recall",scores_recall.mean())
print("scores_recall",scores_recall.std())


# Part 7 — Look at consistency

# Don't only calculate the mean.

# Also calculate:

# scores.std()
# Why?

# Suppose:

# Model A:
# 0.69
# 0.70
# 0.71
# 0.70
# 0.69

# versus:

# Model B:
# 0.50
# 0.85
# 0.62
# 0.79
# 0.55

# Both might have a similar average.

# But which one would make you more comfortable putting into production?

# 🔴 Explain why.

# This is the beginning of model stability/reliability thinking.
# ans: i would make model A because the difference of the vlaues are minimal which shows model is more or
# less working in same way

