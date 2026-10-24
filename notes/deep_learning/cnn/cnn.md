Concept | What it means | Why we need it
Pixel | A numerical value representing image brightness or color | Images become numerical inputs
Channel One component of an image, such as grayscale or RGB Tells the model the input structure
Filter/kernel A small grid of numbers applied across an image Detects local patterns
Convolution Applying a filter at different image locations Creates a feature map
Pooling Reducing the spatial dimensions Makes later processing smaller
CNN classifier CNN features followed by classification layers Predicts the image category

What is a pixel? What does the shape (5, 5) mean?
a pixel is a numerical value representing the image brighntess or color.
shape (5, 5)- represent the kerner or filter size - which means a small grid of numbers applied on image to detect the local patterns.
the first 5- height of the filter(spanning 5 pixels vertically)
the second 5- width of the filter (spanning 5 pixels horizontally).

What is a filter?
A filter, also called a kernel, is a small grid of numbers. It slides over the image, multiplies its values by the corresponding image pixels, and adds the results.

For learning purposes, we'll use this vertical-edge filter:
k = [-1,0,1]
[-1,0,1]
[-1,0,1]
It compares the left side of a region with the right side. Strong differences can produce large positive or negative values.

What is Conv2d?
It is a PyTorch layer that applies learnable filters to image data. The 2d means that each filter moves across two spatial dimensions: height and width.

What is pooling?
Pooling reduces the height and width of a feature map. Max pooling keeps the largest number in each small region, reducing the amount of information the next layers need to process.

max pooling -
The top-left 2×2 region is:
1 3
5 6

Max pooling keeps the largest value: 6. It does the same for each of the other three 2×2 regions, producing a 2×2 grid instead of a 4×4 grid.

Why do we need it?
It reduces spatial size, which makes later computation smaller. But it also discards some spatial detail, so pooling is a design choice rather than magic.

Concepts learned

Pixel and image tensor

Filter/kernel and convolution

Feature map

ReLU and max pooling

Flattening and linear classification

Cross-entropy loss and Adam optimizer

Manual convolution

I represented a 5×5 image as numbers and applied a 3×3 filter. Each result came from multiplying corresponding pixels and filter values, then adding the products. Moving the filter produced a feature map.

Pooling

Max pooling selects the largest value from each local region. In the 4×4 example, it reduced the grid to 2×2.

CNN architecture

Input → convolution → ReLU → pooling → convolution → ReLU → pooling → flatten → linear layers → 10 class scores.

Training

I used a forward pass, cross-entropy loss, backpropagation and Adam, then evaluated on unseen test data.

Results 1. Training loss:
2.Test accuracy: 3. Saved model path:

Explain in your own words why a CNN uses filters and pooling for images.
image is represented as a grid of numbers so a kernal or filter of defined size matrix or vector will be moved across the image for feature detection, pattern recognition and in the pooling stage a max number from the product of the filter is selected to preverse the pattern or retain the important identification and pass the less input to the next layer for further processing.

(all are of my own words so correct me)

Interview questions

1. Why are CNNs useful for image classification?
   because they automatically learn visually pattern from simple edges to complex objects layer by layer.
   Their sliding filters allow them to recognize features anywhere in the frame regardless of position.

2. What does a convolution filter do?
   convolution filter acts as small sliding window that scan across an image pixel by pixel. as it moves it extract a local features like edges, corners, and textures. By reusing the exact same filter weights across the entire grid, it efficiently detects specific visual patterns no matter where they appear in the image.

3. What is a feature map?
   A feature map is the output grid produced when a convolution filter slides across an image, acting as a "heatmap" that highlights where specific patterns (like edges, curves, or textures) are located.

4. Why use padding?
   Padding involves adding a border of zeros (or replica values) around the edges of an image or feature map before applying a convolution filter to prevent shrinking, preserve edge information

5. What does max pooling do?
   Max pooling is a downsampling operation that shrinks the size of a feature map by sliding a small window (usually2\*2) across it and keeping only the maximum value in that window, discarding the rest.

6. Why does the final layer have 10 outputs?
   because the model is designed to classify an image into 10 distinct categories

7. Why use cross-entropy for this task?
   because it mathemetically desinged to measure how well a model's predicted probabilities match the true category labels.

8. What is the difference between model.eval() and torch.no_grad()?
   model.eval() - switch on the evaluation mode
   torch.no_grad() - disables gradient calculation because we are predicting, not training.

9. Why evaluate on unseen test data?
   because to test or know how well the model performs on the unseen data

10. What does state_dict() save?
    Returns the model's learned parameters, such as weights and biases. We save these instead of retraining the model each time.
