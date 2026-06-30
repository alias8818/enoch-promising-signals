# Intermediate Layer Linear Probe as Zero-VRAM Drafter

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `intermediate-layer-linear-probe-as-zero-vram-drafter-6bfab5df7469`
Run ID: `intermediate-layer-linear-probe-as-zero-vram-drafter-6bfab5df7469-20260529T003303435114+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f12390d6958e

## What looked useful

Layer 3/6/9/11 fitted probes matched GPT-2 final greedy top-1 at 26.1%/32.5%/49.4%/69.6%, beating raw layer logit-lens agreement of 16.6%/22.2%/33.7%/36.8%. The probe is tiny for GPT-2-small, about 1.13 MiB fp16, but useful agreement appears mainly near the final layer.

## Boundaries and scale limits

CPU-only local run; GPT-2-small only; 2,048 train and 2,048 test token positions per layer; greedy same-position agreement proxy only; no production speculative decoding loop, no multi-token autoregressive drafting, no larger-model validation.

## Claim scope

On GPT-2-small over 2,048 Wikitext-2 token positions per layer, a ridge linear map from intermediate hidden states to final hidden states improves greedy next-token agreement over raw logit lens, but mid-layer agreement remains too low for a standalone drafter claim.

## Why it stopped

Proxy evidence does not support the practical zero-VRAM drafter claim: mid-layer greedy agreement is low, and high agreement only appears after most target-model layers have already run.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test confidence-gated early-exit speculative decoding wall-clock speed on GPT-2-small before considering larger models.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Confidence-Gated Early-Exit Probe Drafter on GPT-2 Small
- Success threshold: At least 1.10x wall-clock speedup over normal GPT-2-small greedy decoding on the same CPU or GPU while preserving at least 99% exact greedy-token agreement after fallback verification.
- Stop condition: Stop if confidence-gated probe exits cover under 20% of generated positions or wall-clock speedup is under 1.05x after implementation overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/intermediate-layer-linear-probe-as-zero-vram-drafter-6bfab5df7469`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
