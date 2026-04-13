import pandas as pd
import numpy as np 

import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

# ----------------------------------------------------------
# This is K and R style for Dennia Rechie
# Function Name : DiabeticLogistic
# Description   : This is main pipeline controller
#                 It loads the dataset , show the raw data
#                 It preprocess the dataset and train the model
# Parameter     : Data path of dataset file
# Return        : None
# Date          : 13/04/2026
# Author        : Shreya Pramodkumar Borate
# ----------------------------------------------------------

#--------------------------------------------------------
# Function name : LoadPreservedModel
# Description   : It is used to load preserved model
# Parameters    : filename
# Return        : Model
# Date          : 13/04/2026
# Author        : Shreya Pramodkumar Borate
#--------------------------------------------------------

def LoadPreservedModel(filename):
    loaded_model = joblib.load(filename)

    print("Model Sucessfully Loaded")

    return loaded_model



#----------------------------------------------------------
# Function  Name : PreserveModel
# Description    : It is used to preserve model on secondary
# Parameters     : model,filename
# Return         : None
# Date           : 13/04/2026
# Author         : Shreya Pramodkumar Borate
#----------------------------------------------------------
# Presserve the model

def PreserveModel(model,filename):
        joblib.dump(model,filename)
        print("Model Preserve Sucessfully with Name : ",filename)

# ----------------------------------------------------------
# Function Name : TrainDiabeticModel 
# Description   : It Does split X,Y training data , Testing data
# Parameter     : df
#                 title (str)
# Return        : None
# Data          : 13/04/2026
# Author        : Shreya Pramodkumar Borate
# -----------------------------------------------------------

def TrainDiabeticModel(df):

    # split features and labels
    X = df.drop("Outcome",axis = 1)
    Y = df["Outcome"]

    print("\n Features : ")
    print(X.head())

    print("\n Lables : ")
    print(Y.head())

    print("\n Shape of X : ",X.shape)
    print("\n Shape of Y : ",Y.shape)

    X_train , X_test , Y_train , Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("X_train Shape ",X_train.shape)
    print("X_test Shape ",X_test.shape)
    print("Y_train Shape ",Y_train.shape)
    print("Y_test Shape ",Y_test.shape)

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train,Y_train)

    print("\n Model Trained Sucessfully")

    print("\n Intercept of Model : ")
    print(model.intercept_)


    # This shows how important each feature is for the model (it displays the weight or coefficient of the feature)
    print("\n Coefficient of model")

    for features,coefficient in zip (X.columns,model.coef_[0]):
        print(features , " : ", coefficient)

    PreserveModel(model,"Diabetic.pkl")

    loaded__model = LoadPreservedModel("Diabetic.pkl")

    Y_pred = loaded__model.predict(X_test)

    accuracy = accuracy_score(Y_pred,Y_test)

    print("Accuracy is : ",accuracy)

    cm = confusion_matrix(Y_pred,Y_test)
    print("Confusion Matrix is : ")
    print(cm)








   




# ----------------------------------------------------------
# Function Name : DisplayInfo 
# Description   : This Displays fromated title 
# Parameter     : title (str)
# Return        : None
# Data          : 13/04/2026
# Author        : Shreya Pramodkumar Borate
# -----------------------------------------------------------

def DisplayInfo(title):
    print("\n" + "=" * 70)
    print(title)
    print("="*70)


# ----------------------------------------------------------
# Function Name : Showdata
# Description   : It shows basic information about dataset
# Parameter     : df , message
#                 df -> pandas dataframe object message
#                 message -> Heading text to display
# Return        : None
# Data          : 13/04/2026
# Author        : Shreya Pramodkumar Borate
# ----------------------------------------------------------- 

def ShowData(df,message):

    DisplayInfo("\n First 5 rows of dataset")
    print(df.head())

    print("\n Shape of dataset")
    print(df.shape)

    print("\n Column Names : ")
    print(df.columns.tolist())

    print("\n Missing Values in each column ")
    print(df.isnull().sum())



# -----------------------------------------------------------
# Function Name : CleanDeabeticData
# Decsription   : It does preprocessing 
#                 It removes unncessary columns
#                 It handles missing values
#                 It convert text data to numeric format
#                 It does encoding to categorical columns (if necessary)
# Prameters     : df
#                 df -> pandas dataframe
#                 df -> Clean pandas dataframe
# Return        : None
# Date          : 13/04/2026
# ----------------------------------------------------------

