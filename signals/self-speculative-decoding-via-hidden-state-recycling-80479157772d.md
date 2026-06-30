# Self-Speculative Decoding via Hidden-State Recycling

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `68`
Project ID: `self-speculative-decoding-via-hidden-state-recycling-80479157772d`
Run ID: `self-speculative-decoding-via-hidden-state-recycling-80479157772d-20260619T081202202213+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 10, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- weak evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/24e16e9faa51

## What looked useful

Hidden-state recycling preserved the toy early-exit trajectory reasonably well, but early-exit token agreement with the full model was only about 6.8%, making speculative acceleration non-viable in this setup.

## Boundaries and scale limits

No pretrained transformer, natural-language benchmark, attention KV-cache, GPU latency, or production serving path was tested; evidence is a short CPU-only proxy run.

## Claim scope

Synthetic NumPy residual-model probe of whether a learned linear map can recycle early-exit hidden states across drafted tokens.

## Why it stopped

Proxy-only useful signal: state recycling was mechanically feasible in the toy model, but the low early-exit acceptance prevents any paper-ready acceleration claim.

## Recommended next action

Run a bounded direct follow-up on an actual early-exit/self-speculative checkpoint and stop if recycled drafting fails to preserve at least 90% of baseline early-exit acceptance or reduce draft-side compute by at least 25%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct hidden-state recycling test on an early-exit self-speculative checkpoint
- Success threshold: Recycled drafting preserves >=90% of baseline early-exit acceptance and reduces draft-side compute or latency by >=25% on a small real-checkpoint benchmark.
- Stop condition: Stop if acceptance drops below 90% of baseline early-exit drafting, verification changes final outputs, or latency/compute savings are below 25%.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-hidden-state-recycling-80479157772d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
