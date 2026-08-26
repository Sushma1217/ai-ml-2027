import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Part 1 — One final EDA calculation
# For Contract, calculate:
# Number of customers

types_Contract = (df["Contract"].value_counts())
churn_customer=(df.loc[df["Churn"]=="Yes","Contract"].value_counts())
churn_rate = (churn_customer.div(types_Contract, fill_value=0) * 100).round(2)
# copied this syntax form google
print("churn_rate",churn_rate)


# Part 2 — Interpret it

# Answer:

# Which contract type has the highest churn rate?
# ans-Month-to-month

# Then answer:

# Is this the same as the contract type with the highest number of churned customers?
# yes

# This is the final EDA lesson I want from you.


# Part 3 — Identify preprocessing problems
# Now inspect:
# df.dtypes
print("df.dtypes",df.dtypes)
# Look at the dataset and identify:

# Numerical columns
# Categorical columns
# Columns that shouldn't be used as features
# Columns containing missing/invalid values

# Write them down.

# Numerical columns - MonthlyCharges,Total charges(now its showing as str), tenure
# Categorical columns- Churn, PaymentMethod,PaperlessBilling, Contract, StreamingMovies, TechSupport,DeviceProtection
# PhoneService,MultipleLines,OnlineBackup,OnlineSecurity etc
# Columns that shouldn't be used as features - PaperlessBilling, StreamingMovies, TechSupport,DeviceProtection
# PhoneService,MultipleLines,OnlineBackup,OnlineSecurity, SeniorCitizen,Dependents,Partner

missing_values = df.isna().sum()
print("missing_values",missing_values)
total_charges = pd.to_numeric(df["TotalCharges"], errors="coerce")
print("missing_values",total_charges.isna().sum())

# Columns containing missing/invalid values- 11 in total charges

# Part 4 — Understand encoding

# This is our first actual preprocessing concept.

# Suppose:

# Contract

# Month-to-month
# One year
# Two year

# A model can't directly understand those strings.

# We need to convert them into numbers.

# Conceptually:

# Month-to-month → ?
# One year       → ?
# Two year       → ?

# This is called:

# Categorical Encoding

# Why can't most ML algorithms directly work with "Month-to-month", "One year", etc.?
# ans- ml algorithm requires only numerical data to perform the operation and may be string data can lead to confusion

# Part 5 — Understand scaling

# Suppose we have:

# age        → 20–80
# salary     → 20,000–200,000
# experience → 0–30

# One feature has values in tens.

# Another has values in hundreds of thousands.

# Some ML algorithms can be affected by these different scales.

# This is why we have techniques such as:

# Standardization
# Normalization
# Don't learn the formulas yet.

# Your task:

# In your own words, why might feature scaling be necessary?
# so we can treat outliers, normalize the value to get better results

# Part 6 — The most important question ⭐

# Imagine our dataset has:

# MonthlyCharges
# TotalCharges
# Contract
# InternetService
# Churn

# We're predicting:

# Churn

# Which columns need and classify them

#  MonthlyCharges - Scaling because amount can vary and have extreme values
# TotalCharges- Scaling because amount can vary and have extreme values
# Contract- endcoding as its a categorical cols
# InternetService - endcoding as its a categorical cols
# phoneservice - endcoding as its a categorical cols
# Churn - target
# tenure- scaling 

