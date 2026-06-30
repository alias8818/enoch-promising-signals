# Rank-1 Optimizer Memory Factorization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `rank-1-optimizer-memory-factorization-6a930cba6180`
Run ID: `rank-1-optimizer-memory-factorization-6a930cba6180-20260528T204931011160+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/24065d3f03ce

## What looked useful

Full rank-1 first+second moment factorization reduced state from 3.1847 MiB to 0.0618 MiB but had mean update cosine 0.0800 vs AdamW and mean validation loss 35.4350 vs 4.9297. Second-moment-only factorization reduced state to 1.6232 MiB and reached mean validation loss 4.8839, but update cosine was only 0.7518 with relative L2 0.7702.

## Boundaries and scale limits

Synthetic data, tiny model, short training horizon, one learning-rate setting, and one simple row/column factorization rule; no GPT-2-small-class real-corpus validation, no mixed-precision/distributed optimizer test, and no broad hyperparameter sweep.

## Claim scope

On a tiny CUDA Transformer trained for 220 steps across 3 seeds on a deterministic synthetic sequence task, simple rank-1 factorization of both Adam first and second moments saved optimizer memory but failed update-fidelity and validation-loss checks; factorizing only the second moment preserved small-task validation loss while saving about half the optimizer state.

## Why it stopped

Proxy/early falsification for the full rank-1 first+second moment hypothesis: the simple factorization produced nearly orthogonal updates and severe validation-loss degradation, although a narrower second-moment-only variant remains worth bounded follow-up.

## Recommended next action

Stop this run as a no-paper useful signal: do not pursue full rank-1 first+second Adam moment factorization without a better signed first-moment estimator; run a bounded real-corpus GPT-2-small-class follow-up for the second-moment-only variant.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus validation of second-moment-only rank-1 optimizer state
- Success threshold: Rank1_v_only validation loss or perplexity within 2% of AdamW at matched tokens and no more than 10% wall-clock slowdown, with at least 45% optimizer-state memory reduction.
- Stop condition: Stop if rank1_v_only exceeds AdamW validation loss/perplexity by more than 5% in two matched real-corpus runs or requires hyperparameters that erase the memory/throughput advantage.

## Evidence references

- Artifact root: `<local-path>/projects/rank-1-optimizer-memory-factorization-6a930cba6180`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
