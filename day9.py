import pandas as pd

employees = pd.DataFrame({
    "name": [
        "Aarav", "Priya", "Rohan", "Ananya", "Vikram",
        "Neha", "Amit", "Pooja", "Rahul", "Sneha",
        "Karan", "Divya"
    ],
    "age": [28, 34, 45, 23, 40, 31, 52, 26, 33, 25, 38, 29],
    "experience": [4, 9, 18, 1, 15, 6, 25, 3, 8, 2, 12, 5],
    "salary": [
        65000, 95000, 140000, 50000, 125000, 72000,
        160000, 58000, 88000, 54000, 115000, 78000
    ],
    "department": [
        "IT", "HR", "Finance", "IT", "Engineering", "Marketing",
        "Finance", "HR", "IT", "Marketing", "Engineering", "IT"
    ]
})
df = pd.DataFrame(employees)

print("df.iloc[2]",df.iloc[2])
print("df.loc[2]",df.loc[2])

print("employees.iloc[0]",df.iloc[0])
print("employees.iloc[0:3]",df.iloc[0:3])
print("employees.iloc[:,0:3]",df.iloc[:,0:3])

print("employees.loc[0]",df.loc[0])
print(df.iloc[0:3])


df.index = [
    "E101", "E102", "E103", "E104",
    "E105", "E106", "E107", "E108",
    "E109", "E110", "E111", "E112"
]
print("employees loc[E103]", df.loc["E103"])
print("employees.iloc[2]", df.iloc[2])

# Part 4 — Aggregation
# average salary
avg_salary = df["salary"].mean()
print("avg_salary", avg_salary)

# median salary
median_salary = df["salary"].median()
print("median_salary", median_salary)

# minimum salary
minimum_salary = df["salary"].min()
print("minimum_salary", minimum_salary)

# maximum salary
max_salary = df["salary"].max()
print("max_salary", max_salary)

# standard deviation
std_deviation = df["salary"].std()
print("std_deviation", std_deviation)

# Part 5 — GroupBy ⭐⭐⭐
mean_grpby= df.groupby("department")["salary"].mean()
print("mean_grpby", mean_grpby)

max_grpby= df.groupby("department")["salary"].max()
print("max_grpby", max_grpby)

count_grpby= df.groupby("department")["salary"].count()
print("count_grpby", count_grpby)

# Multiple aggregations ⭐
multi_agg = df.groupby("department")["salary"].agg(["mean", "min", "max", "count"])
print("multi_agg", multi_agg)

# Part 7 — Sorting grouped results
# Departments ranked by average salary, highest first.
dept_avg_salary_highest = df.groupby("department")["salary"].mean().sort_values(ascending=False)
print("dept_avg_salary_highest", dept_avg_salary_highest)

# ⭐ Day 9 mini challenge
# Using the employee dataset, answer:

# Which department has the highest average salary?
# ans- Engineering

# Which department has the highest-paid individual employee?
# Engineering- using max grpby

# Which department has the most employees?
# it - using grpby.count

# What is the average salary of employees with more than 5 years experience?
above_5exp_avg_salary = df[df["experience"]>5]["salary"].mean()
print("above_5exp_avg_salary",above_5exp_avg_salary)

# What is the average salary of employees younger than 30?
avg_salary_lessthan_30age = df[df["age"]<30]["salary"].mean()
print("avg_salary_lessthan_30age",avg_salary_lessthan_30age)

# Which department has average salary > ₹80,000
dept_avg_salary = df.groupby("department")["salary"].mean()
department_above80k_avg_salary = dept_avg_salary[dept_avg_salary > 80000]
print("department_above80k_avg_salary",department_above80k_avg_salary)