def CleanDiabeticData(df):

    DisplayInfo("Step 2 : Original Data")
    print(df.head())
    
    # Remove Unecwessary Columns
    #drop_columns = ["SkinThickness"]
    #existing_columns = [col for col in drop_columns if col in df.columns]
    
    #print("\n Columns to be dropped : ")
    #print(existing_columns)
       
    # Drop the unwanted columns
    #df = df.drop(columns = existing_columns)
    #DisplayInfo("Step 2 : Data After the column removal")
    #print(df.head())
    
    # Handle Glucose Column

    if "Glucose" in df.columns:
        print("\n Glucose Column Before Preprocessing")
        print(df["Glucose"].head(10))
        
        # coerce -> Invalid value gets converted as NaN
        df["Glucose"] = pd.to_numeric(df["Glucose"],errors="coerce")

        df["Glucose"] = df["Glucose"].replace(0, np.nan)

        glucose_median = df["Glucose"].median()
        print("\n Median of Glucose Column is : ",glucose_median)

        # Replace Missing Values with Median
        df["Glucose"] = df["Glucose"].fillna(glucose_median)

        print("Glucose Column After Preprocessing : ")
        print(df["Glucose"].head(10))
    
    # Handle Pregnancies Column
    if "Pregnancies" in df.columns:
        print("\nPregnancies Column Before Preprocessing")
        print(df["Pregnancies"].head(10))

        # coerce -> Invalid value gets converted as NaN
        df["Pregnancies"] = pd.to_numeric(df["Pregnancies"], errors="coerce")

        # Check missing values
        print("Missing values:", df["Pregnancies"].isnull().sum())

        pregnancies_median = df["Pregnancies"].median()

        # Replace Missing Values with Median
        df["Pregnancies"] = df["Pregnancies"].fillna(pregnancies_median)

        print("Pregnancies Column After Preprocessing")
        print(df["Pregnancies"].head(10))

    # Handle BloodPressure Column

    if "BloodPressure" in df.columns:
        print("\n BloodPressure Column Before Preprocessing")
        print(df["BloodPressure"].head(10))
        
        # coerce -> Invalid value gets converted as NaN
        df["BloodPressure"] = pd.to_numeric(df["BloodPressure"],errors="coerce")

        df["BloodPressure"] = df["BloodPressure"].replace(0,np.nan)

        bloodpressure_median = df["BloodPressure"].median()
        print("\n Blood Pressure of Column is : ",bloodpressure_median)

        # Replace Missing Values with Median
        df["BloodPressure"] = df["BloodPressure"].fillna(bloodpressure_median)

        print("\n Blood Pressure Column After Preprocessing")
        print(df["BloodPressure"].head(10))

    # Handle SkinThickness Column
    if "SkinThickness" in df.columns:
        print("\n SkinThickness Column before preprocessing")
        print(df["SkinThickness"].head(10))
        
        # coerce -> Invalid value gets converted as NaN
        df["SkinThickness"] = pd.to_numeric(df["SkinThickness"],errors="coerce")

        df["SkinThickness"] = df["SkinThickness"].replace(0,np.nan)

        skinthickness_median = df["SkinThickness"].median()
        print("\nSkinthickness of Column is : ",skinthickness_median)
        
        df["SkinThickness"] = df["SkinThickness"].fillna(skinthickness_median)

        print("\n SkinThickness Column after preprocessing")
        print(df["SkinThickness"].head(10))

    # Handle BMI Column

    if "BMI" in df.columns:
        print("\n BMI Column before preprocessing")
        print(df["BMI"].head(10))

        # coerce -> Invalid value gets converted as NaN 
        df["BMI"] = pd.to_numeric(df["BMI"],errors="coerce")

        df["BMI"] = df["BMI"].replace(0,np.nan)

        bmi_median = df["BMI"].median()
        print("\n BMI of Column is : ",bmi_median)

        df["BMI"] = df["BMI"].fillna(bmi_median)

        print("\n BMI Column After Preprocessing")
        print(df["BMI"].head(10))

    # Handle insulin Column 

    if "Insulin" in df.columns:
        print("\n Insulin Column Before Preprocessing")
        print(df["Insulin"].head(10))

        # coerce -> Invalid value gets converted as NaN 
        df["Insulin"] = pd.to_numeric(df["Insulin"],errors="coerce")

        df["Insulin"] = df["Insulin"].replace(0,np.nan)

        insulin_median = df["Insulin"].median()
        print("\n Insulin of Column is : ",insulin_median)
        
        df["Insulin"] = df["Insulin"].fillna(insulin_median)

        print("\n Insulic Column After Preprosessing")
        print(df["Insulin"].head(10))
    
    # Handle Age Column 
    if "Age" in df.columns:
        print("\nAge Column before felling missing values")
        print(df["Age"].head(10))

        # coerce -> Invalid value gets converted as NaN
        df["Age"] = pd.to_numeric(df["Age"],errors="coerce") # For Invalid Value

        df["Age"] = df["Age"].replace(0, np.nan)

        age_median = df["Age"].median()

        # Replace Missing values With Median
        df["Age"] = df["Age"].fillna(age_median)

        print("Age Column After Preprocessing :")
        print(df["Age"].head(10))

    DisplayInfo(" Data After Preprocessing")
    print(df.head())

    print("\n Missing values after preprocessing")
    print(df.isnull().sum())  

    return df



# -----------------------------------------------------------
# Function Name : DiabeticLogistic
# Description   : This is main pipeline controller
#                 It loads the dataset , show the raw data
#                 It preprocess the dataset and train the model
# Parameter     : Data path of dataset file
# Return        : None
# Date          : 13/04/2026
# Author        : Shreya Pramodkumar Borate
# ----------------------------------------------------------

def DiabeticLogistic(Datapath):
    DisplayInfo(" Step 1 = Loading the Dataset")
    df = pd.read_csv(Datapath)

    ShowData(df,"Initial Dataset")

    df = CleanDiabeticData(df)

    TrainDiabeticModel(df)



# ----------------------------------------------------------
# Function Name : main
# Description   : None
# Parameter     : None
# Return        : None
# Date          : 13/04/2026
# ----------------------------------------------------------

def main():
    DiabeticLogistic("diabetes.csv")


if __name__ == "__main__":
    main()