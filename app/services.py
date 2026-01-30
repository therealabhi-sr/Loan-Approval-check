def calculate_risk_score(
    income: float,
    credit_score: int,
    employment_years: int,
    existing_loans:int
    ) -> float:
    score = (
        (credit_score / 850) * 0.4 +
        (income / 100000) * 0.3 +
        (employment_years / 30) * 0.2 -
        (existing_loans * 0.05)
    )
    return score

def make_decision(score: float) ->str:
    if score >= 0.60:
        return "APPROVED"
    else:
        return "REJECTED"

