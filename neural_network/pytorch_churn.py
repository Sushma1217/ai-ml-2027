import pandas as pd
from  sklearn.model_selection  import train_test_split
from src.preprocessing import preprocessor
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import torch 
import torch.nn as nn
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    f1_score,
    recall_score
)
import joblib

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
   nn.Linear(16,1),
   nn.ReLU()
  )
 def forward(self, x):
        return self.network(x)

# Notice that there is no sigmoid in the model this time. We will use BCEWithLogitsLoss, which combines the sigmoid operation and binary cross-entropy in a numerically stable way.

# 5. Train the model
model = ChurnNetwork(X_train_tensor.shape[1])
loss_function = nn.BCEWithLogitsLoss()
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
   predictions = (probabilities>=.5).int().numpy().ravel()

actual = y_test_tensor.numpy().ravel().astype(int)

print(confusion_matrix(actual, predictions))
print(classification_report(actual, predictions))
print("Churn recall:", recall_score(actual, predictions))
print("Churn F1:", f1_score(actual, predictions))


# precision    recall  f1-score   support

#            0       0.00      0.00      0.00      1033
#            1       0.27      1.00      0.42       374

#     accuracy                           0.27      1407
#    macro avg       0.13      0.50      0.21      1407
# weighted avg       0.07      0.27      0.11      1407

# Churn recall: 1.0
# Churn F1: 0.41998877035373383

# Save the trained model
torch.save(model.state_dict(),"churn_model.pth")

# Also save the fitted preprocessing pipeline using joblib
joblib.dump(preprocessor,"churn_preprocessore.joblib")