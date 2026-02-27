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


# Assignment No : 39 
# Decide independent and dependent varibales

features_call = [
    "StudyHours",
	"Attendance",
	"PreviousScore",
	"AssignmentsCompleted",
	"SleepHours"
]
X = df[features_call]
Y = df["FinalResult"]
print("X shape :",X.shape)
print("Y shape : ",Y.shape)

# Train-test split

X_train , X_test , Y_train , Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)
print("Data Spliting Activity Done")

# Build the model 

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)
print("Model Sucessfully Created : ",model)

# Model training

print("Train the model")
model.fit(X_train,Y_train)
print("Model Training Completed")

# Prediction

print("Evaluate the model")
y_pred = model.predict(X_test)
print("Model Testing Completed")

print("Expected Answer")
print(Y_test)

print("Predicted Answer")
print(y_pred)

# Accuracy calculation

print("Evaluate the model accuracy")
accuracy = accuracy_score(Y_test,y_pred)
print("Accuracy of Model is : ",accuracy * 100)

train_accuracy = accuracy_score(Y_train, model.predict(X_train))
test_accuracy = accuracy_score(Y_test, y_pred)

print("Training Accuracy:", train_accuracy * 100)
print("Testing Accuracy:", test_accuracy * 100)

# Confusion matrix generation

cm = confusion_matrix(Y_test,y_pred)
print("Confusion Matrix")
print(cm)

# Compare testing accuracies

for depth in [1, 3, None]:
    dt = DecisionTreeClassifier(
        criterion="gini",
        max_depth=depth,
        random_state=42
    )
    dt.fit(X_train, Y_train)
    acc = accuracy_score(Y_test, dt.predict(X_test))
    print("Max Depth:", depth, "Testing Accuracy:", acc * 100, "%")

# Prediction for new student

new_student = pd.DataFrame(
    [[6, 85, 66, 7, 7]],
    columns=[
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]
)

result = model.predict(new_student)
if result[0] == 1:
    print("Student will PASS")
else:
    print("Student will FAIL")

# Final Conclusion



#Assignment No 40:

importance = model.feature_importances_

for f , imp in zip(features_call,importance):
    print(f , " : " , imp)


# Decide independent and dependent varibales
X = df.drop(columns=["SleepHours","FinalResult"])
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y, 
    test_size=0.2, 
    random_state=42
)
print("Data Spliting Activity Done")


# Build the model 
model2 = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

print("Model Sucessfully Created : ",model2)

# Model training

print("Trained the model")
model2.fit(X_train, Y_train)
print("Model Training Completed")

# Prediction

print("Evaluate the model")
y_pred1 = model2.predict(X_test)
print("Model Testing Completed")

# Calculate Accuracy

print("Evaluate the model accuracy")
accuracy2 = accuracy_score(Y_test,y_pred1)
print("Accuracy of Model without SleepHours : ",accuracy2 * 100)

# Decide independent and dependent varibales
X = df[["StudyHours", "Attendance"]]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)
print("Data Spliting Activity Done")


# Build the model 

print("Study Hourse and Attendance model")
model3 = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

print("Model Sucessfully Created : ",model3)

# Model training

print("Trained the model")
model3.fit(X_train, Y_train)
print("Model Training Completed")

# Model testing (Prediction)

print("Evaluate the model")
y_pred2 = model3.predict(X_test)
print("Model Testing Completed")

# Calculate Accuracy
print("Evaluate the model accuracy")
accuracy3 = accuracy_score(Y_test,y_pred2)
print("Accuracy of Model with two features StudyHours,Attendance : ",accuracy3 * 100)

# Add new dataframe with 5 students
print("New DataFrame Create")
new_student1 = pd.DataFrame(
    [
        [5, 80, 60, 6, 7],
        [8, 90, 85, 9, 8],
        [3, 65, 50, 4, 6],
        [6, 75, 70, 7, 7],
        [2, 55, 40, 3, 5]
    ],
    columns=["StudyHours",
             "Attendance",
             "PreviousScore",
             "AssignmentsCompleted",
             "SleepHours"
             ]
)
# Prediction
predictions = model.predict(new_student1)
new_student1["Prediction"] = predictions
print(new_student1)
print("New DataFrame Created 5 new Students")

# Calculate accuracy manually
print("Accuracy Without using accuracy_score(Manually)")
manual_accuracy= sum(Y_test.values == y_pred2)
Accuracy4 = manual_accuracy / len(Y_test)
print("Manual Accuracy:", Accuracy4 * 100)

# Misclassified students
print("Misclassified Students")
misclassifide = X_test[Y_test != y_pred2]
print(misclassifide)
print("Total Misclassified students :", misclassifide.shape[0])

# Compare testing with random_state [0,10,42]
print("Compare testing accuracy ")
for rs in [0, 10, 42]:
    model_rs = DecisionTreeClassifier(
        random_state=rs
    )
    model_rs.fit(X_train, Y_train)
    accuracy5 = accuracy_score(Y_test, model_rs.predict(X_test))
    print("Random State:", rs, "Accuracy:", accuracy5 * 100)

# Visualisation
print("Decision Tree Visualisation")
plt.figure(figsize=(7,5))
plot_tree(model,
         feature_names=features_call,
         class_names=["Fail","Pass"],
         filled=True
        )
plt.show()

print("Performance Feature")
df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

# Decide independent and dependent varibales
X = df[features_call + ["PerformanceIndex"]]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, 
    Y, 
    test_size=0.2,
    random_state=42
)
print("Data Spliting Activity Done")


# Build the model 

print("Performance Feature model create")
model4 = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
    )

print("Model Sucessfully Created : ",model4)

# Model training

print("Trained the model")
model4.fit(X_train, Y_train)
print("Model Training Completed")

# Model testing (prediction)

print("Evaluate the model")
y_pred3 = model4.predict(X_test)
print("Model Testing Completed")

# Calculate accuracy

print("Evaluate the model accuracy")
accuracy7 = accuracy_score(Y_test,y_pred3)
print("Accuracy of Model with PerformanceIndex : ",accuracy7 * 100)


# Build the model 
# Trained the model with max_depth = None
print("Trained the model with max_depth = None")
model5 = DecisionTreeClassifier(
    criterion="gini",
    max_depth=None, 
    random_state=42
    )

print("Model Sucessfully Created : ",model5)

# Model training
print("Trained the model")
model5.fit(X_train, Y_train)
print("Model Training Completed")

# Training Accuracy
train_pred = model5.predict(X_train)
training_accuracy = accuracy_score(Y_train, train_pred)
print("Training Accuracy of Model :", train_accuracy * 100)

# Testing Accuracy
test_pred = model5.predict(X_test)
testing_accuracy = accuracy_score(Y_test, test_pred)
print("Testing Accuracy of Model :", test_accuracy * 100)
