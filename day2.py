 # for loop exercises

# Positive / negative / zero
def type_of_number(num:int):
  if(num>0): print("its a positive number")
  elif(num==0):print("its a positive number")
  else: print("its a negative number")
type_of_number(0)

# Even / odd
def validate_number(num):
  if(num %2==0): print("its a even number")
  else : print("its a odd number")
validate_number(10)

# Largest of 3
def largest_number(num1,num2,num3):
  if(num1>num2 and num1>num3):
    print("largest number is",num1)
  elif(num2>num1 and num2>num3):
    print("largest number is",num2)
  elif(num3>num1 and num3>num2):
    print("largest number is",num3)
  else: print("all are equal")
largest_number(15,15,16)

# leap year
def check_leap_year(year):
  if(year % 4==0 and year %100 !=0) or (year %400==0):
    print(f"{year} is a leap year")
  else:
    print(f"{year} is not a leap year")
check_leap_year(2024)
check_leap_year(1900)
check_leap_year(2000)

# Student Result System
student_name = input("Enter your name ")
student_roll_number = input("Enter your roll number ")
marks = []
for mark in range(5):
    val = float(input(f"Enter your marks {mark+1}: "))
    marks.append(val)
print(marks)

total_marks = 500
def calculate_results(): 
    total = 0 
    has_failed_subject = False
    for mark in marks:
     total += mark
    percentage = (total/total_marks)*100
    if mark < 35:
            has_failed_subject = True
    # If any single subject is below 35, the student fails overall
    if has_failed_subject:
        print("Result: Failed (scored below 35 in one or more subjects)")
    elif percentage >= 85:
        print("Your grade is 'A'")
    elif percentage >= 60:
        print("Your grade is 'B'")
    elif percentage >= 35:
        print("Your grade is 'C'")

    print("Your name is : ",student_name)
    print("Your roll number is : ",student_roll_number)
    print("Your percentage is : ",percentage)
    print("Your Total marks is : ",total_marks)

calculate_results()

# login validation
user_name = input("enter your username")
password = input("enter your password")
if(user_name and password): print("you are logged in")
else: print("user name and password are mandatory")

# Print numbers 1–20
for number in range(1,21):
    print("numbers are",number)

# Print even numbers 1–50
for number in range(1,51):
    if(number % 2 ==0):
     print(number)

# for num in range(2, 51, 2):
#     print(num)

# Sum numbers 1–100
total=0;
for num in range(1,101):
   total += num
print(total)

# Multiplication table
table_number = int(input("enter the number for table"))
def return_table(num):
#    tables from 1 to 10
   for i in range(1,11):
      result = num*i
      print(f"{num} x {i} = {result}")
return_table(10)



# Count vowels in a string
def count_vowels(word):
   vowels = ['a','e','i','o','u']
   count=0
   for char in word:
        if char.lower() in vowels:
            count += 1
   print(count)
count_vowels("sushma") 

# Find the largest number in a list
numbers_list = [1, 10, 80, 190, 100]
def find_max():
    max_num = numbers_list[0]
    for num in numbers_list:
      if num > max_num:
          max_num = num
    print(max_num)
    return max_num
find_max()

# Count positive and negative numbers
num_array = [1,-2,45,-15,-60]
def count_numbers():
   negavtive_numbers = 0
   positive_numbers = 0
   for num in num_array:
      if(num > 0):
         positive_numbers += 1
      else: negavtive_numbers +=1
   print("positive_numbers negavtive_numbers",positive_numbers, negavtive_numbers)
count_numbers()

# while loop
# keep asking for passworduntil correct
# Password checker
# Keep asking the user for a password until they enter the correct password.
# Then add:
# Maximum 3 attempts.
password ="sushma" 
max_efforts = 3

def password_checker():
    attempts = 0
    while attempts < max_efforts:
      entered_pwd = input("Enter your password: ")
      attempts += 1
      if entered_pwd == password:
      #  entered_pwd= input("Enter the correct password")
        print("access granted")
        break
      else:
         remaining = max_efforts-attempts
         if(remaining>0):
          print(f"Incorrect. {remaining} attempt(s) left.\n")
         else:   print("access denied")
      
password_checker()

# break
# Print numbers 1–20, but stop when you reach 13.
i = 1
while i<20:
  print("numbers are", i)
  i+=1
  if i ==13:
    break



# continue
# Print numbers 1–20, but skip multiples of 3
value=0
while value<20:
  value+=1;
  if value % 3==0:
    continue
  print("values are",value)

# Mini Project
# Student Result System

student_name = input("Enter your name ")
student_roll_number = input("Enter your roll number ")
marks = []
for mark in range(5):
    val = float(input(f"Enter your marks {mark+1}: "))
    marks.append(val)
print(marks)
total_marks = 500
def calculate_results(): 
    total = 0 
    has_failed_subject = False
    for mark in marks:
     total += mark
     percentage = (total/total_marks)*100
     if mark < 35:
            has_failed_subject = True
    # If any single subject is below 35, the student fails overall
     if has_failed_subject:
        print("Result: Failed (scored below 35 in one or more subjects)")
     elif percentage >= 85:
        print("Your grade is 'A'")
     elif percentage >= 60:
        print("Your grade is 'B'")
     elif percentage >= 35:
        print("Your grade is 'C'")

    print("Your name is : ",student_name)
    print("Your roll number is : ",student_roll_number)
    print("Your percentage is : ",percentage)
    print("Your Total marks is : ",total_marks)

calculate_results()

# find_largest(numbers) that accepts a list:
def find_largest(numbers):
    max_num = numbers[0]
    for num in numbers :
        if(num>max_num):
            max_num = num
    print("Max num is", max_num)
find_largest([12, 45, 7, 89, 23])