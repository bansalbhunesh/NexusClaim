import json
import sys
import os

# Import our NexusClaim fraud agent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agent import fraud_agent

def run_plyson_tests():
    print("Starting Route 2: Plyson Declarative Test Runner")
    
    with open('tests.json', 'r') as f:
        schema = json.load(f)
        
    print(f"Loaded Project: {schema['project_name']}")
    
    total_tests = 0
    passed_tests = 0
    
    for suite in schema['test_suites']:
        print(f"\nRunning Suite: {suite['suite_name']}")
        
        for idx, test in enumerate(suite['test_cases']):
            total_tests += 1
            print(f"  Test {idx+1}: {test['test_name']}")
            
            # Setup payload
            payload = {
                "claim_id": f"TEST-{idx}",
                "claim_amount": test['input']['claim_amount'],
                "claim_description": test['input']['claim_description']
            }
            
            # Execute Agent
            result = fraud_agent.invoke(payload)
            
            # Assertions
            passed = True
            
            # Check fraud boolean
            if result['is_fraudulent'] != test['expected_fraudulent']:
                print(f"    ❌ FAILED: Expected is_fraudulent={test['expected_fraudulent']}, got {result['is_fraudulent']}")
                passed = False
                
            # Check score boundaries
            if 'expected_max_score' in test and result['risk_score'] > test['expected_max_score']:
                print(f"    ❌ FAILED: Score {result['risk_score']} exceeded max {test['expected_max_score']}")
                passed = False
                
            if 'expected_min_score' in test and result['risk_score'] < test['expected_min_score']:
                print(f"    ❌ FAILED: Score {result['risk_score']} fell below min {test['expected_min_score']}")
                passed = False
                
            if passed:
                print(f"    ✅ PASSED (Score: {result['risk_score']})")
                passed_tests += 1
                
    print(f"\n🎯 Route 2 Test Summary: {passed_tests}/{total_tests} Passed")

if __name__ == "__main__":
    run_plyson_tests()
