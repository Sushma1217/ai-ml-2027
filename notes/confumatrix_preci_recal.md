Accuracy alone doesn't tell us which type of predictions the model gets wrong. Classification metrics help us understand whether the model is actually useful, especially when one class is more important or less common.

## confusion matrix

a simple table helps to know how well a classification model performs by comparing the model predicted results with actual

## The Four Key Outcomes

True Positive (TP): The model correctly predicts the positive outcome.
True Negative (TN): The model correctly predicts the negative outcome.
False Positive (FP): The model incorrectly predicts the positive outcome (a Type I error).
False Negative (FN): The model incorrectly predicts the negative outcome (a Type II error).

## Precision

the proportion of postivie predictions made by model that are actually correct.
Of all customers the model predicted would churn, how many actually churned?

That's precision.

Example:

Model predicted 20 customers will churn.

15 actually churned.
5 didn't.

Precision:

15 / 20 = 75%

## recall

how many positive prediction did the model made.

Precision
Out of all things predicted as positive, how many are truly positive?
recall
Out of all actual positive items, how many did the model find?
There is usually an inverse relationship between precision and recall.

## The distinction I want you to remember

Precision:
When the model says YES, how often is it right?

Recall:
Of all actual YES cases, how many did the model find?

## For a churn prediction system, do you think precision or recall might be more important?

may be recall because it says how many customers churn the model able to predict out of how many are actually churn.

## interview questions

## What is a confusion matrix?

the matrix or table that shows how model performed by comparing the predicted results with actual.

What is TP?
the model predicted postive and actual result is also positive.

What is TN?
the model predicted negative and actual result is also negative
What is FP?
the model predicted positive and actual result is negative

What is FN?
the model predicted negative and actual result is positive.

What is precision?
out of the positive, how many are correctly predicted by the model.

What is recall?
out of the all postive prediction, how many the model was able to predict correctly.

What is the difference between precision and recall?
Precision measures how many of the model's positive predictions are correct, while recall measures how many of the actual positive cases the model manages to find.

Why isn't accuracy always enough?
accuracy shows the metric how well the model performed but when we actually verify with the actual results with predicted we might see the difference and there the question arises to know where the model prection went wrong which can be find using cm, recall, precision.

In churn prediction, why might false negatives matter?
because when model predict as churn customers as false or negative it will ignore and takes no action on that so it will lose the customers which can impact the business.
