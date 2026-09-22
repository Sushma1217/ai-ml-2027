from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer


# identify and segregating the column
numerical_columns = ["MonthlyCharges","TotalCharges","tenure"]
categorical_columns = ["gender","Partner","Dependents","PhoneService","MultipleLines","InternetService","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport",
                       "StreamingTV","StreamingMovies","Contract","PaperlessBilling","PaymentMethod","SeniorCitizen"]

# create the transoformers
numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown="ignore",drop="first")

# Part 5 — Create and return the ColumnTransformer

def preprocessor():
    preprocessor = ColumnTransformer(transformers=[("num",numeric_transformer,numerical_columns),("cat",categorical_transformer,categorical_columns)])
    return preprocessor