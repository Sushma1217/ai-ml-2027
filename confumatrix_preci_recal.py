import pandas as pd
from  sklearn.model_selection  import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

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


model = LogisticRegression(max_iter=1000)


# Part 3 — Put preprocessing + model together ⭐
model_pipeline = Pipeline([("processing",preprocessor),("model",model)])

# Part 4 — Train the model
model_pipeline.fit(X_train,y_train)



# Part 5 — Make predictions
y_pred = model_pipeline.predict(X_test)

print(y_pred[:20])


# Part 6 — Compare prediction vs reality
print("test data",y_test.head(20))
print("predicted data",y_pred[:20])

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


# 🔴🔴🔴🔴🔴🔴🔴🔴
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Part 3 🔴 Manual

# Write down:

# TN = model predicted negative and real value is also negative
# FP = model precited positive and real value is negative
# FN = model predicted neative and real value is positive
# TP = model predicted positive and real value is also positive

# Then figure out which number corresponds to which position in your confusion matrix.

# Part 4 — Classification report
print(classification_report(y_test,y_pred))
#  precision    recall  f1-score   support

# Part 5 — Precision
