import torch
import torch.nn as nn
from torchvision import datasets, transforms

class FashionCNN(nn.Module):
    def __init__(self):
        super().__init__()

        self.features = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
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
        return self.classifier(self.features(x))

# Load the saved model

model = FashionCNN()

model.load_state_dict(
    torch.load(
        "deep_learning/cnn/fashion_cnn.pth",
        map_location="cpu",
        weights_only=True
    )
)

model.eval()

# FashionCNN() creates the network structure with its initial parameters.
# torch.load(...) reads the saved parameter file.
# load_state_dict(...) puts the learned parameters into the network.
# map_location="cpu" loads it onto your CPU.
# model.eval() switches the network into evaluation mode.

# Part 4 — Load one test image
test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=transforms.ToTensor()
)

image, actual_label = test_data[0]

print("Image shape:", image.shape)
print("Actual label:", actual_label)

# Part 5 — Make a prediction
class_names = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]
with torch.no_grad():
    scores = model(image.unsqueeze(0))
    predicted_label = scores.argmax(dim=1).item()
print("Predicted:", class_names[predicted_label])
print("Actual:", class_names[actual_label])

# Why unsqueeze(0)? The model expects a batch of images, even when we have only one. 
# It adds a batch dimension, changing the shape from [1, 28, 28] to [1, 1, 28, 28].

# argmax(dim=1) selects the highest-scoring class. The prediction may match the actual label, or it may be wrong. Both outcomes are useful for learning.