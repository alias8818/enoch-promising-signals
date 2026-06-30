# Tiny-transformer confirmation of blockwise int8 AdamW state quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-transformer-confirmation-of-blockwise-int8-adamw-stat-82af356d7d`
Run ID: `tiny-transformer-confirmation-of-blockwise-int8-adamw-stat-82af356d7d-20260628T132911441749+0000`

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

- Parent run decision: 8-bit AdamW: blockwise vs per-tensor optimizer state quantization: enoch://control-plane/projects/8-bit-adamw-blockwise-vs-per-tensor-optimizer-state-quantization-22848bf99cf4/runs/8-bit-adamw-blockwise-vs-per-tensor-optimizer-state-quantization-22848bf99cf4-20260628T131251349883+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/dc6d1b4c93e6

## What looked useful

Naive blockwise int8 AdamW state reduced optimizer-state bytes to roughly 26-31% of fp32 state, but baseline lr=3e-4 runs degraded or diverged for block sizes 64-1024. Smaller blocks and lower lr stayed finite over 2 seeds, suggesting a stability boundary rather than broad confirmation.

## Boundaries and scale limits

Not tested on real corpora, GPT-2-small-class models, long convergence windows, or production 8-bit optimizer variants with clipping/outlier/error-feedback machinery.

## Claim scope

Local tiny causal Transformer on deterministic synthetic next-token data; matched fp32 AdamW versus custom blockwise-int8-state AdamW over short bounded GPU runs.

## Why it stopped

Proxy/local early falsification of the naive blockwise int8-state AdamW confirmation: the baseline tiny-transformer setting was unstable or materially worse than fp32 AdamW, while the finite lower-LR sensitivity result is not full validation.

## Recommended next action

Stop this no-paper confirmation attempt; run a bounded deepen follow-up that maps the stability boundary with a production-quality 8-bit AdamW design before considering larger validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stability boundary for blockwise int8 AdamW state in tiny language-model training
- Success threshold: No NaN/divergence in any seed, mean final loss delta int8 minus fp32 <= 0.25, max seed loss delta <= 0.5, and optimizer-state byte ratio <= 0.40.
- Stop condition: Stop if any improved quantization variant diverges in at least 2 of 3 seeds at block size <=64, or if state byte ratio must exceed 0.50 to match fp32 loss.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-transformer-confirmation-of-blockwise-int8-adamw-stat-82af356d7d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
