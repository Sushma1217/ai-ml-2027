import pandas as pd
from  sklearn.model_selection  import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.model_selection import cross_val_score
from sklearn.metrics import make_scorer, precision_score, recall_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# load data
df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"],errors="coerce")

df = df.dropna()
df= df.drop(columns="customerID")

# identify and segregating the column
numerical_columns = ["MonthlyCharges","TotalCharges","tenure"]
categorical_columns = ["gender","Partner","Dependents","PhoneService","MultipleLines","InternetService","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport",
                       "StreamingTV","StreamingMovies","Contract","PaperlessBilling","PaymentMethod","SeniorCitizen"]

# Separate features and target
X= df.drop(columns="Churn")
y= df["Churn"]

# train, test and split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.2, random_state=42)

# Preprocessing
# create the transoformers
numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown="ignore",drop="first")

# Part 5 — Create the ColumnTransformer
preprocessor = ColumnTransformer(transformers=[("num",numeric_transformer,numerical_columns),("cat",categorical_transformer,categorical_columns)])

# decision tree
decison_tree = DecisionTreeClassifier(random_state=42)

# decison tree pipeline
dt_pipeline = Pipeline([("preprocessing",preprocessor),("model",decison_tree)])

# train
dt_pipeline.fit(X_train, y_train)

# Predict:
dt_pred  = dt_pipeline.predict(X_test)

# 🟢 Part 4 — Evaluate Calculate: Accuracy, Precision, Recall,F1
accuracy = accuracy_score(y_test, dt_pred)
dt_accuracy_percentage = round(accuracy*100,2)
print("dt_accuracy_percentage",dt_accuracy_percentage) #71.57

# traing accuracy 
dt_training_prediction = dt_pipeline.predict(X_train)
dt_training_accuracy = accuracy_score(y_train, dt_training_prediction)
dt_accuracy_percentage_train = round(accuracy*100,2)
print("dt_accuracy_percentage_train",dt_accuracy_percentage_train) #71.57

# precision, recall, f1
print("classification matrix",classification_report(y_test, dt_pred)) 
# for all positive calss
# precison-  .47
# recall - .51
# f1-  0.49


# 🟢🟢🟢🟢🟢 Part 5 — Random Forest
random_forest = RandomForestClassifier(n_estimators=100, random_state=42)

random_pipeline = Pipeline([("preprocessing",preprocessor),("model",random_forest)])


# training_model
random_pipeline.fit(X_train, y_train)

# predict
random_pred = random_pipeline.predict(X_test)

# Evaluting
random_accuracy = accuracy_score(y_test, random_pred)
random_accuracy_percentage = round(accuracy*100,2)
print("random_accuracy_percentage",random_accuracy_percentage) #71.57

# training_evaluation
random_pred_train = random_pipeline.predict(X_train)
random_accuracy_train =  accuracy_score(y_train, random_pred_train) 
random_accuracy_percentage_train = round(accuracy*100,2)
print("random_accuracy_percentage_train",random_accuracy_percentage_train) #71.57


# precision, recall, f1
print("classification_report of random", classification_report(y_test, random_pred))
# for all positive calss
# precison-  0.63 
# recall - 0.47
# f1-   0.54



