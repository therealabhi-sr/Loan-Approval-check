from fastapi import FastAPI,HTTPException
from app.schemas import LoanRequestSchema,ResponseSchema
from app.errors import ErrorResponse
from app.services import calculate_risk_score,make_decision

app=FastAPI(title="Loan Approval APi")

AVAILABLE_MODELS=["rule_based_v1"]

@app.get("/health")
def result():
    return{"status":"ok"}

@app.get("/models")
def models():
    return AVAILABLE_MODELS

@app.post(
    "/predict/{model_name}",
    response_model=ResponseSchema,
    responses={404:{"model":ErrorResponse},
               400:{"model":ErrorResponse}}
)
def predict(model_name:str,req:LoanRequestSchema):
    if model_name not in AVAILABLE_MODELS:
        raise HTTPException(
            status_code=400,
            detail={
                "error_code": "MODEL_NOT_FOUND",
                "message": "Model not found"
            }
        )
    if req.income<1000:
        raise HTTPException(
            status_code=404,
            detail={
                "error_code": "LOW_INCOME",
                "message": "Income too low"
            }
        )

    score = calculate_risk_score(
        req.income,
        req.credit_score,
        req.employment_years,
        req.existing_loans
    )
    decision = make_decision(score)
    return {
        "approved": decision=="APPROVED",
        "risk_score": score,
        "decision": decision
    }  
