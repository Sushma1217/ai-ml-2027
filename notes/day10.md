# Day 10 — Data Cleaning

## Missing values

## isna()

returns bool val for each cell.
non nan - false
nan- true
it ignores - ""

isna().sum()- returns the count of nan values

## dropna()

remove any row that contains atleast 1 missing value(nan, none)
parameters
axis=0 to drop rows with missing values (default),
axis=1 to drop columns with missing values.
subset- only specific col names to check for na
inplace: Set inplace=True to modify the original data DataFrame directly instead of returning a new one.

## fillna()

fill nan with values as per the requirement

## Mean vs Median

Why is the median much more representative here?
ans- median represent the middle value so it wont be beyod the data scale

google ans
The median is more representative in exploratory data analysis (EDA) because it is robust to outliers and unaffected by skewness.

## Duplicates

duplicated()- identify duplicate rows, returns bool val.
if the row is duplicated - True

## Outliers

the data values which are extremely out of the boundry or different

It is a data point that behaves differently from all other data points in the dataset

## What confused me

syntax, checking for outliers

## What became easier

missing val, some portion of fillna

## AI/ML connection

EDA- data cleaning

## Decisions I made

mean fill for age and median for salary

## interview questions

isna- check for nan, true if its nan vice versa
notna() - true for not null val

dropna() vs fillna()
dropna() deletes rows or columns that have missing data
fillna()- filling with some values like mean, median, mode etc

Mean vs median for missing-value imputation
mean- for normal distribution with without outliers
median - for skewed data or datasets containing extreme outliers

Why can't we blindly remove duplicates?
can break ops sys, destroy valid historical data, erase critical data

Should every outlier be removed?
Not necessarily. When to remove
data errors
Impossible values
Model constraints
