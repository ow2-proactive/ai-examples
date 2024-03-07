# CIFAR-10 Logistic Regression Classifier

This project involves training and evaluating a logistic regression model on the [CIFAR-10 dataset](https://www.kaggle.com/datasets/fedesoriano/cifar10-python-in-csv/) converted to CSV format. The model is designed to classify images based on pixel values.

## Project Structure

- `train.py`: Trains the logistic regression model on the CIFAR-10 training dataset. It preprocesses the data, splits it into training and validation sets, trains the model, evaluates it on the validation set, and saves the model.
- `eval.py`: Evaluates the saved logistic regression model on the CIFAR-10 test dataset. It loads the model, preprocesses the test data, makes predictions, and saves these predictions to a text file.
- `models/`: Directory for storing the trained logistic regression model (`logistic_regression_model.pkl`).
- `predictions/`: Directory for storing the predictions of the logistic regression model on the test set (`logistic_regression.txt`).
- `dataset/cifar10-csv/`: Contains the CIFAR-10 dataset in CSV format (`train.csv` and `test.csv`). Use `download_dataset.sh` script to download the dataset.

## Getting Started

### Prerequisites

- Python 3.9
- pandas 2.2.1
- scikit-learn 1.4.1.post1
- joblib 1.3.2
- numpy 1.26.4

Install the necessary libraries using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Downloading the Dataset

Navigate to the `dataset` directory and run the `download_dataset.sh` script to download the CIFAR-10 dataset in CSV format:

```bash
cd dataset
./download_dataset.sh
```

### Training the Model

To train the logistic regression model, run:

```bash
python train.py
```

This will preprocess the training data, train the model, evaluate it on the validation set, and save the model in the `models/` directory.

### Evaluating the Model

To evaluate the saved model on the test dataset, run:

```bash
python eval.py
```

This loads the trained model, preprocesses the test data, makes predictions, and saves those predictions in the `predictions/` directory as `logistic_regression.txt`.

## Notes

- Make sure the CIFAR-10 CSV dataset are in the `dataset/cifar10-csv/` directory before running the scripts.
- If your CSV files contain header rows, adjust the `header` parameter in the `pd.read_csv()` function in the scripts accordingly.
