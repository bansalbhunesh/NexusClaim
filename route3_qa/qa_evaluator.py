import csv
import sys
import os

# Import our NexusClaim fraud agent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agent import fraud_agent

def run_qa_evaluator():
    print("Starting Route 3: QA-Agent Data-Driven Evaluator")
    
    csv_file = os.path.join(os.path.dirname(__file__), 'QASheet.csv')
    total_tests = 0
    passed_tests = 0
    
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            total_tests += 1
            claim_id = row['claim_id']
            amount = float(row['amount'])
            description = row['description']
            expected_fraud = row['expected_fraud'].lower() == 'true'
            
            print(f"  Evaluating {claim_id} (${amount})...")
            
            # Setup payload
            payload = {
                "claim_id": claim_id,
                "claim_amount": amount,
                "claim_description": description
            }
            
            # Execute Agent
            result = fraud_agent.invoke(payload)
            
            # Assertions
            if result['is_fraudulent'] == expected_fraud:
                print(f"    ✅ MATCH (Agent says: {result['is_fraudulent']})")
                passed_tests += 1
            else:
                print(f"    ❌ MISMATCH! Expected {expected_fraud}, but agent said {result['is_fraudulent']}")
                
    print(f"\n🎯 Route 3 QA Summary: {passed_tests}/{total_tests} Accuracy")

if __name__ == "__main__":
    run_qa_evaluator()
