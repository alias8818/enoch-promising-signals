# Streaming Low-Memory Adam Moments on a Small Language Model

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `streaming-low-memory-adam-moments-on-a-small-language-mode-306e86668c`
Run ID: `streaming-low-memory-adam-moments-on-a-small-language-mode-306e86668c-20260514T020106779070+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/0af97e7226e1

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Mechanism support was demonstrated in a Tier 1 controlled small direct CUDA test, but the evidence is not publication-grade because it uses synthetic data, short horizons, and a reference CPU-streamed optimizer rather than real-corpus training with production baselines.

## Recommended next action

Run a bounded medium direct-evidence follow-up on a real tokenized corpus with a GPT-2-small-class or parameter-matched model, comparing streamed/offloaded Adam moments against standard AdamW and at least one established low-memory optimizer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus Medium Validation for Streamed Adam Moment Storage
- Success threshold: Reduce CUDA peak optimizer-state memory by at least 80% of the theoretical two-fp32-moment AdamW footprint while keeping validation loss within 1% of standard AdamW at the matched step budget and avoiding more than 2x wall-clock slowdown.
- Stop condition: Stop if validation loss diverges by more than 3% from standard AdamW after warmup, if UMA/MemAvailable telemetry shows unsafe memory pressure, or if wall-clock slowdown exceeds 3x without a clear implementation fix.

## Evidence references

- Artifact root: `<local-path>/projects/streaming-low-memory-adam-moments-on-a-small-language-mode-306e86668c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
