# Machine Learning Zoomcamp 2026

This repository contains the completed work for Modules 1, 2, and 3 of the DataTalksClub Machine Learning Zoomcamp 2026 course. The project covers an introductory machine learning workflow, regression, and classification.

## Project Structure

```text
.
├── 01-intro/
│   └── homework_1.ipynb
├── 02-regression/
│   └── homework_2.ipynb
├── 03-classification/
│   └── homework_3.ipynb
├── .gitignore
└── README.md
```

## Module 1: Introduction to Machine Learning

Module 1 introduces the machine learning workflow and foundational tools used throughout the course. The completed [Homework 1 notebook](01-intro/homework_1.ipynb) covers:

- CRISP-DM and the main stages of a machine learning project
- Pandas and NumPy refreshers for loading, inspecting, and transforming data
- Missing-value analysis and mode-based imputation
- Filtering and aggregating tabular data
- Normal equation implementation using matrix operations

## Module 2: Machine Learning for Regression

Module 2 focuses on regression modeling and evaluation using the fuel efficiency dataset. The completed [Homework 2 notebook](02-regression/homework_2.ipynb) covers:

- Target analysis and exploratory data analysis of `fuel_efficiency_mpg`
- Train / Validation / Test split (60% / 20% / 20%) with reproducible shuffling
- Baseline linear regression from scratch using Normal Equation with bias trick: w = (X^T X)^(-1) X^T y
- Imputation strategies comparison (zero vs. training mean) without data leakage
- L2 / Ridge Regularization: w = (X^T X + r I)^(-1) X^T y with parameter tuning
- Model stability evaluation across multiple random seeds via standard deviation of RMSE
- Final model training on concatenated (Train + Validation) sets and evaluation on the Test set

## Module 3: Machine Learning for Classification

Module 3 applies classification methods to a lead-scoring dataset. The completed [Homework 3 notebook](03-classification/homework_3.ipynb) covers:

- Categorical and numerical missing-value handling and feature exploration
- Reproducible 60% / 20% / 20% train / validation / test split
- Training-set mutual information analysis for categorical features
- One-hot encoding and logistic regression evaluation
- Feature elimination and regularization parameter tuning

## Local Setup

Create and activate the Python virtual environment from the repository root, then install the required packages.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install pandas numpy matplotlib seaborn scikit-learn jupyter ipykernel
```

### macOS and Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install pandas numpy matplotlib seaborn scikit-learn jupyter ipykernel
```

After activating the environment, open the notebook files in VS Code or launch Jupyter to run them.