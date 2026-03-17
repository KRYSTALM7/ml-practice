# ML Practice

> A structured collection of Machine Learning algorithm implementations in Python — covering classification, clustering, deep learning, and NLP.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![sklearn](https://img.shields.io/badge/scikit--learn-1.3+-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## Structure
```
ml-practice/
├── classification/     # SVM, KNN, AdaBoost, Logistic Regression
├── clustering/         # KMeans, KModes, Elbow Method
├── deep_learning/      # MLP, Neural Networks
├── nlp/                # Real-time speech transcription + GPT
├── math_utils/         # GCD, Euclidean algorithm
└── data/               # CSV datasets
```

---

## 🗂Algorithms Covered

### Classification
| File | Algorithm | Dataset |
|------|-----------|---------|
| `adaboost_iris.py` | AdaBoost | Iris |
| `adaboost_cancer_comparison.py` | AdaBoost with 4 base classifiers | Breast Cancer |
| `svm_cancer.py` | SVM (linear kernel) | Breast Cancer |
| `svm_apples_oranges.py` | SVM (RBF kernel) | Custom CSV |
| `knn_manual.py` | KNN (K=1 vs K=5) | Manual points |
| `knn_obesity_dataset.py` | KNN | Obesity CSV |
| `knn_optimal_k.py` | KNN elbow curve | Obesity CSV |
| `logistic_regression_digits.py` | Logistic Regression | Digits (images) |

### Clustering
| File | Algorithm | Dataset |
|------|-----------|---------|
| `kmeans_iris.py` | KMeans (K=2–7) + Elbow | Iris |
| `kmeans_social_media.py` | KMeans + Elbow | Social media selling data |
| `kmodes_bank.py` | KModes (Cao + Huang) | Bank marketing |

### Deep Learning
| File | Algorithm | Dataset |
|------|-----------|---------|
| `mlp_iris.py` | Multi-Layer Perceptron | Iris |

### NLP
| File | What it does |
|------|-------------|
| `speech_to_text_gpt.py` | Real-time mic transcription via AssemblyAI + GPT reply |
| `openai_helper.py` | OpenAI GPT completion helper |

---

## Installation
```bash
git clone https://github.com/KRYSTALM7/ml-practice.git
cd ml-practice
pip install -r requirements.txt
```

For NLP scripts, copy `.env.example` to `.env` and add your API keys:
```bash
cp .env.example .env
```

---

## Running Scripts
```bash
python classification/svm_cancer.py
python clustering/kmeans_iris.py
python deep_learning/mlp_iris.py
```

---

## 30-Day Practice Roadmap

| Day | Topic | File to create |
|-----|-------|---------------|
| 1 | Linear Regression from scratch | `classification/linear_regression_scratch.py` |
| 2 | Decision Tree on Iris | `classification/decision_tree_iris.py` |
| 3 | Random Forest on Cancer | `classification/random_forest_cancer.py` |
| 4 | PCA dimensionality reduction | `clustering/pca_iris.py` |
| 5 | Naive Bayes classifier | `classification/naive_bayes.py` |
| 6 | DBSCAN clustering | `clustering/dbscan.py` |
| 7 | Gradient Boosting | `classification/gradient_boosting.py` |
| 8 | Cross-validation techniques | `classification/cross_validation.py` |
| 9 | Feature importance visualization | `classification/feature_importance.py` |
| 10 | Neural net from scratch (numpy) | `deep_learning/nn_from_scratch.py` |
| 11 | CNN on MNIST | `deep_learning/cnn_mnist.py` |
| 12 | RNN for sequence prediction | `deep_learning/rnn_sequence.py` |
| 13 | LSTM on time series | `deep_learning/lstm_timeseries.py` |
| 14 | Text preprocessing (tokenization) | `nlp/text_preprocessing.py` |
| 15 | TF-IDF vectorizer | `nlp/tfidf_vectorizer.py` |
| 16 | Sentiment analysis | `nlp/sentiment_analysis.py` |
| 17 | Word2Vec embeddings | `nlp/word2vec.py` |
| 18 | Logistic Regression on text | `nlp/text_classification.py` |
| 19 | Confusion matrix visualization | `classification/confusion_matrix_viz.py` |
| 20 | Hyperparameter tuning (GridSearch) | `classification/grid_search.py` |
| 21 | ROC curve + AUC | `classification/roc_auc.py` |
| 22 | Hierarchical clustering dendrogram | `clustering/hierarchical.py` |
| 23 | Gaussian Mixture Models | `clustering/gmm.py` |
| 24 | Autoencoder | `deep_learning/autoencoder.py` |
| 25 | Transfer learning basics | `deep_learning/transfer_learning.py` |
| 26 | Batch normalization demo | `deep_learning/batch_norm.py` |
| 27 | Regularization (L1/L2) | `classification/regularization.py` |
| 28 | Ensemble methods comparison | `classification/ensemble_comparison.py` |
| 29 | Stats: mean/variance/distributions | `math_utils/statistics_basics.py` |
| 30 | End-to-end ML pipeline | `classification/full_pipeline.py` |

---

## License

MIT License — Copyright (c) 2024 Sujan