# Data Version Control (DVC) Pipeline – Data Processing Workflow

This project demonstrates how to:
- Use **DVC (Data Version Control)** with Git
- Organize raw and processed data
- Create a reproducible data pipeline
- Track data processing stages using `dvc.yaml` and `dvc.lock`

---

## Step 1: Install DVC and Initialize Environment

Install DVC, create the project directory, and initialize Git and DVC.

```bash
pip install dvc
mkdir ques7
cd ques7
git init
dvc init
```

---

## Step 2: Set Up Data Directories and Create Raw Data

Create the directory structure for raw data.

```bash
mkdir data
cd data
mkdir raw
cd raw
```

Create the CSV file:

```bash
gedit data.csv
```

### Content of `data.csv`

```text
1,10
2,20
3,30
```

Save and close the file.

---

## Step 3: Create Processed Data Directory

Navigate back and create a directory for processed data.

```bash
cd ..
mkdir processed
cd ..
cd ..
```

---

## Step 4: Create Scripts Directory and Cleaning Script

Create a directory for scripts and add the data cleaning script.

```bash
mkdir scripts
cd scripts
gedit clean.py
```

### Content of `clean.py`

```python
import pandas as pd

df = pd.read_csv("data/raw/data.csv", header=None)
df.columns = ["id", "value"]
df["value"] = df["value"] * 2
df.to_csv("data/processed/clean.csv", index=False)
```

Save and close the file.

---

## Step 5: Create DVC Pipeline Stage

Navigate back to the project root and create a DVC pipeline stage.

```bash
cd ..
dvc stage add -n clean \
-d scripts/clean.py \
-d data/raw/data.csv \
-o data/processed/clean.csv \
python scripts/clean.py
```

This command automatically generates the `dvc.yaml` file.

---

## Step 6: Configure Git and Commit Changes

Configure Git user details (if not already configured).

```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

Add and commit the DVC configuration files.

```bash
git add dvc.yaml data/processed/.gitignore
git commit -m "Add Pipeline"
```

---

## Step 7: Run the DVC Pipeline

Execute the pipeline to process the data.

```bash
dvc repro
```

This generates the cleaned dataset in the processed directory.

---

## Step 8: Version Control the Lock File

Track the pipeline state by committing the `dvc.lock` file.

```bash
git add dvc.lock
git commit -m "Track pipeline state"
```

---

## Generated Files Reference

### `dvc.yaml` (Automatically Created)

```yaml
stages:
  clean:
    cmd: python scripts/clean.py
    deps:
    - data/raw/data.csv
    - scripts/clean.py
    outs:
    - data/processed/clean.csv
```

---

## Final Outcome

- Raw and processed data tracked using DVC
- Reproducible data pipeline created
- Data processing steps versioned
- Pipeline state tracked via `dvc.lock`
- Git and DVC working together for data science workflows

---

## Project Structure

```text
ques7/
├── data/
│   ├── raw/
│   │   └── data.csv
│   └── processed/
│       └── clean.csv
├── scripts/
│   └── clean.py
├── dvc.yaml
├── dvc.lock
└── README.md
```
