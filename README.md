# Loan Approval API (FastAPI)

A rule-based ML-style backend service built using FastAPI that evaluates
loan eligibility based on applicant financial and credit information.\
This project demonstrates production-style API design, input validation,
service-layer separation, and response control.

------------------------------------------------------------------------

## 🚀 Features

-   FastAPI framework\
-   Pydantic schema validation\
-   ML-style decision logic\
-   Clean project structure\
-   Response filtering using response models\
-   Structured error handling\
-   Swagger UI documentation

------------------------------------------------------------------------

## 🧱 Project Structure

loan_api/ │ ├── app/ │ ├── main.py \# API routes │ ├── schemas.py \#
Request & Response models │ ├── services.py \# Business logic │ ├──
errors.py \# Error schemas │ ├── requirements.txt └── README.md

------------------------------------------------------------------------

## ⚙️ Tech Stack

-   Python 3.10+\
-   FastAPI\
-   Uvicorn\
-   Pydantic

------------------------------------------------------------------------

## 📦 Setup Instructions

Create virtual environment:

python -m venv venv

Activate:

Windows: venv`\Scripts`{=tex}`\activate`{=tex}

Linux / Mac: source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

------------------------------------------------------------------------

## ▶️ Run Server

uvicorn app.main:app --reload

Open in browser:

http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## 🔍 Available Endpoints

### Health Check

GET /health

Response: { "status": "ok" }

------------------------------------------------------------------------

### List Models

GET /models

Response: \["rule_based_v1"\]

------------------------------------------------------------------------

### Loan Prediction

POST /predict/{model_name}

Example: POST /predict/rule_based_v1

Request Body:

{ "age": 30, "income": 60000, "credit_score": 720, "employment_years":
5, "existing_loans": 1 }

Response:

{ "approved": false, "risk_score": 0.502, "decision": "REJECTED" }

------------------------------------------------------------------------

## 🧠 Decision Logic

risk_score = (credit_score / 850) \* 0.4 + (income / 100000) \* 0.3 +
(employment_years / 30) \* 0.2 - (existing_loans \* 0.05)

If risk_score \>= 0.6 → APPROVED\
Else → REJECTED

------------------------------------------------------------------------

## 🚨 Error Examples

Unknown Model:

{ "detail": { "error_code": "MODEL_NOT_FOUND", "message": "Model not
found" } }

Low Income:

{ "detail": { "error_code": "LOW_INCOME", "message": "Income too low" }
}

------------------------------------------------------------------------

## 🎯 Learning Outcomes

-   Backend ML API design\
-   Validation-driven development\
-   Separation of concerns\
-   Production-style FastAPI patterns

------------------------------------------------------------------------

## 📌 Future Improvements

-   Add real trained ML model\
-   Add unit tests\
-   Add Docker support\
-   Add authentication

------------------------------------------------------------------------

## 👤 Author

Abhishek\
Computer Science & Engineering Student\
Aspiring AI/ML Engineer
