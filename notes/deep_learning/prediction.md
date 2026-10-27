What is inference?
Inference means using a trained model to predict an output for input data. Unlike training, inference does not update the model's weights.

Loading a model
Recreate the same model architecture.
Load the saved state_dict.
Call model.eval().
Use torch.no_grad() during prediction.

Predicting an image

FashionMNIST returns an image tensor and its actual label. We add a batch dimension, pass the image to the CNN, and use argmax to choose the class with the highest score.

Results
Actual category: Ankle boot
Predicted category: Ankle boot
Correct prediction? Yes / No - Yes

Interview questions

1. What is the difference between training and inference?
   training is a phase where model learns the parameters and get trained against the trained data.
   inference - phase where model uses a learned params like weights and biases to make the prediction on new data

2. Why do we recreate the model architecture when loading a state_dict?
   so that we load it freshly and model cant make use of already learnt params to avoid data leakage.

3. Why does the model need a batch dimension?
   no idea. pls answer

4. What does argmax return?
   selects the highest-scoring class

5. Can a model's prediction be wrong even when its test accuracy is high? Why?
   yes can go wrong. it depends on class imbalance, tricky data etc
