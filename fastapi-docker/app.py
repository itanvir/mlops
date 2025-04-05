from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import numpy as np
import pickle

# Define the path to the saved model
MODEL_PATH = "iris_model.pkl"

# Load the Iris dataset class names (assuming train.py has been run)
try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
        from sklearn.datasets import load_iris
        iris = load_iris()
        class_names = iris.target_names
except FileNotFoundError:
    print(f"Error: Model file not found at {MODEL_PATH}. Please run train.py first.")
    class_names = ["setosa", "versicolor", "virginica"]  # Default if model not found

# Define Pydantic models for request and response
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class PredictionResponse(BaseModel):
    predicted_class: str
    probability: float

app = FastAPI(title="Iris Classification API", description="API for predicting Iris flower species")

@app.get("/")
async def root():
    return {"message": "Welcome to the Iris Classification API. Go to /docs for API documentation."}

@app.post("/predict", response_model=PredictionResponse)
async def predict_iris(features: IrisFeatures):
    try:
        # Create a numpy array from the input features
        input_features = np.array([[
            features.sepal_length,
            features.sepal_width,
            features.petal_length,
            features.petal_width
        ]])

        # Load the model if not already loaded (useful for separate runs or reloads)
        if not hasattr(predict_iris, "model"):
            try:
                with open(MODEL_PATH, "rb") as f:
                    predict_iris.model = pickle.load(f)
            except FileNotFoundError:
                raise HTTPException(status_code=500, detail="Model file not found. Please ensure train.py has been run.")
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error loading model: {e}")

        # Make the prediction
        probabilities = predict_iris.model.predict_proba(input_features)[0]
        predicted_class_index = np.argmax(probabilities)
        predicted_class_name = class_names[predicted_class_index]
        probability = probabilities[predicted_class_index]

        return {"predicted_class": predicted_class_name, "probability": float(probability)}

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)