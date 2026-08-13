orders = [
    {"customer": "Asha", "product": "Laptop", "category": "Electronics", "amount": 75000},
    {"customer": "Rahul", "product": "Phone", "category": "Electronics", "amount": 45000},
    {"customer": "Asha", "product": "Headphones", "category": "Electronics", "amount": 5000},
    {"customer": "Priya", "product": "Saree", "category": "Clothing", "amount": 8000},
    {"customer": "Rahul", "product": "Shoes", "category": "Clothing", "amount": 6000},
    {"customer": "Asha", "product": "Table", "category": "Furniture", "amount": 12000},
    {"customer": "Vikram", "product": "Chair", "category": "Furniture", "amount": 7000},
    {"customer": "Priya", "product": "Laptop", "category": "Electronics", "amount": 85000},
    {"customer": "Rahul", "product": "Watch", "category": "Accessories", "amount": 10000},
    {"customer": "Vikram", "product": "Phone", "category": "Electronics", "amount": 55000},
    {"customer": "Priya", "product": "Bag", "category": "Accessories", "amount": 4000},
    {"customer": "Asha", "product": "Shoes", "category": "Clothing", "amount": 5000},
]
# Customer spending
def get_customer_spending():
    customer_spending={}
    for order in orders:
        customer_name = order["customer"]
        if customer_name in customer_spending:
            customer_spending[customer_name] += order["amount"]
        else: customer_spending[customer_name] = order["amount"]
    return customer_spending
print("get_customer_spending",get_customer_spending())

# def get_customer_spending():
#     customer_spending = {}
#     for order in orders:
#         name = order["customer"]
#         customer_spending[name] = customer_spending.get(name, 0) + order["amount"]
#     return customer_spending
# print("get_customer_spending", get_customer_spending())
# Output: {'A': 85000, 'B': 75000, 'C': 4500}

# Highest spending customer
def get_highest_spending_customer():
    customer_spending = get_customer_spending()
    highest_amt = list(customer_spending.values())[0]
    highest_name = list(customer_spending.keys())[0]
    customer_spending_arr= []
    for key, value in customer_spending.items():
        if(value >= highest_amt):
            highest_amt = value
            highest_name = key
            customer_spending_arr.append({highest_name, highest_amt})
    return customer_spending_arr
print("get_highest_spending_customer()",get_highest_spending_customer())

# Revenue by category
def get_revenue_by_category():
 revenue_category = {}
 for val in orders:
     cat_name = val["category"]  
     if cat_name in revenue_category:
         revenue_category[cat_name] += val["amount"]
     else:  revenue_category[cat_name] = val["amount"]
 return revenue_category
print("get_revenue_by_category",get_revenue_by_category())

# Highest revenue category
def highest_revenue_category():
    revenue_by_category = get_revenue_by_category()
    max_cat = None
    max_rev = 0
    for key, value in revenue_by_category.items():
        if value>max_rev :
            max_rev = value
            max_cat = key
    return max_cat
    # return max(revenue_by_category, key=revenue_by_category.get)
print("get_revenue_by_category",highest_revenue_category())


# def highest_revenue_category():
#     revenue_by_cat = get_revenue_by_category()

#     # 1. Find the maximum revenue number
#     max_rev = max([val for val in revenue_by_cat.values()])

#     # 2. Extract the category name matching that max revenue
#     return [cat for cat, val in revenue_by_cat.items() if val == max_rev][0]

# print("highest_revenue_category:", highest_revenue_category())


# Employee department salary
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
def get_department_salary_higest_paid_department():
    department_salary = {}
    for record in employee_data:
        department_name = record["department"]
        if department_name in department_salary:
            department_salary[department_name]+= record["salary"]
        else: department_salary[department_name] = record["salary"]
       
    highest_paid_amt=  max( max for max in department_salary.values())
    highest_paid_department = [key for key, value in department_salary.items() if value==highest_paid_amt ]
    return department_salary,highest_paid_department
print("get_department_salary_higest_paid_department",get_department_salary_higest_paid_department())