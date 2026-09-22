from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from src.data_preparation import prepare_data,load_data
from src.preprocessing import preprocessor


def pipeline_building():
    # Unpack all four returned values directly into four variables
    df = load_data()
    X_train, X_test, y_train, y_test = prepare_data(df)
    processor = preprocessor()
    model = LogisticRegression(C=0.1, max_iter=1000, class_weight="balanced") 
    #c value we got it from grid serach - refer hyperparameters
    # Part 3 — Put preprocessing + model together ⭐
    model_pipeline = Pipeline([("processing",processor),("model",model)])

    # Part 4 — Train the model
    model_pipeline.fit(X_train,y_train)

    # Part 5 — Make predictions
    # y_pred = model_pipeline.predict(X_test)
    return model_pipeline
   