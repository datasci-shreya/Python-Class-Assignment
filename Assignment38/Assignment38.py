import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import(
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)
# FinalResult : Target Variable 
# 1 - Pass
# 0 - Fail

# Dataset Loading

print("Step 1 : Load the Data")
Datasetpath = "student_performance_ml.csv"
df = pd.read_csv(Datasetpath)
print("Dataset get loaded sucessfully")

# Data Analysis

print("Initial Entries from Dataset (First 5 records)")
print(df.head())

print("Last 5 records")
print(df.tail())

print("Total number of rows and columns : ",df.shape)

print("List of column names : ",list(df.columns))

print("Data types of each column : ",df.dtypes)

print("Total number of students in Dataset : ",len(df))

print("Count of Passed Students : ",df[df["FinalResult"] == 1].shape[0])

print("Count of Failed Students : ",df[df["FinalResult"] == 0].shape[0])

print("Average StudyHours :",df["StudyHours"].mean())

print("Average Attendence : ",df["Attendance"].mean())

print("Maximum PreviosScore : ",df["PreviousScore"].max())

print("Minimum SleepHours : ",df["SleepHours"].min())

print("Distribution Of FinalResult")
print(df["FinalResult"].value_counts())

print("Calculate the persentage of Pass Students and Fail Studentas")
print(df["FinalResult"].value_counts(normalize=True) * 100)

# Visualization

plt.figure(figsize=(7,5))
plt.hist(df["StudyHours"])
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.title("Histogram of Study Hours")
plt.show()

pass_students = df[df["FinalResult"] == 1]
fail_students = df[df["FinalResult"] == 0]
plt.scatter(pass_students["StudyHours"], pass_students["PreviousScore"], label="Pass")
plt.scatter(fail_students["StudyHours"], fail_students["PreviousScore"], label="Fail")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("StudyHours vs PreviousScore")
plt.legend()
plt.show()

plt.boxplot(df["Attendance"])
plt.title("Boxplot of Attendance")
plt.ylabel("Attendance")
plt.show()

plt.boxplot([df[df["FinalResult"] == 0]["AssignmentsCompleted"],
             df[df["FinalResult"] == 1]["AssignmentsCompleted"]],
            labels=["Fail", "Pass"])

plt.xlabel("Final Result")
plt.ylabel("Assignments Completed")
plt.title("AssignmentsCompleted vs FinalResult")
plt.show()

plt.boxplot([df[df["FinalResult"] == 0]["SleepHours"],
             df[df["FinalResult"] == 1]["SleepHours"]],
            labels=["Fail", "Pass"])

plt.xlabel("Final Result")
plt.ylabel("Sleep Hours")
plt.title("SleepHours vs FinalResult")
plt.show()


