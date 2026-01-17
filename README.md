# SMS-Detection

## Introduction

SMS-Detection is a machine learning project designed to classify SMS messages as spam or not spam. The repository contains code for data preprocessing, model training, evaluation, and prediction. It serves as an educational example of applying natural language processing and classification techniques to real-world SMS data.

## Features

- Detects spam messages from SMS text using machine learning.
- Includes data preprocessing, feature extraction, and model training steps.
- Supports multiple classification algorithms.
- Provides evaluation metrics for model performance.
- Ready-to-use scripts for training and prediction.

## Requirements

To run this project, ensure you have the following dependencies:

- Python 3.6 or higher
- pandas
- numpy
- scikit-learn
- matplotlib (for visualization)
- nltk (for text preprocessing)
- pickle (for model saving/loading)
- Jupyter Notebook (recommended for interactive use)

You can install dependencies using pip:

```bash
pip install pandas numpy scikit-learn matplotlib nltk joblib
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Sourav1000888/SMS-Detection.git
   cd SMS-Detection
   ```

2. Install the required packages (see above).

3. Download the SMS Spam Collection Dataset if not already included.

## Usage

### Training the Model

1. Prepare the dataset in the required format (CSV with 'label' and 'message' columns).
2. Run the training script or open the Jupyter notebook for an interactive session.
3. The script will preprocess the data, extract features, train the model, and display evaluation metrics.

Example command to run training:

```bash
python train.py --data data/spam.csv --model output/model.pkl
```

### Making Predictions

1. Use the trained model to predict new SMS messages.
2. Load the model and input the message(s) you want to classify.

Example usage in Python:

```python
from joblib import load
model = load('output/model.pkl')
prediction = model.predict(['Congratulations, you have won!'])
print(prediction)
```

### Jupyter Notebook

For step-by-step execution, open the notebook:

```bash
jupyter notebook sms_detection.ipynb
```

### Results
 1. Training Accuracy : 97%
 2. Testing Accuacy : 97%
 3. Precision : 100%


