# Neural Reusable Operator Transfer vs Fact Memory Baseline

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `neural-reusable-operator-transfer-vs-fact-memory-baseline-16c767cdcb`
Run ID: `neural-reusable-operator-transfer-vs-fact-memory-baseline-16c767cdcb-20260611T012539310740+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Memory Doctrine: Reusable Operator Learning vs Fact Recall: enoch://control-plane/projects/memory-doctrine-reusable-operator-learning-vs-fact-recall-4ae67b2a8689/runs/memory-doctrine-reusable-operator-learning-vs-fact-recall-4ae67b2a8689-20260610T234620332680+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d9d36ccd668d

## What looked useful

Across 20 seeds, reusable held-out exact accuracy was 1.0000 versus 0.015625 uniform expected exact accuracy for the fact-memory baseline; a random-operator control stayed near chance at 0.0098 held-out exact accuracy.

## Boundaries and scale limits

Synthetic 64-fact task only; no language-model setting, no GPT-2-small-class baseline, no parameter-matched dense neural baseline, and no nonlinear/noisy operator families.

## Claim scope

In a small synthetic bit-vector task with 8 structured affine/permutation-style operators over 64 facts, a reusable neural operator model transferred to held-out operator/fact combinations while an independent fact-memory table baseline stayed at chance.

## Why it stopped

Tier 1 controlled direct test produced useful mechanism support but is too synthetic and baseline-limited for publication readiness.

## Recommended next action

Run a bounded deepen test with a parameter-matched dense neural baseline receiving the same fact features and include nonlinear operator families before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-matched neural baseline for reusable operator transfer
- Success threshold: Reusable model mean held-out exact accuracy >= 0.80 and at least +0.20 absolute over the best parameter-matched dense baseline across 20 seeds, with train exact accuracy >= 0.90.
- Stop condition: Stop as negative if the dense baseline matches within 0.05 held-out exact accuracy or if reusable accuracy falls below 0.60 on nonlinear operators despite fitting the training split.

## Evidence references

- Artifact root: `<local-path>/projects/neural-reusable-operator-transfer-vs-fact-memory-baseline-16c767cdcb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
