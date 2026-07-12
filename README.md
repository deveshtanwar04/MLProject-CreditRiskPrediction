# 🏦 Credit Risk & Default Prediction Engine

**Automated Underwriting & Borrower Assessment System**  
An end-to-end Machine Learning project transitioning from raw CSV data to a fully deployed, decoupled microservices architecture.

[![Live App](https://img.shields.io/badge/Live_App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://credit-risk-pred-engine.streamlit.app/)
[![API Backend](https://img.shields.io/badge/API_Backend-FastAPI-009688?style=for-the-badge&logo=fastapi)](https://credit-risk-pred-engine.fastapicloud.dev/docs)
[![Kaggle](https://img.shields.io/badge/Kaggle-Notebook-20BEFF?style=for-the-badge&logo=Kaggle)](https://www.kaggle.com/code/deveshtanwar/loan-approv-data-cleaning-feature-eng-model)

## 📌 Overview
This project is a comprehensive Machine Learning pipeline designed to assess credit risk and predict loan defaults. By analyzing borrower demographics, income streams, collateral assets, and credit history, the engine automates the underwriting process and flags high-risk applications in real time. 

Built with the Kaggle Loan Approval dataset, the project emphasizes model accuracy, realistic financial logic, and **production-grade software architecture**.

## 🏗️ System Architecture (Microservices Upgrade)
To mimic real-world enterprise environments, the application was upgraded from a monolithic script into a decoupled, two-part microservice architecture:
* **The Backend (FastAPI):** A dedicated RESTful API hosted on **FastAPI Cloud**. It handles strict data validation via Pydantic, executes the ML feature engineering, and serves predictions from the serialized model.
* **The Frontend (Streamlit):** A lightweight client UI hosted on **Streamlit Community Cloud**. It collects user inputs, sends JSON payloads to the API via HTTP POST requests, and renders the risk assessment.
* **Why this matters:** This separation of concerns allows the ML model to scale independently and makes the Prediction API accessible to other web or mobile applications.

## 🧠 Model Development & Stress Testing

**1. The Baseline Model (Logistic Regression)**
* **Metrics:** F1 Score: 0.935 | Precision: 0.972
* **The Problem:** Despite excellent test-split metrics, **stress-testing the model with manually and AI-crafted edge-case inputs** revealed fatal flaws. The model drastically over-weighted the CIBIL score and learned misleading linear correlations (e.g., *Higher loan amount → higher approval probability*). 

**2. The Final Model (Random Forest Classifier)**
* Instead of forcing fixes on the linear model, I pivoted to a Random Forest architecture.
* **The Fix:** The tree-based model successfully captured non-linear relationships, handled outliers naturally, and evaluated Debt-to-Income (DTI) and Asset-to-Loan ratios with realistic underwriting logic.
* **Final Metrics:** **F1 Score: 0.963 | Precision: 0.997**

## 🚀 Key Features

* **Strict API Data Validation:** Utilizes Pydantic models to enforce data types and constraints (e.g., preventing negative incomes or zero-division errors) before the data ever reaches the ML model.
* **Financial Feature Engineering:** Custom underwriting metrics calculated dynamically in the API layer:
  * **EMI-to-Income Ratio (DTI):** Evaluates monthly debt burden.
  * **Asset-to-Loan Ratio:** Assesses collateral coverage.
  * **CIBIL Score Binning:** Categorizes raw credit scores into standardized risk tiers.
* **Interactive UI:** A highly intuitive, column-structured frontend allowing underwriters to instantly generate approval/rejection decisions based on API confidence scores.

## 🛠️ Tech Stack

* **Language:** Python
* **Backend Framework:** FastAPI, Pydantic
* **Frontend Framework:** Streamlit, Requests
* **Machine Learning:** Scikit-Learn, Pandas, NumPy, Pickle
* **Cloud Infrastructure:** FastAPI Cloud (API), Streamlit Community Cloud (UI)

## 📂 Project Structure

```text
├── backend/
│   ├── api.py                 # FastAPI server and inference logic
│   ├── Model.pickle           # Serialized Random Forest pipeline
│   ├── pyproject.toml         # Build configuration
│   └── requirements.txt       # Backend ML dependencies
├── frontend/
│   ├── app.py                 # Streamlit UI client
│   └── requirements.txt       # Frontend dependencies (streamlit, requests)
├── Loan Approval Prediction NB.ipynb
└── README.md