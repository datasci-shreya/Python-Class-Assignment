import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#----------------------------------------------------------
def DisplayInfo(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

#----------------------------------------------------------
# Step 1: Load Dataset
#----------------------------------------------------------
def LoadData(path):

    df = pd.read_csv(path, sep=';')   # IMPORTANT

    DisplayInfo("Step 1: Dataset Loaded")

    print(df.head())
    print("\nShape:", df.shape)

    return df

#----------------------------------------------------------
# Step 2: Select Features
#----------------------------------------------------------
def SelectFeatures(df):

    DisplayInfo("Step 2: Feature Selection")

    df = df[["G1", "G2", "G3", "studytime", "failures", "absences"]]

    print(df.head())

    return df

#----------------------------------------------------------
# Step 3: Scaling
#----------------------------------------------------------
def PreprocessData(df):

    DisplayInfo("Step 3: Data Scaling")

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    return scaled_data

#----------------------------------------------------------
# Step 4: Elbow Method
#----------------------------------------------------------
def ElbowMethod(data):

    DisplayInfo("Step 4: Elbow Method")

    inertia = []
    K = range(1, 10)

    for k in K:
        model = KMeans(n_clusters=k, random_state=42)
        model.fit(data)
        inertia.append(model.inertia_)

    plt.plot(K, inertia, marker='o')
    plt.xlabel("Number of Clusters (K)")
    plt.ylabel("Inertia")
    plt.title("Elbow Method Graph")
    plt.show()

#----------------------------------------------------------
# Step 5: Apply K-Means
#----------------------------------------------------------
def ApplyClustering(data):

    DisplayInfo("Step 5: K-Means Clustering")

    kmeans = KMeans(n_clusters=3, random_state=42)

    clusters = kmeans.fit_predict(data)

    return clusters

#----------------------------------------------------------
# Step 6: Analyze Clusters
#----------------------------------------------------------
def AnalyzeClusters(df, clusters):

    DisplayInfo("Step 6: Cluster Analysis")

    df["Cluster"] = clusters

    print("\nCluster Means:")
    print(df.groupby("Cluster").mean())

    return df

#----------------------------------------------------------
# Step 7: Visualization
#----------------------------------------------------------
def PlotClusters(df):

    DisplayInfo("Step 7: Visualization")

    plt.scatter(df["G3"], df["studytime"], c=df["Cluster"])
    plt.xlabel("Final Grade (G3)")
    plt.ylabel("Study Time")
    plt.title("Student Clusters")
    plt.show()

#----------------------------------------------------------
# Main Function
#----------------------------------------------------------
def main():

    df = LoadData("student-mat.csv")

    df = SelectFeatures(df)

    scaled_data = PreprocessData(df)

    # Elbow Method
    ElbowMethod(scaled_data)

    # Clustering
    clusters = ApplyClustering(scaled_data)

    df = AnalyzeClusters(df, clusters)

    PlotClusters(df)

    DisplayInfo("Final Result")

    print("""
Cluster 0 → Top Performers
Cluster 1 → Average Students
Cluster 2 → Struggling Students
""")

#----------------------------------------------------------
if __name__ == "__main__":
    main()