import pandas as pd
import joblib

# create new customer
new_customer = pd.DataFrame({'gender': ['Female'],
    'SeniorCitizen': [0],
    'Partner': ['Yes'],
    'Dependents': ['No'],
    'tenure': [1],
    'PhoneService': ['No'],
    'MultipleLines': ['No phone service'],
    'InternetService': ['DSL'],
    'OnlineSecurity': ['No'],
    'OnlineBackup': ['Yes'],
    'DeviceProtection': ['No'],
    'TechSupport': ['No'],
    'StreamingTV': ['No'],
    'StreamingMovies': ['No'],
    'Contract': ['Month-to-month'],
    'PaperlessBilling': ['Yes'],
    'PaymentMethod': ['Electronic check'],
    'MonthlyCharges': [19.85],
    'TotalCharges': [30.85]})

model_pipleline =joblib.load("churn_pipeline.joblib") #we should not use prepare_model because re training the model again every time you run predict.py

# # predict()
model_pipleline.predict(new_customer)
# print("prediction for new customer",model_pipleline.predict(new_customer))

# predict_proba()
model_pipleline.predict_proba(new_customer)[:1]
print(" prediction probability for new customer",model_pipleline.predict_proba(new_customer))


