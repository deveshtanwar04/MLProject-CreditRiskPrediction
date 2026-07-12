import streamlit as st
import requests
import time

API_URL = "http://127.0.0.1:8000/predict"

# ---------- PAGE CONFIG ----------
# Sets the browser tab title and widens the layout
st.set_page_config(page_title="Credit Risk Engine", page_icon="🏦", layout="wide")

# ---------- TITLE SECTION ----------
st.markdown(
    "<h1 style='text-align: center;'>🏦 Credit Risk & Default Prediction Engine</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; color: white;'>Automated Underwriting & Borrower Assessment System</p>",
    unsafe_allow_html=True
)
st.divider()

# ---------- FORM SECTION ----------
with st.form("input_form"):
    # UI Upgrade: Logical grouping of inputs
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 👤 Applicant Info")
        annual_income = st.number_input("Annual Income (₹): ", min_value=100000, step=10000, max_value=50000000)
        cibil_score = st.number_input("CIBIL Score: ", min_value=300, step=10, max_value=900)
        dependents = st.number_input("No. of Dependents: ", min_value=0, step=1, max_value=10)
        education = 1 if st.selectbox("Education: ", options=["Not Graduate", "Graduate"]) == 'Graduate' else 0
        self_employed = 0 if st.selectbox("Employment Status: ", options=["Self-employed", "Salaried"]) == 'Self-employed' else 1

    with col2:
        st.markdown("#### 🏠 Asset Declaration")
        residential_assets_value = st.number_input("Residential Assets (₹): ", min_value=0, step=10000)
        commercial_assets_value = st.number_input("Commercial Assets (₹): ", min_value=0, step=10000)
        luxury_assets_value = st.number_input("Luxury Assets (₹): ", min_value=0, step=10000)
        bank_asset_value = st.number_input("Bank Assets (₹): ", min_value=0, step=10000)
    
    with col3:
        st.markdown("#### 📝 Loan Details")
        loan_amount = st.number_input("Loan Amount (₹): ", min_value=10000, step=10000  , max_value=100000000)
        loan_tenure = st.number_input("Loan Tenure (Years): ", min_value=1, step=1, max_value=30)
    

    st.write("") # Adding little space before the submit button
    submit = st.form_submit_button("Run Risk Assessment", use_container_width=True)


# ---------- OUTPUT ----------
if submit:
    input_data = {
        "loan_amount": loan_amount,
        "education": education,
        "residential_assets_value": residential_assets_value,
        "luxury_assets_value": luxury_assets_value,
        "loan_tenure": loan_tenure,
        "annual_income": annual_income,
        "bank_asset_value": bank_asset_value,
        "self_employed": self_employed,
        "cibil_score": cibil_score,
        "dependents": dependents,
        "commercial_assets_value": commercial_assets_value
    }

    with st.spinner("Analyzing applicant data via API..."):
        try:
            time.sleep(1)
            response = requests.post(API_URL, json=input_data)
            response.raise_for_status() # Check for HTTP errors
            
            result = response.json()
            prediction = result["prediction"][0]

            st.divider()

            if prediction == 1:
                st.success("**Low Default Risk: Loan Approved**", icon="✅")
                st.write("<p style='text-align: center; color: gray;'>The loan application has been approved based on the low default risk assessment.</p>", unsafe_allow_html=True)
            else:
                st.error("**High Default Risk: Loan Rejected**", icon="❌")
                st.write("<p style='text-align: center; color: gray;'>Please review the applicant's financials and consider alternative collateral options.</p>", unsafe_allow_html=True)
            

            st.divider()
            st.write("")
            st.write("")
            st.divider()
            with st.expander("View Raw API Response"):
                st.json(result)

        except requests.exceptions.ConnectionError:
            st.error("🚨 **Connection Error:** Could not connect to the API...")
        except Exception as e:
            st.error(f"⚠️ **Error:** {e}")