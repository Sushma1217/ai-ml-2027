# Day 15 — EDA Challenges

## Challenge 1 — Contract vs Churn

Question: Which contract type appears to have the highest churn?
Analysis: used group by for contract as we need to know which contract type and unique values or segregation is churn type
Result:month to month contract type highest churn follwed by one year type

Visualization:

1. tried with box plot and got an error. conclusion - box plot needs at least one numerical col
2. bar plot is the great choice for two categorical column comparison
   unstack()- for plot grouped (clustered) side-by-side bars
   Observation:

## Challenge 2 — InternetService vs Churn

Question: Does churn appear to differ between InternetService types?

# Investigate:

# DSL

# Fiber optic

# No

Analysis: Based on this dataset, Fiber optic appears to have the highest proportion/number of churned customers followed by DSL and DSL have highest portion of customers who did not churn
Result: Fiber optic appears to have the highest proportion
Visualization: box plot
Observation: more customers in fiber optic

## Challenge 3 — Tenure Groups vs Churn

Question: You already discovered that churned customers have lower tenure.

<!-- # Now ask:

# Are customers with very short tenure more likely to churn?

# Create tenure groups yourself:
# 0–12 months
# 13–24 months
# 25–48 months
# 49+ months

# Then investigate churn across these groups. -->

Analysis: used group by for tenure and value counts for churn
Result: most of the cusomers who chur comes under ~10 months which is a shorter tenure
Visualization: box plot
Observation: outliers for churn and Yes as most of the cusomers who chur comes under ~10 months which is a shorter tenure

## Challenge 4 — Number vs Rate

My reasoning: No as the rate depends on how much portion of total customers who churn have month to month contract

## Challenge 5 — My Own EDA Question

Question:
Feature:
Analysis:
Visualization:
Observation:
Conclusion:

## What I learned about interpreting graphs

## What still confuses me

## AI/ML connection
