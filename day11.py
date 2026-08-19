import pandas as pd
import numpy as np

employees = pd.DataFrame({
    "name": ["Asha", "Rahul", "Priya", "Vikram", "Neha", "Karan"],
    "age": ["28", "32", "35", "40", "29", "31"],
    "salary": ["65000", "80000", "75000", "95000", "72000", "85000"],
    "department": [
        "IT",
        "it",
        "Information Technology",
        "HR",
        "hr",
        "Finance"
    ]
})
df = pd.DataFrame(employees)
print("df.dtypes",df.dtypes)

# Part 2 — Convert data types
df["age"]= df["age"].astype(int)
df["salary"] = df["salary"].astype(float)
print("df.dtypes afert conversion",df.dtypes)

# Part 3 — What happens when conversion fails?
# df.loc[2,"age"] = "unknown"
# df["age"].astype(int)



df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["age"] = df["age"].astype("Int64")
# im getting the same error thats why added comment  and changed to Int64
# Invalid value 'unknown' for dtype 'int64'

# Part 4 — Standardizing categories
df["department"].unique()
print("df department unique",df["department"].unique())

df["department"].value_counts()
print("df department value counts",df["department"].value_counts())

df = df.replace(["it", "Information Technology"],"IT")
df = df.replace("hr","HR")

# Part 5 — String cleaning
print("upper",df["department"].str.upper())
print("lower",df["department"].str.lower())
print("strip",df["department"].str.strip())

# ⭐ Part 6 — Main challenge
# Create your own dataset with at least 15 employees.
# Include deliberately:
# ages stored as strings
# salaries stored as strings
# "unknown" in one numeric column
# "IT", "it", "It" and "Information Technology"
# "HR", "hr"
# at least one department with leading/trailing spaces

# Then create a cleaning pipeline:

# Raw data
#    ↓
# Inspect dtypes
#    ↓
# Fix numeric columns
#    ↓
# Handle invalid numeric values
#    ↓
# Inspect categories
#    ↓
# Standardize categories
#    ↓
# Check final data
df1 = pd.DataFrame({
    "name": ["Asha", "Rahul", "Priya", "Vikram", "Neha", "Karan", "Siddharth", "Meera"],
    
    # Ages as strings + "unknown"
    "age": ["28", "32", "unknown", "40", "29", "31", "45", "26"],
    
    # Salaries as strings
    "salary": ["65000", "80000", "75000", "95000", "72000", "85000", "120000", "58000"],
    
    # Mixed casing, full names, and leading/trailing spaces
    "department": [
        "IT", 
        "it", 
        "It", 
        "Information Technology", 
        "HR", 
        " hr ",         # spaces
        "Finance ",     # spaces
        "IT "           # spaces
    ]
})

# Inspect dtypes
print("data types",df1.dtypes)

# Fix numeric columns and # Handle invalid numeric values
df1["age"] = pd.to_numeric(df1["age"], errors="coerce").astype("Int64")
df1["salary"] = df1["salary"].astype(float)
print("data types after conversion",df1.dtypes)

# Inspect categories
print("unique",df1["department"].unique())
print("value counts",df1["department"].value_counts())

# Standardize categories
df1["department"] = df1["department"].str.strip()
df1["department"] = df1["department"].replace(["it","It","Information Technology"],"IT")
df1["department"]= df1["department"].replace("hr","HR")
df1["department"]= df1["department"].str.upper()
print("value counts after standardizing category",df1["department"].value_counts())

# final data -age is showing NA in unknown place hence filling with mean
df1["age"] = df1["age"].fillna(df1["age"].mean())
# Check final data
print("fianl data",df1)