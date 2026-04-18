import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error,r2_score

#----------------------------------------------------------------
# Load the dataset
#----------------------------------------------------------------

df = pd.read_csv("California_housing.csv")
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

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#----------------------------------------------------------------
# Create Base model 
#----------------------------------------------------------------

base_model = DecisionTreeRegressor(random_state=42)

#----------------------------------------------------------------
# Create Bagging Model 
#----------------------------------------------------------------

bagging_model = BaggingRegressor(
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
print("Mean Squared error : ",mean_squared_error(Y_test,Y_pred ))

print("R squarre : ",r2_score(Y_test,Y_pred))

















