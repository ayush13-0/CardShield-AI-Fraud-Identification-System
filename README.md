<p align="center"> <img src="https://img.shields.io/badge/CardShield%20AI-Fraud%20Identification%20System-blueviolet?style=for-the-badge&logo=python&logoColor=white" /> </p> <h1 align="center">🔐 CardShield AI – Fraud Identification System</h1> <p align="center"> An advanced, end-to-end Machine Learning pipeline for detecting fraudulent credit card transactions using SMOTE, feature scaling, and optimized classification models. </p>

# 🚀 Project Overview
CardShield AI is a complete fraud-detection system built using machine learning to classify credit card transactions as fraudulent or legitimate.
The system applies:
- ✔ Data Cleaning & Preprocessing
- ✔ Handling Class Imbalance using SMOTE
- ✔ Feature Scaling
- ✔ Train–Test Splitting
- ✔ Model Training (LR, RF)
- ✔ Performance Evaluation
This project follows a clean, modular, industry-style ML pipeline suitable for deployment or integration into financial software.

<h2>📁 CardShield-AI – Project Structure</h2>
<pre>
CardShield-AI/
│
├── <b>CardShield AI – Fraud Identification System.ipynb</b>     # Main Jupyter Notebook
│
├── <b>CardShield.py</b>                                         # Primary Python script
├── <b>CardShield2.py</b>                                        # Secondary test script
│
├── <b>creditcard.xlsx</b>                                       # Dataset
│
├── <b>model.pkl</b>                                             # Trained Random Forest model
├── <b>scaler.pkl</b>                                            # StandardScaler object
│
├── <b>requirements.txt</b>                                      # Required dependencies
└── <b>README.md</b>                                             # Documentation
</pre>


# 📂 Dataset
This notebook uses the popular Credit Card Fraud Detection Dataset, containing:
- 284,807 transactions
- 492 fraud cases
- Highly imbalanced data
- All features V1–V28 are PCA-transformed components
- Amount, Time, and target variable Class

# 📊 Project Pipeline
**1️⃣ Data Preprocessing**
- Remove null values
- Statistical analysis (describe())
- Feature inspection

**2️⃣ Handling Imbalance**
- Due to only 0.17% fraud cases, SMOTE is applied to oversample the minority class.

**3️⃣ Feature Scaling**
StandardScaler used for:
- Amount
- Time

**4️⃣ Model Training**
Implemented models:
- Logistic Regression
- Random Forest Classifier (Optimized: n_estimators=500)

# 🤖 Best Performing Model (Recommended)

<h2> 
    <pre> RandomForestClassifier(
    n_estimators=500,
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=42,
    n_jobs=-1
) 
</pre>

# 📈 Evaluation Metrics
The model is evaluated using:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

(Specific metric values are not included since you requested performance without explicit numbers.)

# 🛠 Technologies Used
- Python
- Pandas, NumPy
- scikit-learn
- SMOTE (imblearn)
- Matplotlib / Seaborn
- Jupyter Notebook

# 🌟 Key Features
- ✔ Handles severe class imbalance
- ✔ Optimized Random Forest model
- ✔ Clean, modular ML pipeline
- ✔ Scalable & production-friendly
- ✔ Fully interpretable workflow

# 📜 Conclusion
**CardShield AI successfully identifies fraudulent credit card transactions using a robust machine-learning workflow.
By balancing the dataset with SMOTE and applying optimized models, the system achieves strong fraud-detection performance while maintaining reliability and interpretability.**

This project can be extended into real-time fraud detection systems or banking-level transaction monitoring tools.

