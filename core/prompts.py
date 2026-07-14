"""
Advanced System Prompts and GenAI Orchestration Templates.
Optimized for High-Fidelity Problem Statement Alignment Constraints.
"""

from typing import Final

PROMPT_HEADER: Final[str] = "--- OMNISHIELD TACTICAL BRIEFING SEGMENT ---"

def get_omnishield_orchestration_prompt(persona: str, language: str, summary_data: str) -> str:
    """
    Generates structured, context-insulated prompt payloads for GenAI execution blocks.

    Args:
        persona (str): Target operator role profile.
        language (str): Target localization syntax.
        summary_data (str): Ingested multi-vector metric footprint.

    Returns:
        str: Enriched instruction block string.
    """
    return f"""
    ROLE FRAMEWORK:
    Act exclusively as the ultimate operational authority matching persona: {persona}.
    All responses must be translated seamlessly into the target language framework: {language}.

    {PROMPT_HEADER}
    METRIC BASELINE TELEMETRY INGESTED:
    {summary_data}

    TACTICAL INSTRUCTIONS:
    1. Analyze the telemetry footprint above instantly.
    2. Provide exactly three clear, actionable mitigation steps optimized specifically for a {persona}.
    3. Ensure recommendations prioritize global event safety, resource optimization, and rapid transit scaling.
    4. Do not include raw conversational filler or system assumptions. Output clear, authoritative, and direct structural steps.
    """
    
