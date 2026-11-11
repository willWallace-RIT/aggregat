"""
Stage 5: Dual-Tier Dividend Distribution Engine
Executes 60% base egalitarian distribution and 40% weighted contribution distribution.
"""

from typing import List, Dict
from models.data_types import AggregateSolution, DividendReport
from config import BASE_DIVIDEND_FRACTION, WEIGHTED_DIVIDEND_FRACTION

class DividendEngine:
    def calculate_distributions(self, job_id: str, total_pool: float, valid_worker_ids: List[str], aggregate_solution: AggregateSolution) -> DividendReport:
        if not valid_worker_ids:
            return DividendReport(
                job_id=job_id,
                total_pool=total_pool,
                base_pool=0.0,
                weighted_pool=0.0,
                payouts={}
            )

        base_pool = total_pool * BASE_DIVIDEND_FRACTION
        weighted_pool = total_pool * WEIGHTED_DIVIDEND_FRACTION

        # 60% Equal Split
        per_worker_base = base_pool / len(valid_worker_ids)
        
        payouts: Dict[str, Dict[str, float]] = {}
        weights = aggregate_solution.contribution_weights

        for worker_id in valid_worker_ids:
            weight = weights.get(worker_id, 0.0)
            worker_weighted_share = weighted_pool * weight
            total_payout = per_worker_base + worker_weighted_share

            payouts[worker_id] = {
                "base_payout_60": round(per_worker_base, 2),
                "weighted_payout_40": round(worker_weighted_share, 2),
                "total_dividend": round(total_payout, 2),
                "contribution_weight": weight
            }

        return DividendReport(
            job_id=job_id,
            total_pool=total_pool,
            base_pool=base_pool,
            weighted_pool=weighted_pool,
            payouts=payouts
        )
