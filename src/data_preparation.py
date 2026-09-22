import pandas as pd
from  sklearn.model_selection  import train_test_split



# load data
def load_data():
    df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    return df

# convert TotalCharges
def prepare_data(df):
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"],errors="coerce")
    # drop invalid rows
    df = df.dropna()

    # drop customerID
    df= df.drop(columns="customerID")

    # Separate features and target
    X= df.drop(columns="Churn")
    y= df["Churn"]

    # train, test and split
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.2, random_state=42)
    return X_train, X_test, y_train, y_test
