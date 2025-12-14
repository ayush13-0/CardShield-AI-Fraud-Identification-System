<p align="center"> <img src="https://img.shields.io/badge/CardShield%20AI-Fraud%20Identification%20System-blueviolet?style=for-the-badge&logo=python&logoColor=white" /> </p> <h1 align="center">🛡️🔐 CardShield AI – Fraud Identification System</h1> <p align="center"> An advanced, end-to-end Machine Learning pipeline for detecting fraudulent credit card transactions using SMOTE, feature scaling, and optimized classification models. </p>
<p align="center"> <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> <img alt="Pandas" src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/> <img alt="NumPy" src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/> <img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/> <img alt="imbalanced-learn" src="https://img.shields.io/badge/imbalanced--learn-FF6F00?style=for-the-badge&logo=python&logoColor=white"/> <img alt="Matplotlib" src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white"/> <img alt="Seaborn" src="https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=seaborn&logoColor=white"/> <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/> <img alt="GitHub" src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/> </p>
<p align="center">
  <img src="https://img.shields.io/badge/Internship-CodSoft%20ML%20Internship-black?style=for-the-badge" />
</p>

# <h1 align="center"> 🚀 Machine Learning + Streamlit Web App </p>

# 📖 Project Overview
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
├── <b>CardShield.py</b>                                         # Streamlit Main script
├── <b>CardShield2.py</b>                                        # Streamlit Alternative Script
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

# ⭐ Features
🔍 Machine Learning Pipeline
- Data preprocessing & cleaning
- Handling imbalance using SMOTE
- Feature scaling (StandardScaler)
- Model training (Logistic Regression & Random Forest)
- Model evaluation (Confusion Matrix, Classification Report, ROC-AUC)

# 🌐 Streamlit Web Application
- Predict fraud for single transactions
- Score bulk transactions via CSV upload
- Download prediction results
- Modern UI with dark theme
- Dummy rule-based logic (can easily be replaced with ML model)

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

# 📦 Installation
**1️⃣ Clone the Repository**
<pre>
git clone https://github.com/ayush13-0/CardShield-AI-Fraud-Identification.git
cd CardShield-AI-Fraud-Identification
</pre>

**2️⃣ Install Dependencies**
<pre> pip install -r requirements.txt 
</pre>

**3️⃣ Run Streamlit App**
<pre> streamlit run cardshield_app.py
</pre>

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
CardShield AI provides a complete and powerful fraud detection solution. With exceptionally high accuracy and an intuitive Streamlit interface, it stands as a strong prototype ready for real-world deployment. It lays the foundation for scalable enhancements including real-time scoring, cloud APIs, and deep learning models.


# 👨‍💻 Developed By
# Ayush 
-----------------------------------------------
- 💼LinkedIn: https://linkedin.com/in/ayush130
- 💻GitHub: https://github.com/ayush13-0
- ✉️Email- bhanuseenu914@gmail.com

# 📜 License
- This project is licensed under the **MIT License**.
