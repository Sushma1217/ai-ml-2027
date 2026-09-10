Why are we learning this?
We don't want to choose model settings randomly. Hyperparameter tuning lets us systematically search for settings that improve model performance while using cross-validation to avoid relying on one lucky split.

Pipeline
↓
Model
↓
Cross-validation
↓
Hyperparameters
↓
Tuning
↓
Better model

What is a hyperparameter?
the specification which we give for model training.
google
Hyperparameters are external configuration settings that you choose before training a machine learning model to control how the learning process work

What is C?
google ans:
it is the penalty setting for making mistakes.
machine learning model is allowed to fit the training data perfectly without any penalties, it will cheat. It will memorize every single quirk, noise, and rare exception in your dataset

My prediction before tuning

What is GridSearchCV?
it is a tool used to find the best settings(hyperparams) for a ml model by testing every single combination in a user-defined grid

What does model\_\_C mean?

Best C: {'model\_\_C': 0.1}

Best CV F1: 0.632

Before vs After

Why shouldn't we tune on test data?
because then the model can be unbiased and works by learning from the test data

Interview questions
What is hyperparameter tuning?
it is the external configuration setting that we do suring training to control how model learning process work.

What is the difference between a parameter and hyperparameter?
parameters is something the model learns during the training. ex std, mean

hyperparameters is the external setting or specification we provide during training to control model work.
ex: class weight, max iteration

What is C in Logistic Regression?
it is the penalty that we give for model means the rules we keep for model to not to overperform or underperform

What confused me
C, the flow of ml model, that day we added pipeline which was ok for understanding now we are just adding one by one like cv, hyperparams and finding accuracy, precision etc.. what are we doing exactly??? whats the flow???

What is GridSearchCV?
it is the tool to find the best seeting or congig(hyperparams) for ml model by testing every single combo in the grid.

Why do we combine GridSearchCV with cross-validation?
to prevent overfitting to a single validation split and to ensure the selected hyperparams are reliable or works better for unseen data.

What does model\_\_C mean?
a tuning parameters

Why shouldn't we tune using the test set?
because model may become lazy and may not works better for unseen data because there is a chances of learning params duing fit

What is best*params*?
an attribute that returns optimal combo of hyperparams found during an automated search.

What is best*estimator*?
returns model instance that achieved the highest score during training.

Why can CV performance improve while test performance doesn't?
may be because of unseen data??
google ans:
primarily due to data leakage, distribution shift, or overfitting to the validation structure.

What became clearer

AI/ML connection
