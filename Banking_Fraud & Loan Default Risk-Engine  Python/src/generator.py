import csv
import random


class DataGenerator:

  def __init__(self, filename="data/bank_records.csv"):
    self.filename = filename

  def generate_records(self, num_records=500):
    random.seed(42)
    headers = [
        "applicant_id","age",
        "annual_income","credit_score",
        "loan_amount","debt_to_income_ratio",
        "transaction_amount","is_fraudulent","default_risk",
    ]

    rows = []
    for i in range(1, num_records + 1):
      applicant_id = 10000 + i
      age = random.randint(21, 65)
      annual_income = random.randint(25000, 150000)
      credit_score = random.randint(580, 850)
      loan_amount = random.randint(5000, 50000)
      debt_to_income_ratio = round(random.uniform(0.1, 0.6), 2)
      transaction_amount = random.randint(100, 5000)

      # Realistic logic for risk triggers
      is_fraudulent = (
          1 if transaction_amount > 4000 and credit_score < 620
          else 0
      )
      default_risk = (
          1
          if (credit_score < 630 or debt_to_income_ratio > 0.45)
          and loan_amount > 30000
          else 0
      )

      rows.append([
          applicant_id,
          age,
          annual_income,
          credit_score,
          loan_amount,
          debt_to_income_ratio,
          transaction_amount,
          is_fraudulent,
          default_risk,
      ])

    with open(self.filename, mode="w", newline="") as file:
      writer = csv.writer(file)
      writer.writerow(headers)
      writer.writerows(rows)

    print(
        f"Successfully generated {num_records} pure Python records in"
        f" {self.filename}"
    )