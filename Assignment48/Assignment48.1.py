# Write a Python program that calculates the mean of a dataset using NumPy for the following values:
# [6, 7, 8, 9, 10, 11, 12]

import numpy as np

def CalculateMean():

    data = np.array([6,7,8,9,10,11,12])

    print("\nDataset : ")
    print(data)

    mean = np.mean(data)

    print("\nMean of Dataset : ")
    print(mean)

CalculateMean()