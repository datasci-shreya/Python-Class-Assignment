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

    df = pd.read_csv(path, sep=';')   # dataset uses ;

    DisplayInfo("Step 1: Dataset Loaded")

    print(df.head())
    print("\nShape:", df.shape)

    return df

#----------------------------------------------------------
# Step 2: Select Required Features
#----------------------------------------------------------
def SelectFeatures(df):

    DisplayInfo("Step 2: Feature Selection")

    # Select only required columns
    df = df[["G1", "G2", "G3", "studytime", "failures", "absences"]]

    print(df.head())

    return df

#----------------------------------------------------------
# Step 3: Preprocessing (Scaling)
#----------------------------------------------------------
def PreprocessData(df):

    DisplayInfo("Step 3: Data Scaling")

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    return scaled_data

#----------------------------------------------------------
# Step 4: Apply K-Means Clustering
#----------------------------------------------------------
def ApplyClustering(data):

    DisplayInfo("Step 4: K-Means Clustering")

    kmeans = KMeans(n_clusters=3, random_state=42)

    clusters = kmeans.fit_predict(data)

    return clusters, kmeans

#----------------------------------------------------------
# Step 5: Analyze Clusters
#----------------------------------------------------------
def AnalyzeClusters(df, clusters):

    DisplayInfo("Step 5: Cluster Analysis")

    df["Cluster"] = clusters

    print(df.groupby("Cluster").mean())

    return df

#----------------------------------------------------------
# Step 6: Visualization
#----------------------------------------------------------
def PlotClusters(df):

    DisplayInfo("Step 6: Visualization")

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

    clusters, model = ApplyClustering(scaled_data)

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