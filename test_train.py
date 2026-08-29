from sklearn.model_selection import train_test_split
import pandas as pd
df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
df_processed = df.copy()


df_processed["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
print(df_processed["TotalCharges"].isna().sum())
print(df_processed["TotalCharges"].dtype)

# Remove customerID 🔴
df_processed = df_processed.drop(columns=["customerID"])
print(df_processed.columns)

X = df_processed.drop(columns="Churn")
Y = df_processed["Churn"]
X_encoded= pd.get_dummies(X, drop_first=True)
print(X_encoded.shape)

# "" TRAIN TEST SPLIT  """
# Part 2 — Train/Test Split
X_train, X_test, Y_train, Y_split = train_test_split(X,Y, test_size=0.2, random_state=42)
# Part 3 — Check the shapes
print("X_train",X_train.shape)
print("X_test",X_test.shape)
print("Y_train",Y_train.shape)
print("Y_split",Y_split.shape)

# Approximately what percentage of the data went into training and testing?
# may be around 20% for test and 80% for training

# Part 4 — Understand random_state
# trying with random_state=10
Z_train, Z_test, A_train, A_split =  train_test_split(X,Y, test_size=0.2, random_state=10)
print("X_train",Z_train.shape)
print("X_test",Z_test.shape)
print("Y_train",A_train.shape)
print("Y_split",A_split.shape)

# Part 5 — Your first Data Leakage challenge
