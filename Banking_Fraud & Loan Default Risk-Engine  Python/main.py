from src.engine import PurePythonRiskEngine
from src.generator import DataGenerator

if __name__ == "__main__":
  print("Starting Pure Python Financial Risk Engine...")

  # Generate Data using standard libraries
  generator = DataGenerator()
  generator.generate_records(num_records=1000)

  # Run Custom Python Risk & Fraud Engine
  engine = PurePythonRiskEngine()
  engine.evaluate_portfolio()

  print("Execution Complete!")