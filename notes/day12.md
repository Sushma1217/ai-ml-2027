# Day 12 — Exploratory Data Analysis

## Dataset

- Name:
  WA*Fn-UseC*-Telco-Customer-Churn.csv
- Rows:7043
- Columns:21

## Understanding the dataset

### shape - number of rows and cols

### columns- col names

### dtypes- tyes of the column

### info- col names, non null count,

### describe- statistics info like count, mean, median, percentilse

## Numerical columns

50th percentile is mathematically identical to the median

## Categorical columns

all columns other than tenure, monthly charges, total charges

A column's data type and its meaning are not always the same thing.

find the unique values

Contract:
→ Most customers are on Month-to-month contract.
most customers are on Electronic check than credit catd
most customers are using Fiber optic InternetService and few people dnt have at all

Churn:
→ More customers no than yes.

## Target variable

struggled to find. i did not understand how to find a target variable

## Missing values

total charges -11

## TotalCharges investigation-

object type
I initially thought the dataset had no missing values because isna() returned 0. But TotalCharges was stored as object/string, and 11 records contain blank strings. After converting the column to numeric with errors="coerce", those blank values became NaN.

## Business Question 1

Do customers who churn have higher monthly charges?

Result: yes
Interpretation: because the average of cusotmers who churn is 79.650% which is higher than who dnt churn(64%)

## Business Question 2

Do customers with longer tenure churn less?

Result: Yes
Interpretation: both mid point and average values 38.0% and 37% respectivley says that longer tenure customer churn less than cusotmer who churn as they are of statics 10% and 17% of avg

## Manual challenge

faced some syntax issue

## My EDA observations

At the end, write 3–5 observations about the dataset.

<!-- # null values are 11 which is obtained after total charges covnersion
# no changes of label for categorical columns
# numerical - tenure and monthly charges
# type of total charges is object which should be int or float
# avg monlthy charges of customers who churn(yes) is 74% which is morethan the customer who did not churn
# half of the customer monthly charges who churn yes is above  79.650 %
# half of the customer monthly charges who churn no is above  64.4 %
# avg tenure of churn customer is   17% which is lower than  37% who did not churn
# half of the customer did not churn  38.0% above as compared to 10% who churned -->

## What confused me

identifying the target variable

## What became easier

statical ops

## AI/ML connection

EDA
