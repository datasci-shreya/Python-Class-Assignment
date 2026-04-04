import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

#----------------------------------------------------------
def DisplayInfo(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

#----------------------------------------------------------
# 1. Load & Explore
#----------------------------------------------------------
def LoadAndExplore(DataPath):
    DisplayInfo("Step 1 : Load and Explore Dataset")

    df = pd.read_csv(DataPath)

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nShape:", df.shape)

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nBasic Statistics:")
    print(df.describe())

    # Class distribution
    print("\nClass Distribution:")
    print(df["y"].value_counts())

    return df

#----------------------------------------------------------
# 2. Preprocess
#----------------------------------------------------------
def PreprocessData(df):

    DisplayInfo("Step 2 : Data Preprocessing")

    # Convert target
    df["y"] = df["y"].map({"yes": 1, "no": 0})

    # Replace unknown
    df = df.replace("unknown", np.nan)

    # Fill missing
    for col in df.columns:
        if df[col].dtype == "object":
            df[col].fillna(df[col].mode()[0], inplace=True)
        else:
            df[col].fillna(df[col].median(), inplace=True)

    # One-hot encoding
    df = pd.get_dummies(df, drop_first=True)

    # Split X, Y
    X = df.drop("y", axis=1)
    Y = df["y"]

    # Scaling
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    return X, Y

#----------------------------------------------------------
# 3. Split Data
#----------------------------------------------------------
def SplitData(X, Y):

    DisplayInfo("Step 3 : Train-Test Split")

    return train_test_split(X, Y, test_size=0.2, random_state=42)

#----------------------------------------------------------
# 4 & 5. Train + Evaluate Models
#----------------------------------------------------------
def TrainAndEvaluate(X_train, X_test, Y_train, Y_test):

    DisplayInfo("Step 4 & 5 : Train and Evaluate Models")

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "KNN": KNeighborsClassifier(n_neighbors=5),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
    }

    results = {}

    for name, model in models.items():
        print("\n🔹", name)

        model.fit(X_train, Y_train)

        Y_pred = model.predict(X_test)
        Y_prob = model.predict_proba(X_test)[:, 1]

        acc = accuracy_score(Y_test, Y_pred)
        cm = confusion_matrix(Y_test, Y_pred)
        report = classification_report(Y_test, Y_pred)
        roc = roc_auc_score(Y_test, Y_prob)

        results[name] = (acc, roc)

        print("Accuracy:", acc)
        print("Confusion Matrix:\n", cm)
        print("Classification Report:\n", report)
        print("ROC AUC Score:", roc)

        # ROC Curve
        fpr, tpr, _ = roc_curve(Y_test, Y_prob)
        plt.plot(fpr, tpr, label=name)

    return results

#----------------------------------------------------------
# 6. Visualization
#----------------------------------------------------------
def PlotResults():

    DisplayInfo("Step 6 : ROC Curve")

    plt.plot([0, 1], [0, 1])  # baseline
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve Comparison")
    plt.legend()
    plt.show()

#----------------------------------------------------------
# Main Pipeline
#----------------------------------------------------------
def MarvellousBankFullPipeline(DataPath):

    df = LoadAndExplore(DataPath)

    X, Y = PreprocessData(df)

    X_train, X_test, Y_train, Y_test = SplitData(X, Y)

    results = TrainAndEvaluate(X_train, X_test, Y_train, Y_test)

    PlotResults()

    # Best Model
    best_model = max(results, key=lambda x: results[x][0])

    DisplayInfo("Final Result")

    print("Best Model:", best_model)
    print("Accuracy:", results[best_model][0])

#----------------------------------------------------------
def main():
    MarvellousBankFullPipeline("bank.csv")

#----------------------------------------------------------
if __name__ == "__main__":
    main()