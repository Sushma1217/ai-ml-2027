For Logistic Regression:

positive coefficient → pushes prediction toward the positive class (Yes / churn)
negative coefficient → pushes prediction toward the negative class (No / not churn)
coefficient magnitude indicates the strength of that feature's contribution within this fitted model and feature representation

# Get Transformed Feature Names

Scikit-Learn transformers (like ColumnTransformer or individual pipelines) provide a built-in method called get_feature_names_out() to retrieve the exact feature names after one-hot encoding, scaling, or imputation.

# get_feature_names_out()

when we apply the transformers like one hot encoder, single column is expaned into multiple binary columns, so gey_feature_names tells the exact coumn order with a names.

# coefficent

these are the weights that the model assigned to a specific input feature to determine its influence on the output prediction.

1.Pick 3 features with the largest positive coefficients. What does that suggest about churn?
cat**InternetService_Fiber optic 0.636416
num**TotalCharges 0.402194
catPaymentMethod_Electronic check 0.307711

ans: A positive coefficient means that, holding the other model inputs constant, that feature contributes toward a higher predicted churn tendency.
out of all the features the model looked into, these features have high impact on pushing customers toward leaving.

2. Pick 3 features with the most negative coefficients.What does that suggest?
   cat**Contract_One year -0.694682
   num**tenure -1.151536
   cat\_\_Contract_Two year -1.152299

tenure has a relatively large negative coefficient, meaning higher tenure contributes toward lower predicted churn probability, all else equal.
so the tenure and contract type is not the areas needs the attension for now.

3. If a feature has: coefficient = +1.5 and another has: coefficient = -1.5

what is the general direction of their effects?
The feature with a +1.5 coefficient pushes predictions toward churn- likelihood of leaving
coefficient = -1.5 - less chance of churn

4.

Does a positive coefficient mean:

"This customer will definitely churn"?

Explain why/why not.
no positive coefficient is the weight assigned of their influence on output prediction not a deciding value on the prediction

5.Why can we not simply say:
"The feature with the biggest coefficient is the most important feature in every situation"?
Think about encoding, scaling, model type, and context.
No because scaling- numerical values might have a different scale range,
encoding for reference

correct ans
But because your numerical features are standardized, comparing coefficient magnitudes among those standardized numeric features is more meaningful than it would be on completely different raw scales.

However, categorical one-hot coefficients and numeric coefficients still require context, and coefficients describe the model's linear relationship, not universal real-world feature importance.

# Top positive coefficients

| Feature                                | Coefficient | Interpretation                                                                        |
| -------------------------------------- | ----------: | ------------------------------------------------------------------------------------- |
| cat\*\*InternetService_Fiber optic     |    0.636416 | interet service was fiber optic might be poor so churning                             |
| num\*\*TotalCharges                    |    0.402194 | charges mau be high so churniing                                                      |
| cat\*\* PaymentMethod_Electronic_check |    0.307711 | payment method electronic churn is might not be convient to the customers so churning |

# Top negative coefficients

| Feature                  | Coefficient | Interpretation                                                   |
| ------------------------ | ----------: | ---------------------------------------------------------------- |
| cat\_\_Contract_One year |   -0.694682 | contract type is not the impact factor pushing customers leaving |
| num\_\_tenure            |   -1.151536 | tenure is not the area of needing an attension                   |
| cat\_\_Contract_Two year |   -1.152299 | contract type is not the impact factor pushing customers leaving |
