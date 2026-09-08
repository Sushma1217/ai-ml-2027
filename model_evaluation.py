
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

# 🔴🔴🔴🔴🔴🔴🔴🔴

# Part 1 — Establish your baseline
# Record these values:

# Train accuracy:80.91
# Test accuracy: 78.68
# Precision — Yes:  0.62
# Recall — Yes:   0.51    
# F1 — Yes:   0.56 
# Confusion Matrix:
# [[915 118]
#  [182 192]]

# 🔴 Manual What do I think is the biggest weakness of my current model?
# overfitting as model perfomred well with traning data as compared to test.
# model failed in false negative(recall cm(182)) and it did not predict accurately for cusomter who churn 
# overall in predicted yes class the model did not perform well 

# Part 2 — Look at the confusion matrix properly
# TN = 915
# FP = 118
# FN = 182
# TP = 192

# 🔴 Then answer:
# How many customers who actually churned did we miss?
# 182

# How many customers did we incorrectly classify as churners?
# 118

# Which error would be more expensive for a telecom company?
# recall because its about of all churn customer how many the model was able to predict, so the missed 
# count of customer is a loss of revenue for the company as they lost them


# Part 3 — Calculate metrics manually
# Accuracy- (TP+TN)/(TP+TN+FP+FN)
# (192+915)/ (915+118+182+192) = .78

# Precision
# TP / (TP + FP)  
# 192/(192+118) = .61

# Recall
# TP/(TP+FN) 
# 192 /(192+182) = .51

# F1 For now, use:
# 2 × (Precision × Recall)
# ------------------------
#  Precision + Recall
# 2*(.61 *.51)/.61+.51 = 0.5098

# Part 4 — Check class distribution
print(y.value_counts())

print(y.value_counts(normalize=True))

# 🔴 Answer:
# How many Yes?   1869
# How many No?  5163
# What percentage is each? 
# no- 0.73
# Yes    0.26
# Is the target balanced? no

# Then think:
# # Could this imbalance be one reason accuracy isn't telling the complete story?
# # might be as the value class not properly distributed
# model = LogisticRegression(
#     max_iter=1000,
#     class_weight="balanced"
# )

# balanced_accuracy =  accuracy_score(y_test, y_pred)
# balanced_accuracy_percentage = balanced_accuracy*100

# cm1 = confusion_matrix(y_test, y_pred)
# print(cm1) 
# # [[915 118]
# #  [182 192]]

# print("classification_report", classification_report(y_test,y_pred))

2*(.61 *.51)/.61+.51 = 0.5098

#                  Original     Balanced
# Accuracy          78              73.13
# Precision: Yes    0.62             0.50
# Recall: Yes       0.51             0.79   
# F1                0.50            .70

# the balanced one
# Why?
# when we look that metrics, the recall is high which means the balanced model was able to predict more customers who churn out of all 
# churn customers which helps company to take some action to retain them.
# the precision is low which means the false positive that is the model was able to predict
#  correctly nearly 50% with little more false alarms compared to the original
# the metric F1 the combination of recall and precision shows high in balanced model which shows model efficiency.

# Part 8 — Interview-level scenario
# Your model has 79% accuracy. Why should I hire you if you can't get 90%?"
# ans: the model efficiency do not soley depends on the accuracy. it depends on the class distribution among the
# data moints when we do the model evaluation we must carefully examine the factors like precision, recall and F1 etc
# higher the recall shows the large number of positive cases found by model example model was able to find 
# large numbers of customer who churn so that company can take some measures to retain them
# similarly higher the precision means model predicted positive most of the time which shows efficiency of the model
# fewer the false positive and false negative are the important indicators of the model accuaray.
# we can even compare f1 which combines the results of precision and recall.
# we can even take measure on model improvement by identifiying where it is making wrong prediciton

