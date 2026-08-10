# dictionary
# updating
# Direct Assignment (Single Key)
user = {"name":"sush","age":26, "mail":"gmail"}
user["mail"] = ".com"

# Using the update() Method (Multiple Keys)
user.update({"age":25, "mail":"123@gmail.com"})

# Using the Merge and Update Operators 
user |= {"age":26, "mail":"124@gmail.com"}

# adding
user["occupation"] = "salaried"
print(user)

dict_a = {"a":12, "b":"xx"}
dict_b = {"d": 2, "c": 3}
dict_a.update(dict_b)
print("dict_a",dict_a)

# deleting
# Remove by Key Name
user_data = {"name": "Alice", "age": 25, "city": "Seattle"}
del user_data["age"]

# pop
user_data.pop("name")
#  Remove by Value Content
scores = {"math": 90, "science": 65, "history": 90}
for key, val in list(scores.items()):
    if(val == 90):
        del scores[key]
print("scores",scores)

# .get() Method (Safe Access)
user_list = {"name": "Alice", "age": 30,"area":"bangalore"}
print(user_list.get("name"))


# Retrieve All Values at Once - .values()
user_list = {"name": "Alice", "age": 30,"area":"bangalore"}
user_list.values()

# iterates
for val in user_list.values():
    print("val",val)
# set intersection python


# Employee Data Analyzer
employees = [
    {
        "name": "A",
        "department": "IT",
        "salary": 70000
    },
    {
        "name": "B",
        "department": "HR",
        "salary": 60000
    },
    {
        "name": "C",
        "department": "IT",
        "salary": 80000
    }
]
# Your program should:

# Display all employees.
# Find the employee with the highest salary.
# Calculate average salary.
# Find employees belonging to IT.
# Find unique departments.
# Count employees in each department.

def display_all_employees():
    emp_names=[]
    for emp in employees:
     emp_names.append(emp["name"]);
    return emp_names
print(display_all_employees())

def find_highest_salary():
   higest_salary = employees[0].get("salary")
   for record in employees:
        if record["salary"]> higest_salary:
           higest_salary = record["salary"]
   return higest_salary
print(find_highest_salary())

def calculate_average_salary():
   num_of_items = len(employees)
   total = 0
   for record in employees:
      total += record["salary"]
      avg_salary = (total/num_of_items)
      return round(avg_salary,2)
print(calculate_average_salary())

# Find employees belonging to IT.
def get_employees_by_department():
   for record in employees:
      if(record["department"]=="IT"):
         return record["name"]
print(get_employees_by_department())

def get_unique_departments():
    departments=[]
    for record in employees:
        departments.append(record["department"])
    return set(departments)
print (get_unique_departments())

# This iterates through each dictionary in employees, extracts "department", and automatically handles duplicates.
# def get_unique_departments():
#    return { employees["department"] for record in employees}

# Count employees in each department.
def count_employees_department():
    employee_count = {}
    for record in employees:
       dept = record["department"]
       if(dept in employee_count):
          employee_count[dept]+=1
       else:
          employee_count[dept] =1
    return employee_count
print(count_employees_department())
