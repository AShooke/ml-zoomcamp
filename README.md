# Machine Learning Zoomcamp 2026

This repository contains the completed work for Module 1, Introduction to Machine Learning, of the DataTalksClub Machine Learning Zoomcamp 2026 course. The current project is centered on Homework 1 and uses a car fuel efficiency dataset to practice core data analysis and machine learning concepts.

## Module 1 Overview

Module 1 introduces the machine learning workflow and foundational tools used throughout the course. The completed [Homework 1 notebook](01-intro/homework_1.ipynb) covers:

- CRISP-DM and the main stages of a machine learning project
- Pandas and NumPy refreshers for loading, inspecting, and transforming data
- Missing-value analysis and mode-based imputation
- Filtering and aggregating tabular data
- Normal equation implementation using matrix operations

## Local Setup

Create and activate the Python virtual environment from the repository root, then install the required packages.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install pandas numpy matplotlib seaborn jupyter ipykernel
```

### macOS and Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install pandas numpy matplotlib seaborn jupyter ipykernel
```

After activating the environment, open `01-intro/homework_1.ipynb` in VS Code or launch Jupyter to run the notebook.