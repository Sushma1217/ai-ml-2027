import pandas as pd
from  sklearn.model_selection  import train_test_split
from src.preprocessing import preprocessor
import torch 
import torch.nn as nn
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    f1_score,
    recall_score
)
import joblib


import random
import numpy as np
import torch

random.seed(42)
np.random.seed(42)
torch.manual_seed(42)

# Load the CSV with pandas.
df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Drop customerID
df = df.drop(columns="customerID")

# Convert TotalCharges to numeric, handling blank values.
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"],errors="coerce")

# drop invalid rows
df = df.dropna()

# Set Churn as the target (Yes = 1, No = 0).
X= df.drop(columns="Churn")
y= df["Churn"]
y = y.map({"Yes":1,"No":0})

# Split into training and test sets using
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.2,random_state=42,stratify=y)

# encoding, scaling
processor = preprocessor()

# Important: fit the preprocessing pipeline on X_train only, then transform both training and test data. This avoids data leakage.
# for this we are using this approach

# Fit preprocessing on training data only
processor.fit(X_train)

# Transform both datasets
X_train_processed = processor.transform(X_train)
X_test_processed = processor.transform(X_test)


# Convert the processed data to PyTorch tensors
X_train_tensor = torch.tensor(X_train_processed, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test_processed,dtype=torch.float32)

y_train_tensor = torch.tensor(y_train.to_numpy().reshape(-1,1), dtype=torch.float32)
y_test_tensor = torch.tensor(y_test.to_numpy().reshape(-1,1),dtype=torch.float32)

#Build the netwrok 
class ChurnNetwork(nn.Module):
 def __init__(self,input_size):
  super().__init__()

  self.network = nn.Sequential(
   nn.Linear(input_size,32),
   nn.ReLU(),
   nn.Linear(32,16),# 32 Input feature, 16 output
   nn.ReLU(),
   nn.Linear(16,1)
 
  )
 def forward(self, x):
        return self.network(x)

# Notice that there is no sigmoid in the model this time. We will use BCEWithLogitsLoss, which combines the sigmoid operation and binary cross-entropy in a numerically stable way.

# 5. Train the model
model = ChurnNetwork(X_train_tensor.shape[1])
# loss_function = nn.BCEWithLogitsLoss()
positive_count = y_train_tensor.sum()
negative_count = len(y_train_tensor) - positive_count

pos_weight = negative_count / positive_count

loss_function = nn.BCEWithLogitsLoss(
    pos_weight=pos_weight
)

print("Positive class weight:", pos_weight.item())
optimizer = torch.optim.Adam(model.parameters(),lr=0.001)

# Train for 50 epochs initially:
for epoch in range(50):
   model.train()

   logits= model(X_train_tensor)
   loss= loss_function(logits,y_train_tensor)

   optimizer.zero_grad()
   loss.backward()
   optimizer.step() #updates the weights

   if(epoch +1) %10 ==0:
      print(f"Epoch {epoch+1}",f"loss {loss.item():.4f}")   #loss is decreasing 
    # .4f - truncating the decimal for 4 digits

# 6. Evaluate the model
model.eval()

with torch.no_grad():
   logits = model(X_test_tensor)
   probabilities = torch.sigmoid(logits)
   print("Probability minimum:", probabilities.min().item())
   print("Probability maximum:", probabilities.max().item())
   print("Probability mean:", probabilities.mean().item())
   print(
      "Predicted churn count:",
      (probabilities >= 0.5).sum().item()
   )
   predictions = (probabilities>=.5).int().numpy().ravel()

actual = y_test_tensor.numpy().ravel().astype(int)

print(confusion_matrix(actual, predictions))
print(classification_report(actual, predictions))
print("Churn recall:", recall_score(actual, predictions))
print("Churn F1:", f1_score(actual, predictions))


# [[696 337]
#  [ 71 303]]
#               precision    recall  f1-score   support

#            0       0.91      0.67      0.77      1033
#            1       0.47      0.81      0.60       374

#     accuracy                           0.71      1407
#    macro avg       0.69      0.74      0.69      1407
# weighted avg       0.79      0.71      0.73      1407

# Save the trained model
torch.save(model.state_dict(),"churn_model.pth")

# Also save the fitted preprocessing pipeline using joblib
joblib.dump(processor,"churn_preprocessor.joblib")

# Load the saved preprocessing pipeline
loaded_processor = joblib.load("churn_preprocessor.joblib")

# Transform the SAME test data
loaded_X_test = loaded_processor.transform(X_test)
loaded_X_test_tensor = torch.tensor(
    loaded_X_test,
    dtype=torch.float32
)
# Create a fresh model with the same architecture
loaded_model = ChurnNetwork(loaded_X_test_tensor.shape[1])

# Load saved weights
loaded_model.load_state_dict(
    torch.load("churn_model.pth", weights_only=True)
)
loaded_model.eval()

# Compare original and loaded predictions
model.eval()

with torch.no_grad():
    original_probs = torch.sigmoid(model(X_test_tensor))
    loaded_probs = torch.sigmoid(
        loaded_model(loaded_X_test_tensor)
    )

print(
    "Predictions match:",
    torch.allclose(original_probs, loaded_probs, atol=1e-6)
)
# Predictions match: True