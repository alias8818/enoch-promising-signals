# Fused GPT-2-small DynResAct latency and metadata accounting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `fused-gpt-2-small-dynresact-latency-and-metadata-accountin-c5841e0478`
Run ID: `fused-gpt-2-small-dynresact-latency-and-metadata-accountin-c5841e0478-20260517T155104810310+0000`

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

- Internal Enoch project: Fused GPT-2-small DynResAct latency and metadata accounting: internal_generated:fused-gpt-2-small-dynresact-latency-and-metadata-accountin-c5841e0478

## What looked useful

DynResAct-style MLP compute skipping produced real latency wins in several batch-4 prefill cells after metadata accounting, but batch-1 cells and B4/S256/active0.5 were neutral or negative. Host-visible route metadata added 3.5% to 8.7% latency over device-only routing; dense masking without compute skipping was negative in every cell.

## Boundaries and scale limits

No trained checkpoint, perplexity, downstream quality, recovery training, autoregressive KV-cache serving loop, or true custom fused CUDA/Triton kernel was tested. The measured implementation uses PyTorch eager top-k/gather/scatter, so results are not a full fused-kernel validation.

## Claim scope

Latency-only GPT-2-small-dimension BF16 inference microbenchmark on NVIDIA GB10 for a 12-layer random-weight stack, batch 1/4, sequence length 128/256, active ratios 0.25/0.5, comparing dense baseline with DynResAct-style MLP compute skipping and route metadata accounting.

## Why it stopped

Tier-2 direct latency evidence is mixed: the mechanism is useful in selected regimes but not robust across the tested grid, and the run lacks true kernel fusion and language-model quality validation.

## Recommended next action

Run one bounded deepen follow-up implementing a true fused CUDA/Triton routing plus residual-scatter kernel with compressed metadata, then require sustained batch-4 speedups after metadata accounting before any quality or paper escalation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: True fused DynResAct route+scatter kernel for GPT-2-small prefill
- Success threshold: After metadata accounting, top-k fused DynResAct must achieve at least 1.25x speedup in every batch-4 cell at sequence lengths 128 and 256 for active ratios 0.25 and 0.5, with no more than 5% median latency regression in any batch-1 cell.
- Stop condition: Stop if the fused implementation still loses in B4/S256/active0.5 or if host-visible metadata accounting reduces all batch-4 speedups below 1.25x.

## Evidence references

- Artifact root: `<local-path>/projects/fused-gpt-2-small-dynresact-latency-and-metadata-accountin-c5841e0478`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
