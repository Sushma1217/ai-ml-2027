🔴 Part 6 — Create your comparison table

This is important.

Create:
| Model | Accuracy | Precision | Recall | F1 |
| ------------------- | -------: | --------: | -----: | -: |
| Logistic Regre| 78.68 | 0.62 | 0.51 | 0.56 |
| Decision Tree | 71.57 | 0.47 | 0.51 | 0.49 |
| Random Forest | 71.57 | 0.63 | 0.47 | 0.54 |

# Part 7 — Manual reasoning

Before deciding which is "best", answer:

1. Which model has the highest F1?
   ans:Logistic Regression with .56

2. Which has the highest recall?
   ans:Logistic Regression and decision tree are same 0.51

3.Which has the highest precision?
random forest with .63

4.If our business priority is catching as many churners as possible, which model would you choose?
logistic regression by considering its precision and recall values 0.62 & 0.51 respectively.
in a simpler way the f1 score is higher for logistic as compare to other models.

5. Would you automatically choose the model with the highest accuracy?
   no accuracy is not a sole metric to determine the model performance we must compare with precision, recall etc also these will helps us to interpret how any positive predictions made by the model which is utmost important for business requirement.

# interview questions

Why compare multiple ML models?
so we get a better comparision among the models and we can choose the best one for business logic.

What is the difference between Logistic Regression and Decision Tree?
logistic regression is the learning model used to predict the output is between two classes like true or false, 0/1, yes or no where as decision tree is used when the target is of continuous values, flow chart or hierarchy relationhsip

What is a Random Forest?
A Random Forest is a popular supervised machine learning algorithm that combines multiple decision trees to make highly accurate and stable predictions.

Why shouldn't we compare models using only accuracy?
accuracy is not a sole metric to determine the model performance we must compare with precision, recall etc also these will helps us to interpret how any positive predictions made by the model which is utmost important for business requirement.

What does random_state=42 do?
it ensures that data splitting or model evaluation produces the same results everytime we run a code or process it

Why should all models use the same test set?
because using we are predicting against the same data set, using the same test gives fine comaprison among all the models

If Logistic Regression has higher recall but Random Forest has higher accuracy, which would you choose for churn?
i would prefer logistic regression because recall is about how many positive prediction made by the model out of all the positive values whicch is most important parameter as it tells how many customers are leaving and business can take action to retain them.
accuracy is about how many correct prediction made from the total prediction so it can incluse the No class as well and for business prequirement No class is not a threat.

Is the model with the highest score always the best model?
no accuracy is not a sole metric to determine the model performance we must compare with precision, recall etc also these will helps us to interpret how any positive predictions made by the model which is utmost important for business requirement.

Why should we avoid tuning every model blindly?
its a reduandant work and not useful in any way. tuning on the best model saves times and gives better results.

Explain your ML model-selection workflow.
calculate accuracy, precion, recall and F1.
compare the F1(covers precion and recall )
compare accuracy
and choose the best model based on all the metrics.
