import streamlit as st
import time
import uuid
from agent import fraud_agent

st.set_page_config(page_title="NexusClaim Maestro Simulator", page_icon="🛡️", layout="wide")

if "cases" not in st.session_state:
    st.session_state.cases = []

st.title("🛡️ NexusClaim: Multi-Agent Case Orchestration")
st.markdown("UiPath Maestro Simulator with **Adversarial Red-Team Debate** for fraud detection.")

# --- Sidebar for Intake ---
with st.sidebar:
    st.header("📄 Claim Intake (IDP)")
    with st.form("intake_form"):
        claim_amt = st.number_input("Claim Amount ($)", min_value=0.0, value=500.0)
        claim_desc = st.text_area("Claim Description", "Minor fender bender, small scratch on bumper.")
        submit_claim = st.form_submit_button("Submit Claim to Maestro")
        
    if submit_claim:
        new_case = {
            "case_id": f"CASE-{str(uuid.uuid4())[:8]}",
            "claim_amount": claim_amt,
            "claim_description": claim_desc,
            "status": "Investigation",
            "agent_results": None,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        st.session_state.cases.append(new_case)
        st.success(f"Case {new_case['case_id']} created!")

# --- Main Dashboard ---
tab1, tab2, tab3 = st.tabs(["Maestro Dashboard", "Action Center (Human Approval)", "Adversarial Config"])

with tab1:
    st.header("📊 Active Cases")
    
    if not st.session_state.cases:
        st.info("No active cases. Submit a claim from the sidebar.")
    else:
        for idx, case in enumerate(st.session_state.cases):
            with st.expander(f"{case['case_id']} - Status: {case['status']}"):
                st.write(f"**Amount:** ${case['claim_amount']}")
                st.write(f"**Description:** {case['claim_description']}")
                
                if case['status'] == "Investigation":
                    if st.button(f"Trigger Multi-Agent Debate ##{idx}", key=f"run_agent_{idx}"):
                        st.write("---")
                        st.subheader("⚖️ Live Multi-Agent Debate Transcript")
                        transcript_placeholder = st.empty()
                        
                        # Run the agent (which has built-in time.sleep for simulation)
                        result = fraud_agent.invoke({
                            "claim_id": case['case_id'],
                            "claim_amount": case['claim_amount'],
                            "claim_description": case['claim_description']
                        })
                        
                        # Animate the transcript
                        transcript_text = ""
                        for message in result['debate_transcript']:
                            icon = "🕵️‍♂️" if message['speaker'] == "Investigator" else "🧑‍🦱"
                            transcript_text += f"**{icon} {message['speaker']}:** {message['text']}\n\n"
                            transcript_placeholder.markdown(transcript_text)
                            time.sleep(1) # Simulate real-time typing
                            
                        st.session_state.cases[idx]["agent_results"] = result
                        
                        if result["is_fraudulent"]:
                            st.session_state.cases[idx]["status"] = "Pending Human Approval"
                            st.error("🚨 Debate concluded: High risk detected! Routed to Action Center.")
                        else:
                            st.session_state.cases[idx]["status"] = "Settlement"
                            st.success("✅ Debate concluded: Low risk. Auto-routed to Settlement.")
                        
                        time.sleep(2)
                        st.rerun()
                        
                elif case['agent_results']:
                    res = case['agent_results']
                    st.write("---")
                    st.subheader("⚖️ Debate Transcript")
                    for message in res['debate_transcript']:
                        icon = "🕵️‍♂️" if message['speaker'] == "Investigator" else "🧑‍🦱"
                        st.markdown(f"**{icon} {message['speaker']}:** {message['text']}")
                    
                    st.write("---")
                    st.write("**🤖 Final Ruling:**")
                    st.metric("Risk Score", res['risk_score'])
                    st.write(f"**Fraudulent:** {res['is_fraudulent']}")
                    st.write(f"**Reasoning:** {res['agent_reasoning']}")

with tab2:
    st.header("🧑‍⚖️ Action Center (Human-in-the-Loop)")
    pending_cases = [c for c in st.session_state.cases if c['status'] == "Pending Human Approval"]
    
    if not pending_cases:
        st.success("Inbox zero! No claims require human review right now.")
    else:
        for case in pending_cases:
            st.error(f"Review Required: {case['case_id']}")
            st.write(f"**Amount:** ${case['claim_amount']}")
            st.write(f"**Agent Reasoning:**", case['agent_results']['agent_reasoning'])
            
            with st.expander("View Full Debate Transcript"):
                for message in case['agent_results']['debate_transcript']:
                    icon = "🕵️‍♂️" if message['speaker'] == "Investigator" else "🧑‍🦱"
                    st.markdown(f"**{icon} {message['speaker']}:** {message['text']}")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Approve Claim", key=f"approve_{case['case_id']}"):
                    for c in st.session_state.cases:
                        if c['case_id'] == case['case_id']:
                            c['status'] = "Settlement"
                    st.success("Claim approved and sent to Settlement.")
                    st.rerun()
            with col2:
                if st.button("Reject (Fraud)", key=f"reject_{case['case_id']}"):
                    for c in st.session_state.cases:
                        if c['case_id'] == case['case_id']:
                            c['status'] = "Rejected"
                    st.error("Claim rejected and case closed.")
                    st.rerun()

with tab3:
    st.header("🧠 Adversarial Debate Configuration")
    st.markdown("""
    Inspired by **Gauntlet**, this implementation upgrades standard evaluations to active **Multi-Agent Debates**.
    
    - **Skeptical Investigator:** Programmed to find logic gaps and policy violations.
    - **Claimant Persona:** An adversarial LLM initialized with the claim's details, instructed to defend the claim.
    
    The Maestro Case orchestrator governs this debate natively. If the Investigator scores a definitive "win" by cornering the Claimant, the case is routed to human review.
    """)
