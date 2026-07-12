from fastapi import FastAPI
import pickle
from pydantic import BaseModel, Field
from typing import Literal

app = FastAPI(title="Credit Risk Prediction API")

# Defining the input data model
class InputData(BaseModel):
    loan_amount: float=Field(..., gt=0)
    education: Literal[0, 1]
    residential_assets_value: float
    luxury_assets_value: float
    loan_tenure: int=Field(..., gt=0)
    annual_income: float
    bank_asset_value: float
    self_employed: Literal[0, 1]
    cibil_score: int=Field(..., ge=300, le=900)
    dependents: int
    commercial_assets_value: float

# Loading the pre-trained model
with open('Model.pickle', 'rb') as f:
    model = pickle.load(f)

# Defining the prediction endpoint
@app.post('/predict')
def predict(input_data: InputData):

    # Calculating derived features
    loan_to_income=input_data.loan_amount/input_data.annual_income
    assets_to_loan=(input_data.residential_assets_value + input_data.commercial_assets_value + input_data.luxury_assets_value + input_data.bank_asset_value)/input_data.loan_amount
    estimated_EMI=input_data.loan_amount/(input_data.loan_tenure*12)
    EMI_isto_income=(estimated_EMI/(input_data.annual_income/12))
    def categorise_cibil_score(x):
        if x>=300 and x<=579:
            return 1
        elif x>=800 and x<=900:
            return 5
        elif x>=670 and x<=739:
            return 3
        elif x>=740 and x<=799:
            return 4
        else:
            return 2
    cibil_score=categorise_cibil_score(input_data.cibil_score)
    
    # Final input data for prediction
    model_input = [[input_data.dependents, input_data.education, input_data.self_employed, cibil_score, 
                    input_data.loan_tenure, loan_to_income, assets_to_loan, EMI_isto_income]]
    
    # Making prediction using the loaded model
    prediction = model.predict(model_input)

    # Returning the prediction result
    return {"prediction": prediction.tolist()}