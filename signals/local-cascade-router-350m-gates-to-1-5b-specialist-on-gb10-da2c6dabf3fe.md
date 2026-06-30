# Local Cascade Router: 350M Gates to 1.5B Specialist on gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-cascade-router-350m-gates-to-1-5b-specialist-on-gb10-da2c6dabf3fe`
Run ID: `local-cascade-router-350m-gates-to-1-5b-specialist-on-gb10-da2c6dabf3fe-20260630T163532770132+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/98573a40af07

## What looked useful

The 350M-class router cost about 3.8-4.7 ms versus 14-18 ms for the 1.5B-class specialist, making expected sequential service viable only if specialist route rate remains below roughly 68-73%. Strict synchronous microbatch latency did not beat dense specialist-only serving for any tested nonzero route fraction.

## Boundaries and scale limits

Single GB10 host, synthetic decode-shaped projection/MLP kernels, batches 1/2/4/8/16, no real tokenizer, KV cache, scheduler, model weights, routing accuracy, or quality evaluation.

## Claim scope

Synthetic GB10 serving-cost proxy for a resident BF16 350M-class router gating a resident BF16 1.5B-class specialist; no router training or task quality was tested.

## Why it stopped

Proxy serving-cost evidence is mixed: it supports sparse/asynchronous cascade plausibility but falsifies a broad latency-win claim for synchronous microbatches at the tested nonzero route fractions.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should measure a real router's safe specialist-avoidance rate and real model latency under online and microbatched serving.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real router avoidance-rate and latency validation for 350M-to-1.5B local cascade
- Success threshold: At least 70% specialist avoidance with quality within 2% absolute of dense specialist baseline and end-to-end p50 latency faster than dense specialist-only serving in the intended serving regime.
- Stop condition: Stop if safe specialist avoidance is below 60% or if real end-to-end latency remains slower than dense specialist-only serving after scheduler/KV-cache measurement.

## Evidence references

- Artifact root: `<local-path>/projects/local-cascade-router-350m-gates-to-1-5b-specialist-on-gb10-da2c6dabf3fe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
