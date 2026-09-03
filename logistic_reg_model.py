import pandas as pd
from  sklearn.model_selection  import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# load data
df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# check the types and shape- already done so directly fixing  the data type
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"],errors="coerce")

# Handle missing values
# print("missing value",df.isna().isnull())

# dropping missing values as the count is less
df = df.dropna()

# removing unwanted columns
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

# the pipeline
# Pipeline = Pipeline([("processing",preprocessor)])

# X_train_processed = Pipeline.fit_transform(X_train)
# X_test_processed = Pipeline.transform(X_test)


# Part 2 —  Logistic Regression
# Create the model:
# model = LogisticRegression()
model = LogisticRegression(max_iter=1000)

# Why do we need to create a model object?
# its initializing the LogisticRegression() 
# When you call LogisticRegression(), Python creates an instance (a concrete object) in memory. 
# This object acts as a dedicated container that will hold both your settings (hyperparameters) 
# and your learned results (trained weights).

# Part 3 — Put preprocessing + model together ⭐
model_pipeline = Pipeline([("processing",preprocessor),("model",model)])

# Part 4 — Train the model
model_pipeline.fit(X_train,y_train)

# What is the model actually learning from X_train and y_train?
# fit is learning the parameters or values for example min, max or avergare from feature tain data(X_train).
# may be applies the learnt params in Y train and analyse

# Part 5 — Make predictions
y_pred = model_pipeline.predict(X_test)

print(y_pred[:20])

# Why are we passing X_test to predict()
# because now model has processed and learnt the parameters on training data so we pass the test data 
# to the model to transoform and predict the results by using the params that it learnt so that it can perform 
# well and give the accurate results and can even handle the future data

# Part 6 — Compare prediction vs reality
print("test data",y_test.head(20))
print("predicted data",y_pred[:20])

# Manual challenge
# Count roughly how many predictions appear correct in those 20.
# around 4 or 5

# Part 7 — Your first metric: Accuracy
accuracy = accuracy_score(y_test, y_pred)
# print("accuracy,",accuracy) 0.78
accuracy_percentage = round(accuracy*100,2)
print("accuracy_percentage,",accuracy_percentage) 

# Part 8 — Check the model's training accuracy too
train_pred = model_pipeline.predict(X_train)
train_accuracy = accuracy_score(y_train,train_pred)
train_accuracy_percentage = round(train_accuracy*100,2)

print("accuracy_percentage,",accuracy_percentage)  #78.68
print("train_accuracy_percentage,",train_accuracy_percentage) #80.91

# Is the training accuracy higher or lower than the test accuracy?
# training accuracy is higher

# Part 9 — Mini experiment ⭐
# Now change LogisticRegression() to: LogisticRegression(max_iter=1000)

# Run again Compare your result.You may or may not see a meaningful difference.
# ans: no difference