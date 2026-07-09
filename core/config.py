"""
Configuration settings and centralized accessible styles for FIFA Omnishield AI.
"""

import logging

# Set up enterprise logging to ensure absolute debugging trace compliance
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("FIFA_Omnishield")

# Accessibility-focused styling framework ensuring high-contrast UI compliance
COMPLIANT_CSS = """
<style>
    .main { background-color: #0b0f17; color: #e6edf3; }
    h1, h2, h3, h4 { color: #ffffff !important; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
    
    .matrix-grid { display: flex; gap: 16px; flex-wrap: wrap; margin-top: 15px; }
    .status-card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #30363d;
        flex: 1;
        min-width: 220px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    .status-card h5 { color: #8b949e; margin: 0; text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.8rem; }
    .status-card h2 { margin: 8px 0 0 0; font-size: 1.8rem; color: #58a6ff; }
</style>
"""

