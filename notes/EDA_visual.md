# Day 14 — EDA Visualization

## Why visualization?

gives pictorial representation of the flow. helps to understand the trend,
easy to figure out the range like low, high, most of the people etc

## Histogram

u shape, more number of customer falls between 0-5 and followed by 65-70 tenure
normaly distributed, no much outliers

correct:
Customer tenure is concentrated at both the very low and very high ends, with fewer customers in the middle. The distribution does not appear normally distributed.

### Tenure

Observation:
outliers in yes churn above 70
median of the customer who did not churn is around 37
not able to interpret much

### MonthlyCharges

Observation:
most customers concentrated between 70-110 range
i can see more distribution towards 20-30 compared to other range
extreme values? yes. between 0-30

corrected:
There is a noticeable concentration around 70–110, with another group at the lower end. I cannot conclude that the 0–30 values are outliers from this histogram alone.

## Churn distribution

Observation:
customer who did not churn is higher than who churn
around 5k customer did not churn and around 2.5 cusotmer churn

## Contract distribution

Observation:
Month-to-month contract is high around 3.8k customers
one year contract(~1.3) is little lower than two year contract(~1.5)

## MonthlyCharges vs Churn

Observation:
for customer who did not churn
min monthly charges start from ~18 charges
half of the customer falls around ~65 charges

for who churn
range is ~18-~110(min- max) charges
half of the customer falls around ~78 charges

## Tenure vs Churn

Observation:
matched with who did not churn but mismatching with who churn(i can see some outliers)
some confusion in interpreting the box plot is there
corrected:
Customers who churn generally have shorter tenure than customers who don't churn.

What I learned: A box plot shows the median and spread of the data. I should not compare its values directly with the mean from groupby(). Mean and median can be different.

## What confused me

box plot interpretation

## What became easier

plot code

## AI/ML connection

## Interview questions
