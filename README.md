# Hybrid Disorder Prediction System Using Machine Learning

## Project Overview
This project implements a hybrid machine learning system to predict disorders using supervised algorithms such as Support Vector Machine (SVM), Gradient Boosting, and XGBoost. It includes data preprocessing, model training, evaluation, and hyperparameter tuning for optimized predictions.

## Setup
1. Clone the repo.
2. Place your dataset as `data/disorder_data.csv`.
3. Create a virtual environment and install dependencies:

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```

## Usage
Run the pipeline with:
```bash
python main.py
```

## Project Structure
- `data/` - Dataset folder
- `src/` - Source code for preprocessing, training, and evaluation
- `notebooks/` - Exploratory Data Analysis (EDA)
- `main.py` - Entry point to run the project
