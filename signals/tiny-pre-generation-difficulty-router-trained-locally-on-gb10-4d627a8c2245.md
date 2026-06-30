# Tiny pre-generation difficulty router trained locally on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-pre-generation-difficulty-router-trained-locally-on-gb10-4d627a8c2245`
Run ID: `tiny-pre-generation-difficulty-router-trained-locally-on-gb10-4d627a8c2245-20260628T121043444324+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1d6ea97e5fcf

## What looked useful

Across five seeds, in-distribution router accuracy/AUC was 1.000/1.000 and simulated quality averaged 0.934 at cost 5.52 versus always-big cost 10.0. Under shifted templates, expected routing quality fell to 0.579, and on a length-cue challenge split it fell to 0.726, showing calibration brittleness despite strong ranking signal.

## Boundaries and scale limits

Synthetic labels only; no live small/large model generations; CPU-only local runs; five seeds; prompt templates are toy distributions and do not validate broad real-world LLM routing.

## Claim scope

On a synthetic prompt-family difficulty task, a tiny prompt-only MLP router can reduce simulated large-model routing cost in-distribution while meeting a 0.90 expected-quality target, but its validation-selected threshold fails under template shift.

## Why it stopped

No-paper useful signal: the synthetic proxy supports a narrow mechanism in-distribution but directly falsifies robust threshold transfer under prompt-template shift.

## Recommended next action

Run a bounded follow-up with live small/large model outcome labels and mixed-domain threshold calibration; stop treating synthetic-only threshold success as evidence for deployment.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-label calibration test for tiny pre-generation difficulty routing
- Success threshold: Achieve expected quality >= 0.90 on every held-out prompt family while reducing mean cost by at least 25% relative to always-big, with no held-out family below 0.88 quality.
- Stop condition: Stop as negative if any held-out prompt family falls below 0.88 expected quality at thresholds chosen from non-held-out validation data, or if cost reduction versus always-big is under 15%.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-pre-generation-difficulty-router-trained-locally-on-gb10-4d627a8c2245`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
