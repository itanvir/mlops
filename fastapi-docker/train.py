from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Define the path to save the model
MODEL_PATH = "iris_model.pkl"

if __name__ == "__main__":
    # Load the Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Train a Logistic Regression model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # Save the trained model
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

    print(f"Trained model saved to {MODEL_PATH}")