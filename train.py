import joblib
from src.model import pipeline_building

trained_pipeline = pipeline_building()

# 5. Save the ENTIRE Pipeline to Disk
joblib.dump(trained_pipeline,"churn_pipeline.joblib")
print("Model pipeline successfully trained and saved to churn_pipeline.joblib!")
