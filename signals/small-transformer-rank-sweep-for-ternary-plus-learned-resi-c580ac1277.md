# Small Transformer Rank Sweep for Ternary Plus Learned Residual Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-transformer-rank-sweep-for-ternary-plus-learned-resi-c580ac1277`
Run ID: `small-transformer-rank-sweep-for-ternary-plus-learned-resi-c580ac1277-20260520T181412380935+0000`

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

- Parent run decision: Learned Residual Channels for Ternary-Plus-Correction Quantization: enoch://control-plane/projects/learned-residual-channels-for-ternary-plus-correction-quantization-329e57a71a01/runs/learned-residual-channels-for-ternary-plus-correction-quantization-329e57a71a01-20260520T145805882509+0000
- Parent run decision: Direct Small-Model Validation of Ternary Plus Learned Residual Channels: enoch://control-plane/projects/direct-small-model-validation-of-ternary-plus-learned-resi-7b8edc17df/runs/direct-small-model-validation-of-ternary-plus-learned-resi-7b8edc17df-20260520T163542372725+0000

## What looked useful

Ternary+residual rank sweep showed a stable mechanism signal: mean validation loss improved from 2.11805 at rank 0 to 2.09167 at rank 16, while low-rank-only controls were far worse. The dense baseline remained best at 1.99172, so the method is not competitive at this tested scale.

## Boundaries and scale limits

Small character-level LM only; not GPT-2-small-class, not a tokenized web benchmark, not long-convergence training, and no real quantized inference speed or memory measurement.

## Claim scope

On a 4-layer character-level Tiny Shakespeare transformer trained for 900 steps over seeds 0, 1, and 2, learned low-rank residual channels monotonically improve ternary-linear validation loss but do not match the dense baseline.

## Why it stopped

Tier 2 fixed-seed evidence found useful mechanism support but a persistent direct validation gap versus dense, so this is no-paper evidence rather than paper-positive support.

## Recommended next action

Run one bounded deepen follow-up with a parameter-matched dense baseline and a tokenized LM benchmark before spending on larger scale; stop if the dense gap remains above 0.03 validation-loss/perplexity-equivalent at the best residual rank.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-matched tokenized LM check for ternary plus learned residual channels
- Success threshold: Best ternary+residual condition is within 0.03 validation loss or equivalent perplexity margin of parameter-matched dense and shows a credible memory/throughput advantage path.
- Stop condition: Stop if rank 16 or 32 remains more than 0.03 validation loss behind parameter-matched dense after the planned training budget, or if quantized inference has no plausible memory/throughput advantage.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-rank-sweep-for-ternary-plus-learned-resi-c580ac1277`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
