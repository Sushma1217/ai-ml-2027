# Day 22 — ColumnTransformer & Pipeline

## 🎯 Why are we learning this?

we are learning this to build the ML model and handles the column without manually managing every column

## Numerical columns

monthlyCharges, tenure,TotalCharges

## Categorical columns

rest all(seniorcitizen is binary)

## ColumnTransformer

My understanding:
a tool which applies to the data preprocessing to seperate the columns.
instead of treating every column in the same way it will seperate numerical,categorical

One small refinement: it doesn't necessarily "automatically" identify the columns. We specify which columns belong to which transformer, and ColumnTransformer applies the appropriate transformation. Your code does that with numerical_columns and categorical_columns

Like applying scaler to numerical, encoder to cat helps in data leakage

## OneHotEncoder

My understanding:
a tool applied to encode the categorical columns.
encode means covnerts categorical columns values ito numerical values 1/0 and each value have its own matrix

## handle_unknown

handles the new values of the data the encoder didnt encounter during fitting,

It means that if the transformer encounters a category during transformation that wasn't present when it was fitted, it won't throw an error.
My understanding:

## Fit vs Transform

Training: learns the parameters of train and applies using transform()
Testing: since the model learnt so we just need to apply transform

Why?

## Before vs After

Shape before:
X_train (5625, 19)
X_test (1407, 19)
Shape after:
X_train_processded (5625, 30)
X_test_processed (1407, 30)

Why did the columns increase?
Number of columns have increased because the coulmn transfer tool has performed encoding where categorical columns have converted into numeric values using one hot encoder(in 0/1 forms) where each value got its own column as machine can under only numeric values.

## Pipeline

An sklearn Pipeline chains preprocessing steps and a model into a single reproducible workflow.

Imagine your project has:

10 preprocessing steps

- ML model

Doing every step manually creates opportunities for:

mistakes
inconsistent transformations
leakage
forgotten steps during deployment

A pipeline packages the process into one reproducible workflow.

## Interview questions

What is ColumnTransformer?
A tool in data preprocessing that trasnforms the data by divdies the columns into numerical and categorical and applies feature scaling or encoding eliminating manual work.
it doesn't necessarily "automatically" identify the columns. We specify which columns belong to which transformer, and ColumnTransformer applies the appropriate transformation. Your code does that with numerical_columns and categorical_columns

Why can't we use the same preprocessing for numerical and categorical features?
because machine can understand only the numerical values and it helps in smooth processing

better explanation
Numerical and categorical features have different representations and therefore require different preprocessing techniques.

What is the purpose of handle_unknown="ignore"?
it will help in handling unknown vlaues that model is not aware during fit and helps in
preventing crash

Why do we use fit_transform() on training data?
so that model can learn and apply the parameters efficently instead of memorizing and
prevents data leakage.

Why only transform() on test data?
model has already processed and learnt the parameters based on train data so there is no need of fit again so we can directly apply transform on test data

What problem does a Pipeline solve?
it combines all the stages like data collection, preprocessing, model deployment and monitoring elemintates manual tasks
stages

1. data preperation -
   1.auto fetching data from db, api or cloud
   2.data cleaning- missing number, duplicates
   3.feature enginerring
2. model enginerring - model training, evaluation, hyper tuning
   3.ops and deployment

What is the difference between ColumnTransformer and Pipeline?
ColumnTransformer - a tool in preprocessing for data transformation
pipeline - complete package for end to end work from data collection til model deployment

## What confused me

## What became clearer

## AI/ML connection
