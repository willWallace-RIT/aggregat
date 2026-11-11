"""
Pipeline Orchestrator
Coordinates sequential execution from security filter through to 60/40 dividend calculation.
"""

from typing import List, Dict, Any
from models.data_types import Submission, DividendReport
from pipeline.security_filter import SecurityFilter
from pipeline.task_verifier import TaskVerifier
from pipeline.deconstructor import SolutionDeconstructor
from pipeline.aggregator import SolutionAggregator
from pipeline.dividend_engine import DividendEngine

class EvaluationPipeline:
    def __init__(self):
        self.security_filter = SecurityFilter()
        self.task_verifier = TaskVerifier()
        self.deconstructor = SolutionDeconstructor()
        self.aggregator = SolutionAggregator()
        self.dividend_engine = DividendEngine()

    def run_batch(self, job_id: str, total_reward_pool: float, submissions: List[Submission]) -> DividendReport:
        valid_submissions: List[Submission] = []
        valid_worker_ids: List[str] = []
        deconstructed_list = []

        for sub in submissions:
            # 1. Security Filter
            sec_res = self.security_filter.evaluate(sub)
            if not sec_res.passed:
                print(f"[REJECTED Security] {sub.id}: {sec_res.rejection_reason}")
                continue

            # 2. Task Completion Verifier
            ver_res = self.task_verifier.verify(sub)
            if not ver_res.completed:
                print(f"[REJECTED Completion] {sub.id}: {ver_res.feedback}")
                continue

            # Passed verification
            valid_submissions.append(sub)
            valid_worker_ids.append(sub.worker_id)

            # 3. Deconstruct Solution
            deconstructed = self.deconstructor.deconstruct(sub)
            deconstructed_list.append(deconstructed)

        # 4. Synthesize Aggregate Solution & Assign Weights
        aggregate_solution = self.aggregator.synthesize(job_id, valid_submissions, deconstructed_list)

        # 5. Dual-Tier Dividend Distribution (60/40 Split)
        report = self.dividend_engine.calculate_distributions(
            job_id, total_reward_pool, valid_worker_ids, aggregate_solution
        )

        return report
