# Joblib

In machine learning, Joblib is a Python library used primarily for model serialization (saving and loading trained models) and parallel computing.

1. Saving only the Logistic Regression model loses the fitted scaler and encoder.
2. A raw new customer cannot go directly into the model without matching the exact training preprocessing.
3. Saving the combined Pipeline (preprocessor + model) preserves learned means, variances, and category mappings.
4. joblib.dump() freezes the assembly line so new customer data is automatically cleaned, scaled, and predicted identically.

# Notes

1. Problem
   What are we predicting?
   we are predicting the churn customers for telecom data set

2. Data
   What dataset did we use?
   WA*Fn-UseC*-Telco-Customer-Churn.csv

3. Preprocessing
   Why did we scale and encode?
   we scale and encode for a data smooth processing by model. Machine can understand only the numerical values so we encode the catgorical coulmns to convert into machine readable form.
   numerical columns can be of different range and a larger numbers can dominate the results so we have to scale it and transform into a scale range.

google ans
We scaled numerical features so large values wouldn't dominate features on smaller scales during model training.
We encoded categorical variables because machine learning algorithms can only process numbers, not raw text labels like contract types.

4. Model
   Why did we start with Logistic Regression?
   because the business requirement is to predict the churn customers YES/NO whether they churn or not so this algorim is used for classification problems

5. Evaluation

Why wasn't accuracy alone enough?
ther performance of the model cannot be decided only by accuracy because its the ratio between the correct prediction made out of all the prediction so when the data is imbalance(one class domindated) the required precition can be influenced. so we have to consider recall and precision too as it evalues the true postive and true negative values

6. Cross-validation

Why did we use it?
cross validation let us to evaluate the model performacne with different split eg: 50:50, 80:20, 60:40 giving us a more reliable view of its performance.

. Hyperparameter tuning

What is C and what did we find?
C controls the strength of regularization in Logistic Regression.

And importantly:

Smaller C → stronger regularization
Larger C → weaker regularization

8. Model comparison
   Which models did we compare and what did we learn?
   we compared with decision tree and random forest and learnt that logistic regression is the best suited based on metric like f1, recall, precision etc

9. Threshold
   Why does changing the threshold affect precision/recall?
   because threshold has the direct relationship with prediction class, if it is lowere, the prediction results are pushed into positive class more and if its higher the data points are classified into the negative class more. so it incluence the value of true positive and negative values hence affecting precision/recall

10. Interpretation
    What do Logistic Regression coefficients tell us?
    these are the weights assinged to a certain features to determine its influence on the output prediction.

11. Prediction

How can the trained pipeline predict a new customer?
it uses the fitted model its parameters as pipeline is blundled with preprocessing and the model so it makes the new data to undergo the same steps and predict the output.

12. Final conclusion

Explain the project in 5–8 sentences as if an interviewer asked:

"Tell me about your ML project."

My project is about predicting the churn customers from telecom data set. I used the logistic regression algorithm for the prediction as its best suited for classification problems even I compared with other models too.
started with loading data, preprocessing which includes identifying missing data, removing irrelevant columns, dividing the data into features and target, spliting into train and test data.
then we used a pipeline to create a model as its acts a bundle pacakge for preproessing model building and predicted the values.
we performed model evaluation by interpreting its accuracy, precision, recall, f1 etc metrics and cross validating it against a 5 folds, with hyperparamer turing we identified the best vlaue of C and checked model prediction against different threhold values too.
the libraries which we used are pandas, numpy, scikit learn
