import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

#----------------------------------------------------------------
# Load the dataset
#----------------------------------------------------------------

df = pd.read_csv("Breast_Cancer.csv")
print("Shape of dataset : ",df.shape)
print("First 5 Records ",df.head())

#----------------------------------------------------------------
# Seperate features and labels
#----------------------------------------------------------------

X = df.drop("target",axis=1)
Y = df["target"]

#----------------------------------------------------------------
# Split dataset for training and testing
#----------------------------------------------------------------

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
    )

#----------------------------------------------------------------
# Create Base model 
#----------------------------------------------------------------

base_model = DecisionTreeClassifier(random_state=42)

#----------------------------------------------------------------
# Create Bagging Model 
#----------------------------------------------------------------

bagging_model = BaggingClassifier(
    estimator=base_model,
    n_estimators=10,                                             # mostly this value become a odd
    random_state=42
)

#----------------------------------------------------------------
# Trained Bagging Model 
#----------------------------------------------------------------

bagging_model.fit(X_train,Y_train)

#----------------------------------------------------------------
# Test Bagging Model 
#----------------------------------------------------------------

Y_pred = bagging_model.predict(X_test)

#----------------------------------------------------------------
# Accuracy / Evaluate Bagging Model
#----------------------------------------------------------------

print("Bagging Accuracy : ",accuracy_score(Y_test,Y_pred))

#----------------------------------------------------------------
# Confusion Matrix
#----------------------------------------------------------------

cm = confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix \n",cm)













