import pandas as pd
df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Part 3 — Your first implementation
# Create a small example yourself:

contract_example = pd.DataFrame({"Contract": [
        "Month-to-month",
        "One year",
        "Two year",
        "Month-to-month"
    ]})
encoded_df  = pd.get_dummies(contract_example, columns=["Contract"])


print("encoded_df",encoded_df)

# What happened to the original Contract column?
# replaced it with binary col

# Part 4 — Apply it to the real dataset
# create copy
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
# print(X_encoded.head())

# print(X_encoded.dtypes)

# Part 5 — Boolean vs integer
# Part 6 — Compare before vs after
print("Before:", X.shape)
print("After:", X_encoded.shape)
# Before: (7043, 19)
# After: (7043, 30)

# Ask yourself:

# Why did the number of columns increase?

# This is an important practical understanding.
# because i can see that categorical column has been divded like Contract_oneyear, partner_Yes etc 
# each value of the(categorical column) has been fragmented into a new columns with bool value