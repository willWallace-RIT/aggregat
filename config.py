"""
Pipeline Configuration Parameters
Defines dividend allocation ratios and security evaluation thresholds.
"""

# Dividend Distribution Ratios
BASE_DIVIDEND_FRACTION = 0.60    # 60% divided equally among all valid submissions
WEIGHTED_DIVIDEND_FRACTION = 0.40 # 40% distributed based on aggregate contribution weight

# Security Parameters
MAX_PAYLOAD_SIZE_KB = 512
BLOCKED_PATTERNS = ["import os", "eval(", "exec(", "subprocess", "system("]
