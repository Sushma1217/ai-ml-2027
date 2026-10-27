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
   You recreate the architecture so the saved weights have a matching structure

3. Why does the model need a batch dimension?
   Let's use an everyday example.

Imagine you're asking the model to identify one photograph. The photograph has shape:

[1, 28, 28]

- 1 = one grayscale channel
- 28 = height
- 28 = width
  But PyTorch image models normally expect a batch of images, even when the batch contains only one image. So we add a leading dimension:

[1, 1, 28, 28]

The four numbers mean:

[number of images, channels, height, width]
One image before adding the batch dimension
1 × 28 × 28
Channel × Height × Width

1 × 1 × 28 × 28
Batch × Channel × Height × Width

This line adds that extra dimension:
image.unsqueeze(0)

unsqueeze(0) does not change the pixel values. It simply tells PyTorch, “Treat this as a batch containing one image.”

Why is this useful? During training, the model processes batches of 64 images together. Using the same input structure for one image and for 64 images makes the model's interface consistent.

4. What does argmax return?
   selects the highest-scoring class

5. Can a model's prediction be wrong even when its test accuracy is high? Why?
   yes can go wrong. it depends on class imbalance, tricky data etc
