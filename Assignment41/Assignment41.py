import numpy as np
import math

# Euclidean Distance Function
def EucDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)
    return Ans


def MarvellousKNeighborsClassifier():

    border = "-"*40

    data = [
        {'point':'A','X':1,'Y':2,'label':'Red'},
        {'point':'B','X':2,'Y':3,'label':'Red'},
        {'point':'C','X':5,'Y':1,'label':'Blue'},
        {'point':'D','X':6,'Y':5,'label':'Blue'}
    ]

    print(border)
    print("Training Data Set")
    print(border)

    for i in data:
        print(i)

    print(border)

    # -------------------------
    # Accept user input
    # -------------------------

    x = int(input("Enter X coordinate : "))
    y = int(input("Enter Y coordinate : "))

    new_point = {'X':x,'Y':y}

    # Calculate distances
    for d in data:
        d['distance'] = EucDistance(d,new_point)

    print(border)
    print("Calculated Distances")
    print(border)

    for d in data:
        print(d)

    # Sort distances
    sorted_data = sorted(data,key=lambda item:item['distance'])

    print(border)
    print("Sorted Data")
    print(border)

    for d in sorted_data:
        print(d)

    # -------------------------
    # Prediction K=3
    # -------------------------

    k = 3
    nearest = sorted_data[:k]

    print(border)
    print("Nearest 3 Neighbors")
    print(border)

    for d in nearest:
        print(d)

    votes = {}

    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label,0) + 1

    predicted_class = max(votes,key=votes.get)

    print(border)
    print("Predicted Class :",predicted_class)
    print(border)


    # -------------------------
    # Prediction when K changes
    # -------------------------

    print("Prediction when K changes")
    print(border)

    K_values = [1,3,4]

    for k in K_values:

        votes = {}

        nearest = sorted_data[:k]

        for neighbour in nearest:
            label = neighbour['label']
            votes[label] = votes.get(label,0) + 1

        predicted_class = max(votes,key=votes.get)

        print("K =",k,"->",predicted_class)

    print(border)


def StudentPassFail():

    border = "-"*40

    student_data = [
        {'Hours':2,'Attendance':60,'Result':'Fail'},
        {'Hours':5,'Attendance':80,'Result':'Pass'},
        {'Hours':6,'Attendance':85,'Result':'Pass'},
        {'Hours':1,'Attendance':50,'Result':'Fail'}
    ]

    print(border)
    print("Student Dataset")
    print(border)

    for i in student_data:
        print(i)

    print(border)

    # Input
    study = int(input("Enter Study Hours : "))
    attendance = int(input("Enter Attendance : "))

    new_student = {'Hours':study,'Attendance':attendance}

    # Distance calculation
    for d in student_data:
        d['distance'] = math.sqrt((d['Hours']-study)**2 + (d['Attendance']-attendance)**2)

    sorted_data = sorted(student_data,key=lambda item:item['distance'])

    k = 3
    nearest = sorted_data[:k]

    votes = {}

    for n in nearest:
        label = n['Result']
        votes[label] = votes.get(label,0) + 1

    predicted = max(votes,key=votes.get)

    print(border)
    print("Predicted Result :",predicted)
    print(border)


def main():

    MarvellousKNeighborsClassifier()

    StudentPassFail()


if __name__ == "__main__":
    main()