# Day 17 — Data Cleaning and Features

## 🎯 Why are we learning this?

## 1. Working copy

Why use a copy?
to not to destroy the original data set while processinf

## 2. TotalCharges conversion

What was the problem?
type is object, supposed to be floar or int
What changed after conversion?
dtype to float

## 3. Missing value handling

How many rows were removed?
11

Why did I choose dropna?
since the missing value rows are less i,e 11 and wont largely impact the ultimate decion

Could another approach be used?
if the rows are little more then we would have used mean or median

## 4. Removing customerID

Why remove it?
not required as it just contains who are the cusotmers

Why keep other categorical features?
those may have some useful information for churn rate calculation

## 5. Features and Target

X = column excluding churn
y = churn

## 6. Feature types

### Numerical

MonthlyCharges, tenure, totalcharges

### Binary categorical

SeniorCitizen

### Multi-category categorical

gender, Partner, Dependents, PaperlessBilling, contract, payment method etc

## 7. Encoding thinking challenge

### Contract

My reasoning:
No i wont use as its a multi lable columns and tomorrow if one more label is added the number will be just increasing and can cause a problem in interpretation

### InternetService

My reasoning:
no i want use. 1,2,3 for the same reason if its only two category like yes or no or order then we can

## 🎤 Interview angle

Why is preprocessing important before training an ML model?
Raw data will be messy so preprocessing will be helful to convert into the meaningful data by investigating the type, fixing it, handling missing value, eleminating the unnecessay columns, seperating features and target etc so that we can operate using the processed data for better results

## What confused me

may be the order as of now
segregating the numerical, categorical co

## What became clearer

checking types, missing values, seperating features and target
