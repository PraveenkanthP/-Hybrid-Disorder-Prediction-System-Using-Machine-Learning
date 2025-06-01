from src.data_preprocessing import load_and_preprocess_data
from src.train_models import train_models
from src.evaluate import evaluate_models

def main():
    # Load and preprocess data
    X_train, X_test, y_train, y_test = load_and_preprocess_data('data/disorder_data.csv')

    # Train models
    models = train_models(X_train, y_train)

    # Evaluate models
    evaluate_models(models, X_test, y_test)

if __name__ == "__main__":
    main()