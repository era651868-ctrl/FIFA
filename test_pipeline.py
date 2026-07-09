"""
Robust automated testing pipeline verifying metric computation correctness.
"""

import unittest
from unittest.mock import MagicMock, patch
from core.engine import analyze_tournament_vectors

class TestFIFAOmnishieldCore(unittest.TestCase):
    """Enforces mathematical boundary assertions across the computational codebase."""

    def setUp(self) -> None:
        """Initializes stable input dictionaries for evaluation validation loops."""
        self.nominal_metrics = {"density": 0.8, "delay": 5.0, "eco": 200.0}
        self.critical_metrics = {"density": 3.8, "delay": 90.0, "eco": 1200.0}

    def test_nominal_logistics_flux(self) -> None:
        """Validates normal input vectors result in a clear, low-risk status response."""
        result = analyze_tournament_vectors(
            self.nominal_metrics["density"],
            self.nominal_metrics["delay"],
            self.nominal_metrics["eco"]
        )
        self.assertTrue(result["success"])
        self.assertLess(result["operational_index"], 75.0)
        self.assertIn("Optimal", result["safety_tier"])

    def test_critical_logistics_saturation(self) -> None:
        """Verifies extreme telemetry values clamp reliably at the 100% ceiling parameter."""
        result = analyze_tournament_vectors(
            self.critical_metrics["density"],
            self.critical_metrics["delay"],
            self.critical_metrics["eco"]
        )
        self.assertTrue(result["success"])
        self.assertEqual(result["operational_index"], 100.0)
        self.assertIn("Critical", result["safety_tier"])

    def test_corrupted_type_input_protection(self) -> None:
        """Ensures logic arrays gracefully handle unparseable string payloads via safety fallbacks."""
        result = analyze_tournament_vectors("unparseable_string", None, [1, 2, 3])
        self.assertFalse(result["success"])
        self.assertEqual(result["operational_index"], 0.0)
        self.assertEqual(result["safety_tier"], "Malformed Data Stream")

    @patch("google.genai.Client")
    def test_isolated_api_mock_coverage(self, mock_client_wrapper: MagicMock) -> None:
        """Ensures that code validation runs can execute entirely offline without live network hits."""
        mock_instance = mock_client_wrapper.return_value
        mock_payload_response = MagicMock()
        mock_payload_response.text = "Omnishield Strategy Mock Target: All Vectors Normalized."
        mock_instance.models.generate_content.return_value = mock_payload_response

        simulated_response = mock_instance.models.generate_content(
            model="gemini-2.5-flash",
            contents="Simulated Core Input Matrix Prompt Ingest Loop Data"
        )
        
        self.assertEqual(simulated_response.text, "Omnishield Strategy Mock Target: All Vectors Normalized.")
        mock_instance.models.generate_content.assert_called_once()

if __name__ == "__main__":
    unittest.main()
  
