# Chunked Pretraining with Exact-Anchor Replay

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `chunked-pretraining-with-exact-anchor-replay-98632728b87f`
Run ID: `chunked-pretraining-with-exact-anchor-replay-98632728b87f-20260525T034821640858+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7a13d09d61dc

## What looked useful

Exact-anchor replay was bitwise-identical to uninterrupted training (max parameter delta 0.0, eval-loss delta 0.0); missing RNG, missing optimizer state, and weights-only anchors diverged in parameter space.

## Boundaries and scale limits

Synthetic corpus, 160 optimizer steps, tiny 2-layer transformer, single GPU/process, no distributed data loader, no AMP/scheduler state, no real-corpus GPT-2-small-class baseline, and no checkpoint I/O overhead analysis.

## Claim scope

In a tiny deterministic CUDA PyTorch language-model pretraining proxy, chunked restart from exact anchors containing model, optimizer, and RNG state exactly reproduced uninterrupted training across four restart boundaries.

## Why it stopped

No-paper closure: bounded local mechanism evidence is useful, but the result is a tiny proxy rather than direct publication-grade validation.

## Recommended next action

Run a medium real-corpus transformer replay test with explicit scheduler, AMP, data-loader cursor, optimizer, and RNG capture before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium real-corpus exact-anchor replay confirmation
- Success threshold: Exact-anchor runs have zero or numerically negligible parameter/loss-trace divergence from uninterrupted controls at every restart boundary, while omitted-state controls show reproducible parameter divergence; checkpoint overhead is quantified.
- Stop condition: Stop if exact anchors diverge after all relevant state is captured, or if omitted-state controls do not diverge under stochastic training conditions.

## Evidence references

- Artifact root: `<local-path>/projects/chunked-pretraining-with-exact-anchor-replay-98632728b87f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
