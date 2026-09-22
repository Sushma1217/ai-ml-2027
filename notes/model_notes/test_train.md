# Day 19 — Train/Test Split

## 🎯 Why are we learning this?

We need to evaluate a model on data it hasn't seen during training. Train/test splitting gives us a more realistic estimate of how the model will perform on new customers.

## Why can't we train and test on the same data?

if the data is huge i can create a problem as it takes more time, looping issue etc

<!-- google -->

Training and testing on the same data leads to memorization rather than true learning, making it impossible to measure how well a model performs on new data

## Train/Test Split

### Code

X_train, X_test, Y_train, Y_split = train_test_split(X,Y, test_size=0.2, random_state=42)

### Shapes

X_train (5634, 19)
X_test (1409, 19)
Y_train (5634,)
Y_split (1409,)

## random_state

My understanding:
random_state will let same random results every single time you run the code.
thats why even after random+state=10 we get the same split.
X_train (5634, 19)
X_test (1409, 19)
Y_train (5634,)
Y_split (1409,)

Random splitting can produce different samples. random_state lets us reproduce the same split when we rerun the code.

## Data Leakage

My understanding:

## Preprocessing before vs after splitting

Which is safer and why?
i feel Full dataset
↓
Train/Test Split
↓
Fit preprocessing using training data
↓
Transform training + test data
is safer as it will check for a fit for model

We split the data into train and test so that the model doesn't just rely on memorized data, allowing us to evaluate how well it will predict unseen future data. Keeping the test data strictly separate prevents data leakage, ensuring our evaluation metrics are honest and reliable for real-world use.

Data Leakage- Accidental sharing of test information (like means, maxes, or future signals) during training.

## Interview Questions

What is train/test split?
training and testing on the same data leads to memorization rather than true learning

Why shouldn't we evaluate a model on its training data?
may be it will set a min, max value or some range so fails to handle the future data

What does random_state do?
it will make the random split to be same at each time of model run.

What is data leakage?
Data leakage occurs when information that would not legitimately be available when making a prediction becomes available to the model during training.

For our current example, if we calculate the scaler's mean/std using both train and test data, the test set has influenced the training process. That's leakage—even though we never directly put the test labels into the model.

## What confused me

data leakage

## What became clearer

random state, splitting test, train data

which preprocessing order avoids leakage?
Full Raw Dataset
↓

1. Train/Test Split
   ├───────────────────────────────┐
   ↓ ↓
   Train Data Test Data
   ↓ │
2. FIT Preprocessor │
   (Compute Mean, Max, Encoders) │
   ↓ │
3. TRANSFORM Train Data │
   ↓ │
4. Train Model │
   │ │
   └──────────────┬────────────────┘
   ↓ 5. TRANSFORM Test Data
   (Using TRAIN Preprocessor)
   ↓ 6. Evaluate Model

## AI/ML connection
