# Factorized quality ablation with equalized unique-example count

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `factorized-quality-ablation-with-equalized-unique-example-14a9eb3fb4`
Run ID: `factorized-quality-ablation-with-equalized-unique-example-14a9eb3fb4-20260629T085446323130+0000`

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

- Parent run decision: Dataset quality benchmark for generalized understanding beyond scale: enoch://control-plane/projects/frontier-dataset-quality-generalized-understanding-benchmark-20260628/runs/frontier-dataset-quality-generalized-understanding-benchmark-20260628-20260629T064245391541+0000
- Linear ALI-208 frontier research issue: linear-ALI-208
- Jeremy frontier AI research intake: DSpark, post-training, dataset quality: user-frontier-ai-research-tracks-20260628

## What looked useful

Equalized unique-example count did not erase quality effects: 30% label noise increased test BCE by +0.3408 versus balanced clean, biased clean coverage reduced accuracy by -0.0292 and increased BCE by +0.0597, and combining both had the worst mean accuracy and BCE.

## Boundaries and scale limits

Synthetic mixture data, logistic regression, 30 seeds, 1000 unique examples per condition, and two narrow quality factors only. No LLM, real corpus, deduplication pipeline, large-scale training, or long-run validation was tested.

## Claim scope

In a controlled synthetic binary-classification proxy with 1000 unique training examples per condition, fixed optimizer budget, fixed model class, and balanced held-out testing, label correctness and coverage quality both measurably affect held-out accuracy or BCE after unique-example count is equalized.

## Why it stopped

The local run provides a reproducible useful signal but remains a synthetic proxy, so it is not a full validation or paper-ready result.

## Recommended next action

Run a bounded deepen follow-up on a real small benchmark with explicit deduplication, equal unique-example counts, matched token/update budgets, and a small neural baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Equalized unique-count quality ablation on a real small benchmark
- Success threshold: Quality-degraded conditions show a consistent held-out loss or accuracy degradation versus the high-quality baseline across at least 5 seeds while preserving equal unique-example count and matched update budget.
- Stop condition: Stop if equalization cannot be verified, the run exceeds the local compute budget without checkpointed metrics, or quality-degraded conditions do not consistently underperform the high-quality baseline.

## Evidence references

- Artifact root: `<local-path>/projects/factorized-quality-ablation-with-equalized-unique-example-14a9eb3fb4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
