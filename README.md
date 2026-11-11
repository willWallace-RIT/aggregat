# Submission Evaluation Pipeline

A modular submission assessment framework designed to perform security filtering, task completion verification, solution deconstruction, aggregate solution synthesis, and dual-tier dividend distribution.

## Overview
This repository provides a complete execution pipeline for evaluating incoming federated job submissions. The framework processes submissions through five sequential stages:

1. **Security Filtering:** Scans submissions for malicious payloads, unsafe script patterns, rate-limit violations, and structural anomalies.
2. **Task Completion Assessment:** Verifies whether the submitted output correctly fulfills the target task requirements and meets validation criteria.
3. **Solution Deconstruction:** Breaks down passing solutions into atomic modular components, functional traits, and algorithmic steps.
4. **Aggregate Solution Synthesis:** Synthesizes atomic components from all successful submissions into an optimized aggregate master solution.
5. **Weighted Dividend Distribution:** Allocates total job payouts using a two-tier economic model:
   - **60% Egalitarian Base Tier:** Divided equally among all valid, task-completing submissions.
   - **40% Merit/Contribution Tier:** Distributed proportionally based on each submission's relative contribution weight to the final aggregate solution.

## Repository Structure
```
submission-evaluation-pipeline/
├── README.md
├── config.py                 # Pipeline thresholds and dividend percentage splits (60/40)
├── main.py                   # CLI entry point to run full evaluation batches
├── pipeline/
│   ├── __init__.py
│   ├── orchestrator.py       # Sequential pipeline coordinator
│   ├── security_filter.py    # Stage 1: Security and safety envelope verification
│   ├── task_verifier.py     # Stage 2: Functional correctness & task completion check
│   ├── deconstructor.py      # Stage 3: Modular solution breakdown
│   ├── aggregator.py         # Stage 4: Aggregate solution synthesis & weight assignment
│   └── dividend_engine.py    # Stage 5: 60/40 dividend distribution math
└── models/
    ├── __init__.py
    └── data_types.py         # Data models for submissions, evaluations, and payouts
```

## Quick Start

### 1. Run Pipeline Evaluation Batch
```python
from pipeline.orchestrator import EvaluationPipeline
from models.data_types import Submission

submissions = [
    Submission(id="sub_101", worker_id="node_a", content={"code": "def solve(): return True"}, metadata={}),
    Submission(id="sub_102", worker_id="node_b", content={"code": "def solve(): return True"}, metadata={})
]

pipeline = EvaluationPipeline()
report = pipeline.run_batch(job_id="job_889", total_reward_pool=1000.0, submissions=submissions)
print(report)
```

## Dividend Distribution Math
- **Total Pool:** $P$
- **Base Dividend Pool (60%):** $P_{base} = 0.60 \times P$
- **Base Payout per Valid Node:** $D_{base} = \frac{P_{base}}{N_{valid}}$
- **Weighted Dividend Pool (40%):** $P_{weighted} = 0.40 \times P$
- **Weighted Payout for Node $i$:** $D_{weighted, i} = P_{weighted} \times W_i$ where $\sum W_i = 1.0$
- **Total Payout for Node $i$:** $D_{total, i} = D_{base} + D_{weighted, i}$

## License
MIT License
