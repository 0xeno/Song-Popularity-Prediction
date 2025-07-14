# 🎵 Song Popularity Prediction

> **Predicting the popularity of a song based on its audio features using Machine Learning**

## 📌 Project Overview

The global music industry is worth over **$26.2 billion**, yet faces up to **90% failure rate** in launching new songs. Each artist investment ranges from **$500K–$2M**, making **early prediction of song popularity** crucial for reducing risk and optimizing marketing budgets.

This project builds a machine learning pipeline to predict the **popularity score** of songs using **audio features** such as `danceability`, `energy`, `valence`, `loudness`, and others. The goal is to evaluate the viability of using only audio-based metrics to estimate song performance.

---

## 📂 Dataset

- **Source:** [Kaggle - Song Popularity Dataset](https://www.kaggle.com/datasets/yasserh/song-popularity-dataset)
- **Size:** ~18,000 songs
- **Features:** 15 audio attributes, including:
  - `song_name`, `song_popularity`, `danceability`, `energy`, `valence`, `loudness`, `speechiness`, `acousticness`, `instrumentalness`, `key`, `tempo`, `time_signature`, `mode`, etc.

---

## 🔍 Key Steps

### 1. **Data Cleaning & EDA**
- No missing values, but **high presence of outliers** detected in `instrumentalness`, `liveness`, and `speechiness`.
- Used **4 methods for outlier detection**: IQR, Z-Score, Modified Z-Score, Isolation Forest.
- Visualized numerical and categorical distributions.
- Significant imbalance detected in features like `time_signature` and `audio_mode`.

### 2. **Feature Selection**
- Dropped features with high outlier contamination or low statistical impact:
  - ❌ `instrumentalness`, `liveness`, `speechiness`, `tempo`, `time_signature`, `energy`
- Final features retained:  
  `loudness`, `acousticness`, `danceability`, `audio_valence`, `song_duration_min`, `key_encoded`, `audio_mode_encoded`

### 3. **Statistical Tests**
- Performed **T-test** and **Chi-Square** analysis to validate discriminative power of features.
- Most features showed **weak correlation** with popularity → complex, non-linear problem.

### 4. **Scaling & Encoding**
- StandardScaler for numerical features.
- Encoded `key` and `mode` for modeling.


### 5. **Modeling**
- Tested 9 algorithms:
  - Linear Models: `LinearRegression`, `Ridge`, `Lasso`
  - Tree-Based: `DecisionTree`, `RandomForest`, `GradientBoosting`
  - Others: `KNN`, `SVR`, `XGBoost`
- **Best model: Gradient Boosting (R² = 0.024)** – still very low performance.

---

## ⚠️ Challenges & Insights

- Most audio features had **very weak correlation** with popularity.
- Even advanced models struggled: **low R² scores across the board**.
- **Real-world popularity** likely influenced by external factors (e.g., artist fame, marketing, social media), which aren't captured in audio metadata.

---

## ✅ Key Takeaways

- Audio-only features are **insufficient** for popularity prediction.
- Recommend including:
  - Listener engagement data (streams, likes)
  - Artist-level metadata
  - Social media mentions or virality metrics
- This project is a **proof-of-concept** and highlights the importance of **multimodal data** in ML for entertainment analytics.

---

## 📊 Tools & Technologies Used

- **Languages**: Python
- **Libraries**: pandas, numpy, matplotlib, seaborn, scikit-learn
- **Models**: Linear Regression, Decision Trees, Gradient Boosting, etc.
- **Other**: Feature Engineering, Statistical Testing, Outlier Analysis

---

## 🚀 Live Deployment

🔗 [Streamlit App (Demo)](https://song-popularity-prediction-kjn7fvlr4csrcjos44qmyz.streamlit.app/)  

---

## 📁 Repository Structure

```bash
├── notebook/
│   └── song_popularity_prediction.ipynb
├── data/
│   └── song_data.csv
├── fitur/
│   └── home.py
│   └── prediksi.py
│   └── rekomendasi.py
├── utils/
│   └── style.py
├── App.py
├── best_regression_model_20250529_131743.joblib
├── requirements.txt
└── README.md
