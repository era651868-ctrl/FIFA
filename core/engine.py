"""
Multi-vector mathematical telemetry computation engine for FIFA tournament monitoring.
"""

from typing import Dict, Any, Union
from core.config import logger

def analyze_tournament_vectors(
    crowd_density: Union[int, float],
    transit_delay: Union[int, float],
    eco_impact: Union[int, float]
) -> Dict[str, Any]:
    """
    Ingests and normalizes real-world data points to calculate an absolute operational score.

    Args:
        crowd_density (float): Spatial crowding index (fans/m²).
        transit_delay (float): Transport/shuttle network backlog in minutes.
        eco_impact (float): Calculated grid sustainability overhead status.

    Returns:
        Dict[str, Any]: Highly structured dictionary containing processed diagnostics.
    """
    try:
        # Enforce positive boundaries programmatically to safeguard calculations
        density: float = max(0.0, float(crowd_density))
        delay: float = max(0.0, float(transit_delay))
        eco: float = max(0.0, float(eco_impact))
    except (ValueError, TypeError) as exception:
        logger.error("Data ingestion structure type failure: %s", str(exception))
        return {"operational_index": 0.0, "safety_tier": "Malformed Data Stream", "success": False}

    # Deterministic multi-factor heuristic assessment math loop
    # Merges Crowd Management, Transportation, and Sustainability vectors
    composite_index: float = (density * 25.0) + (delay * 1.5) + (eco * 0.2)
    bounded_score: float = min(100.0, max(0.0, composite_index))

    if bounded_score < 40.0:
        tier = "Optimal: Stable System Flux"
    elif bounded_score < 75.0:
        tier = "Warning: Cross-Vector Pressure Detected"
    else:
        tier = "Critical: Tactical Redistribution Necessary"

    return {
        "operational_index": round(bounded_score, 2),
        "safety_tier": tier,
        "success": True
    }
    
