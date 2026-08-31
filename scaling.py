import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data = pd.DataFrame({
    "age": [20, 30, 40, 50, 60],
    "salary": [20000, 30000, 40000, 50000, 60000]
})

mean = data.mean()
std = data.std()
print("mean",mean)
print("std",std)


# Task 2 🔴 Manual
# Before using StandardScaler, answer:

# Which feature has the larger numerical scale: age or salary?
# Salary
# Then:

# Does salary being numerically larger mean that salary is automatically more important?
# No

# Task 3 — Your first scaler
scaler = StandardScaler()

scaled_data = scaler.fit_transform(data)
print("scaled_data",pd.DataFrame(scaled_data))

# Task 4 — Understand fit_transform
# answered in the notes

# Task 5 🔴 Manual

# Now separate the operations:
print("fit",scaler.fit(data)) 
#o/p StandardScaler()
print("transof",scaler.transform(data))
# p/p values in matrices

# Task 6 — Inspect what the scaler learned
print("Scaler mean", scaler.mean_)
print("Scaler scale", scaler.scale_)

# Task 7 🔴 The important one
# Create a train/test split of your small dataset.

# Then answer:

# Should this be:

# scaler.fit(X)

# or:

# scaler.fit(X_train)

# ?

# And why? Then implement it.
# answer: scaler.fit(X_train) because model will process and calculate the parameters on train data and helps in
# avoiding the memorizing calcualted parameters value while processing the test data which impacts the ultimate results
X= data[["age","salary"]]
Y= data=[""]
X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size=.2, random_state=42)
scaler_train_data = scaler.fit_transform(X_train)
print("scaler_train_data",scaler_train_data) 
# error as there is no array for Y
