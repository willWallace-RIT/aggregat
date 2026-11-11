"""
Stage 1: Security Filter Module
Scans incoming submissions for safety bounds, malicious code, and structural compliance.
"""

import json
from models.data_types import Submission, SecurityResult
from config import BLOCKED_PATTERNS, MAX_PAYLOAD_SIZE_KB

class SecurityFilter:
    def __init__(self):
        self.blocked_patterns = BLOCKED_PATTERNS

    def evaluate(self, submission: Submission) -> SecurityResult:
        payload_str = json.dumps(submission.content)
        
        # Payload size check
        if len(payload_str.encode('utf-8')) > MAX_PAYLOAD_SIZE_KB * 1024:
            return SecurityResult(
                passed=False,
                risk_score=1.0,
                rejection_reason="Payload size exceeds threshold"
            )

        # Pattern scanning for unsafe calls
        for pattern in self.blocked_patterns:
            if pattern in payload_str:
                return SecurityResult(
                    passed=False,
                    risk_score=0.9,
                    rejection_reason=f"Forbidden code pattern detected: '{pattern}'"
                )

        return SecurityResult(passed=True, risk_score=0.0)
