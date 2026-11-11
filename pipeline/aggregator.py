"""
Stage 4: Aggregate Solution Synthesizer
Combines deconstructed components into a master solution and computes contribution weights.
"""

from typing import List, Dict
from models.data_types import Submission, DeconstructionResult, AggregateSolution

class SolutionAggregator:
    def synthesize(self, job_id: str, valid_submissions: List[Submission], deconstructed: List[DeconstructionResult]) -> AggregateSolution:
        if not valid_submissions:
            return AggregateSolution(job_id=job_id, synthesized_blueprint={}, contribution_weights={})

        master_components = []
        worker_scores: Dict[str, float] = {}

        for sub, dec in zip(valid_submissions, deconstructed):
            score = sum(c.uniqueness_score for c in dec.components) + 1.0
            worker_scores[sub.worker_id] = worker_scores.get(sub.worker_id, 0.0) + score
            for c in dec.components:
                master_components.append({
                    "contributor": sub.worker_id,
                    "component": c.feature_name,
                    "snippet": c.code_snippet
                })

        # Normalize contribution weights to sum to 1.0
        total_score = sum(worker_scores.values())
        contribution_weights = {
            w_id: round(score / total_score, 4) for w_id, score in worker_scores.items()
        }

        synthesized_blueprint = {
            "job_id": job_id,
            "total_contributors": len(valid_submissions),
            "merged_components": master_components
        }

        return AggregateSolution(
            job_id=job_id,
            synthesized_blueprint=synthesized_blueprint,
            contribution_weights=contribution_weights
        )
