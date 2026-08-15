import numpy as np
employees1 = np.array([
    [25, 2, 50000],
    [32, 6, 70000],
    [26, 8, 66000],
    [30, 3, 109000],
    [29, 4, 55000],
    [24, 1, 44000],
    [21, 7, 38000],
    [24, 5, 24000],
    [27, 9, 16000],
    [28, 2, 89000]
])
# Age | Experience | Salary
# Task A

# Find: # Use axis
# average age
avg_age= np.mean(employees1, axis=0)[0]
print("avg_Age",avg_age)

# average experience
avg_exp= np.mean(employees1, axis=0)[1]
print("avg_exp",avg_exp)

# average salary
avg_salary= np.mean(employees1, axis=0)[2]
print("avg_exp",avg_salary)

# task b
# Find employees whose: salary > 70000 Use Boolean masking.
employees_above_70k_salary = employees1[employees1[:,2]>70000]
print("employees_above_70k_salary",employees_above_70k_salary)

# Task C
# Find employees whose experience > 5
emp_above_5_exp =  employees1[employees1[:,1]>5]
print("emp_above_5_exp",emp_above_5_exp)

# Task D ⭐
# Find employees who satisfy both salary > 70000 AND experience > 5
emp_70k_with_5exp = employees1[(employees1[:,2]>70000) & (employees1[:,1]>5)]
print("emp_70k_with_5exp",emp_70k_with_5exp)


# Mini ML-style problem ⭐⭐⭐
# Creating the 10 employee data records
# Age | Experience | Salary | Performance
employees = np.array([
    [50,  7,  89000,  52],
    [36,  7,  76000,  86],
    [29,  2,  53000, 100],
    [42, 20, 153000,  56],
    [40,  1,  58000,  70],
    [44, 11,  92000,  58],
    [32,  5,  60000,  88],
    [32,  1,  59000,  67],
    [45, 20, 138000,  53],
    [57, 32, 196000,  74]
])

# What is the average salary?
employees_avg_salary = np.mean(employees, axis=0)[2]
print("employees_avg_salary",employees_avg_salary)

# employees_avg_salary = np.mean(employees[:,2])

# What is the average performance?
employees_avg_performance = np.mean(employees, axis=0)[3]
print("employees_avg_performance",employees_avg_performance)



# Which employees have performance >= 80?
employees_above80_performance = employees[employees[:,3]>80]
print("employees_above80_performance",employees_above80_performance)
# or
employees_above80_performance_with_where =  np.where(employees[:,3]>80)[0]
print("employees_above80_performance_with_where",employees_above80_performance_with_where)

# experience >= 5 AND performance >= 80
# employee_with_5exp_80perform = employees[(employees[:,1]>=5) & (employees[:,3]>=80)]
# print("employee_with_5exp_80perform",employee_with_5exp_80perform)
# using where
employee_with_5exp_80perform = np.where((employees[:,1]>=5) & (employees[:,3]>=80))[0]
print("employee_with_5exp_80perform",employee_with_5exp_80perform)

# Which employees have salary > average salary?
employee_above_avg_salary = np.where(employees[:,2]>employees_avg_salary)[0]
print("employee_above_avg_salary",employee_above_avg_salary)
# with normal
# employee_above_avg_salary = employees[(employees[:,2]>employees_avg_salary)]
# print("employee_above_avg_salary",employee_above_avg_salary)

# Find the employee with the highest performance.
highest_performance =  np.max(employees[:,3])
print("highest_performance",highest_performance)

# Find the employee with the highest performance among employees with experience >= 5
employees_5exp_and_above = employees[employees[:,1]>=5]
# employees_max_perform_5exp_and_above = np.where(np.max(employees_5exp_and_above[:,3]))[0]
employee = np.max(employees_5exp_and_above[:,3])
employees_max_perform_5exp_and_above = employees[employees[:,3] == employee]
print("employees_max_perform_5exp_and_above",employees_max_perform_5exp_and_above)



