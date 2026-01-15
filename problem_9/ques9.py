from sklearn.linear_model import LinearRegression
import numpy as np
from skl2onnx import to_onnx
import onnxruntime as ort
import time

# --- 1. Train a model ---
# Generate dummy data
X = np.random.rand(1000, 1)
y = 3 * X + 5

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

# --- 2. Export it to ONNX ---
# Convert the scikit-learn model to ONNX format
onnx_model = to_onnx(model, X)

# Save the ONNX model to a binary file
with open("model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

# --- 3. Runtime Session ---
# Create an inference session using the saved ONNX model
sess = ort.InferenceSession("model.onnx")

# --- 4. Benchmark Performance ---
# Benchmark Scikit-learn Native Model
t0 = time.time()
for _ in range(10000):
    model.predict(X)
sktime = time.time() - t0

# Benchmark ONNX Runtime
t0 = time.time()
for _ in range(10000):
    # The input name "X" is automatically assigned by to_onnx
    sess.run(None, {"X": X})
onnxtime = time.time() - t0

# --- 5. Print Results ---
print("Scikit-learn time:", sktime)
print("ONNX time:", onnxtime)
