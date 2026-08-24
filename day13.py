# Your manual thinking exercise
# Scenario 1
# A bank wants to predict whether a customer will default on a loan.
# Target: loan defaulter
# Possible features: loan amount, no of unpaid emi, remaining tenure, principal remaining

# Scenario 2
# A company wants to predict an employee's salary.
# Target = salary
# Features = experience, role(technical ot non technical), grade, skills

# Scenario 3
# Netflix wants to predict whether a user will watch a movie.
# Target = watch 
# Features = cast, genere, age, previous history, language

# Scenario 4
# A hospital wants to predict whether a patient will be readmitted.
# Target = readmission
# Features = age, disease level, clinical follow up 

# Write:
# Create one ML problem yourself.
# Problem:check whether employee is eligible for promotion 
# Target: promotion 
# Possible features: expericence, performance level, role, OTC contribution, skills


# Part 4 — Identify feature types of telco dataset

# Take your 8 features and classify each:
# Monthlycharges- numeric
# tenure - numeric 
# gender- categorical
# seniorcitizen- binary
# Partner-categorical
# Dependents- categorical
# PaperlessBilling- categorical
# StreamingTV- categorical
# StreamingMovies- categorical

# Part 5 — One very important question ⭐
# Look at: customerID
# Ask yourself:
# Should customerID be used as an ML feature?
# no, i guess this is the unique id to represent the customers and useful to interpret the results like which user churn, 
# did not churn, who are senior citizen etc plays a label role