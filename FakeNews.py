import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

#----------------------------------------------------------
def DisplayInfo(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

#----------------------------------------------------------
# Part 1: Load & Prepare Data
#----------------------------------------------------------
def LoadData():

    DisplayInfo("Step 1: Load Dataset")

    fake = pd.read_csv("Fake.csv")
    true = pd.read_csv("True.csv")

    # Add labels
    fake["label"] = 0
    true["label"] = 1

    # Combine datasets
    df = pd.concat([fake, true], axis=0)

    print("Dataset Shape:", df.shape)

    return df

#----------------------------------------------------------
# Part 1: Cleaning
#----------------------------------------------------------
def CleanData(df):

    DisplayInfo("Step 2: Cleaning Data")

    # Use only text column
    df = df[["text", "label"]]

    # Drop null values
    df = df.dropna()

    print("After Cleaning Shape:", df.shape)

    return df

#----------------------------------------------------------
# Part 2: Feature Extraction (TF-IDF)
#----------------------------------------------------------
def FeatureExtraction(df):

    DisplayInfo("Step 3: TF-IDF Vectorization")

    X = df["text"]
    Y = df["label"]

    tfidf = TfidfVectorizer(max_features=5000)

    X = tfidf.fit_transform(X)

    return X, Y

#----------------------------------------------------------
# Part 3: Train Models
#----------------------------------------------------------
def TrainModels(X, Y):

    DisplayInfo("Step 4: Train Models")

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    # Individual Models
    lr = LogisticRegression(max_iter=1000)
    dt = DecisionTreeClassifier()

    # Voting Classifier
    voting_hard = VotingClassifier(
        estimators=[('lr', lr), ('dt', dt)],
        voting='hard'
    )

    voting_soft = VotingClassifier(
        estimators=[('lr', lr), ('dt', dt)],
        voting='soft'
    )

    models = {
        "Logistic Regression": lr,
        "Decision Tree": dt,
        "Hard Voting": voting_hard,
        "Soft Voting": voting_soft
    }

    for name, model in models.items():

        print("\nModel:", name)

        model.fit(X_train, Y_train)

        Y_pred = model.predict(X_test)

        acc = accuracy_score(Y_test, Y_pred)

        print("Accuracy:", acc)
        print("Confusion Matrix:\n", confusion_matrix(Y_test, Y_pred))
        print("Classification Report:\n", classification_report(Y_test, Y_pred))

#----------------------------------------------------------
# Main Function
#----------------------------------------------------------
def main():

    df = LoadData()

    df = CleanData(df)

    X, Y = FeatureExtraction(df)

    TrainModels(X, Y)

#----------------------------------------------------------
if __name__ == "__main__":
    main()