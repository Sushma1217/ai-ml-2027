import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print(df.shape)
print(df.dtypes)

# converting total charges into num col
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
print(df.dtypes)

# Handle missing values
print(df.isna().sum())

# dropping missing values as the count is low
df = df.dropna()
print("after dropping missing vlaue",df.isna().sum())

# removing irrelevant columns 
df = df.drop(columns="customerID")
# df_processed = df_processed.drop(columns=["customerID"])
print(df.columns)

# Separate features and target
X = df.drop(columns="Churn")
Y = df["Churn"]

# Part 2 — Train/Test Split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=.2, random_state=42)

# Part 3 — Identify columns
print(df.dtypes)
# numerical = MonthlyCharges, TotalCharges, tenure
# binary category - senionCitizen
# categorical - rest all

numerical_columns = ["MonthlyCharges","TotalCharges","tenure"]
categorical_columns = ["gender","Partner","Dependents","PhoneService","MultipleLines","InternetService","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport",
                       "StreamingTV","StreamingMovies","Contract","PaperlessBilling","PaymentMethod","SeniorCitizen"]

# Part 4 — Create the transformers
numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown="ignore",drop="first")

# Part 5 — Create the ColumnTransformer
preprocessor = ColumnTransformer(transformers=[("num",numeric_transformer),("cat",categorical_transformer)])
print("preprocesser",preprocessor)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numerical_columns),
        ("cat", categorical_transformer, categorical_columns)
    ]
)

# What is ColumnTransformer doing here?
# it is dividing the columns into numeric and categorical and applying scalar, encoder and merging it together.

# Part 6 — Fit and transform
X_train_processded = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

# Part 7 — Inspect the result
print("X_train", X_train.shape)
print("X_test", X_test.shape)

print("X_train_processded", X_train_processded.shape)
print("X_test_processed", X_test_processed.shape)

# observation
# The number of columns will increase
# Reason:
# Number of columns have increased because the coulmn transfer tool has performed encoding where 
# categorical columns have converted into numeric values using one hot encoder(in 0/1 forms) where each 
# value got its own column as machine can under only numeric values.

# Part 8 — The Pipeline
# For now, create a pipeline containing only the preprocessor:
Pipeline = Pipeline([("preprocessing",preprocessor)])

X_train_processed = Pipeline.fit_transform(X_train)
X_test_processed = Pipeline.fit_transform(X_test)

print("X_train_processed ", X_train_processed.shape)
print("X_test_processed ", X_test_processed.shape)

# //same output
# X_train_processed  (5625, 30)
# X_test_processed  (1407, 30)


