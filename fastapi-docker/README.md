# Iris Classification API

This project implements a simple RESTful API using FastAPI to predict the species of Iris flowers based on their sepal length, sepal width, petal length, and petal width. The model used for prediction is a Logistic Regression model trained on the classic Iris dataset.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
  - [Locally](#locally)
  - [Using Docker](#using-docker)
- [API Usage](#api-usage)
  - [Base URL](#base-url)
  - [Prediction Endpoint](#prediction-endpoint)
  - [Request Body](#request-body)
  - [Response Body](#response-body)
  - [Example Usage (curl)](#example-usage-curl)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Prerequisites

Before you begin, ensure you have the following installed:

**For Local Development and Model Training:**

* **Python 3.7+**: The programming language used for the application and training script.
* **pip**: Python package installer (or conda, if you are using Anaconda).

**For Running with Docker:**

* **Docker**: To build and run the containerized application.

**Note:** If you only intend to run the application using Docker, you do not need to install Python or pip locally. Docker will handle the necessary environment within the container.

## Training

1.  **Clone the repository (if applicable):**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a Conda environment (recommended):**

    ```bash
    conda create --name iris_env python=3.12  # Or your preferred Python version
    conda activate iris_env
    ```

    Replace `iris_env` with your desired environment name and `3.9` with your preferred Python version.

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    You can generate the `requirements.txt` file using:

    ```bash
    pip freeze > requirements.txt
    ```

    Make sure your `requirements.txt` contains at least the following:

    ```
    fastapi
    uvicorn
    pydantic
    numpy
    scikit-learn
    ```

4.  **Train the Iris classification model:**

    Run the `train.py` script to train the Logistic Regression model and save it to `iris_model.pkl`:

    ```bash
    python train.py
    ```

    You should see output similar to: `Trained model saved to iris_model.pkl`.

## Running the Application

### Locally

1.  Navigate to the project directory in your terminal.
2.  Run the FastAPI application using Uvicorn:

    ```bash
    uvicorn app:app --reload
    ```

    * `app`: Refers to the `app.py` file.
    * `app`: Refers to the FastAPI application instance named `app` within `app.py`.
    * `--reload`: Enables automatic reloading of the server when you make code changes (useful for development).

3.  The API will be accessible at `http://localhost:8000`. You can view the automatically generated API documentation at `http://localhost:8000/docs`.

### Using Docker

1.  **Build the Docker image:**

    Ensure you have the `Dockerfile` in your project's root directory. Run the following command to build the Docker image:

    ```bash
    docker build -t iris-classifier .
    ```

    * `iris-classifier`: The name you want to give to your Docker image.
    * `.`: Indicates that the Dockerfile is in the current directory.

2.  **Run the Docker container:**

    ```bash
    docker run -p 8000:8000 iris-classifier
    ```

    * `-p 8000:8000`: Maps port 8000 on your host machine to port 8000 inside the container.
    * `iris-classifier`: The name of the Docker image you built.

3.  The API will be accessible at `http://localhost:8000`. The API documentation will be available at `http://localhost:8000/docs`.

## API Usage

### Base URL

The base URL for the API is `http://localhost:8000` (or the appropriate address if deployed elsewhere).

### Prediction Endpoint

The prediction endpoint is `/predict`. It accepts HTTP POST requests.

### Request Body

The request body should be a JSON object containing the four Iris flower features:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

### Example Usage (Curl)
```
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
  }' \
  http://localhost:8000/predict
```