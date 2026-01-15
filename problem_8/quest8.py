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
