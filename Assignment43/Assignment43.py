import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def MarvellousPlayPredictor(Datapath):

    Border = "-" * 40

    #-----------------------------------------------
    # Step 1 : Load Dataset
    #-----------------------------------------------
    print(Border)
    print("Step 1 : Load Dataset")
    print(Border)

    df = pd.read_csv(Datapath)

    print("Shape of dataset : \n",df.shape)

    print("First few records of dataset :")
    print(df.head())

    print("Shape of dataset : \n",df.shape)


    #-----------------------------------------------
    # Step 2 : Check Missing Values
    #-----------------------------------------------
    print(Border)
    print("Step 2 : Check Missing Values")
    print(Border)

    print("Missing values count : ",df.isnull().sum())

    #-----------------------------------------------
    # Step 3  Encoding
    #-----------------------------------------------
    print(Border)
    print("Step 3 : Data Preparation")
    print(Border)

    le_weather = LabelEncoder()
    le_temp = LabelEncoder()
    le_play = LabelEncoder()

    df['Weather'] = le_weather.fit_transform(df['Weather'])
    df['Temperature'] = le_temp.fit_transform(df['Temperature'])
    df['Play'] = le_play.fit_transform(df['Play'])

    print("Encoded Dataset :")
    print(df.head())

    #-----------------------------------------------
    # Step 4 : Split Dataset into Independent and Dependent Variables
    #-----------------------------------------------
    print(Border)
    print("Step 4 : Split Dataset into Independent and Dependent Variables")
    print(Border)

    X = df[['Weather','Temperature']]
    Y = df['Play']

    print("Shape of X :",X.shape)
    print("Shape of Y :",Y.shape)

    #-----------------------------------------------
    # Step 5 : Train Test Split
    #-----------------------------------------------
    print(Border)
    print("Step 5 : Train Test Split")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    print("Shape of X_train :",X_train.shape)
    print("Shape of X_test :",X_test.shape)

    #-----------------------------------------------
    # Step 6 : create and trained the model 
    #-----------------------------------------------
    print(Border)
    print("Step 6 : create and trained the model ")
    print(Border)

    model = DecisionTreeClassifier()

    model.fit(X_train,Y_train)

    #-----------------------------------------------
    # Step 7 : Test the Model
    #-----------------------------------------------
    print(Border)
    print("Step 7 : Test Model")
    print(Border)

    y_pred = model.predict(X_test)

    print("Predictions :",y_pred)

    #-----------------------------------------------
    # Step 8 : Evaluate the model / Accuracy
    #-----------------------------------------------
    print(Border)
    print("Step 8 : Model Accuracy")
    print(Border)

    accuracy = accuracy_score(Y_test,y_pred)

    print("Accuracy :",accuracy*100,"%")

    #-----------------------------------------------
    # Step 9 : Compare the acutal and predicted values 
    #-----------------------------------------------
    print(Border)
    print("Step 9 : Actual vs Predicted")
    print(Border)

    Result = pd.DataFrame({'Actual':Y_test.values,
                           'Predicted':y_pred})

    print(Result.head())

def main():

    MarvellousPlayPredictor("MarvellousInfosystems_PlayPredictor.csv")


if __name__ == "__main__":
    main()