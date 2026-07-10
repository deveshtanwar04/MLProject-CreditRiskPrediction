# 🏦 Credit Risk & Default Prediction Engine

**Automated Underwriting & Borrower Assessment System**  
An end-to-end Machine Learning project taking data from raw CSV to a fully deployed, interactive web application.

[![Live App](https://img.shields.io/badge/Live_App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://mlproject-loanapprovalpred.streamlit.app/)
[![Kaggle](https://img.shields.io/badge/Kaggle-Notebook-20BEFF?style=for-the-badge&logo=Kaggle)](https://www.kaggle.com/code/deveshtanwar/loan-approv-data-cleaning-feature-eng-model)

## 📌 Overview
This project is a comprehensive Machine Learning pipeline designed to assess credit risk and predict loan defaults. By analyzing borrower demographics, income streams, collateral assets, and credit history, the engine automates the underwriting process and flags high-risk applications in real time. 

Built with the Kaggle Loan Approval dataset, the project emphasizes not just model accuracy, but **model behavior, realistic logic, and production deployment**.

## 🧠 Model Development

**1. The Baseline Model (Logistic Regression)**
* **Metrics:** F1 Score: 0.935 | Precision: 0.972
* **The Problem:** Despite excellent test-split metrics, **stress-testing the model with manually and AI crafted edge-case inputs** revealed fatal flaws. The model was drastically over-weighting the CIBIL score and learned misleading linear correlations (e.g., *Higher loan amount → higher approval probability*). 

**2. The Final Model (Random Forest Classifier)**
* Instead of forcing fixes on the linear model, I pivoted to a Random Forest architecture.
* **The Fix:** The tree-based model successfully captured non-linear relationships, handled outliers naturally, and evaluated Debt-to-Income (DTI) and Asset-to-Loan ratios with realistic underwriting logic.
* **Final Metrics:** **F1 Score: 0.963 | Precision: 0.997**

## 🚀 Key Features

* **Financial Feature Engineering:** Created custom underwriting metrics to give the model better financial context:
  * **EMI-to-Income Ratio (DTI):** Evaluates monthly debt burden.
  * **Asset-to-Loan Ratio:** Assesses collateral coverage.
  * **CIBIL Score Binning:** Categorizes raw credit scores into standardized risk tiers.
* **Robust ML Pipeline:** Utilized Scikit-Learn's `Pipeline` to seamlessly handle data scaling and model prediction without data leakage.
* **Interactive Web App:** A fully functional UI built in pure Python, allowing users/industries to input applicant data and receive an instant *Approve/Reject* decision based on default risk.

## 🛠️ Tech Stack

* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Random Forest, Pipelines)
* **Web Deployment:** Streamlit Community Cloud
* **Serialization:** Pickle

## 🌐 Production & Deployment
Taking a model from a Jupyter Notebook to a live application introduces a new set of challenges. During deployment, I navigated and resolved:
* Library version mismatches between local environments and the cloud server.
* Environment dependency errors (`requirements.txt` configurations).
* Streamlit-specific caching and state management bugs.
