import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    #----------------------------------------------
    # Step 1 : Load the dataset
    #----------------------------------------------
    print("Step 1 : Load the dataset")
    df = pd.read_csv("Mall_Customers.csv")

    print("First few records : ")
    print(df.head())

    print("Shape of dataset : ")
    print(df.shape)

    print("Missing Values : ")
    print(df.isnull().sum())

    #----------------------------------------------
    # Step 2 : Select features (Inddependengt)
    #----------------------------------------------
    print(" Step 2 : Select features (Independengt)")
    X = df[["AnnualIncome","SpendingScore"]]

    print("Selected festures :")
    print(X.head())

    print("Shape of dataset : ")
    print(X.shape)

    #----------------------------------------------
    # Step 3 : Scaled Data
    #----------------------------------------------
    print("Step 3 : Scaled Data")

    scalar = StandardScaler()
    X_scaled = scalar.fit_transform(X)

    print("data After Scaling : ")
    print(X_scaled[:5])

    #----------------------------------------------
    # Step 4 : Use Elbow method
    #----------------------------------------------
    print("Step 4 : Use Elbow method")

    WCSS = []

    for i in range(1,11):
        model = KMeans(n_clusters=i,random_state=42)
        model.fit(X_scaled)
        WCSS.append(model.inertia_)


    plt.figure(figsize=(8,5))
    plt.plot(range(1,11),WCSS,marker="o")
    plt.xlabel("Number Of Clusters")
    plt.ylabel("WCSS")
    plt.title("Elbow Method")
    plt.grid(True)
    plt.show()

    #----------------------------------------------
    # Step 5 : Train the model
    #----------------------------------------------
    print(" Step 5 : Train the model")

    model = KMeans(n_clusters=4,random_state=42,n_init=10)
    clusters = model.fit_predict(X_scaled)

    df["cluster"] = clusters

    print("Datasset with clusters")
    print(df.head(30))

if __name__ == "__main__":
    main()
