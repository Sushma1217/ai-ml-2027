A loss function tells the model how wrong its prediction was.
actual = 1
Prediction = 0.2- loss is high
Prediction = 0.9 - loss is low

Which prediction should have the smaller loss — 0.9 or 0.2? Why?
0.9 as its prediction is near to the actual value so the loss is smaller

# Binary Cross-Entropy (BCE).

it answers:How far was my predicted probability from the actual binary answer.

🟢 Your notes
Explain in your own words:

1. What is a loss function?
   it is the parameter that explain how wrong the model prediction was

2. Why do we need one?
   so we will come to know matemetically how the model prediction went wrong.

3. What does BCE measure?
   it measures how far the predicited probability from the actual ans

4. Why should a prediction of 0.9 have a smaller loss than 0.2 when actual = 1?
   because when the actual is 1 then 0.9 is a probability of class 1 which means model prediction is right and on the other way 0.2 classifies the prediction into 0(false) which is a wrong prediction so the loss is higher than the .9 prediction.

5. What happens when the model predicts something very confidently but is completely wrong?
   When a model makes a confident prediction that is completely wrong, the Binary Cross-Entropy loss produces a massive penalty spike.
   Because loss measures how far off the prediction is, high confidence in the wrong direction causes the loss to grow exponentially.
