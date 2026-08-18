import pandas as pd
import numpy as np

employees = pd.DataFrame({
    "name": [
        "Asha", "Rahul", "Priya", "Vikram",
        "Asha", "Neha", "Karan", "Ravi"
    ],
    "age": [
        28, np.nan, 32, 40,
        28, np.nan, 35, 29
    ],
    "salary": [
        65000, 80000, np.nan, 95000,
        65000, 72000, np.nan, 500000
    ],
    "department": [
        "IT", "IT", "HR", "Finance",
        "IT", "HR", "IT", "IT"
    ]
})
df = pd.DataFrame(employees)

# Number of missing values per column
print("employees.isna()",df.isna())

num_missing_col = df.isna().sum()
print("num_missing_col.",num_missing_col)

# Rows containing missing values
df_with_nan = df[df.isna().any(axis=1)]
print("df_with_nan.",df_with_nan)

# Duplicate rows
duplicate_rows = df[df.duplicated()]
print("duplicate_rows.",duplicate_rows)

# Number of duplicate rows
num_of_duplicate_rows = df.duplicated().sum()
print("num_of_duplicate_rows.",num_of_duplicate_rows)

# Part 3 — dropna()
# df = df.dropna(subset=["salary"])
df.dropna(subset=["salary"])

# fillna()
df["age"].fillna((df["age"]).mean())
df["salary"].fillna((df["salary"]).median())

print("na age filled with mean",df["age"].fillna((df["age"]).mean()))
print("na salary filled  with median",df["salary"].fillna((df["salary"]).median()))


# Part 5 — Mean vs median ⭐
salary = pd.Series([
    50000,
    55000,
    60000,
    65000,
    1000000
])
salary.mean()
salary.median()

# duplicate
df.drop_duplicates()



# Create the dataset
data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 104],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hank", "Ivy", "Jack", "Karen", "Leo", "Mia", "Nina", "David"],
    "Department": ["Engineering", "HR", "Sales", "Engineering", "Marketing", "HR", "Sales", "Engineering", "Marketing", "HR", "Sales", "Engineering", "Marketing", "HR", "Engineering"],
    "Age": [28, np.nan, 35, 42, 29, 31, np.nan, 45, 26, 38, 50, 33, 27, 41, 42],
    "Salary": [85000, 62000, np.nan, 95000, 58000, 64000, 71000, 98000, np.nan, 67000, 73000, 89000, 60000, 1250000, 95000]
}

# Load into a pandas DataFrame
df1 = pd.DataFrame(data)

# Display the DataFrame
# print(df1)
# Missing-value analysis
print("missing_values",df1.isna().sum())

# Duplicate analysis
print("Duplicate_values",df1.duplicated().sum())

# Decide how to handle missing values
# mean for age
# median for salary- coz of the outliers 
df1 = df1["age"].fillna(df1["age"].mean())
df1 = df1["salary"].fillna(df1["salary"].median())

# Remove duplicates if appropriate
df1 = df1.drop_duplicates()

# Age:
# → filled missing values using median
# → because...
# i filled with mean, i thought since its has 2 digit or less pointer avg would be the good choice

# Salary:
# → filled using median
# → because...
#  it can be of any numbers, outliers would be possible so filled with median, 
# Median is the middle value after the data is sorted. It is less affected by extreme values than the mean.

# Mean vs median → depends on the distribution, not the number of digits.

# Duplicates:
# → removed
# → because...
# I should remove duplicates only after confirming that they represent duplicate records rather than legitimate repeated events.

# 500000 salary:
# → investigated rather than automatically removed
# → because...i did not understand this question