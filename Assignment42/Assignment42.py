import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():

    # Load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent variables : X",X)
    print("Values of Dependent variables : Y",Y)

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("X_mean is :",mean_x)
    print("Y_mean is :",mean_y)

    n = len(X)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x)**2)

    # slope
    m = numerator / denominator
    print("Slope of line is m :",m)

    # intercept
    c = mean_y - (m * mean_x)
    print("Y intercept of line ie C :",c)

    print("Regression Equation : Y =",m,"X +",c)

    # Prediction
    y_new = m*6 + c
    print("Predicted Y for X = 6 :",y_new)

    # Predicted Y values
    yp = []

    for i in range(n):
        y_pred = m*X[i] + c
        yp.append(y_pred)
        print("X =",X[i],"Predicted Y =",y_pred)

    # MSE
    mse = 0
    for i in range(n):
        mse = mse + (Y[i] - yp[i])**2

    mse = mse/n
    print("Mean Squared Error :",mse)

    # R2 Score
    ss_total = 0
    ss_res = 0

    for i in range(n):
        ss_total = ss_total + (Y[i] - mean_y)**2
        ss_res = ss_res + (Y[i] - yp[i])**2

    r2 = 1 - (ss_res/ss_total)
    print("R2 Score :",r2)

    # Visualisation
    x = np.linspace(1,6,n)
    y = c + m * x

    plt.plot(x,y,label="Regression line")
    plt.scatter(X,Y,label="Scatter plot")

    plt.xlabel("X : Independent Variables")
    plt.ylabel("Y : Dependent Variables")

    plt.legend()
    plt.show()


def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()