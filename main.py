"""
CLI Entry Point for Submission Evaluation Pipeline
"""

from models.data_types import Submission
from pipeline.orchestrator import EvaluationPipeline

def main():
    print("=== Initializing Submission Evaluation Pipeline ===")
    
    # Sample incoming submissions pool
    test_submissions = [
        Submission(
            id="sub_001",
            worker_id="node_alpha",
            content={"status": "SUCCESS", "code": "def process_data(): return [1, 2, 3]"}
        ),
        Submission(
            id="sub_002",
            worker_id="node_beta",
            content={"status": "SUCCESS", "code": "def process_data_fast(): return [1, 2, 3]\ndef optimize(): pass"}
        ),
        Submission(
            id="sub_003",
            worker_id="node_gamma",
            content={"status": "SUCCESS", "code": "import os\nos.system('echo malicious')"}
        ),
        Submission(
            id="sub_004",
            worker_id="node_delta",
            content={"status": "FAILED", "code": ""}
        )
    ]

    pipeline = EvaluationPipeline()
    report = pipeline.run_batch(job_id="job_batch_4092", total_reward_pool=5000.0, submissions=test_submissions)

    print("\n=== Dividend Allocation Report (60/40 Split) ===")
    print(f"Job ID: {report.job_id}")
    print(f"Total Pool: ${report.total_pool:.2f}")
    print(f"60% Base Pool: ${report.base_pool:.2f}")
    print(f"40% Weighted Pool: ${report.weighted_pool:.2f}\n")
    
    for worker_id, payout in report.payouts.items():
        print(f"Worker [{worker_id}]:")
        print(f"  - Base 60% Share:     ${payout['base_payout_60']:.2f}")
        print(f"  - Weighted 40% Share: ${payout['weighted_payout_40']:.2f} (Weight: {payout['contribution_weight']})")
        print(f"  - Total Dividend:     ${payout['total_dividend']:.2f}\n")

if __name__ == "__main__":
    main()
