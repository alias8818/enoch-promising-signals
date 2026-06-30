# Real-corpus sub-100M validation for blockwise 8-bit AdamW

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-corpus-sub-100m-validation-for-blockwise-8-bit-adamw-a7d66c1e93`
Run ID: `real-corpus-sub-100m-validation-for-blockwise-8-bit-adamw-a7d66c1e93-20260621T134307546516+0000`

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

- Parent run decision: 8-bit AdamW Blockwise for Sub-100M Models: enoch://control-plane/projects/8-bit-adamw-blockwise-for-sub-100m-models-38d163321912/runs/8-bit-adamw-blockwise-for-sub-100m-models-38d163321912-20260621T110702205274+0000
- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/e2df2029c8a7

## What looked useful

Production blockwise 8-bit AdamW passed the Tier 1 direct threshold on a real corpus, but implementation details matter: a simple symmetric int8 moment store reduced memory and failed optimization badly.

## Boundaries and scale limits

Single corpus, character tokenization, one seed, 600-step early training, 3.23M parameters, optimizer-state memory only; no GPT-2-small-class, BPE, multi-seed, long-run persistence, or large-corpus validation.

## Claim scope

On a 3.23M-parameter sub-100M causal Transformer trained for 600 matched steps on the real Tiny Shakespeare corpus, production bitsandbytes AdamW8bit matched fp32 AdamW validation loss within 0.011% while using 25.9% of the persistent optimizer-state memory; a naive symmetric local blockwise int8 implementation diverged.

## Why it stopped

No-paper useful signal: Tier 1 direct validation supports the production implementation locally, but the evidence is too small, single-seed, and implementation-dependent for publication readiness.

## Recommended next action

Run a bounded medium confirmation with bitsandbytes AdamW8bit versus fp32 AdamW on a larger sub-100M BPE Transformer and real corpus for at least 3 seeds, including late-step persistence checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium multi-seed real-corpus confirmation for production 8-bit AdamW
- Success threshold: Across 3 seeds, bitsandbytes AdamW8bit final validation loss mean is within 2% of fp32 AdamW, no seed diverges beyond 5%, and persistent optimizer state is <=35% of fp32 AdamW.
- Stop condition: Stop as negative if any seed diverges beyond 5% final validation-loss ratio, if late-step loss spikes recur, or if the 8-bit optimizer state exceeds 35% of fp32 state.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-sub-100m-validation-for-blockwise-8-bit-adamw-a7d66c1e93`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
