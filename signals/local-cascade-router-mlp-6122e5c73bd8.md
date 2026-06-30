# Local Cascade Router MLP

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-cascade-router-mlp-6122e5c73bd8`
Run ID: `local-cascade-router-mlp-6122e5c73bd8-20260528T144854332361+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5b66d5fcf0a5

## What looked useful

The bottleneck cascade run reached 100% validation and hard-token accuracy with hard-token gate mean 0.1943 versus easy-token gate mean 0.0096, a clear router-specialization diagnostic. The result is not an architecture win because dense_cheap also reached 100% accuracy with a lower FFN compute proxy.

## Boundaries and scale limits

Synthetic task only, one seed, one-block small transformer, analytical FFN compute proxy only, no actual inference branch skipping or wall-clock serving speedup, no GPT-2-small-class language-model baseline.

## Claim scope

One-block PyTorch transformer synthetic sequence-labeling probes on GB10 show a local cascade FFN router can learn higher gate values on hard synthetic tokens than easy tokens while preserving accuracy, but the tested tasks are also solved by much cheaper dense FFN baselines.

## Why it stopped

The tested synthetic probes do not support a practical cascade advantage: the router specializes, but simpler cheap dense baselines solve the task with equal accuracy and lower compute proxy.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use a harder benchmark where the cheap dense baseline is verified insufficient before evaluating cascade routing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Harder Local Cascade Router Benchmark With Verified Cheap-Baseline Gap
- Success threshold: Cascade matches dense_full within 2% relative validation loss or absolute task accuracy, beats dense_cheap by at least half the dense_full-vs-dense_cheap gap, and reduces measured inference FFN compute or latency by at least 40%.
- Stop condition: Stop as negative if dense_cheap solves the benchmark, if cascade collapses to dense_cheap accuracy, or if measured inference savings are below 20% after branch skipping is implemented.

## Evidence references

- Artifact root: `<local-path>/projects/local-cascade-router-mlp-6122e5c73bd8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
