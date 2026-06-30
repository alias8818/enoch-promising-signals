# 8-bit AdamW with Loss-Scaled Updates for GPT-2 Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adamw-with-loss-scaled-updates-for-gpt-2-pretraining-5b5bc63119ce`
Run ID: `8-bit-adamw-with-loss-scaled-updates-for-gpt-2-pretraining-5b5bc63119ce-20260528T092223882890+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9f6fadd21e81

## What looked useful

The int8-state optimizer reduced measured optimizer-state bytes to about 25% of AdamW but diverged at lr=3e-4 and lr=1e-4 where AdamW trained stably. It only stayed finite at lr=3e-5, where it remained far worse than AdamW at competitive learning rates. Ordinary loss scaling produced identical losses to plain int8 in the diagnostic and added overhead, so it did not fix the quantized-moment failure mode.

## Boundaries and scale limits

Not full GPT-2 pretraining; no real text corpus; small model; short run; no fused/blockwise production 8-bit optimizer; no broad hyperparameter sweep beyond three learning rates.

## Claim scope

Bounded CUDA synthetic causal-LM probe of a simple symmetric per-tensor int8-moment AdamW implementation, with and without ordinary backward loss scaling, on a small GPT-style transformer for 200 steps across 3 seeds.

## Why it stopped

Proxy/early falsification: in a direct small transformer LM training loop, the proposed loss-scaled int8-state AdamW was unstable at useful AdamW learning rates and loss scaling did not change the trajectory.

## Recommended next action

Stop this mechanism as no-paper evidence; a bounded follow-up should test blockwise int8 second-moment quantization with an explicit denominator floor/residual against the same AdamW controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blockwise int8 AdamW with denominator floor for GPT-style LM training
- Success threshold: At lr=1e-4, blockwise/floored int8 remains finite for all seeds, reaches final eval loss within 0.2 nats of AdamW at the same LR, and keeps optimizer-state bytes at or below 35% of AdamW excluding diagnostics.
- Stop condition: Stop if any seed diverges before 200 steps at lr=1e-4 or if the required stabilizers push deployable optimizer-state memory above 50% of AdamW.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adamw-with-loss-scaled-updates-for-gpt-2-pretraining-5b5bc63119ce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
