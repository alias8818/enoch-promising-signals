# Blockwise 8-bit Adam + CPU Offload

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `blockwise-8-bit-adam-cpu-offload-a0ce7c1edc59`
Run ID: `blockwise-8-bit-adam-cpu-offload-a0ce7c1edc59-20260526T033011477511+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/acd2798a41c2

## What looked useful

Blockwise 8-bit CPU-offloaded Adam can materially reduce GPU memory footprint, but the naive copy-to-CPU/update/copy-back implementation is too slow and less stable at default learning rate to justify a paper or drop-in replacement claim.

## Boundaries and scale limits

Evidence is limited to short synthetic MLP runs, not real language-model training, long-horizon convergence, validation perplexity, or optimized pinned/asynchronous offload implementations.

## Claim scope

On a local GB10 synthetic 55.6M-parameter fp32 MLP regression workload, a naive blockwise int8 Adam prototype with CPU-resident moments reduced optimizer state to 25.05% of AdamW and PyTorch CUDA peak allocation to 49.13% of AdamW in stable low-learning-rate runs, but made steps about 4.76x slower and diverged at lr=1e-3.

## Why it stopped

Short local evidence supports the memory mechanism but not practical speed or default-learning-rate stability; this is a bounded proxy result rather than publication-grade direct training evidence.

## Recommended next action

Stop this run as no-paper useful signal; if continuing, run one bounded deepen test with pinned/asynchronous offload and a learning-rate stability sweep on a GPT-2-small-class workload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pinned asynchronous 8-bit Adam CPU offload stability and overhead test
- Success threshold: Blockwise CPU-offloaded 8-bit Adam keeps GPU peak allocation at least 35% below AdamW, keeps final validation/proxy loss within 2% of AdamW, has no NaNs in the tested learning-rate sweep, and reduces mean step-time overhead below 2x AdamW.
- Stop condition: Stop if lr=1e-4 still exceeds 3x AdamW step time after pinned/asynchronous implementation, or if any tested learning rate required for AdamW parity diverges while AdamW remains stable.

## Evidence references

- Artifact root: `<local-path>/projects/blockwise-8-bit-adam-cpu-offload-a0ce7c1edc59`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
