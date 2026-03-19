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

## Algorithms Covered

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
## License
[MIT License](LICENSE) — Copyright (c) 2026 Sujan
