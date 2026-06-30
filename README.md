# 💳 Credit Card Fraud Detection Web Application

A Machine Learning-powered web application that detects fraudulent credit card transactions in real time. This project uses **Scikit-learn**, **XGBoost**, and **SMOTE** to build a high-performance fraud detection model and deploys it through a **Flask** web application with a modern user interface.

---

## 📌 Project Overview

Credit card fraud is one of the major challenges in digital banking and online transactions. Due to the highly imbalanced nature of fraud datasets, traditional classification algorithms often fail to detect fraudulent transactions accurately.

This project addresses this challenge by applying data preprocessing, handling class imbalance using **SMOTE (Synthetic Minority Over-sampling Technique)**, training machine learning models, and deploying the best-performing model as an interactive web application.

---

## ✨ Features

* 🔍 Detects fraudulent credit card transactions
* 🤖 Machine Learning-based prediction
* ⚖️ Handles imbalanced data using SMOTE
* 🚀 Fast predictions using Flask backend
* 🎨 Modern and responsive web interface
* 📊 Model evaluation with ROC-AUC and Confusion Matrix
* 💾 Saved trained model for instant inference
* 📱 Easy to run locally

---

## 🛠 Tech Stack

### Machine Learning

* Python
* Scikit-learn
* XGBoost
* Pandas
* NumPy
* Imbalanced-learn (SMOTE)

### Backend

* Flask

### Frontend

* HTML5
* CSS3
* JavaScript

### Visualization

* Matplotlib
* Seaborn

---

## 📂 Project Structure

```text
Credit-Card-Fraud-Detection/
│
├── app.py                  # Flask application
├── model.pkl               # Trained ML model
├── scaler.pkl              # Feature scaler (if used)
├── requirements.txt
├── README.md
│
├── dataset/
│   └── creditcard.csv
│
├── notebooks/
│   └── model_training.ipynb
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│
├── models/
│   └── training.py
│
└── screenshots/
    ├── home.png
    ├── prediction.png
    └── confusion_matrix.png
```

---

## 📊 Dataset

This project uses the **Credit Card Fraud Detection Dataset** containing anonymized transactions made by European cardholders.

### Dataset Information

* Total Transactions: **284,807**
* Fraudulent Transactions: **492**
* Features: **30**
* Target Variable:

  * **0** → Legitimate Transaction
  * **1** → Fraudulent Transaction

---

## ⚙️ Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Feature Scaling
4. Handle Class Imbalance using SMOTE
5. Train-Test Split
6. Train Machine Learning Models
7. Evaluate Models
8. Save Best Model
9. Deploy using Flask

---

## 🧠 Algorithms Used

* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost (Best Performing Model)

---

## 📈 Evaluation Metrics

The trained model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC Score
* Confusion Matrix

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/credit-card-fraud-detection.git

cd credit-card-fraud-detection
```

### 2. Create a Virtual Environment (Optional)

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

## 💻 How to Use

1. Launch the Flask application.
2. Open the web interface.
3. Enter the required transaction details.
4. Click **Predict**.
5. The application displays whether the transaction is **Legitimate** or **Fraudulent**.

---

## 📸 Screenshots

Add screenshots of your application inside the `screenshots/` folder.

Example:

```text
screenshots/
├── home.png
├── prediction.png
├── confusion_matrix.png
├── roc_curve.png
```

Then display them like this:

```markdown
## Home Page

![Home](screenshots/home.png)

## Prediction Result

![Prediction](screenshots/prediction.png)

## Confusion Matrix

![Confusion Matrix](screenshots/confusion_matrix.png)
```

---

## 📌 Future Improvements

* Deep Learning models (LSTM, Autoencoders)
* Real-time transaction monitoring
* Explainable AI (SHAP/LIME)
* REST API integration
* Cloud deployment (AWS, Azure, GCP)
* Docker containerization
* User authentication and dashboard
* Continuous model retraining

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Your Name**

* GitHub: https://github.com/your-username
* LinkedIn: https://linkedin.com/in/your-profile

---

## ⭐ Support

If you found this project helpful:

* ⭐ Star this repository
* 🍴 Fork the project
* 💡 Share your feedback
* 🛠 Contribute to improvements

---

### Thank you for visiting this project! 🚀
