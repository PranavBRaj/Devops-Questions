# FastAPI ML Model Deployment with Docker and Testing

This project demonstrates an **end-to-end ML API workflow**, including:
- Training a simple Machine Learning model
- Serving the model using **FastAPI**
- Input validation with **Pydantic**
- API testing using **Pytest**
- Containerization using **Docker**

---

## Step 1: Setup and Installation

### Create Project Directory
Create a directory for the project and navigate into it.

```bash
mkdir ml-api-project
cd ml-api-project
```

### Install Required Libraries

```bash
pip install fastapi uvicorn scikit-learn joblib pytest
```

---

## Step 2: Create and Train the Model

### Create Training Script
Create a file named `train.py`.

```bash
gedit train.py
```

Add the following code:

```python
from sklearn.linear_model import LinearRegression
import joblib

# Initialize the model
model = LinearRegression()

# Dummy data for training
X = [[1], [2], [3]]
y = [2, 4, 6]

# Train the model
model.fit(X, y)

# Save the model
joblib.dump(model, "model.pkl")
```

### Run Training Script

```bash
python3 train.py
```

This generates a `model.pkl` file in the project directory.

---

## Step 3: Create the FastAPI Application

### Create API File
Create a file named `main.py`.

```bash
gedit main.py
```

Add the following code:

```python
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
model = joblib.load("model.pkl")

class Input(BaseModel):
    x: float

@app.post("/predict")
def predict(data: Input):
    return {"prediction": model.predict([[data.x]])[0]}
```

### Run API Locally (Optional)

```bash
uvicorn main:app --reload
```

### Verify Using Curl (Optional)

```bash
curl -X POST http://127.0.0.1:8000/predict \
-H "Content-Type: application/json" \
-d '{"x": 5}'
```

---

## Step 4: Write Test Cases

### Create Test File
Create a file named `test_api.py`.

```bash
gedit test_api.py
```

Add the following code:

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict():
    result = client.post("/predict", json={"x": 6})
    assert result.status_code == 200
```

### Run Tests

```bash
pytest
```

---

## Step 5: Create Requirements File

Generate the requirements file for Docker.

```bash
pip freeze > requirements.txt
```

---

## Step 6: Containerize with Docker

### Create Dockerfile
Create a file named `Dockerfile` (no extension).

```bash
gedit Dockerfile
```

Add the following content:

```dockerfile
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Step 7: Build and Run Docker Container

### Build Docker Image

```bash
docker build -t ml-api .
```

### Run Docker Container

```bash
docker run -p 8000:8000 ml-api
```

---

## Step 8: Final Verification

Verify the running Docker container using `curl`.

```bash
curl -X POST http://0.0.0.0:8000/predict \
-H "Content-Type: application/json" \
-d '{"x": 9}'
```

Expected response:

```json
{"prediction": 18.0}
```

---

## Final Outcome

- Machine Learning model trained and saved
- Model served using FastAPI with input validation
- API tested using Pytest
- Application containerized using Docker
- API successfully accessed via Docker container

---

## Project Structure

```text
ml-api-project/
├── train.py
├── main.py
├── test_api.py
├── model.pkl
├── requirements.txt
├── Dockerfile
└── README.md
```
