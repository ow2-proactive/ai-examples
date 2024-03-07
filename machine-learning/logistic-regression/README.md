# CIFAR-10 Logistic Regression Classifier

This project involves training and evaluating a logistic regression model on the [CIFAR-10 dataset](https://www.kaggle.com/datasets/fedesoriano/cifar10-python-in-csv/) that has been converted to CSV format. The goal is to classify images based on their pixel values.

## Project Structure

- `train.py`: Script to train the logistic regression model on the CIFAR-10 training dataset. It includes steps for data preprocessing, training/validation set splitting, model training, validation set evaluation, and model saving.
- `eval.py`: Script to evaluate the saved logistic regression model on the CIFAR-10 test dataset. It loads the model, preprocesses the test data, makes predictions, and saves these predictions to a text file.
- `models/`: Directory where the trained logistic regression model (`logistic_regression_model.pkl`) is saved.
- `predictions/`: Directory where the model's predictions on the test set (`logistic_regression.txt`) are stored.
- `dataset/cifar10-csv/`: Contains the CIFAR-10 dataset in CSV format (`train.csv` and `test.csv`). The `download_dataset.sh` script is used to download the dataset.

## Getting Started

### Prerequisites

The project requires Python 3.9 and the following Python libraries:

- pandas 2.2.1
- scikit-learn 1.4.1.post1
- joblib 1.3.2
- numpy 1.26.4

To install the necessary libraries, use the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Downloading the Dataset

To download the CIFAR-10 dataset in CSV format, navigate to the `dataset` directory and execute the `download_dataset.sh` script:

```bash
cd dataset
./download_dataset.sh
```

### Training the Model

To train the logistic regression model, run:

```bash
python train.py
```

This script preprocesses the training data, trains the model, evaluates it on the validation set, and saves the model in the `models/` directory.

### Evaluating the Model

To evaluate the saved model on the test dataset, execute:

```bash
python eval.py
```

This script loads the trained model, preprocesses the test data, makes predictions, and saves those predictions in the `predictions/` directory as `logistic_regression.txt`.

## Notes

- Ensure the CIFAR-10 CSV dataset are properly placed in the `dataset/cifar10-csv/` directory before running the scripts.
- Adjust the `header` parameter in the `pd.read_csv()` function within the scripts as necessary, depending on whether your CSV files include header rows.
