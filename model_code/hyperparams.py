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
from sklearn.model_selection import GridSearchCV

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
f1_yes_scorer = make_scorer(f1_score, pos_label="Yes")

 # 🔴🔴🔴🔴🔴🔴🔴🔴   # 🔴🔴🔴🔴🔴🔴🔴🔴   # 🔴🔴🔴🔴🔴🔴🔴🔴   # 🔴🔴🔴🔴🔴🔴🔴🔴 
 # 🔴🔴🔴🔴🔴🔴🔴🔴 hyperparameters

param_grid = {"model__C":[0.01, 0.1, 1, 10, 100]} #two underscores Because your Logistic Regression is inside your Pipeline:

gird_search = GridSearchCV(model_pipeline,param_grid=param_grid,cv=5,scoring=f1_yes_scorer)

gird_search.fit(X_train,y_train)

print("grid_search.best_params_",gird_search.best_params_)  #{'model__C': 0.1}
print("grid_search.best_score_",gird_search.best_score_)  #0.63


# 🔴 Part 5 — Understand what just happened
# This is the most important part.

# Suppose sklearn says:

# Best C = 10
# Best CV F1 = 0.64

# It essentially tested:

# C=0.01 → CV
# C=0.1  → CV
# C=1    → CV
# C=10   → CV ⭐
# C=100  → CV

# And each candidate itself goes through the 5-fold CV process.

# So you're not simply:

# "Trying five values."

# You're doing:

# five hyperparameter choices × five validation folds.

# That's 25 model evaluations.

# You don't need to manually calculate this; just understand what's happening.

# 🟢 Part 6 — Evaluate on the actual test set
best_model = gird_search.best_estimator_
y_pred_ = best_model.predict(X_test)

cm = confusion_matrix(y_test, y_pred_)
print(cm)

print("classification_report", classification_report(y_test,y_pred_))

# 🔴 Compare against your previous model.

# Create:

# Metric	Before tuning	After tuning
# Accuracy		     .73          .74
# Precision	            .5        .5	
# Recall		       .79         .79
# F1		             .61       .61


# inspect all results
# print("gird_search.cv_results_", gird_search.cv_results_)

# Convert the relevant pieces into a DataFrame:
results = pd.DataFrame(gird_search.cv_results_)
print("results", results)

#   0.632592 mean_test_score,  rank_test_score - 1, {'model__C': 0.1} 