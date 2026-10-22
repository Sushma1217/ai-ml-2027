# Day 49 — Understanding FastAPI Deployment

## 1. What is FastAPI?

FastAPI is a Python framework used to expose Python functionality through HTTP APIs. It lets another application send customer information and receive a prediction without running the training script.

## 2. Understanding `app.py`

### Imports

- `FastAPI`: Creates the API application.
- `pandas`: Converts the incoming customer data into a DataFrame.
- `torch` and `torch.nn`: Load and run the PyTorch neural network.
- `joblib`: Loads the saved preprocessing pipeline.
- `Path`: Builds file paths reliably, regardless of the working directory.

### Project path

`BASE_DIR = Path(__file__).resolve().parent.parent`

This locates the project root relative to `app.py`, so the model and preprocessing files can be found.

### Model architecture

`ChurnNetwork` recreates the same neural-network structure used during training. The architecture must match the saved model's parameters.

### Loading the preprocessor

`joblib.load(...)` restores the fitted preprocessing pipeline. It applies the same scaling and one-hot encoding learned from the training data.

### Loading the model

`model.load_state_dict(...)` loads the trained weights into the recreated network.

`model.eval()` switches the model to evaluation mode.

### Home endpoint

`@app.get("/")` creates a GET endpoint. Visiting the root URL returns a message confirming that the API is running.

### Prediction endpoint

`@app.post("/predict")` creates an endpoint that accepts customer data.

1. `pd.DataFrame([customer])` converts the JSON customer into a one-row DataFrame.
2. `preprocessor.transform(df)` applies the fitted preprocessing steps. We use `transform`, not `fit_transform`, because we must not relearn preprocessing from incoming customers.
3. `torch.tensor(..., dtype=torch.float32)` converts processed features into a tensor the model can accept.
4. `torch.no_grad()` disables gradient calculation because we are predicting, not training.
5. `model(tensor)` produces a raw score called a logit.
6. `torch.sigmoid(logit)` converts the logit into a value between 0 and 1.
7. The code compares that probability against `0.5` to return `Yes` or `No`.

## 3. What does HTTP 200 mean?

HTTP 200 means the request succeeded. It does not mean the model is 100% accurate.

## 4. Training vs. inference

- Training learns model parameters from historical data.
- Inference uses the saved parameters to predict for new data.
- Our API performs inference; it does not retrain the model.

## 5. Interview questions

1. Why do we use FastAPI?
   We use FastAPI because it is a high-performance, modern Python web framework specifically optimized for building fast, reliable REST APIs and backend microservices

2. Why load a saved model instead of training on every request?
   its a redudant and time cosuming and in real time the data will be in million so we cant train on every request. so we load a trained, saved model which are trained using same params or hyperparams that can be used to predict new or unseen data

3. Why must the model architecture match the saved weights?
   model architecture is like a blueprint of a trained model it should match because
   tensor shape mismtach can throw error after crashing

4. Why use `transform()` instead of `fit_transform()`?
   on test data or new data we must use transform() which trasnforms the data based on the params it learnt during the training and makes the predcition to avoid data leakage.
   fit_transform() - is used during training

5. What is the difference between a logit and a probability?
   logit- raw output from nn laters can be of any numbers -infinity to +infinity
   probability - score will be 0 to 1 so we use activation function to convert logit into probability score for prediction.

6. Why use `model.eval()` and `torch.no_grad()`?
   model.eval() - for evaluating the model
   torch.no_grad() - disables gradient calculation because we are predicting, not training.

7. What does HTTP 200 indicate?
   its the indication of successful of HTTP request.

## 6. Important limitations

The current API is a learning project, not a production-ready service. A production version should validate input fields and types, define a request schema, handle invalid inputs, secure the endpoint, and monitor model performance. The 0.5 threshold is a chosen decision rule, not a universal rule.
