# NLP: IMDB Sentiment Analysis Description

## Achievement
Accuracy of the best model on test dataset is 91.6%.

## Analysis

The corpus has less noises compared to some other datasets, and I believe a good quality of the data is the first step to do modeling. So I spent more time on text cleaning and then tried on at most four typical traditional machine learning models and built three deep learning models.

## Text Preprocessing

Rules are used to process the text as follow:

    Remove non-ASCII characters
    Lowercase
    Split contraction words 
    Lemmatize verbs
    Replace all integer into the word “digit” 
    Remove stop words except for “wh-” words

## Word Embedding
Both of TF-IDF and FastText word embeddings on the whole corpus cleaned before were trained and used them as the input of the models later.

## Modeling
With two different tracks of word embedding, TF-IDF embedding was used more in traditional ML models:

    Linear Regression

    Support Vector Machine

    XGBoost

    Random Forest

FastText embedding performs better on deep learning models I tried on: 
    
    Bi-LSTM

    Bi-LSTM+CNN+Attention

    Virtual Adversarial Training

In the TF-IDF, hyper parameters like max_features and n-gram are tuned with many times, while the size of the FastText is fixed with 300.

Here, grid search was used to select promising models base on the f-score of 5-fold cross validation.

## Evaluation

Traditional model winner:  SVM   (acc: 0.9, training time: 1h)

Deep Learning model winner:  Bi-LSTM+CNN+Attention   (acc: 0.916, training time: 4h)

Experiment result is attached as follow:



