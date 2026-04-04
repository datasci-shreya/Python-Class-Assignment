import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

#----------------------------------------------------------
# Function : DisplayInfo
#----------------------------------------------------------
def DisplayInfo(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

#----------------------------------------------------------
# Function : ShowData
#----------------------------------------------------------
def ShowData(df, message):
    DisplayInfo(message)

    print("\nFirst 5 rows of dataset")
    print(df.head())

    print("\nShape of dataset")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nMissing values in each column")
    print(df.isnull().sum())

#----------------------------------------------------------
# Function : PreserveModel
#----------------------------------------------------------
def PreserveModel(model, filename):
    joblib.dump(model, filename)
    print("\nModel saved as:", filename)

#----------------------------------------------------------
# Function : LoadPreserveModel
#----------------------------------------------------------
def LoadPreserveModel(filename):
    model = joblib.load(filename)
    print("\nModel loaded successfully")
    return model

#----------------------------------------------------------
# Function : CleanDiabetesData
#----------------------------------------------------------
def CleanDiabetesData(df):
    DisplayInfo("Step 2 : Data Cleaning")

    print("\nBefore Cleaning:")
    print(df.head())

    # Columns where 0 means missing
    cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

    for col in cols:
        df[col] = df[col].replace(0, np.nan)
        df[col] = df[col].fillna(df[col].median())

    print("\nAfter Cleaning:")
    print(df.head())

    print("\nMissing values after cleaning:")
    print(df.isnull().sum())

    return df

#----------------------------------------------------------
# Function : TrainDiabetesModel
#----------------------------------------------------------
def TrainDiabetesModel(df):

    # Split features and target
    X = df.drop("Outcome", axis=1)
    Y = df["Outcome"]

    print("\nFeatures:")
    print(X.head())

    print("\nLabels:")
    print(Y.head())

    print("\nShape of X:", X.shape)
    print("Shape of Y:", Y.shape)

    # Train-Test Split
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    print("\nTraining Shape:", X_train.shape)
    print("Testing Shape:", X_test.shape)

    # Model
    model = LogisticRegression(max_iter=1000)

    model.fit(X_train, Y_train)

    print("\nModel trained successfully")

    # Coefficients
    print("\nIntercept:", model.intercept_)

    print("\nCoefficients:")
    for feature, coef in zip(X.columns, model.coef_[0]):
        print(feature, ":", coef)

    # Save Model
    PreserveModel(model, "DiabetesModel.pkl")

    # Load Model
    loaded_model = LoadPreserveModel("DiabetesModel.pkl")

    # Prediction
    Y_pred = loaded_model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(Y_test, Y_pred)
    print("\nAccuracy:", accuracy)

    # Confusion Matrix
    cm = confusion_matrix(Y_test, Y_pred)
    print("\nConfusion Matrix:")
    print(cm)

#----------------------------------------------------------
# Function : Main Pipeline
#----------------------------------------------------------
def MarvellousDiabetesLogistic(DataPath):

    DisplayInfo("Step 1 : Loading Dataset")

    df = pd.read_csv(DataPath)

    ShowData(df, "Initial Dataset")

    df = CleanDiabetesData(df)

    TrainDiabetesModel(df)

#----------------------------------------------------------
# Main Function
#----------------------------------------------------------
def main():
    MarvellousDiabetesLogistic("diabetes.csv")

#----------------------------------------------------------
if __name__ == "__main__":
    main()