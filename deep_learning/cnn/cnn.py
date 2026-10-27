import numpy as np
import torch 
import torch.nn as nn

image = np.array([
    [0,   0,   0,   0, 0],
    [0, 255, 255, 255, 0],
    [0, 255, 255, 255, 0],
    [0, 255, 255, 255, 0],
    [0,   0,   0,   0, 0]
])

# print(image)
# print("Shape:", image.shape)
# print("Pixel:", image[1, 1])


kernel = np.array([
     [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

# Select the top-left 3x3 region
region = image[0:3,0:3]
print("Image region:", region)


print("Kernel:",kernel)


result = np.sum(region * kernel)

print("Convolution result:", result)

# Move the filter across the image
for row in range(3):
    for col in range(3):
        region = image[row:row + 3, col:col + 3]
        result = np.sum(region * kernel)
        print(f"Position ({row}, {col}): {result}")

        # The two loops move the 3×3 filter over the 5×5 image. Since a 3×3 region fits in three positions horizontally and three vertically, we get nine results.

#         Expected grid of results:
            # 510      0    -510
            # 765      0    -765
            # 510      0    -510


# This output is a feature map. It tells us how strongly this particular filter responds at each location.

# Important distinction: we chose these filter numbers ourselves. A real CNN starts with initial filter values and learns better values during training using backpropagation.

# The collection of results forms a feature map. A CNN learns its filters during training; we manually chose the filter only to understand the operation.

# Part 4 — Task 3: Let PyTorch perform convolution
# Concept: nn.Conv2d applies learnable filters to image tensors. Unlike our manually chosen kernel, its filter weights can be adjusted by backpropagation to improve predictions.

# One image: batch=1, channel=1, height=5, width=5
image_tensor = torch.tensor(image,dtype=torch.float32).reshape(1,1,5,5)

conv = nn.Conv2d(in_channels=1,out_channels=2,kernel_size=3)
feature_maps = conv(image_tensor)

print("Input shape:", image_tensor.shape)
print("Output shape:", feature_maps.shape)


# float32: the numerical format used for the pixel values and model calculations.
# reshape(1, 1, 5, 5): PyTorch expects a batch dimension and a channel dimension as well as the image height and width.
#     First 1: one image in this batch.
#     Second 1: one grayscale channel.
#     5, 5: the image's height and width.
# in_channels=1: the input is grayscale.
# out_channels=2: the layer learns two different filters.
# kernel_size=3: each filter is three pixels wide and three pixels high.

# pooling
feature_map = torch.tensor([
    [1.0, 3.0, 2.0, 4.0],
    [5.0, 6.0, 1.0, 2.0],
    [2.0, 1.0, 7.0, 8.0],
    [3.0, 4.0, 2.0, 9.0]
])
pool = nn.MaxPool2d(kernel_size=2)
pooled_maps = pool(feature_map.reshape(1,1,4,4))
print(pooled_maps.reshape(2, 2))


################actual building of CNN ########################
class FashionCNN(nn.Module):
    def __init__(self):
        super().__init__()

        self.features = nn.Sequential(
             nn.Conv2d(1, 16, kernel_size=3, padding=1),  # kerneral_size =3, uses the kernel to extract features
            nn.ReLU(),
            nn.MaxPool2d(2),  #  2 is also a kerneral size but uses the kernel to extract features
            # Pooling reduces spatial size; convolution learns filters to extract features.
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(32 * 7 * 7, 64),
            nn.ReLU(),
            nn.Linear(64, 10)
        )
    def forward(self, x):
      x = self.features(x)
      return self.classifier(x)

# How to read this code:
# - nn.Sequential(...) runs its layers in the order listed.
# - The features section detects and reduces image patterns.
# - nn.Flatten() converts the feature maps into a vector.
# - The classifier section uses that vector to calculate ten class scores.
# - forward() defines the path the input follows through the model.
# nn.Conv2d(1, 16, ...) means one input channel and 16 output filters. 
# nn.Conv2d(16, 32, ...) receives those 16 feature maps and produces 32 new ones.

model = FashionCNN()
loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# - CrossEntropyLoss measures how well the ten class scores match the correct category.
# - Adam updates the model's weights using gradients.
# - lr=0.001 is the learning rate, which controls the size of the updates.
# The key difference from your binary churn model is that this is a multiclass classification problem: each image belongs to one of ten categories.

###############Load the dataset######################

from torch.utils.data import DataLoader
from torchvision import datasets, transforms

transform = transforms.ToTensor()

train_data = datasets.FashionMNIST(
    root="data", train=True,
    download=True, transform=transform
)

test_data = datasets.FashionMNIST(
    root="data", train=False,
    download=True, transform=transform
)

train_loader = DataLoader(
    train_data, batch_size=64, shuffle=True
)

test_loader = DataLoader(
    test_data, batch_size=64, shuffle=False
)

# ToTensor() converts each image into a tensor with pixel values scaled to 0–1. The DataLoader provides batches of 64 images at a time. 
# The training loader shuffles the examples; the test loader does not.

# Train for one epoch
model.train()
total_loss = 0.0
for images, labels in train_loader:
    optimizer.zero_grad()

    outputs = model(images)
    loss = loss_function(outputs, labels)
    loss.backward()
    optimizer.step()

    total_loss += loss.item()

print("Average training loss:",
      total_loss / len(train_loader))

# This is the same training loop you used previously:
# 1. Run a forward pass.
# 2. Calculate the loss.
# 3. Calculate gradients with loss.backward().
# 4. Update the parameters with optimizer.step().
# One epoch processes the entire training dataset once. 
# We'll do one epoch today so you can focus on understanding the model rather than tuning it.


############## Evaluate and save ##########
model.eval()
correct = 0
total = 0

with torch.no_grad():
    for images, labels in test_loader:
        outputs = model(images)
        predictions = outputs.argmax(dim=1)
        correct += (predictions == labels).sum().item()
        total += labels.size(0)
print(f"Test accuracy: {correct / total:.2%}")

torch.save(
    model.state_dict(),
    "deep_learning/cnn/fashion_cnn.pth"
)

# argmax(dim=1) selects the highest-scoring category for each image.
# Test accuracy tells us the fraction of test images classified correctly
# The saved state_dict contains the trained parameters; to use it later


# Expected results:
# - An average training loss.  0.53
# - A test accuracy percentage.  85.49%
# - A saved model at deep_learning/cnn/fashion_cnn.pth. - yes