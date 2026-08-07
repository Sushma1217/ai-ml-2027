# name = input("Enter your name: ")

print(int("42"))
print(int(3.05))
print(int(1.09))
print(int(True))

""" float """
print(float(1))
print(float(1.1))
print(float(True))  #1.0

print(str(1)) #1
print(str(True)) #true

print(bool(1)) #true
print(bool(False)) #False
print(bool("Hello")) #True
print(bool(" ")) #False

print(int(float(12.5))) #12
print(str(bool(0))) #False
print(float(int(False))) #0.0


""" and, not or """
is_username_correct = True
is_password_correct= False

if(is_username_correct and is_password_correct) :
    print("Access granted")
else: print("Access denied")

isToday:str = "Monday"
if(isToday=="Sunday" or isToday=="Saturday") :
    print("discount availed")
else : print("No discount")

is_weekend = False
is_publicholiday = True

if(is_weekend or is_publicholiday):
    print("discount availed")
else : print("No discount")

is_out_of_stock= False

if not is_out_of_stock: 
    print("Item added to cart.")  # Output: Item added to cart.
else:
    print("Sorry, item unavailable.")


height = 115
age = 15
special_permission = False

if(height >=120 and age>=10) or  special_permission :
    print("Can ride")
    
else: print("You cannot ride.")


""" practical questions """

# Check if a number is positive or negative.
number = -1
if(number >0):print("its a positive number")
else : print("negative number")

# Check if a number is even or odd.
check_number = 10
if(check_number %2 ==0): print("Its a even number")
else: print("Its a odd number")

#Find the larger of two numbers.
def findLargerNumber(a,b):
 if(a>b):
    print("larger number is :",a)
 elif(a<b):
    print("larger number is :",b)
 else : print("both are equal")
findLargerNumber(16,16)
#using ternary
a=15
b=15
larger_num = a if a>b else b
print("larger_num", larger_num)

#Find the largest of three numbers.
number1=18;number2=18; number3=18

if(number1>number2 and number1>number3) :
   print("larger_num", number1)
elif(number2>number3 and number2>number1):
    print("larger_num", number2)
elif number2 >= number3:
    print("larger_num", number3)
else: print("eqal",number1,number2, number3)

largest= max(number1,number2,number3)
print("largest", largest)

# Check if a person is eligible to vote.
eligile_for_vote = 18
def voter_eligibility(age):
    if(age>=eligile_for_vote):
     print("You are eligible for vote!")
    else: print("You are not eligible for vote!")
voter_eligibility(9)

#Check if a year is a leap year.
def validate_leapyear(year): 
   if(year % 4 == 0):   print("its a leap year")
   else:  print("its a not a leap year")
validate_leapyear(1994) 

# Grade calculator:
grade:str
def generate_grade(marks):
    if(marks >=90 and marks <=100): 
     grade = "A"
     print("Your grade is :",grade)
    elif(marks >=80 and marks <=89):
       grade = "B"
       print("Your grade is :",grade)
    elif(marks >=70 and marks <=79):
        grade = "C"
        print("Your grade is :",grade)
    else :
     grade = "Fail"
     print("Your grade is :",grade)
generate_grade(82)

def calculate_BMI():
    # Convert string inputs to floats (height should be in meters, e.g., 1.75)
    height = float(input("Enter your height in meters (e.g., 1.75): "))
    weight = float(input("Enter your weight in kg (e.g., 70): "))

    bmi = weight / (height**2)
    print(f"\nYour BMI is: {bmi:.2f}")

    # Categorize the BMI based on standard health thresholds
    if bmi < 18.5:
        print("Weight Category: Underweight")
    elif 18.5 <= bmi < 25:
        print("Weight Category: Normal weight")
    elif 25 <= bmi < 30:
        print("Weight Category: Overweight")
    else:
        print("Weight Category: Obese")
calculate_BMI()


# Check whether a character is a vowel or consonant
vowels= ['a','e','i','o','u']
def check_vowels(char):
  for item in vowels:
        if item == char.lower():
            print("It's a vowel")
            return  # Stop the function as soon as a match is found
            
    # This only runs if the loop finishes without finding a vowel
print("It's a consonant")
check_vowels('b')

# def check_vowels(char):
#     # .lower() ensures uppercase letters like 'A' are also recognized
#     if char.lower() in vowels:
#         print("It's a vowel")
#     else:
#         print("It's a consonant")

# check_vowels('a')

#  Check if a number is divisible by both 5 and 11.  

def number_divisble(num):
    if(num % 5==0 and num % 11==0 ):
        print("Yes. it is divisble by both 5 and 11")
    else: print("No. it is not divisble by both 5 and 11")

number_divisble(110)

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


