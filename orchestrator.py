import time
from agent import fraud_agent

class MockMaestroOrchestrator:
    def __init__(self):
        self.cases = {}
        print("🚀 UiPath Mock Maestro Orchestrator Initialized")

    def create_case(self, claim_data):
        """Simulates Intake Stage via Document Understanding."""
        case_id = f"CASE-{int(time.time())}"
        print(f"\n[Maestro: INTAKE] Document parsed. Creating case {case_id}...")
        self.cases[case_id] = {
            "status": "Investigation",
            "data": claim_data
        }
        return case_id

    def run_investigation(self, case_id):
        """Simulates Investigation Stage calling the Coded Agent."""
        print(f"[Maestro: INVESTIGATION] Sending {case_id} to Coded Agent (Fraud Detection)...")
        case = self.cases[case_id]
        
        # Invoke the LangGraph Agent
        result = fraud_agent.invoke(case["data"])
        
        # Update case with agent findings
        case["agent_results"] = result
        
        if result["is_fraudulent"]:
            print(f"⚠️ [Maestro: EXCEPTION] High risk detected! Routing to Human-in-the-Loop Action Center.")
            case["status"] = "Pending Human Approval"
        else:
            print(f"✅ [Maestro: AUTO-APPROVAL] Low risk. Routing to Settlement.")
            case["status"] = "Settlement"

    def settle_case(self, case_id):
        """Simulates Settlement Stage."""
        case = self.cases[case_id]
        if case["status"] == "Settlement":
            print(f"[Maestro: SETTLEMENT] Processing payment for {case_id}... Done.")
            case["status"] = "Closed"
        elif case["status"] == "Pending Human Approval":
            print(f"[Maestro: SETTLEMENT] Cannot settle {case_id}. Awaiting human review in Action Center.")
            
if __name__ == "__main__":
    orchestrator = MockMaestroOrchestrator()
    
    # Simulate a high-risk claim
    high_risk_claim = {
        "claim_id": "CLM-999",
        "claim_amount": 25000.0,
        "claim_description": "Whiplash and severe back pain.",
        "risk_score": 0.0, "is_fraudulent": False, "agent_reasoning": ""
    }
    
    case1 = orchestrator.create_case(high_risk_claim)
    orchestrator.run_investigation(case1)
    orchestrator.settle_case(case1)
    
    # Simulate a low-risk claim
    low_risk_claim = {
        "claim_id": "CLM-111",
        "claim_amount": 500.0,
        "claim_description": "Minor scratch on bumper.",
        "risk_score": 0.0, "is_fraudulent": False, "agent_reasoning": ""
    }
    
    case2 = orchestrator.create_case(low_risk_claim)
    orchestrator.run_investigation(case2)
    orchestrator.settle_case(case2)
