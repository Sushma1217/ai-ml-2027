# Part 1 — Create a tiny dataset
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.DataFrame({
    "age": [20, 22, 25, 28, 30, 35, 40, 45, 50, 55],
    "salary": [20000, 22000, 25000, 28000, 30000,
               35000, 40000, 45000, 50000, 55000],
    "churn": ["No", "No", "No", "No", "Yes",
              "Yes", "Yes", "Yes", "Yes", "Yes"]
})

# features and target
X = data.drop(columns="churn")
Y = data["churn"]
# Part 2 🔴 Manual challenge
# Split this data into train/test.
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=42)
print(X_train.shape)
print(X_test.shape)

# Part 3 — See the difference

# Calculate the mean using the entire dataset.

# Then calculate the mean using only the training dataset.

# Compare them.

# You don't need complicated code here. Use Pandas.

whole_salary_data_mean = data["salary"].mean()
print("whole_salary_data_mean",whole_salary_data_mean) 
# //35000

X_train = pd.DataFrame(X_train, columns=X.columns)
split_salary_data_mean = X_train["salary"].mean()
print("split_salary_data_mean",split_salary_data_mean)
# 34750.0

# Which mean should a real ML model be allowed to know during training?
# the splitted mean or trained mean so it will work well for future data as well instead of memorizing

# correct ans:
# The preprocessing parameters must be learned only from the training data so that information from the test data doesn't influence the model-building process.
# Part 4 — The same idea with an encoder

# Think about this situation:

# Full dataset
#     ↓
# get_dummies()
#     ↓
# Train/Test Split

# versus:

# Full dataset
#     ↓
# Train/Test Split
#     ↓
# Fit encoder on training data
#     ↓
# Transform train
#     ↓
# Transform test
# 🔴 Manual challenge

# Explain why the second approach is safer, even though one-hot encoding doesn't calculate a mean like scaling does.

# This is a slightly harder question. Take your time.
# ans: failed to guess the answer- i think for better accuracy and handle if any new catefory comes

# Part 5 — One important real-world scenario

# Imagine we're predicting whether a customer will churn next month.

# Someone accidentally creates this feature:

# customer_cancelled_account

# Ask yourself:

# Is this a useful feature or leakage?

# And why?

# This is where I want you to start thinking beyond syntax.

# ans: yes it is useful feature and contains the information to predict the traget 

# Interview questions
# What is data leakage?
# when we train the model on the entire set it will sneak the information, leads to memorization rather than actual learning 
# so prediction wont be accurate

# Why does leakage make evaluation unreliable?
# model will memorize it, will not work and results will be inaccurate.

# Give one example of preprocessing leakage.
# no idea

# google 
# 🏡 The Real Estate ExampleImagine you are building a model to predict house prices based on their size in square feet.
# The Mistake: You take your entire dataset of 1,000 houses and find the maximum size (let's say 10,000 sq ft) and the minimum size (say 500 sq ft). 
# You use these two numbers to scale all house sizes between 0 and 1.
# The Leak: After doing this, you split your data into a training set and a testing set. The testing set contains a mansion that is 10,000 sq ft.
# The Problem: Even though you split the data, your training set now "knows" that 10,000 sq ft is the absolute maximum size because of how it was scaled. It has secretly absorbed information about a house in the test set.
# 🚫 Why This Ruins Your Model: When you deploy this model in the real world, a new buyer might enter a house that is 12,000 sq ft. 
# Because the model was trained to believe 10,000 sq ft was the absolute maximum (based on information leaked from the test set),
# it will get confused and make a poor prediction.

# Should we fit a scaler on train + test together?
# no first we need to fit on train and then apply on both 

# Should we fit preprocessing separately on train and test?
# no 


