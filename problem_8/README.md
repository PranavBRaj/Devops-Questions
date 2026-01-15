# MLflow Experiment Tracking with Logistic Regression (Iris Dataset)

This project demonstrates how to:
- Train a Logistic Regression model on the Iris dataset
- Track experiments using **MLflow**
- Log parameters, metrics, and models
- Visualize results using the MLflow UI

---

## 1. Python Script (`quest8.py`)

Create a Python script that trains a Logistic Regression model with different hyperparameters and logs the results using MLflow.

### File: `quest8.py`

```python
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn

# Load Iris dataset (Corrected version from video)
X, y = load_iris(return_X_y=True)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Loop through different values of C (Regularization Strength)
for c in [0.1, 1.0]:
    with mlflow.start_run():
        # Initialize and train Logistic Regression model
        m = LogisticRegression(C=c, max_iter=200)
        m.fit(X_train, y_train)
        
        # Calculate accuracy score
        acc_score = accuracy_score(y_test, m.predict(X_test))
        
        # Log parameters, metrics, and the model
        mlflow.log_param("C", c)
        mlflow.log_metric("accuracy", acc_score)
        mlflow.sklearn.log_model(m, "model")
```

---

## 2. Execution Steps

### Step 1: Open Terminal
Launch your Ubuntu/Linux terminal.

---

### Step 2: Create Python File

```bash
gedit quest8.py
```

Paste the script above into the file, then save and close it.

---

### Step 3: Run the Python Script
Execute the script to run the ML experiments.

```bash
python3 quest8.py
```

This will:
- Train models with different `C` values
- Log parameters, metrics, and models into MLflow

---

### Step 4: Launch MLflow Dashboard
Start the MLflow UI to visualize experiment results.

```bash
mlflow ui
```

---

### Step 5: View Results in Browser
Open the generated URL in a web browser:

```
http://127.0.0.1:5000
```

You can now view:
- Experiment runs
- Logged parameters (`C`)
- Accuracy metrics
- Saved model artifacts

---

## Notes

- No manual HTML or YAML files are required
- MLflow automatically creates experiment tracking files and artifacts
- Ensure `mlflow`, `scikit-learn`, and dependencies are installed in your environment

---

## Final Outcome

- Logistic Regression model trained on Iris dataset
- Multiple experiments tracked using MLflow
- Hyperparameters and accuracy logged
- Models stored as MLflow artifacts
- Results visualized through MLflow UI

---

## Project Structure

```text
.
├── quest8.py
├── mlruns/
└── README.md
```
