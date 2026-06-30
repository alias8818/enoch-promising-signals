# Blockwise Quantized Adam for GPT-2-small CPU Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `blockwise-quantized-adam-for-gpt-2-small-cpu-pretraining-016df1a8280a`
Run ID: `blockwise-quantized-adam-for-gpt-2-small-cpu-pretraining-016df1a8280a-20260609T090102972452+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/47ec9868743a

## What looked useful

Blockwise int8 moment storage achieved the intended optimizer-state compression, but the naive symmetric quantization design destabilized AdamW updates in a GPT-style CPU training proxy and was also slower than AdamW. The observed failure persisted with smaller blocks and a 3x lower learning rate.

## Boundaries and scale limits

This run did not train GPT-2-small, did not use natural-language pretraining data, did not run beyond 30-step bounded proxy/ablation tests, and only analytically estimated GPT-2-small optimizer moment-state memory.

## Claim scope

On a 118,528-parameter CPU GPT-style causal Transformer proxy with deterministic synthetic next-token data, a naive symmetric-int8 blockwise AdamW moment store reduced optimizer moment-state memory by about 3.94x but diverged badly relative to fp32 AdamW over 30 steps.

## Why it stopped

Proxy evidence shows the tested naive blockwise symmetric-int8 AdamW variant is unstable despite memory savings; this is not a full GPT-2-small validation.

## Recommended next action

Stop this naive variant as an early proxy falsification; only continue via a bounded improved-quantizer test that protects second-moment denominators and must match AdamW loss within 5 percent on the same proxy before scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stability-preserving blockwise Adam moment quantization for GPT-style CPU training
- Success threshold: Improved quantized optimizer final loss within 5 percent of AdamW after at least 200 proxy steps, at least 3x optimizer moment-state reduction, and throughput no worse than 0.75x AdamW.
- Stop condition: Stop if the improved optimizer exceeds AdamW final loss by more than 20 percent, diverges, or runs below 0.5x AdamW throughput on the proxy.

## Evidence references

- Artifact root: `<local-path>/projects/blockwise-quantized-adam-for-gpt-2-small-cpu-pretraining-016df1a8280a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
