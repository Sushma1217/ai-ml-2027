# why are we learning this

We need to demonstrate that we can take a new customer record and get a prediction from the trained pipeline. This is the bridge between: ML experimentation → ML application

# Question and answers

1. Why shouldn't we manually apply StandardScaler to the new customer?
   because we must use the same scaling values and we might not sure which scalar we might applied during the model fit so its better to use the pipeline

2. Why shouldn't we manually perform one-hot encoding?
   because we must use the same same encoder and we are not sure which encoder we might applied during the model fit so its better to use the pipeline

3. What would happen if a new customer had a categorical value that wasn't present during training?
   if we would have given handle_unknow = ignore during the model fit or encoding then it will ignore and model will not crash.

4. Why is putting preprocessing + model inside one Pipeline useful when deploying an ML model?
   it will eliminate the manul task and rememberance of which sclaers or encoder used suring model fit, avoids data leakage and ensures cosistency.

google ans
Putting preprocessing and the model into a single Pipeline bundles all data transformations and predictions into one unified object. When deploying, you simply pass raw customer data to `pipeline.predict()`, preventing data leakage, ensuring transformation consistency, and avoiding broken prediction code in production.

5. What's the difference between:
   training data and new customer data
   training data- the data used during model fit or building which parameters or values that model has analysed and learnt.

new customer data: new unseen data which is fed into model to predict.
