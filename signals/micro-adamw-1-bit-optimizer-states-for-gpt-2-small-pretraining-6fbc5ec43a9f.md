# Micro-AdamW: 1-bit optimizer states for GPT-2-small pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `micro-adamw-1-bit-optimizer-states-for-gpt-2-small-pretraining-6fbc5ec43a9f`
Run ID: `micro-adamw-1-bit-optimizer-states-for-gpt-2-small-pretraining-6fbc5ec43a9f-20260605T083254123052+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/bdff207184ae

## What looked useful

OneBitAdamW at the AdamW default LR trailed AdamW by 0.133 mean final validation loss, but at LR 1e-3 reduced the gap to 0.028 on the proxy. Analytic optimizer-state memory fell from 6.240 MiB to 0.195 MiB for the tested model, about 31.9x. This supports bounded follow-up but not a paper-ready GPT-2-small pretraining claim.

## Boundaries and scale limits

This did not train GPT-2-small, did not use a real text corpus, did not validate long-run stability, and did not implement production bit-packing; PyTorch int8 signs and temporary dense reconstructed moments mean wall-clock speed and peak allocation are not evidence of deployable memory savings.

## Claim scope

A self-contained 817,920-parameter GPT-style synthetic language-model proxy showed that a sign-plus-scale 1-bit-state AdamW variant can train without divergence for 300 steps and can approach the best AdamW control after learning-rate tuning, while analytically reducing two-moment optimizer state from 64 bits per parameter to about 2 bits per parameter plus tensor scales.

## Why it stopped

Proxy-only evidence supports mechanism viability but is insufficient for GPT-2-small pretraining validation or a paper-positive claim.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up on a real-token 10M-50M parameter causal LM with a better-specified 1-bit nonnegative second-moment encoding and true memory profiling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus 1-bit AdamW state test on a 10M-50M parameter GPT proxy
- Success threshold: The 1-bit-state variant stays within 0.05 final validation loss of the best AdamW control with at least 16x measured optimizer-state memory reduction and no divergence across runs.
- Stop condition: Stop if the 1-bit variant trails AdamW by more than 0.10 validation loss after tuned LR schedules or shows recurrent instability/divergence on the real-corpus run.

## Evidence references

- Artifact root: `<local-path>/projects/micro-adamw-1-bit-optimizer-states-for-gpt-2-small-pretraining-6fbc5ec43a9f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
