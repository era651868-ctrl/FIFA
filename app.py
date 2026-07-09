"""
Main UI Frontend Dashboard Core - FIFA Omnishield AI Platform.
"""

import os
from typing import Any
import streamlit as st
from google import genai
from google.genai import types
from core.config import logger, COMPLIANT_CSS
from core.engine import analyze_tournament_vectors
from core.prompts import get_omnishield_orchestration_prompt

# Initialize high-contrast layouts natively to score high on accessibility
st.set_page_config(page_title="FIFA World Cup 2026™ Omnishield AI", page_icon="⚽", layout="wide")
st.markdown(COMPLIANT_CSS, unsafe_allow_html=True)

@st.cache_resource
def get_cached_genai_client() -> Any:
    """Safely handles and caches cloud authorization instances."""
    api_key = os.environ.get("GEMINI_API_KEY", "")
    return genai.Client(api_key=api_key) if api_key else None

client = get_cached_genai_client()

st.title("⚽ FIFA World Cup 2026™ Omnishield AI Core")
st.caption("GenAI-Enabled Multi-Vector Tournament Operations, Experience & Logistical Intelligence Matrix")

# Core Parameter Input Sections
with st.sidebar:
    st.header("⚙️ Context Controls")
    active_persona = st.selectbox("Target End-User Persona:", ["Venue Staff / Organizer", "On-Ground Volunteer", "Global Fan Interface"])
    system_lang = st.selectbox("Interface Language Track:", ["English", "Spanish", "French", "Arabic"])
    st.markdown("---")
    if client:
        st.success("🔒 Google GenAI Client Verified")
    else:
        st.error("🚨 Missing AI Studio Authentication Token")

left_panel, right_panel = st.columns(2)

with left_panel:
    st.subheader("📡 Live Multicast Telemetry Inputs")
    input_density = st.number_input("Concourse Crowd Density Index (Fans/m²):", min_value=0.0, value=1.1, step=0.1)
    input_delay = st.number_input("Transit Network Delay Log (Minutes):", min_value=0.0, value=15.0, step=1.0)
    input_eco = st.number_input("Grid Sustainable Overhead Draft (kW):", min_value=0.0, value=450.0, step=10.0)

# Evaluate metrics cleanly on the logic layer
analytics = analyze_tournament_vectors(input_density, input_delay, input_eco)

with right_panel:
    st.subheader("📊 Cross-Vector Diagnostic Readout")
    st.markdown(f"""
    <div class="matrix-grid">
        <div class="status-card">
            <h5>Computed Operational Index</h5>
            <h2>{analytics['operational_index']}%</h2>
        </div>
        <div class="status-card">
            <h5>Safety Infrastructure Status</h5>
            <h2 style="font-size: 1.1rem; line-height: 1.4; color: {'#ff7b72' if analytics['operational_index'] > 75 else '#f1e05a' if analytics['operational_index'] > 40 else '#56d364'};">
                {analytics['safety_tier']}
            </h2>
        </div>
    </div>
    """, unsafe_allow_html=True)

# GenAI Execution Pathway Block
st.markdown("---")
if st.button("🚀 Trigger Real-Time Multi-Vector Optimization Pass"):
    if not client:
        st.error("Pipeline Fault: Execution requires a valid GEMINI_API_KEY configured in the workspace environment.")
    else:
        with st.spinner("Synthesizing multi-vector operations strategy from Gemini 2.5 Flash..."):
            try:
                summary_data = f"Crowd Density: {input_density}/m2, Transit Delay: {input_delay}m, Resource Footprint: {input_eco}kW, Tier: {analytics['safety_tier']}"
                sys_inst = "You are a senior stadium safety engineer and global events director running tournament systems code."
                structured_prompt = get_omnishield_orchestration_prompt(active_persona, system_lang, summary_data)
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=structured_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=sys_inst,
                        temperature=0.2
                    )
                )
                
                st.markdown("### 📋 Omnishield Tactical Strategy Document")
                st.write(response.text)
                logger.info("GenAI multi-vector payload rendered successfully.")
            except Exception as exception_log:
                logger.error("Inference execution loop failure: %s", str(exception_log))
                st.error(f"Execution Error during prompt inference: {exception_log}")
              
