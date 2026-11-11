"""
Stage 3: Solution Deconstruction Module
Breaks down valid submissions into reusable modular components.
"""

from models.data_types import Submission, DeconstructionResult, DeconstructedComponent

class SolutionDeconstructor:
    def deconstruct(self, submission: Submission) -> DeconstructionResult:
        components = []
        code_body = str(submission.content.get("code", ""))
        
        # Deconstruct into modular functional blocks
        lines = code_body.split("\n")
        for idx, line in enumerate(lines):
            if line.strip().startswith("def ") or line.strip().startswith("class "):
                comp_name = line.strip().split("(")[0]
                components.append(
                    DeconstructedComponent(
                        component_id=f"{submission.id}_comp_{idx}",
                        feature_name=comp_name,
                        code_snippet=line,
                        uniqueness_score=0.8
                    )
                )
                
        # Default component if no explicit functions found
        if not components:
            components.append(
                DeconstructedComponent(
                    component_id=f"{submission.id}_comp_default",
                    feature_name="core_logic",
                    code_snippet=code_body[:100],
                    uniqueness_score=0.5
                )
            )

        return DeconstructionResult(submission_id=submission.id, components=components)
