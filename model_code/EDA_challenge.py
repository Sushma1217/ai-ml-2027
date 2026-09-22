import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# 🔴 Challenge 1 — Churn + Contract
# Which contract type appears to have the highest churn?
highest_churn_contract = df.groupby("Contract")["Churn"].value_counts()
print("highest_churn_contract",highest_churn_contract)

# answer is: month to month contract type highest churn follwed by one year type
highest_churn_contract.unstack().plot(kind="bar")
plt.xlabel("Churn")
plt.ylabel("Contract")
plt.title("Contract Churn Distribution")
plt.show()


# 🔴 Challenge 2 — Churn + InternetService
# Does churn appear to differ between InternetService types?
# Investigate:
# DSL
# Fiber optic
# No
internet_Service_churn_type = df.groupby("InternetService")["Churn"].value_counts()
print("internet_Service_churn_type",internet_Service_churn_type)

internet_Service_churn_type.unstack().plot(kind="bar")
plt.xlabel("Churn")
plt.ylabel("Internet Service")
plt.title("Internet Service Churn Distribution")
plt.show()

# answer:
# Based on this dataset, Fiber optic appears to have the highest proportion/number of churned customers followed by DSL.
# and  DSL have highest portion of customers who did not churn

#  🔴 Challenge 3 — Churn + Tenure

# You already discovered that churned customers have lower tenure.

# Now ask:

# Are customers with very short tenure more likely to churn?

# Create tenure groups yourself:
# 0–12 months
# 13–24 months
# 25–48 months
# 49+ months

# Then investigate churn across these groups.

# This is your first taste of feature engineering.
tenure_groupby =  df.groupby("tenure")["Churn"].value_counts()
print("tenure_groupby",tenure_groupby)
df.boxplot(column="tenure", by="Churn")
plt.xlabel("Churn")
plt.ylabel("Tenure")
# plt.title("Tenure Churn Distribution")
plt.show()

# ans: Yes as most of the cusomers who chur comes under ~10 months which is a shorter tenure 

# 🔴 Challenge 4 — Manual reasoning
# f Contract = Month-to-month appears to have the highest number of churned customers, 
# does that automatically mean month-to-month customers have the highest churn rate?
# ans: No as the rate depends on how much portion of total customers who churn have month to month contract

# Challenge 5 — My Own EDA Question

# Choose one feature from the dataset and ask:

# "Does this feature appear to be related to churn?"

# Examples:
# PaymentMethod
# PaperlessBilling
# SeniorCitizen
# Partner
# Dependents
# TechSupport
# OnlineSecurity


# Feature: TechSupport
# Analysis: yes many people opt for internet service by considering technical support.
churn_techsupport = df.groupby("TechSupport")["Churn"].value_counts()
print("churn_techsupport",churn_techsupport)

# Visualization:
# plotting bar graph 
churn_techsupport.unstack().plot(kind="bar")
plt.xlabel("Churn")
plt.ylabel("Tech Support")
plt.title("TechSupport TechSupport Distribution")
plt.show()

# Observation:
# high number of customers churn even there is no tech support 
# i identified there is a unique value 'No internet service' i guess it should be no- correct me if im wrong
# # Conclusion:
# most of customer did not churn and churn without tech support 

