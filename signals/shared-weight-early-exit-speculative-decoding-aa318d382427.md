# Shared-Weight Early-Exit Speculative Decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `shared-weight-early-exit-speculative-decoding-aa318d382427`
Run ID: `shared-weight-early-exit-speculative-decoding-aa318d382427-20260525T124631773266+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/40dd4190e197

## What looked useful

Exact one-step speculative acceptance rose with depth, but the only exits with useful overlap cost about 0.90-0.91 of a full forward pass. Best optimistic speed estimates were 0.595x for distilgpt2 and 0.625x for gpt2 at gamma=2, so raw shared-head early exits are slower than baseline decoding in this setting.

## Boundaries and scale limits

Small GPT-2-class models only; WikiText-2 only; no trained early-exit heads; no KV-cache-aware serving implementation; speedup is an optimistic analytic model using measured GPU partial-forward latency rather than full generation throughput.

## Claim scope

Inference-only early falsification for raw shared-weight early exits on pretrained distilgpt2 and gpt2 over WikiText-2: intermediate hidden states projected through the shared final norm and tied LM head do not provide an optimistic speculative-decoding speedup.

## Why it stopped

Proxy/early falsification: direct distribution-overlap and measured partial-forward costs on GPT-2-class models show no speculative speedup for the untrained shared-weight method, but larger trained or serving-integrated variants were not fully validated.

## Recommended next action

Stop this raw shared-weight early-exit line as no-paper evidence; if continuing locally, test a trained low-depth exit head or calibration loss that must exceed 0.65 exact acceptance at no more than 0.35 full-forward cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train a Low-Cost Early-Exit Draft Head for Shared-Backbone Speculation
- Success threshold: At an exit no deeper than one-third of the model, achieve at least 0.65 exact acceptance with draft_cost_fraction at or below 0.35, or show a measured end-to-end speculative decoding speedup above 1.1x.
- Stop condition: Stop if trained/calibrated exits remain below 0.50 exact acceptance at one-third depth or if measured draft_cost_fraction exceeds 0.50 for all exits with acceptance above 0.60.

## Evidence references

- Artifact root: `<local-path>/projects/shared-weight-early-exit-speculative-decoding-aa318d382427`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
