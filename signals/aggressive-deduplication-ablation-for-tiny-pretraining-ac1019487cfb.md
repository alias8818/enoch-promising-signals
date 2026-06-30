# Aggressive Deduplication Ablation for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `aggressive-deduplication-ablation-for-tiny-pretraining-ac1019487cfb`
Run ID: `aggressive-deduplication-ablation-for-tiny-pretraining-ac1019487cfb-20260527T180841317716+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7a7e6dcc5445

## What looked useful

Aggressive near-dedup removed 83.3% of exact-unique paraphrase documents and was 3.25 nats worse than exact dedup on seen-query loss over 3 seeds; raw duplicates performed best under the fixed-step budget.

## Boundaries and scale limits

Synthetic corpus, 3-layer 96-dim Transformer, 3 seeds, 600 updates per condition; not natural web text, not GPT-2-small-class, not long-run or convergence-matched pretraining.

## Claim scope

In a synthetic tiny causal-LM pretraining proxy with paraphrased fact clusters, aggressive near-dedup that keeps one representative per cluster is substantially worse than exact dedup and raw duplicates under a fixed update budget.

## Why it stopped

Closed as no-paper useful signal: corrected synthetic proxy supports early warning that aggressive paraphrase-level dedup can harm tiny pretraining, but it is not full validation on natural corpora.

## Recommended next action

Run a bounded natural-corpus deepen test comparing raw, exact dedup, and near-dedup on a GPT-2-small-class or parameter-matched tiny LM with fixed-token and fixed-step controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-corpus tiny-LM dedup policy confirmation
- Success threshold: Aggressive near-dedup is at least 0.10 validation-loss nats worse than exact dedup in 2 or more seeds, or exact/raw consistently outperform aggressive at matched retained-token accounting.
- Stop condition: Stop if natural-corpus aggressive near-dedup is within +/-0.05 validation-loss nats of exact dedup across seeds or if removed clusters are dominated by boilerplate rather than semantic paraphrase reinforcement.

## Evidence references

- Artifact root: `<local-path>/projects/aggressive-deduplication-ablation-for-tiny-pretraining-ac1019487cfb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
