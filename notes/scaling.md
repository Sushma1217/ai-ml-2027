Some ML algorithms are sensitive to the scale of numerical features. Scaling puts features onto a comparable scale without changing the underlying information they contain.
And importantly:
Scaling is not required for every ML algorithm.

StandardScaler uses this formula for every single number:
Scaled value = Value- Average
STD
it calcualtes for each value

## Understand fit_transform

fit()- learns/calculates params, does not modify the data
transform()- Modifies the data using previously learned parameters.

## Interview questions

What is feature scaling?
normalizing the values or managing the numerical values into a normal range without modifyting their values.
google ans
a data preprocessing technique used in machine learning to adjust the numerical values of different variables (features) to a common, comparable range.

Why do we scale features?
Improves Accuracy
for better computaion

What does fit() do?
it learn or calculates the parameters in data

What does transform() do?
odifies the data using previously learned parameters.

What is fit_transform()?
a method or function used for feature scaling where it learn the parameters and fit and modify the data to a common scale

Why should we fit the scaler only on training data?
the model learns better and doesn't memorize on the data, leakage doesnt happen.
it will learn, compute the parameters and works on test or future data without the influence of the data values

Does every ML algorithm require scaling?
No
