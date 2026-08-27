import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# create copy
df_processed = df.copy()
print(df_processed.shape)
# print(df_processed.head())

# Fix TotalCharges
df_processed["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
print(df_processed["TotalCharges"].isna().sum())
print(df_processed["TotalCharges"].dtype)

# answer:
# How many missing values now exist? 11
# Why did they only become visible after conversion? - 
# # i guess since the type was no numeric it will consider "" as a value so numeric conversion specify that the empty values are missing values 

# Part 3 — Handle the missing values 🔴
# We have only 11 rows with missing TotalCharges.
df_processed = df_processed.dropna()
print(df_processed.shape)
print(df_processed.isna().sum())

# interview question 
# "Why did you drop these rows instead of filling them with mean or median?"
# since the number of missing rows are less so no harm to the overall dataset size.

# Remove customerID 🔴
df_processed = df_processed.drop(columns=["customerID"])
print(df_processed.columns)

# Why did we remove customerID, but keep columns like TechSupport and Contract?
# because customer ID contains the unique value of cusotmers dnt contain any relevant information to calculate the desired results
# where as TechSupport and Contract etc will have some information which might be needed for churn rate calculation

# Part 5 — Separate features and target 🔴
X = df_processed.drop(columns="Churn")
Y = df_processed["Churn"]
print(X.shape)
print(Y.shape)
print(X.head())
print(Y.head())

# Part 6 — Inspect what still needs preprocessing
# Which features are:
# Numerical?
# MonthlyCharges, tenure, totalcharges
# Binary categorical? 
# SeniorCitizen

# Multi-category categorical?
# gender, Partner, Dependents, PaperlessBilling, contract, payment method etc

# Part 7 — Important thinking challenge 🔴
# Look at:

# Contract

# Month-to-month
# One year
# Two year

# and:

# InternetService

# DSL
# Fiber optic
# No

# Answer:

# Question 1

# Would you use:

# 1
# 2
# 3

# for Contract?

# Why might that create a problem?
# No i wont use as its a multi lable columns and tomorrow if one more label is added the number will be just increasing
# and can cause a problem in interpretation

# Question 2

# Would the same approach make sense for:

# InternetService

# Why or why not?
# no i want use. 1,2,3 for the same reason if its only two category like yes or know then we can 


# This will prepare you for the next topic:

# One-Hot Encoding vs Label/Ordinal Encoding

# That distinction is absolutely worth understanding deeply for interviews and practical projects.