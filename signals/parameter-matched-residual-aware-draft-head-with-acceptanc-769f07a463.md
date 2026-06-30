# Parameter-matched residual-aware draft head with acceptance-length metrics

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `parameter-matched-residual-aware-draft-head-with-acceptanc-769f07a463`
Run ID: `parameter-matched-residual-aware-draft-head-with-acceptanc-769f07a463-20260527T165351079177+0000`

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

- Parent run decision: Residual-Aware Draft for CPU Speculative Decoding: enoch://control-plane/projects/residual-aware-draft-for-cpu-speculative-decoding-5bec6facd99f/runs/residual-aware-draft-for-cpu-speculative-decoding-5bec6facd99f-20260525T115550958373+0000
- Parent run decision: Residual-Aware Draft Head on a Small Real Transformer: enoch://control-plane/projects/residual-aware-draft-head-on-a-small-real-transformer-541bcfe9a6/runs/residual-aware-draft-head-on-a-small-real-transformer-541bcfe9a6-20260527T084803328421+0000

## What looked useful

Three fixed seeds with a real parameter-matched baseline and residual controls showed residual-aware confirmation-run gains: KL to target 0.00833 vs 0.00969 baseline, top-1 match 0.9303 vs 0.9255, sampled acceptance length 3.6029 vs 3.5433 out of 4, and greedy match length 3.4079 vs 3.3128. Shuffled-residual and residual-only controls were worse.

## Boundaries and scale limits

The target was a small residual MLP over character tokens, not a transformer or GPT-2-small-class model; acceptance was measured algorithmically against target distributions rather than as end-to-end wall-clock speculative decoding throughput.

## Claim scope

In a CPU-bounded NumPy residual-MLP character language model on Tiny Shakespeare, a parameter-matched residual-aware draft head improved frozen-target mimicry and direct speculative acceptance-length metrics after sufficient head fitting versus an early-hidden-state baseline.

## Why it stopped

Useful bounded mechanism signal, but not paper-positive because the model is a small NumPy residual MLP and the first calibrated run was mixed while the stronger confirmation effect was modest.

## Recommended next action

Stop short of paper writing; run one bounded transformer replication with a real hidden-state residual and measured decode throughput before escalating the claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer residual-aware draft head with wall-clock speculative decode metrics
- Success threshold: Residual-aware head improves mean accepted tokens by at least 2% and KL by at least 5% over the parameter-matched baseline across at least 3 fixed seeds, with non-negative measured throughput change.
- Stop condition: Stop if transformer replication shows less than 1% mean accepted-token gain, worse KL than baseline, or negative throughput after matched training and evaluation budget.

## Evidence references

- Artifact root: `<local-path>/projects/parameter-matched-residual-aware-draft-head-with-acceptanc-769f07a463`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
