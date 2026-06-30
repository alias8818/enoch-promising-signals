# Local model cascade router on GB10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `local-model-cascade-router-on-gb10-616fc8663998`
Run ID: `local-model-cascade-router-on-gb10-616fc8663998-20260613T033859160727+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bfdae30b842d

## What looked useful

The small-model confidence margin was not reliable enough to route safely: MMLU eval dropped from 58% large accuracy to 56% cascade accuracy with only 2% small accepts, and ARC-Easy eval dropped from 92% to 88% with 10% small accepts. Estimated cascade inference was slower than always-large on both 100-example runs because the small prepass cost was not offset by avoided large calls.

## Boundaries and scale limits

Evidence is limited to local Hugging Face Transformers causal-LM option scoring, 100 examples per medium benchmark, unbatched sequential inference, cached Qwen-family models, and multiple-choice answer-letter scoring. It does not rule out learned routers, better-calibrated small models, batched serving engines, quantized models, or generation workloads.

## Claim scope

A simple confidence-margin cascade from Qwen/Qwen2.5-Coder-0.5B-Instruct or Qwen/Qwen3-0.6B to Qwen/Qwen2.5-3B-Instruct on GB10 did not preserve large-model accuracy or reduce measured inference cost on bounded multiple-choice MMLU college computer science and ARC-Easy tests.

## Why it stopped

Bounded direct GB10 evaluations showed the simple confidence-margin cascade fails to preserve accuracy and is slower than always-large under the tested conditions.

## Recommended next action

Stop this margin-router line as no-paper evidence; if continuing locally, test a learned lightweight router trained to predict small-large disagreement rather than using raw small-model margin.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned disagreement router for local GB10 cascades
- Success threshold: Held-out cascade accuracy no more than 1 percentage point below always-large and at least 25% fewer large-model calls with measured end-to-end speedup greater than 1.15x.
- Stop condition: Stop if the learned router cannot exceed 5% safe small-model accept rate at large-model accuracy parity on held-out data or if end-to-end speed remains slower than always-large.

## Evidence references

- Artifact root: `<local-path>/projects/local-model-cascade-router-on-gb10-616fc8663998`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
