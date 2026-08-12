employee_data = [
    {"ID": 101, "name": "Aarav Sharma", "department": "Engineering", "role": "Python Developer", "salary": 85000, "remote": True,"experience":5},
    {"ID": 102, "name": "Diya Patel", "department": "Data Science", "role": "Data Analyst", "salary": 78000, "remote": False,"experience":2},
    {"ID": 103, "name": "Rohan Gupta", "department": "Engineering", "role": "Backend Engineer", "salary": 92000, "remote": True,"experience":3},
    {"ID": 104, "name": "Ananya Iyer", "department": "Product", "role": "Product Manager", "salary": 125000, "remote": False,"experience":1},
    {"ID": 105, "name": "Kabir Das", "department": "Product", "role": "UI/UX Designer", "salary": 70000, "remote": True,"experience":10},
    {"ID": 106, "name": "Meera Nair", "department": "HR", "role": "HR Specialist", "salary": 60000, "remote": False,"experience":12},
    {"ID": 107, "name": "Arjun Rao", "department": "Engineering", "role": "DevOps Engineer", "salary": 95000, "remote": True,"experience":9},
    {"ID": 108, "name": "Neha Verma", "department": "Finance", "role": "Financial Analyst", "salary": 50000, "remote": False,"experience":8}
]
# Find all employees from IT
def find_IT_employees():
 it_employees=[];
 for emp in employee_data:
    if(emp["department"]=="Engineering"):
      it_employees.append(emp["name"])
 return  it_employees
print(find_IT_employees())

# 2. Find the highest-paid employee
# def highest_salary_employee():
#   max_salary = employee_data[0]["salary"]
#   emp_data={}
#   for emp in employee_data:
#     if emp["salary"]> max_salary :
#      max_salary=emp["salary"]
#      emp_data=emp
#   return emp_data
# print(highest_salary_employee())

def highest_salary_employee():
  highest_paid_emp = employee_data[0]
  for emp in employee_data:
    if emp["salary"] > highest_paid_emp["salary"]:
      highest_paid_emp = emp
  return highest_paid_emp
print(highest_salary_employee())

# Using Built-in max() with a key
# def highest_salary_employee():
#   return max(employee_data, key=lambda emp:emp["salary"]) 
# """ took help """

# 3. Find employees with experience > 5 years
def above_five_experience():
  experienced_professionals=[]
  for emp in employee_data:
    if(emp["experience"]>5):
      experienced_professionals.append(emp["name"])
  return experienced_professionals
print(above_five_experience())

# find employees with salary > 70,000
def margin_salary():
  employees=[]
  for emp in employee_data:
    if(emp["salary"]>70000):
      employees.append(emp["name"])
  return employees
print(margin_salary())

# 5. Calculate average salary
def avg_salary():
  total_salary = 0
  average=0
  num_items= len(employee_data)
  for emp in employee_data:
    total_salary += emp["salary"]
    average = round(total_salary/num_items,2)
  return average
print(avg_salary())

# Count employees in each department
def each_dept_employees():
  emp_data = {}
  for emp in employee_data:
    dept = emp["department"]
    if dept in emp_data:
      emp_data[dept]+=1
    else: emp_data[dept] = 1
  return emp_data 
print(each_dept_employees())

# Employees from IT AND having more than 5 years of experience AND salary above 80,000.
def get_emp_details():
  employees=[]
  for emp in employee_data:
   if emp["department"]=="Engineering" and emp["experience"]>5 and emp["salary"]>80000:
     employees.append(emp)
  return employees
print(get_emp_details())

# list comprehension
numbers = [10, 15, 20, 25, 30, 35, 40]
# Get numbers > 20
filtered_numbers = [x for x in numbers if x >20]
print("filtered_numbers>20",filtered_numbers)

# Get even numbers
even_numbers = [a for a in numbers if a %2==0]
print("even_numbers",even_numbers)

# Multiply every number by 2
two_mmultiplier = [val*2 for val in even_numbers ]
print("two_mmultiplier",two_mmultiplier)

# Get numbers divisible by 5
five_nultiplier = [val*5 for val in numbers]
print("five_nultiplier",five_nultiplier)

