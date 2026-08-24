import pandas as pd

df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
print(df.head())
# print("shape",df.shape)
# print("tail",df.tail())
# print("colums",df.columns)
# print("info",df.info())
# print("describe",df.describe())

# understand the columns

print(df.dtypes)

# Now classify the columns yourself into:

# Numerical

# Columns containing quantities/numbers.

# Categorical

# Columns representing categories/labels.

# Target
# The variable we're eventually going to predict.
# chrun

# Missing-value investigation ⭐
print("missing na",df.isna().sum())
print("missing null",df.isnull().sum())
print("info",df.info())

# Explore categorical columns
print("unique values of gender",df["gender"].value_counts())
print("unique values of contract",df["Contract"].value_counts())
print("unique values of PaymentMethod",df["PaymentMethod"].value_counts())
print("unique values of InternetService",df["InternetService"].value_counts())
print("unique values of Churn",df["Churn"].value_counts())

# 5. Explore numerical columns
print("tenure describe",df["tenure"].describe())
print("MonthlyCharges describe",df["MonthlyCharges"].describe())
print("TotalCharges describe",df["TotalCharges"].describe())

# Answer:

# What is the minimum tenure?
# ans: 0
# Maximum tenure?
# ans: 72.
# Mean tenure?- 32.3
# Median tenure?
# Mean MonthlyCharges? 64.761
# Median MonthlyCharges?  70.35

# Why isn't TotalCharges behaving like a normal numerical column?
# cos its type is string
print("total charges type",df["TotalCharges"].dtype)


# Do customers who churn have higher monthly charges?
churn_monthly_charges_mean =  df.groupby("Churn")["MonthlyCharges"].mean()
churn_monthly_charges_median =  df.groupby("Churn")["MonthlyCharges"].median()
print("churn_monthly_charges_mean",churn_monthly_charges_mean)
print("churn_monthly_charges_median",churn_monthly_charges_median)

# ans- Yes

# In this dataset, customers who churned had a 74.4 average monthly charge compared with customers who did not churn."

# 8. Second business question
# Do customers with longer tenure churn less?
churn_tenure_mean = df.groupby("Churn")["tenure"].mean()
churn_tenure_median = df.groupby("Churn")["tenure"].median()
print("churn_tenure_mean",churn_tenure_mean)
print("churn_tenure_median",churn_tenure_median)

# my observation
# Do customers with longer tenure churn less - No as the mean of tenure is 37.56 and median is  38.0 which confirms that
# customer with longer tenure dnt churn

# 9. 🔴 MANUAL challenge
# Find the average MonthlyCharges for: 
# Churn = Yes
def avg_monthly_charges_churn_yes():
    total =0
    total_records = df.loc[df["Churn"]=="Yes","MonthlyCharges"]
    num_of_records = len(total_records)
    for record in total_records:
        total+= record
        avg = total/num_of_records
    return avg
print("avg_monthly_charges_churn_yes",avg_monthly_charges_churn_yes())

# Churn = no
def avg_monthly_charges_churn_no():
    total =0
    total_records = df.loc[df["Churn"]=="No", "MonthlyCharges"]
    num_of_records = len(total_records)
    for record in total_records:
        total+= record
        avg= total/num_of_records
    return avg
print("avg_monthly_charges_churn_no",avg_monthly_charges_churn_no())

# def avg_monthly_charges_churn_yes():
#     # 1. Filter the 'MonthlyCharges' column where Churn == "Yes"
#     churn_charges = df.loc[df["Churn"] == "Yes", "MonthlyCharges"]
    
#     # 2. Get manual sum and manual count
#     total_sum = sum(churn_charges)
#     count = len(churn_charges)
    
#     # Avoid division by zero if no records match
#     if count == 0:
#         return 0.0
        
#     return total_sum / count

# print("avg_monthly_charges_churn_yes:", avg_monthly_charges_churn_yes())


# 10. ⭐ Your first EDA conclusions
# At the end, write 3–5 observations about the dataset.
# null values are 11 which is obtained after total charges covnersion
# no changes of label for categorical columns
# numerical - tenure and monthly charges 
# type of total charges is object which should be int or float
# avg monlthy charges of customers who churn(yes) is 74% which is morethan the customer who did not churn
# half of the customer monthly charges who churn yes is above  79.650 % 
# half of the customer monthly charges who churn no is above  64.4 % 
# avg tenure of churn customer is   17% which is lower than  37% who did not churn 
# half of the customer did not churn  38.0% above as compared to 10% who churned




# total charges tasks
print((df["TotalCharges"] == " ").sum())
print("blank string of total charges",(df["TotalCharges"]==" ").sum()) #11

# 3. Now compare that with:
print("compare with isna",(df["TotalCharges"].isna()).sum()) #0

# Now test what you learned on Day 11
# converting total charges into numeric

total_charges_numeric = pd.to_numeric(df["TotalCharges"],errors="coerce")

print("total_charges_numeric",total_charges_numeric.isna().sum())