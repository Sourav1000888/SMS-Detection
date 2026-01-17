# SMS Detection

## Introduction

SMS Detection is a machine learning project aimed at identifying and classifying SMS messages as spam or not spam (ham). The repository contains code for preprocessing SMS data, training a classification model, and evaluating its performance. This tool is valuable for anyone interested in natural language processing, text classification, or building spam detection systems.

## Features

- Preprocessing of SMS text data, including cleaning and normalization.
- Feature extraction using techniques such as Bag-of-Words (BoW) and TF-IDF.
- Implementation of machine learning models for binary classification.
- Model evaluation with metrics like accuracy, precision, recall, and F1-score.
- Easy-to-follow code structure suitable for experimentation and extension.
- Example notebook for hands-on experimentation and result visualization.

## Requirements

To run this project, ensure you have the following software and libraries installed:

- Python 3.6 or higher
- pandas
- numpy
- scikit-learn
- nltk
- matplotlib (for visualization)
- jupyter (if running the provided notebook)

To install the required Python libraries, use the following command:

```bash
pip install pandas numpy scikit-learn nltk matplotlib jupyter
```

## Installation

Follow these steps to set up the repository and run the SMS detection project:

1. **Clone the Repository**

   Clone the repository to your local machine using:
   ```bash
   git clone https://github.com/Sourav1000888/SMS-Detection.git
   cd SMS-Detection
   ```

2. **Install Dependencies**

   Install the required Python libraries (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` is not present, install the packages individually as listed above.

3. **Download NLTK Resources**

   Some NLTK functionalities require downloading additional datasets. Start a Python session and run:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

4. **Run the Project**

   Open the provided Jupyter notebook or Python scripts to start data preprocessing, training, and evaluating the model. To launch Jupyter Notebook:
   ```bash
   jupyter notebook SMS_Detection.ipynb
   ```
   Or, to run a Python script:
   ```bash
   python main.py
   ```

5. **Explore and Experiment**

   Modify the code to experiment with different preprocessing methods, feature extraction techniques, or machine learning models.

---
6. **Results**
   1. Training Accuracy : 97%
   2. Testing Accuracy : 97%
   3. Precision Score : 100%
  

For further information, check the code comments and documentation within the repository files. This project is designed for extensibility and learning, making it suitable for both beginners and experienced practitioners in machine learning and natural language processing.
