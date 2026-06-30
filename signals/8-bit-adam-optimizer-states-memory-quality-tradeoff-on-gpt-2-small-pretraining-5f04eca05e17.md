# 8-bit Adam Optimizer States: Memory-Quality Tradeoff on GPT-2-small Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adam-optimizer-states-memory-quality-tradeoff-on-gpt-2-small-pretraining-5f04eca05e17`
Run ID: `8-bit-adam-optimizer-states-memory-quality-tradeoff-on-gpt-2-small-pretraining-5f04eca05e17-20260525T171040982181+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2982fedee8c3

## What looked useful

Optimizer-state compression behaved as expected mechanically, but simple 8-bit moment quantization destabilized validation loss across 3 seeds at block size 2048 and also collapsed in a block-size-64 diagnostic after early improvement.

## Boundaries and scale limits

Not a full GPT-2-small pretraining run; no Transformer stack, real corpus, CUDA kernels, mixed precision, or production bitsandbytes optimizer was tested. GPT-2-small memory impact is an arithmetic estimate from 124M parameters.

## Claim scope

A NumPy byte-level causal language-model proxy with 230,144 parameters shows that naive blockwise 8-bit Adam moment storage reduces optimizer-state memory by about 75% but is not quality-preserving under the tested settings.

## Why it stopped

The tested naive 8-bit Adam-state implementation failed the quality-preservation criterion in a causal-LM proxy, so this is no-paper useful evidence rather than full GPT-2-small validation.

## Recommended next action

Stop this worker run as a proxy early falsification; next bounded test should use a Python/PyTorch environment with a tiny GPT-2 Transformer and a production 8-bit Adam implementation before considering GPT-2-small scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production 8-bit Adam on a Tiny GPT-2 Transformer
- Success threshold: After a fixed token budget, 8-bit Adam validation loss is within 2% of FP32 AdamW in mean over seeds, no seed diverges, and optimizer-state memory is reduced by at least 65%.
- Stop condition: Stop if any 8-bit run diverges before 25% of the token budget or mean validation loss is more than 10% worse than FP32 AdamW at the midpoint checkpoint.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adam-optimizer-states-memory-quality-tradeoff-on-gpt-2-small-pretraining-5f04eca05e17`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
