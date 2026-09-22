1. What does predict_proba() give us?
   it will predict the probability of the value of data calss belongs to.

2. Why might probability be more useful to a business than just Yes/No?
   because probability tells us how much confidence the model is about its prediction so we can consider the choice based on the figures or confidence level rather than mere guess.

3. If a customer has churn probability 0.82, what does that mean?
   it means 82% the possibility or chances of churn or customer may leave.

4. If a customer has probability 0.35, does that mean the customer will definitely not churn?
   no we can say that the chance is 35% so there is a still way for customer to churn.

5. What happens when we change the classification threshold from:
   0.50 → 0.40

Think carefully about:

Recall ↑ or ↓?
since the model prredicts the most positive cases the recall level can go up.

Precision ↑ or ↓?
since the model predicts the most positive cases it can create more false alarms too so the precision level can go down.

| Probability | Actual Churn | Your interpretation                                                    |
| ----------- | ------------ | ---------------------------------------------------------------------- |
| 0.82        | Yes          | 82% of yes churn                                                       |
| 0.73        | No           | 73% of yes churn                                                       |
| 0.61        | Yes          | 61% of yes churn                                                       |
| 0.42        | Yes          | 42% of yes churn                                                       |
| 0.20        | No           | 20% of churn since the threhold limit is 40 % this prediction is right |
