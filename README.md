# NexusClaim: Intelligent Insurance Case Orchestration

NexusClaim is an end-to-end agentic solution for complex, exception-heavy insurance claims. It is designed for **Track 1: UiPath Maestro Case** of the UiPath AgentHack.

## 🚀 Overview
When insurance claims are submitted, they are often processed manually due to unpredictable exceptions (fraud, missing documents, etc.). NexusClaim solves this by utilizing **UiPath Maestro Case** to govern the lifecycle of a claim, delegating reasoning to a LangGraph-based **Coded Agent**.

### Key Features
- **Intake:** Simulates Document Understanding (IDP) parsing claims into structured data.
- **Agentic Investigation:** A Coded Agent (using LangGraph and Python SDK) evaluates the claim for high-risk fraud signals (e.g., specific injury keywords or high amounts).
- **Human-in-the-Loop:** If the Coded Agent detects a high-risk claim, Maestro automatically halts the case and routes it to the Action Center for human approval. Low-risk claims are automatically routed to Settlement.

## 🤖 Coding Agent Bonus (AI-Assisted Development)
This project was entirely scaffolded, written, and tested using **Antigravity (a Claude-powered Coding Agent)**.

### Verifiable Evidence
- **Tool Used:** Antigravity (Claude-based coding assistant)
- **Contribution:** The coding agent designed the architecture, wrote the `agent.py` LangGraph implementation, and created the `orchestrator.py` local Maestro simulator.
- **Proof:** See the attached `coding_agent_logs.md` or review the commit history showing the rapid, end-to-end scaffolding of the Python SDK integration.

## 🛠️ Setup Instructions (Local Simulation)
Since we are bypassing the UiPath Labs cloud environment for local testing, we have provided a mock `orchestrator.py` that simulates the Maestro state machine.

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Maestro Case Simulator:
   ```bash
   python orchestrator.py
   ```
3. You will see the agent successfully evaluate both a high-risk claim (routed to human) and a low-risk claim (auto-settled).
