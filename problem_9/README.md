# ONNX Model Optimization & Inference Benchmarking

This project demonstrates how to **optimize and standardize model inference using ONNX**.  
It covers:
- Training a Scikit-learn model
- Exporting the model to ONNX format
- Running inference using ONNX Runtime
- Benchmarking performance between native Scikit-learn and ONNX

---

## Step 1: Setup Workspace

Create a project directory and navigate into it.

```bash
mkdir onnx-question
cd onnx-question
```

---

## Step 2: Create the Python Script

Create a Python file named `ques9.py`.

```bash
gedit ques9.py
```

Paste the following code into the file, then save and close it.

### File: `ques9.py`

```python
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
```

---

## Step 3: Execute the Script

Run the Python script using Python 3.

```bash
python3 ques9.py
```

---

## Expected Output

The script prints execution times for both inference methods:

```text
Scikit-learn time: <value>
ONNX time: <value>
```

As demonstrated in the video, **ONNX Runtime inference is significantly faster** than native Scikit-learn inference  
(approximately **0.4s vs 0.8s**).

---

## Notes

- ONNX provides a standardized, portable model format
- ONNX Runtime enables faster and optimized inference
- This workflow is useful for **production ML systems** and **cross-platform deployment**

---

## Final Outcome

- Model trained using Scikit-learn
- Model exported to ONNX format
- Inference optimized using ONNX Runtime
- Performance benchmark comparison completed successfully

---

## Project Structure

```text
onnx-question/
├── ques9.py
├── model.onnx
└── README.md
```
