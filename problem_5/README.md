# Python Virtual Environment Setup with Jupyter & Git

This project demonstrates how to:
- Create a Python virtual environment
- Manage dependencies using `requirements.txt`
- Verify the environment using Jupyter Lab
- Track the project using Git and push it to GitHub

---

## Step 1: Project Directory Setup

Create a new project directory and navigate into it.

```bash
mkdir ml-project
cd ml-project
```

---

## Step 2: Virtual Environment Setup

### Install Virtual Environment Package
Install `python3-venv` if it is not already installed.

```bash
sudo apt install python3-venv
```

### Create Virtual Environment

```bash
python3 -m venv myenv
```

### Activate Virtual Environment

```bash
source myenv/bin/activate
```

---

## Step 3: Create Requirements File

Create a file named `requirements.txt`.

```bash
gedit requirements.txt
```

Add the following content:

```text
numpy>=1.22
pandas>=1.5
jupyterlab>=4.1
notebook>=6.5
ipykernel
```

Save and close the file.

---

## Step 4: Install Dependencies

Install all required packages using pip.

```bash
pip install -r requirements.txt
```

---

## Step 5: Verify Setup Using Jupyter Lab

### Launch Jupyter Lab

```bash
jupyter-lab
```

### Verification Script (Run Inside a Jupyter Notebook)

```python
import sys
print(sys.version)

import numpy as np
import pandas as pd

print(np.__version__)
print(pd.__version__)
```

This confirms:
- Python version
- NumPy installation
- Pandas installation

---

## Step 6: Git Version Control

### Initialize Git Repository

```bash
git init
git add .
git commit -m "first commit"
```

### Rename Branch to Main

```bash
git branch -M main
```

### Add Remote Repository

```bash
git remote add origin https://github.com/anixet-14/question8.git
```

### Push Code to GitHub

```bash
git push -u origin main
```

---

## Final Outcome

- Python virtual environment created successfully
- Dependencies installed via `requirements.txt`
- Environment verified using Jupyter Lab
- Project version-controlled using Git
- Code pushed to GitHub repository

---

## Project Structure

```text
ml-project/
├── myenv/
├── requirements.txt
└── README.md
```
