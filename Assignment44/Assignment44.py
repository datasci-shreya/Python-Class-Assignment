import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score


def MarvellousAdvertise(Datapath):
    Border = "-" *40
    #-----------------------------------------------
    # Load Data Set
    #-----------------------------------------------
    print(Border)
    print("Step : 1 :Load Dataset")
    print(Border)

    df = pd.read_csv(Datapath)

    print("Few Records from the datadset :")
    print(df.head())

    #-----------------------------------------------
    # Remove Unwanted Columns
    #-----------------------------------------------
    print(Border)
    print("Step 2 : Remove Unwanted Columns")
    print(Border)

    print("Shape of dataset before removal : \n",df.shape)


    if 'Unnamed: 0' in df.columns:
         df.drop(columns= ['Unnamed: 0'],inplace=True)

    print("Shape of dataset after removal : ",df.shape)

    print(Border)
    print("Clean dataset is : ")
    print(Border)

    print(df.head())


    #-----------------------------------------------
    # Check missing values
    #-----------------------------------------------
    print(Border)
    print("Step 3 :  Check missing values ")
    print(Border)

    print("Missing values count : ",df.isnull().sum())

    #-----------------------------------------------
    # Display Statistical Summary 
    #-----------------------------------------------
    print(Border)
    print("Step 4 :  Display Statistical Summary ")
    print(Border)

    print(df.describe())


    #-----------------------------------------------
    # Correlation Betwwen Columns
    #-----------------------------------------------
    print(Border)
    print("Step 5 : Correlation Betwwen Columns ")
    print(Border)

    print("Correlation  Matrix")


    print(df.corr())

    #-----------------------------------------------
    # Split Dataset into independent and dependent variables
    #-----------------------------------------------
    print(Border)
    print("Step 6 : Split Dataset into independent and dependent variables")
    print(Border)

    X = df[['TV','radio','newspaper']]
    Y = df['sales']

    print("Shape Independent Variables : ",X.shape)
    print("Shape Dependent Variables : ",Y.shape)


    #-----------------------------------------------
    # Split Dataset For training and testing 
    #-----------------------------------------------
    print(Border)
    print("Step 7 : Split Dataset For training and testing s")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("Shape of X_train : ",X_train.shape)
    print("Shape of X_test : ",X_test.shape)

    print("Shape of Y_train : ",Y_train.shape)
    print("Shape of Y_test : ",Y_test.shape)

    #-----------------------------------------------
    # Create  and trained the model 
    #-----------------------------------------------
    print(Border)
    print("Step 8 : Create and trained the model ")
    print(Border)

    model = LinearRegression()

    model.fit(X_train,Y_train)

    #-----------------------------------------------
    # Test the model 
    #-----------------------------------------------
    print(Border)
    print("Step 9 : Test the model ")
    print(Border)

    y_pred = model.predict(X_test)


    #-----------------------------------------------
    # Evaluate the model / Accuracy
    #-----------------------------------------------
    print(Border)
    print("Step 10 : Evaluate the model ")
    print(Border)

    MSE = mean_squared_error(Y_test,y_pred)
    RMSE = np.sqrt(MSE)
    r2 = r2_score(Y_test,y_pred)



    print("Mean Squared errror : ",MSE)
    print("Root Mean Squared errror : ",RMSE)
    print("R Square Value : ",r2)


    #-----------------------------------------------
    # Calculate Model Coefficient
    #-----------------------------------------------
    print(Border)
    print("Step 11 : Calculate Model Coefficient ")
    print(Border)

    for column, value in zip (X.columns,model.coef_):
        print(f"{column} : { value}")

    print("Intercept : ",model.intercept_)

    #-----------------------------------------------
    # Compare the acutal and predicted values 
    #-----------------------------------------------
    print(Border)
    print("Step 12 : Compare the acutal and predicted values  ")
    print(Border)

    Result = pd.DataFrame({'Actual sale ': Y_test.values,
                           'Predicted sale': y_pred
                          }) # create dataframe to display 
    
    print(Result.head())


    #-----------------------------------------------
    # Plot Actual vs Predicted
    #-----------------------------------------------
    print(Border)
    print("Step 13 :Plot Actual vs Predicted")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.scatter(Y_test,y_pred)
    plt.xlabel("Actual sales")
    plt.ylabel("Predicted Sales")
    plt.title("Actual Sales Vs Predicted Sales ")
    plt.grid(True)
    plt.show()



def main():
    MarvellousAdvertise("Advertising.csv")



   
 
if __name__ == "__main__":
    main()
