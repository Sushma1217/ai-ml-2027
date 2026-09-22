import pandas as pd
import numpy as np

employees = pd.DataFrame({
     "name": ["Asha", "Rahul", "Priya", "Vikram"],
    "age": [25, 32, 29, 35],
    "experience": [2, 7, 5, 10],
    "salary": [50000, 80000, 65000, 95000],
    "department": ["IT", "HR", "IT", "Finance"]
})
print("employees",employees)

print("emplyee.shape",employees.shape)
print("emplyee.column",employees.columns)
print("emplyee.dtypes",employees.dtypes)
print("emplyee.info()",employees.info())
print(employees.describe())

# selecting the col
print("salary row", employees["salary"])

# two cols
print("two col selection",employees[["salary","age"]])

# Employees with salary > 70,000
employees_above_70ksalary = employees[employees["salary"]>70000]
print("employees_above_70ksalary",employees_above_70ksalary)

# IT employees
it_employees =  employees[employees["department"] == "IT"]
print("it_employees",it_employees)

# IT employees with salary > 60,000
it_60k_salary =  employees[(employees["department"]== "IT") & (employees["salary"]> 60000)]
print("it_60k_salary",it_60k_salary)

# Sorting
# Employees sorted by salary from highest to lowest.
employees = employees.sort_values(by="salary")
print("employees after sorting",employees)

# desc
# employees = employees.sort_values(by="salary",ascending=False)
# print("employees after sorting",employees)

# Part 7 — Your first real data-analysis task ⭐
employees1 = {
    "name": [
        "Aarav Sharma",
        "Priya Patel",
        "Rohan Kumar",
        "Ananya Singh",
        "Vikram Rao",
        "Neha Gupta",
        "Amit Verma",
        "Pooja Iyer",
        "Rahul Nair",
        "Sneha Joshi",
        "Karan Malhotra",
        "Divya Menon",
        "Manish Reddy",
        "Ankita Das",
        "Siddharth Roy",
    ],
    "age":[28, 34, 45, 23, 40, 31, 52, 26, 33, 25, 38, 29, 47, 22, 36],
    "experience":[4, 9, 18, 1, 15, 6, 25, 3, 8, 2, 12, 5, 20, 0, 10],
    "salary": [
        65000,
        95000,
        140000,
        50000,
        125000,
        72000,
        160000,
        58000,
        88000,
        54000,
        115000,
        78000,
        145000,
        45000,
        110000,
    ],
    "department": [
        "IT",
        "HR",
        "Finance",
        "IT",
        "Engineering",
        "Marketing",
        "Finance",
        "HR",
        "IT",
        "Marketing",
        "Engineering",
        "IT",
        "Finance",
        "HR",
        "Engineering",
    ],
}
df = pd.DataFrame(employees1)

# Average salary
avg_salary  = np.mean(df["salary"])
avg_salary_pd  = df["salary"].mean()
print("avg_salary",avg_salary)
print("avg_salary_pd",avg_salary_pd)

# Highest salary
highest_salary = df["salary"].max()
print("highest_salary",highest_salary)

# lowest salary
lowest_salary = df["salary"].min()
print("highest_salary",lowest_salary)

# Employees with >5 years experience
above_5experience = df[df["experience"]>5]
print("above_5experience",above_5experience)

# Employees earning >₹70,000
above_70salary = df[df["salary"]>70000]
print("above_70salary",above_70salary)

# Employees from IT
IT_employees = df[df["department"] == "IT"]
print("IT_employees",IT_employees)

# IT employees earning >₹70,000
IT_employees_above_70salary = df[(df["department"]=="IT") & (df["salary"]>70000)]
print("IT_employees_above_70salary",IT_employees_above_70salary)

# Top 5 highest-paid employees
top5_paid_employees_data = df.sort_values(by="salary",ascending=False)
top5_paid_employees = top5_paid_employees_data.iloc[0:6,:]
print("top5_paid_employees",top5_paid_employees)

# Average salary of IT employees
avg_it_salary = IT_employees["salary"].mean()
print("avg_it_salary",avg_it_salary)

# Number of employees in each department
employee_count_departmentwise = df.groupby("department").size()
print("employee_count_departmentwise",employee_count_departmentwise)