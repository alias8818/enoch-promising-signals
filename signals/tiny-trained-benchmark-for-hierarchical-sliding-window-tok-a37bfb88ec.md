# Tiny Trained Benchmark for Hierarchical Sliding Window Token Merge

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-trained-benchmark-for-hierarchical-sliding-window-tok-a37bfb88ec`
Run ID: `tiny-trained-benchmark-for-hierarchical-sliding-window-tok-a37bfb88ec-20260522T153104479417+0000`

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

- Parent run decision: Hierarchical Sliding Window with Token Merge: enoch://control-plane/projects/hierarchical-sliding-window-with-token-merge-33405b63da40/runs/hierarchical-sliding-window-with-token-merge-33405b63da40-20260522T141244351815+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/04fb381aed47

## What looked useful

The d=64 HSW merge model reached 100.0% held-out accuracy after 500 steps versus 6.8% for the recent-window baseline and 99.7% for a full-prefix Transformer. A near parameter-matched d=48 HSW model failed the 500-step threshold at 14.6% but reached 100.0% by 1000 steps, showing capacity/training-budget sensitivity rather than a hard mechanism failure.

## Boundaries and scale limits

Evidence is limited to a small synthetic retrieval task on one CPU worker. It does not test natural language modeling, long-context corpora, many random seeds, production attention kernels, or large model scales. The near parameter-matched HSW model needed 1000 steps to reach the same accuracy that the larger HSW model reached in 500 steps.

## Claim scope

In a controlled synthetic far-prefix associative retrieval benchmark with 24 key-value pairs and 16 possible values, a learned hierarchical sliding-window merge model can recover queried values from compressed prefix memory tokens while a recent-window-only Transformer remains at chance.

## Why it stopped

Tier 1 controlled direct test produced useful mechanism support, but the result is synthetic, narrow, and capacity-sensitive, so it is no-paper evidence rather than paper-positive validation.

## Recommended next action

Run a bounded deepen test with repeated seeds, variable key order/distractors, and equalized parameter/FLOP controls before considering any paper-oriented claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Seeded Robustness and Equalized Controls for HSW Token Merge Retrieval
- Success threshold: Mean HSW held-out accuracy >= 80%, mean HSW advantage over recent-window baseline >= 20 absolute points, and no more than one failed seed below 50% accuracy under equalized training budget.
- Stop condition: Stop if HSW mean accuracy is below 50%, if the advantage over recent-window is below 20 absolute points, or if full-prefix control cannot learn the benchmark under the same budget.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-trained-benchmark-for-hierarchical-sliding-window-tok-a37bfb88ec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
