# Write a Python program that calculates the variance and standard deviation of the dataset.
# [6, 7, 8, 9, 10, 11, 12]
import numpy as np

data = np.array([6,7,8,9,10,11,12])

Variance = np.var(data)
StandardDeviation = np.std(data)

print("Dataset :",data)
print("Variance :",Variance)
print("Standard Deviation :",StandardDeviation)