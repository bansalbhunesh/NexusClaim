# NexusClaim: Intelligent Insurance Case Orchestration

## Slide 1: The Problem
**Insurance Claims are Broken.**
- Highly manual, exception-heavy processes.
- Disconnected systems (intake vs. investigation vs. settlement).
- Humans waste time on low-risk claims, missing high-risk fraud.

## Slide 2: The Solution - NexusClaim
**Agentic Orchestration with UiPath Maestro Case**
- **Intake:** Unstructured claim documents are parsed into structured data.
- **Investigation:** A native **UiPath Coded Agent** (built with LangGraph + Python SDK) evaluates risk factors using LLMs.
- **Settlement & Action Center:** Low-risk claims are auto-settled. High-risk exceptions (e.g., fraud indicators) trigger a seamless handoff to human adjusters in the UiPath Action Center.

## Slide 3: Architecture & Tech Stack
- **UiPath Maestro Case:** The backbone state machine governing the claim lifecycle.
- **LangGraph & Python SDK:** Our Coded Agent deployed directly to Orchestrator.
- **UiPath CLI:** The entire agent was scaffolded and deployed by an AI Coding Agent, securing maximum productivity and the +2 Bonus Points.

## Slide 4: Why We Win (The Judging Criteria)
- **Business Impact:** Solves a multi-million dollar problem for enterprise insurers.
- **Platform Usage:** Pushes UiPath Maestro to its limits with Coded Agents and Action Center.
- **Technical Execution:** Exception paths and human-handoffs are built-in natively, not patched on.
- **Innovation:** Multi-agent debate to detect fraud, seamlessly integrated into a low-code UI.

## Slide 5: Demo
(Insert link to 5-minute YouTube video demonstrating the mock local orchestrator evaluating a low-risk claim vs. a high-risk claim).
