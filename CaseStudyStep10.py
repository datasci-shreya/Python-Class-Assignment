import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier,plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*40

###########################################################################################
# Step 1 : Load the Dataset
###########################################################################################
print(Border)

print("Step 1 : Load the Dataset ")

print(Border)

DatasetPath = "iris.csv"

df = pd.read_csv(DatasetPath)

print("Dataset get loaded sucessfully..")

print("Initial enteries from Dataset :")

print(df.head())

###########################################################################################
# Step 2 : Data Analysis (EDA)
###########################################################################################
print(Border)

print("Step 2 : Data Analysis ")

print(Border)

print("Shape of Dataset : ",df.shape)

print("Colunm Names : ",list(df.columns))

print("Missing Values (Per Column )")

print(df.isnull().sum()) #empty 

print("Class Distribution (Species Count)")

print(df["species"].value_counts())

print("Statistical Report of dataset")

print(df.describe())

###########################################################################################
# Step 3 : Decide Independent and dependent variables Identify the features and lables
###########################################################################################
print(Border)

print("Step 3 : Decide Independent and dependent variables ")

print(Border)

# X : Independent variables/features
# Y : Dependent Variables/lables

features_calls = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]
X = df[features_calls]
Y = df["species"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)

###########################################################################################
# Step 4 : Visualisation of dataset
###########################################################################################
print(Border)

print("Step 4 :  Visualisation of dataset ")

print(Border)

# scatter plot
plt.figure(figsize=(7,5))

for sp in df["species"].unique(): #Unique species
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label = sp)

plt.title("Iris : Petal length vs Petal Width")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid(True) #
plt.show()

###########################################################################################
# Step 5 : Split the dataset for traning and testing
###########################################################################################
print(Border)

print("Step 5 : Split the dataset for traning and testing ")

print(Border)

#Total dataset : 150,5
#X : 150,4
#Y: 150 ,1
# test size = 20%
# train size = 80%

#Shuffle
X_train , X_test , Y_train , Y_test = train_test_split(
    X,
    Y,
    test_size=0.5,
    random_state=42 #parameter #shuffle the data 
)
print("Data spliting activity done")

print("X - Independent : ",X.shape) #(150,4)
print("Y - Dependent : ", Y.shape)  #(150,)

print("X_train :",X_train.shape) #(120,4)
print("X_test :",X_test.shape)   #(30,4)

print("Y_train :",Y_train.shape) #(120,)
print("Y_test :",Y_test.shape)   #(30,)

###########################################################################################
# Step 6 : Build the model
###########################################################################################
print(Border)

print("Step 6: Build the model ")

print(Border)

print("We are going to use decision tree classifier")

model = DecisionTreeClassifier(
    criterion ="gini",
    max_depth=3, #3 value for better accuracy 
    random_state=42
)

print("Model Sucessfully Created : ",model)

###########################################################################################
# Step 7 : Train the model
###########################################################################################
print(Border)

print("Step 7 : Train the model ")

print(Border)

model.fit(X_train,Y_train)

print("Model Traning Completed ")

###########################################################################################
# Step 8 : Evaluate/Test the model
###########################################################################################
print(Border)

print("Step 8 : Evaluate/Test the model ")

print(Border)

Y_pred = model.predict(X_test)

print("Model Evaluation (testing) Complete ")

print(Y_pred.shape)

print("Expected Answer :")
print(Y_test)

print("Predicted Answer :")
print(Y_pred)

###########################################################################################
# Step 9 : Evaluate the model performance
###########################################################################################
print(Border)

print("Step 8 : Evaluate the model performance ")

print(Border)

acuuracy = accuracy_score(Y_test,Y_pred)

print("Accuracy of model is : ",acuuracy * 100)

cm = confusion_matrix(Y_test,Y_pred)

print("Confusion Matrix :")
print(cm)

###########################################################################################
# Step 10 : plot confusion matrix
###########################################################################################
print(Border)

print("Step 10 : plot confusion matrix ")

print(Border)


data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)
data.plot()
plt.title("Confusion Matrix Of Iris Dataset")
plt.show() 