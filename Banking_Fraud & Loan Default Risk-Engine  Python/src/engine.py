import csv
import statistics


class PurePythonRiskEngine:

  def __init__(self, filename="data/bank_records.csv"):
    self.filename = filename
    self.records = self._load_data()

  def _load_data(self):
    records = []
    with open(self.filename, mode="r") as file:
      reader = csv.DictReader(file)
      for row in reader:
        # Cast data types correctly from strings
        records.append({
            "applicant_id": int(row["applicant_id"]),
            "age": int(row["age"]),
            "annual_income": int(row["annual_income"]),
            "credit_score": int(row["credit_score"]),
            "loan_amount": int(row["loan_amount"]),
            "debt_to_income_ratio": float(row["debt_to_income_ratio"]),
            "transaction_amount": int(row["transaction_amount"]),
            "is_fraudulent": int(row["is_fraudulent"]),
            "default_risk": int(row["default_risk"]),
        })
    return records

  def calculate_risk_score(self, applicant):
    """Computes a risk score from 0 (Low Risk) to 100 (High Risk)

    using a custom banking scorecard algorithm.
    """
    score = 0

    # Credit Score factor 
    
    cs = applicant["credit_score"]
    if cs < 620:
      score += 40
    elif cs < 680:
      score += 25
    else:
      score += 5

    # Debt to-Income factor
    
    dti = applicant["debt_to_income_ratio"]
    if dti > 0.4:
      score += 30
    elif dti > 0.3:
      score += 15
    else:
      score += 5

    # Loan to-Income factor
    
    lti = applicant["loan_amount"] / applicant["annual_income"]
    if lti > 0.4:
      score += 30
    else:
      score += 10

    return min(score, 100)

  def evaluate_portfolio(self):
    total_applicants = len(self.records)
    fraud_flags = 0
    high_default_risk_count = 0

    print("- Running Pure Python Portfolio Evaluation...")
    for app in self.records:
      risk_score = self.calculate_risk_score(app)

      # Flag potential defaults (Risk score >= 65)
      if risk_score >= 65:
        high_default_risk_count += 1

      # Flag transaction anomalies (Fraud detection rules)
      if (
          app["transaction_amount"] > 3500
          and app["credit_score"] < 640
          and app["is_fraudulent"] == 1
      ):
        fraud_flags += 1

    print(f"Total Applicants Processed: {total_applicants}")
    print(f"High Default Risk Flagged: {high_default_risk_count}")
    print(f"Detected Fraud Patterns: {fraud_flags}")

    # Compute portfolio summary statistics
    incomes = [r["annual_income"] for r in self.records]
    print(f"Average Annual Income: ${statistics.mean(incomes):,.2f}")
    print(f"Median Annual Income: ${statistics.median(incomes):,.2f}")