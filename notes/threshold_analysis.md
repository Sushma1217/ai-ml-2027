| Threshold | Precision | Recall |  F1 |
| --------: | --------: | -----: | --: |
|      0.50 |      0.50 |    .78 | .61 |
|      0.40 |       .45 |    .84 | .59 |
|      0.30 |       .41 |    .91 | .57 |

1. As threshold decreases from 0.50 → 0.40 → 0.30, what happens to recall? Why?
   recall increases which means out of all the positive values the model was able to predict most of the positive values. Beacuse since the threshold decreases the check or mark for positive values increases which makes model to classify the data point into the positive value

2. What happens to precision? Why?
   When the threshold is lowered, more customers are classified as positive. This increases the number of true positives, but it can also increase false positives, which can reduce precision.

3. Which threshold gives the highest F1?
   .50

4. If the telecom company says:
   "Missing a customer who is actually going to churn is very expensive."
   Which threshold would you consider — 0.50, 0.40 or 0.30?
   And why?
   i would consider threshold .30 as its recall is .91 which means the model was able to predict the most of the churn customer though the more fasle alarms by looking at precision but it is fine to put an extra efforts to to customers
