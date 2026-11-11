"""
Data Models for Evaluation Pipeline
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional

@dataclass
class Submission:
    id: str
    worker_id: str
    content: Dict[str, Any]
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class SecurityResult:
    passed: bool
    risk_score: float
    rejection_reason: Optional[str] = None

@dataclass
class VerificationResult:
    completed: bool
    accuracy_score: float
    feedback: str = ""

@dataclass
class DeconstructedComponent:
    component_id: str
    feature_name: str
    code_snippet: str
    uniqueness_score: float

@dataclass
class DeconstructionResult:
    submission_id: str
    components: List[DeconstructedComponent]

@dataclass
class AggregateSolution:
    job_id: str
    synthesized_blueprint: Dict[str, Any]
    contribution_weights: Dict[str, float]  # worker_id -> weight (0.0 to 1.0)

@dataclass
class DividendReport:
    job_id: str
    total_pool: float
    base_pool: float
    weighted_pool: float
    payouts: Dict[str, Dict[str, float]]  # worker_id -> {base, weighted, total}
