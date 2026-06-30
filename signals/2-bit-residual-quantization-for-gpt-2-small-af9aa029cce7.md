# 2-bit residual quantization for GPT-2-small

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `2-bit-residual-quantization-for-gpt-2-small-af9aa029cce7`
Run ID: `2-bit-residual-quantization-for-gpt-2-small-af9aa029cce7-20260528T183831798913+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/862178abae9a

## What looked useful

Two residual 2-bit stages at about 4.25 bits/weight had 2.11x higher weighted relative MSE than a 4-bit uniform baseline. Four residual stages at about 8.5 bits/weight had about 225x higher weighted relative MSE than an 8-bit uniform baseline. Four stages beat 4-bit uniform error by about 26% but used roughly double the payload.

## Boundaries and scale limits

Direct evidence is tensor reconstruction only: 62 GPT-2-small tensors and 136.9M scalar weights. No perplexity, downstream accuracy, generation quality, activation-aware calibration, fine-tuning recovery, or dequantized inference throughput was measured.

## Claim scope

For GPT-2-small rank >= 2 pretrained weight tensors, a simple fixed-level per-group residual 2-bit quantizer with scale-only residual stages is not competitive with ordinary per-group uniform quantization at comparable effective bit budgets.

## Why it stopped

Bounded direct-weight reconstruction evidence is an early falsification of the simple same-budget compression hypothesis, not a full model-quality validation.

## Recommended next action

Stop this simple residual 2-bit GPT-2-small weight-compression line unless a follow-on method adds a qualitatively stronger ingredient such as learned codebooks or activation-aware calibration and evaluates perplexity at matched effective bits.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-residual-quantization-for-gpt-2-small-af9aa029cce7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