# without list comprehension
# Get numbers > 20
def filtered_numbers1():
  num_arr = []
  for num in numbers:
    if num >20:
      num_arr.append(num)
  return num_arr
print("num_arr",filtered_numbers1())

# Get even numbers
def get_even_numbers():
    even_num_arr = []
    for num in numbers:
        if(num%2==0):
            even_num_arr.append(num)
    return even_num_arr
print("get_even_numbers",get_even_numbers())

def get_two_multipliers():
 doubled_number = []
 for num in numbers:
   doubled_number.append(num*2)
 return doubled_number
print("get_two_multipliers",get_two_multipliers())

def five_numbers():
   multipliers = []
   for num in numbers:
      multipliers.append(num*5)
   return multipliers
print("five_numbers",five_numbers())

orders = [
    {"customer": "Asha", "product": "Laptop", "category": "Electronics", "amount": 75000},
    {"customer": "Rahul", "product": "Phone", "category": "Electronics", "amount": 45000},
    {"customer": "Asha", "product": "Headphones", "category": "Electronics", "amount": 5000},
    {"customer": "Priya", "product": "Saree", "category": "Clothing", "amount": 8000},
    {"customer": "Rahul", "product": "Shoes", "category": "Clothing", "amount": 6000},
    {"customer": "Asha", "product": "Table", "category": "Furniture", "amount": 12000},
    {"customer": "Vikram", "product": "Chair", "category": "Furniture", "amount": 7000},
    {"customer": "Priya", "product": "Laptop", "category": "Electronics", "amount": 65000},
    {"customer": "Rahul", "product": "Watch", "category": "Accessories", "amount": 10000},
    {"customer": "Vikram", "product": "Phone", "category": "Electronics", "amount": 55000},
    {"customer": "Priya", "product": "Bag", "category": "Accessories", "amount": 4000},
    {"customer": "Asha", "product": "Shoes", "category": "Clothing", "amount": 5000},
]

# What is the total revenue?
def total_revenue():
    return sum(record["amount"] for record in orders )
print("total revenue",total_revenue())
def for_total_revenue():
    total=0
    for record in orders:
     total += record["amount"]
    return total
print("total for_total_revenue",for_total_revenue())

# What is the average order value?
def avg_order_value():
   total = for_total_revenue()
   num_of_orders = len(orders)
   return total/num_of_orders
print("total avg_order_value",avg_order_value())

# Which order has the highest amount? Return the complete order.
def highest_order():
   highest_order_val = orders[0]
   highest_ordered_customers= []
   for record in orders:
      if record["amount"] > highest_order_val["amount"]:
         highest_order_val = record
   for record in orders:
      if(record["amount"]== highest_order_val["amount"]):
        highest_ordered_customers.append(record)
   return highest_ordered_customers
print("highest_order",highest_order())

# clean approach 
def highest_orders():
    # 1. Find the maximum amount first using sum/max or generator
  max_amount = max(record["amount"] for record in orders)
    # 2. Collect all records matching that maximum amount
  return [record for record in orders if record["amount"]==max_amount]
print("highest_orders", highest_orders())

# How much revenue came from Electronics, Appliances and Furniture
def revenue_by_category():
   electronics_revenue = sum(order["amount"] for order in orders if order["category"]=="Electronics")
   applicane_revenue = sum(order["amount"] for order in orders if order["category"]=="Appliances")
   furniture_revenue = sum(order["amount"] for order in orders if order["category"]=="Furniture")
   return electronics_revenue ,applicane_revenue, furniture_revenue
print("revenue_by_category", revenue_by_category()) 

# Which customer spent the most?
def get_highest_spent_customer():
   highest_data = highest_orders()
   print("highest_data", highest_data) 
   return [order["customer"] for order in highest_data]
print("get_higest_spent_customer", get_highest_spent_customer())

# Which product category generated the highest revenue? 
def get_highest_revenue_category():
   highest_data = highest_orders()
   print("highest_data", highest_data) 
   return [order["category"] for order in highest_data]
print("get_highest_revenue_category", get_highest_revenue_category())


