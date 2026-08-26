# Day 16 — ML Preprocessing Introduction

## 🎯 Why are we learning preprocessing?

## Final EDA — Count vs Rate

count is the simply number of values
rate- shows how much percentage ditributed among the different types

### Contract customer count

count
Month-to-month 1655
One year 166
Two year 48

.div - syntax coplied from google
all other things like usage of gruoup by, vlaue counts i wrote on my own

### Contract churn rate

Month-to-month 42.71
One year 11.27
Two year 2.83

### My observation

## Dataset preprocessing problems

### Numerical columns

MonthlyCharges,Total charges(now its showing as str), tenure

### Categorical columns

Churn, PaymentMethod,PaperlessBilling, Contract, StreamingMovies, TechSupport,DeviceProtection,
PhoneService,MultipleLines,OnlineBackup,OnlineSecurity etc

### Columns to exclude

PaperlessBilling, StreamingMovies, TechSupport,DeviceProtection
PhoneService,MultipleLines,OnlineBackup,OnlineSecurity, SeniorCitizen,Dependents,Partner

### Missing/invalid data

total charges - type is obj or str
missing - 11

## Categorical Encoding

### What is it?

a process of converting categorical data into numerical data so machine can understand process it

### Why do we need it?

because ml algo rely on maths ops

## Feature Scaling

### What is it?

adjust the numerical values to share a common scale

### Why do we need it?

to the larger numbers wont dominant, extreme values can be handled nicely

## Feature classification

| Column | Type | Encoding? | Scaling? | Why? |
| ------ | ---- | --------- | -------- | ---- |

<!-- MonthlyCharges - Scaling because amount can vary and have extreme values
# TotalCharges- Scaling because amount can vary and have extreme values
# Contract- endcoding as its a categorical cols
# InternetService - endcoding as its a categorical cols
# phoneservice - endcoding as its a categorical cols
# Churn - target
# tenure- scaling  -->

## Interview Questions

### Q1

What is feature preprocessing?
cleaning, encoding and normalizing the raw data for ml model to process

### Q2

Why do we encode categorical variables?
a standard format or type will be maintained which helps in better results for maths ops as string may lead to confusion , dta fragmentation

### Q3

Why do we scale numerical features?
so that large numders wont dominat, handle extreme valules

### Q4

Do all ML algorithms require feature scaling?
no

### Q5

Should the target variable be included among input features?
no

## What confused me

concepts

## What became easier

understanding why we need it based on your explanation etc encoding scaling etc
