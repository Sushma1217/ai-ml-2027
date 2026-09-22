import joblib
from model import pipeline_building

# 5. Save the ENTIRE Pipeline to Disk
joblib.dump(pipeline_building,"churn_pipeline.joblib")
print("Model pipeline successfully trained and saved to churn_pipeline.joblib!")
