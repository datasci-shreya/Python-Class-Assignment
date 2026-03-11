import pandas as pd 
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(Datapath):
    Border = "-"*40
    # Step 1 : Load dataset from CSV file

    print(Border)
    print("Step 1 : Load dataset from CSV file")
    print(Border)
    
    df = pd.read_csv(Datapath)
    print(Border)
    print("Some entries from dataset")
    
    print(df.head())
    print(Border)

    # Step 2 : Clean Dataset by removing empty row

    print(Border)
    print("Step 2 : Clean Dataset by removing empty row")
    print(Border)

    df.dropna(inplace=True)
    print("Total records : ",df.shape[0])
    print("Total Columns : ",df.shape[1])
    print(Border)

    # Step 3 : Seperate Independent and Dependent Variables

    print(Border)
    print("Step 3 : Seperate Independent and Dependent Variables")
    print(Border)

    X = df.drop(columns=["Class"])
    Y = df["Class"]

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)


    print(Border)
    print("Input Columnd : ",X.columns.tolist())
    print("Output Column : Class")

    # Step 4 : Split the Dataset for traning and testing 

    print(Border)
    print("Step 4 : Split the Dataset for traning and testing ")
    print(Border)

    X_train , X_test ,Y_train ,Y_test = train_test_split(X,Y,test_size= 0.2,random_state=42,stratify=Y) #stratify after shuffle the 30-20 ch denar still last
    print(Border)

    print("Information Of training and testing data")
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)
    print(Border)

     # Step 5 : Features Scalling

    print(Border)
    print(" Step 5 : Features Scalling")
    print(Border)

    scaler = StandardScaler() #Dataupdate krun pathvla jato

    # Independent Variable Scaling
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)
    print("Feature scaler is done ")

    # Step 6 :Explore the multiple values of K 
    # Hyper parameter tunning(K)

    print(Border)
    print("Step 6 :Explore the multiple values of K ")
    print(Border)

    accuracy_scores = []
    k_values = range(1,21)

    for k in k_values:
        model = KNeighborsClassifier(n_neighbors=k) #defaul k value is k but aapn detoy
        model.fit(X_train_scaled,Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)

    print(Border)
    print("Accuracy Report of All K values from 1 to 20")
    
    for value in accuracy_scores:
        print(value)

    print(Border)

    # Step 7 : Plot graph of  K vs Accuracy 
    print(Border)
    print("Step 7 : Plot graph of  K vs Accuracy ")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.plot(k_values , accuracy_scores,marker = "o")
    plt.title("K values vs Accuracy")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(k_values))
    plt.show()

    
    # Step 8 : Find Best Value of k
    print(Border)
    print("Step 8 : Find Best Value of k ")
    print(Border)

    best_k = list(k_values)[accuracy_scores.index(max(accuracy_scores))]
    print("Best value of K is : ",best_k)

     # Step 9 : Build Final model using best value of k
    print(Border)
    print("Step 9 : Build Final model using best value of k")
    print(Border)

    final_model = KNeighborsClassifier(n_neighbors=best_k)
    model.fit(X_test_scaled,Y_train)

    Y_pred = final_model.predict(X_test_scaled)

     # Step 10 :  Calculate final accuracy
    print(Border)
    print(" Step 10 :  Calculate final accuracy")
    print(Border)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy of mmodel is : ",accuracy*100)

    # Step 11 :  Display Confusion Matrix
    print(Border)
    print(" Step 11 :  Display Confusion Matrix")
    print(Border)

    cm = confusion_matrix(Y_test,Y_pred)
    print(cm)

    # Step 12 :  Display Classsification Report
    print(Border)
    print("Step 12 :  Display Classsification Report")
    print(Border)

    print(classification_report(Y_test,Y_pred))
    
def main():
    Border = "-"*40
    print(Border)
    print("Wine Classifier Using KNN")
    print(Border)
    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()
