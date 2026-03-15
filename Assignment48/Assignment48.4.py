# Write a Python program to calculate the Euclidean distance between two points before and after applying feature scaling, and explain the difference in results.
import numpy as np
import math
from sklearn.preprocessing import StandardScaler

def EucDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)
    return Ans

def MarvellousKNeighborsClassifier():

    border = "-"*40

    data = [
        {'point':'A','X':1,'Y':2,'label':'Red'},
        {'point':'B','X':2,'Y':3,'label':'Red'},
        {'point':'C','X':3,'Y':1,'label':'Blue'},
        {'point':'D','X':5,'Y':6,'label':'Blue'}
    ]

    print(border)
    print("Training Data Set")
    print(border)

    for i in data:
        print(i)

    new_point = {'X':3,'Y':3}

    # Distance Before Scaling
    for d in data:
        d['distance'] = EucDistance(d,new_point)

    print(border)
    print("Distance Before Scaling")
    print(border)

    for d in data:
        print(d['point'],"->",d['distance'])

    # Feature Scaling
    dataset = np.array([[d['X'],d['Y']] for d in data])
    newdata = np.array([[new_point['X'],new_point['Y']]])

    scaler = StandardScaler()

    scaled_dataset = scaler.fit_transform(dataset)
    scaled_new = scaler.transform(newdata)

    print(border)
    print("Scaled Dataset")
    print(border)

    print(scaled_dataset)

    # Distance After Scaling
    print(border)
    print("Distance After Scaling")
    print(border)

    for i,d in enumerate(data):

        P1 = {'X':scaled_dataset[i][0],'Y':scaled_dataset[i][1]}
        P2 = {'X':scaled_new[0][0],'Y':scaled_new[0][1]}

        dist = EucDistance(P1,P2)

        print(d['point'],"->",dist)

def main():
    MarvellousKNeighborsClassifier()

if __name__ == "__main__":
    main()