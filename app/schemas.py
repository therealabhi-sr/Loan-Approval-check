from pydantic import BaseModel,Field

class LoanRequestSchema(BaseModel):
    age: int=Field(...,ge=18,le=70)
    income: float=Field(...,ge=0)
    credit_score: int=Field(...,ge=0)
    employment_years: float=Field(...,ge=0)
    existing_loans: int=Field(...,ge=0)

class ResponseSchema(BaseModel):
    approved: bool
    risk_score: float
    decision: str



