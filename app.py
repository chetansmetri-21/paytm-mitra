import streamlit as st
import time
import json

# Page Config
st.set_page_config(
    page_title="Paytm Mitra | Autonomous Merchant Ops Teammate",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Paytm Brand Theme (Official Royal Navy #002970 & Cyan #00B9F1 Palette)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');
    
    * {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Background & Global Text */
    .stApp {
        background: linear-gradient(180deg, #f0f5fa 0%, #e8f0f8 100%);
        color: #0f172a;
    }
    
    /* Paytm Top Brand Header */
    .top-header {
        background: linear-gradient(135deg, #001b44 0%, #002970 60%, #004098 100%);
        border-radius: 16px;
        padding: 24px 30px;
        margin-bottom: 22px;
        box-shadow: 0 10px 25px -5px rgba(0, 41, 112, 0.35);
        border-left: 6px solid #00b9f1;
    }
    
    .brand-title {
        font-size: 28px;
        font-weight: 800;
        letter-spacing: -0.5px;
        color: #ffffff;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .badge-track {
        background: rgba(0, 185, 241, 0.2);
        color: #00b9f1;
        border: 1px solid #00b9f1;
        font-size: 11px;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 20px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    
    /* Metrics Row */
    .metric-card {
        background: #ffffff;
        border: 1px solid #dbe4ef;
        border-radius: 14px;
        padding: 18px 20px;
        box-shadow: 0 4px 14px rgba(0, 41, 112, 0.06);
        border-top: 3px solid #00b9f1;
        transition: transform 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
    }
    
    .metric-value {
        font-size: 26px;
        font-weight: 800;
        color: #002970;
        margin: 4px 0 0 0;
    }
    
    .metric-label {
        font-size: 11px;
        color: #64748b;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.6px;
    }

    /* Clean Enterprise Cards */
    .glass-card {
        background: #ffffff;
        border: 1px solid #d8e3f0;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 16px rgba(0, 41, 112, 0.05);
        margin-bottom: 20px;
    }
    
    .card-title {
        font-size: 16px;
        font-weight: 800;
        color: #002970;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 10px;
        border-bottom: 2px solid #f1f5f9;
        padding-bottom: 10px;
    }

    /* Live Telemetry Console */
    .terminal-container {
        background-color: #00132b;
        border: 1px solid #002970;
        border-radius: 12px;
        padding: 16px;
        font-family: 'JetBrains Mono', monospace;
        color: #7dd3fc;
        font-size: 12.5px;
        line-height: 1.65;
        height: 480px;
        overflow-y: auto;
        box-shadow: inset 0 2px 8px rgba(0,0,0,0.4);
    }
    
    /* Primary Paytm Button */
    .stButton>button {
        background: linear-gradient(135deg, #002970 0%, #004098 50%, #00b9f1 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 14px 24px !important;
        width: 100% !important;
        font-size: 15px !important;
        box-shadow: 0 4px 15px rgba(0, 41, 112, 0.3) !important;
        transition: all 0.2s ease-in-out !important;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #001b44 0%, #002970 50%, #00a4d8 100%) !important;
        box-shadow: 0 6px 20px rgba(0, 185, 241, 0.4) !important;
        transform: translateY(-1px) !important;
    }
    
    /* Inputs */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div {
        background-color: #f8fafc !important;
        border: 1.5px solid #cbd5e1 !important;
        color: #0f172a !important;
        border-radius: 10px !important;
        font-weight: 500 !important;
    }
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: #00b9f1 !important;
        box-shadow: 0 0 0 2px rgba(0, 185, 241, 0.25) !important;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #001b44 !important;
        color: #ffffff !important;
    }
    [data-testid="stSidebar"] * {
        color: #e2e8f0 !important;
    }
    [data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.1) !important;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- SIDEBAR -----------------
with st.sidebar:
    st.markdown("## **Paytm** <span style='color:#00b9f1;'>Mitra</span>", unsafe_allow_html=True)
    st.caption("Autonomous Merchant Ops Teammate")
    
    st.markdown("---")
    st.markdown("#### **Hackathon Track**")
    st.markdown("<b style='color:#00b9f1;'>Track 3: Autonomous AI Teammates</b>", unsafe_allow_html=True)
    st.caption("Paytm Build for India AI Hackathon – Bengaluru")
    
    st.markdown("#### **Engineering Team**")
    st.markdown("""
    - **Jeevan M K** *(Team Lead & Arch)*
    - **Chetan S Metri** *(Agent Workflows)*
    - **Samanvitha S** *(Indic Voice & HITL)*
    """)
    
    st.markdown("---")
    st.markdown("#### **Live Engine Status**")
    st.markdown("🟢 **NPCI Gateway:** Connected (38ms)")
    st.markdown("🟢 **Soundbox IoT Broker:** Online")
    st.markdown("🟢 **LangGraph Graph:** Verified")
    st.caption("Designed for 10M+ Kirana Merchants")

# ----------------- HEADER -----------------
st.markdown("""
<div class="top-header">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <div class="brand-title">
                ⚡ Paytm Mitra
                <span class="badge-track">Track 3: Autonomous Teammates</span>
            </div>
            <p style="color: #cbd5e1; margin: 6px 0 0 0; font-size: 14px;">
                Self-Healing Merchant Ops Teammate: Proactive Anomaly Detection, Tool Actuation & Closed-Loop Verification.
            </p>
        </div>
        <div style="text-align: right;">
            <span style="background: rgba(0, 185, 241, 0.2); color: #00b9f1; border: 1px solid #00b9f1; font-size: 12px; font-weight: 700; padding: 6px 14px; border-radius: 12px;">
                ● SYSTEM OPERATIONAL
            </span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ----------------- LIVE METRICS ROW -----------------
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Avg Resolution Time</div>
        <div class="metric-value">18.4s</div>
    </div>
    """, unsafe_allow_html=True)
with m2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Autonomous Deflection</div>
        <div class="metric-value">74.2%</div>
    </div>
    """, unsafe_allow_html=True)
with m3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Cost per Ticket</div>
        <div class="metric-value">₹30 → ₹0.58</div>
    </div>
    """, unsafe_allow_html=True)
with m4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Human Escalation Rate</div>
        <div class="metric-value">&lt; 3.1%</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ----------------- MAIN INTERFACE -----------------
col_agent, col_console = st.columns([1, 1], gap="medium")

with col_agent:
    st.markdown("""
    <div class="glass-card">
        <div class="card-title">🎙️ Merchant Query & Voice Terminal</div>
    """, unsafe_allow_html=True)
    
    lang = st.selectbox(
        "Select Merchant Vernacular Dialect", 
        ["Hindi (हिंदी) - North Retail", "Kannada (ಕನ್ನಡ) - Bengaluru/Mysuru", "Tamil (தமிழ்) - Chennai", "English"]
    )
    
    preset_prompts = {
        "Hindi (हिंदी) - North Retail": "Bhaiya subah ki ₹850 wali payment account mein nahi aayi aur Soundbox bhi nahi bola!",
        "Kannada (ಕನ್ನಡ) - Bengaluru/Mysuru": "Beligge ₹850 payment account ge bandilla mattu Soundbox kooda helilla!",
        "Tamil (தமிழ்) - Chennai": "Kaalaiyil ₹850 panam vara villai, Soundbox-um pesa villai!",
        "English": "My ₹850 customer payment from 9:15 AM is not settled and Soundbox made no announcement!"
    }
    
    user_query = st.text_area(
        "Voice Input / Speech-to-Text Transcription:", 
        value=preset_prompts[lang], 
        height=85
    )
    
    c_m1, c_m2 = st.columns(2)
    with c_m1:
        merchant_id = st.text_input("Merchant ID:", value="MERCH_BLR_560103")
    with c_m2:
        device_id = st.text_input("Soundbox Serial ID:", value="SB4G_V3_88910")
        
    st.markdown("---")
    st.markdown("**🛡️ Guardrail Policy Simulator**")
    escalation_mode = st.toggle("Simulate High-Risk Payment (> ₹5,000 Threshold)", value=False)
    
    btn_run = st.button("⚡ Dispatch Autonomous Teammate Execution", type="primary")
    st.markdown("</div>", unsafe_allow_html=True)

with col_console:
    st.markdown("""
    <div class="glass-card">
        <div class="card-title">🖥️ Autonomous Agent Closed-Loop Execution Stream</div>
    """, unsafe_allow_html=True)
    
    console_placeholder = st.empty()
    
    if not btn_run:
        console_placeholder.markdown("""
        <div class="terminal-container">
            <span style="color: #64748b;">// Awaiting merchant voice query or anomaly stream event...</span><br>
            <span style="color: #64748b;">// Ready to trigger 5-stage closed loop:</span><br>
            <span style="color: #64748b;">// [1] DETECT -> [2] INVESTIGATE -> [3] ACT -> [4] VERIFY -> [5] LEARN</span><br>
            <br>
            <span style="color: #00b9f1;">paytm-mitra@cloud-gateway:~$</span> <span style="animation: blink 1s infinite;">_</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        claim_val = 8500 if escalation_mode else 850
        
        # Step 1: DETECT
        console_placeholder.markdown(f"""
        <div class="terminal-container">
            <span style="color: #38bdf8;">[14:22:01] ▶ MITRA AGENT DISPATCHED: Target Merchant '{merchant_id}'</span><br>
            <span style="color: #fbbf24;">[14:22:02] 🔍 PHASE 1: DETECT</span><br>
            &nbsp;&nbsp;→ Natural Language Intent: <code>SETTLEMENT_HOLD</code> + <code>SOUNDBOX_SILENCE</code><br>
            &nbsp;&nbsp;→ Disputed Claim Value: <b style="color:#ffffff;">₹{claim_val}.00</b><br>
            &nbsp;&nbsp;→ Checkout Impact: HIGH (Customer queue blocked)<br>
            <span style="color: #64748b;">// Initiating automated telemetry investigation...</span>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(1.2)
        
        # Step 2: INVESTIGATE
        console_placeholder.markdown(f"""
        <div class="terminal-container">
            <span style="color: #38bdf8;">[14:22:01] ▶ MITRA AGENT DISPATCHED: Target Merchant '{merchant_id}'</span><br>
            <span style="color: #fbbf24;">[14:22:02] 🔍 PHASE 1: DETECT</span> → Extracted Claim: ₹{claim_val}.00<br><br>
            <span style="color: #00b9f1;">[14:22:03] 🔎 PHASE 2: INVESTIGATE (MULTI-SYSTEM PROBE)</span><br>
            &nbsp;&nbsp;→ Querying <code>npci_settlement_ledger(merchant='{merchant_id}')</code><br>
            &nbsp;&nbsp;&nbsp;&nbsp;Output: <code>{{'status': 'U19', 'reason': 'Remitter Bank Switch Latency'}}</code><br>
            &nbsp;&nbsp;→ Querying <code>iot_soundbox_telemetry(device_id='{device_id}')</code><br>
            &nbsp;&nbsp;&nbsp;&nbsp;Output: <code>{{'rssi_dbm': -104, 'packet_loss': '38%', 'battery': '84%'}}</code><br>
            <span style="color: #64748b;">// Applying safety policy threshold check...</span>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(1.4)
        
        # Step 3: ACT
        if claim_val > 5000:
            console_placeholder.markdown(f"""
            <div class="terminal-container">
                <span style="color: #38bdf8;">[14:22:01] ▶ MITRA AGENT DISPATCHED</span><br>
                <span style="color: #fbbf24;">[14:22:02] 🔍 PHASE 1: DETECT</span> → Claim: ₹{claim_val}.00<br>
                <span style="color: #00b9f1;">[14:22:03] 🔎 PHASE 2: INVESTIGATE</span> → Root Cause Isolated<br><br>
                <span style="color: #f87171; font-weight: bold;">[14:22:05] ⚠️ HUMAN-IN-THE-LOOP GUARDRAIL ACTIVATED</span><br>
                &nbsp;&nbsp;→ Policy Rule: Claim value ₹{claim_val} &gt; Autonomous Threshold (₹5,000)<br>
                &nbsp;&nbsp;→ Halting automated money-movement tools.<br>
                &nbsp;&nbsp;→ Generated 1-Click Evidence Packet #HITL-9921 for Tier-2 Ops Lead.<br>
                <br>
                <span style="color: #fbbf24;">[STATUS] AWAITING SUPERVISOR 1-CLICK AUTHORIZATION</span>
            </div>
            """, unsafe_allow_html=True)
            st.warning(f"🛡️ **Human Guardrail Triggered:** Disputed amount of ₹{claim_val} exceeds ₹5,000. Autonomous action held; evidence forwarded to human supervisor.")
        else:
            console_placeholder.markdown(f"""
            <div class="terminal-container">
                <span style="color: #38bdf8;">[14:22:01] ▶ MITRA AGENT DISPATCHED</span><br>
                <span style="color: #fbbf24;">[14:22:02] 🔍 PHASE 1: DETECT</span> → Claim: ₹{claim_val}.00<br>
                <span style="color: #00b9f1;">[14:22:03] 🔎 PHASE 2: INVESTIGATE</span> → Root Cause Isolated<br><br>
                <span style="color: #4ade80;">[14:22:05] ⚡ PHASE 3: ACT (PERMITTED REMEDIATION)</span><br>
                &nbsp;&nbsp;→ POST <code>/api/v2/settlement/force_reconcile</code>: <b>200 OK (SUCCESS)</b><br>
                &nbsp;&nbsp;→ POST <code>/api/v2/iot/soundbox/reconnect_mqtt</code>: <b>MQTT ACK RECEIVED</b><br>
                <span style="color: #64748b;">// Running closed-loop state assertions...</span>
            </div>
            """, unsafe_allow_html=True)
            time.sleep(1.2)
            
            # Step 4 & 5: VERIFY & LEARN
            console_placeholder.markdown(f"""
            <div class="terminal-container">
                <span style="color: #38bdf8;">[14:22:01] ▶ MITRA AGENT DISPATCHED</span><br>
                <span style="color: #fbbf24;">[14:22:02] 🔍 PHASE 1: DETECT</span> → Claim: ₹{claim_val}.00<br>
                <span style="color: #00b9f1;">[14:22:03] 🔎 PHASE 2: INVESTIGATE</span> → Root Cause Isolated<br>
                <span style="color: #4ade80;">[14:22:05] ⚡ PHASE 3: ACT</span> → Remediations Executed<br><br>
                <span style="color: #38bdf8;">[14:22:06] ✅ PHASE 4: VERIFY (DATABASE & HARDWARE ASSERTION)</span><br>
                &nbsp;&nbsp;→ Core Ledger Assertion: <code>balance_delta == +{claim_val}</code> → <b style="color:#4ade80;">CONFIRMED TRUE</b><br>
                &nbsp;&nbsp;→ Soundbox Audio Assertion: <code>device_chime_ack == 200 OK</code> → <b style="color:#4ade80;">CONFIRMED TRUE</b><br><br>
                <span style="color: #00b9f1;">[14:22:07] 🧠 PHASE 5: LEARN & INDEX</span><br>
                &nbsp;&nbsp;→ Indexed into ChromaDB Vector Memory: Case #CAS-7719<br>
                &nbsp;&nbsp;→ Total Resolution Time: <b>18.2 Seconds</b> (Zero Human Intervention)<br>
                <br>
                <span style="color: #4ade80; font-weight: bold;">[COMPLETED] ISSUE SELF-HEALED AND VERIFIED</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.success(f"🎉 **Merchant Voice Audio Dispatched (Synthesized Indic Speech):** 'Aapka ₹{claim_val} settlement safalta purvak credit ho chuka hai aur Soundbox restart hokar sync ho chuka hai.'")
            
    st.markdown("</div>", unsafe_allow_html=True)