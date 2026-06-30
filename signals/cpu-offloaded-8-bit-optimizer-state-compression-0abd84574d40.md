# CPU-Offloaded 8-bit Optimizer State Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-offloaded-8-bit-optimizer-state-compression-0abd84574d40`
Run ID: `cpu-offloaded-8-bit-optimizer-state-compression-0abd84574d40-20260524T210342324545+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/784630b0ac91

## What looked useful

Memory savings are real, but naive per-block 8-bit moment quantization creates large update errors and can destabilize AdamW; stabilization is required before this idea is worth scale testing.

## Boundaries and scale limits

No GPU offload transfer behavior, large-model training, distributed training, or production 8-bit optimizer stabilizers were tested. Evidence is limited to synthetic regression and optimizer-update microbenchmarks under an 80-step CPU budget.

## Claim scope

On a deterministic CPU-only NumPy proxy, naive blockwise 8-bit AdamW moment compression reduced CPU-resident optimizer-state memory by about 3.76x to 3.99x but failed to preserve FP32 AdamW convergence on the medium synthetic regression target.

## Why it stopped

The bounded proxy directly tested compressed AdamW state and found severe convergence degradation despite about 4x memory compression; this is not a full validation, but it is enough to reject the naive mechanism as paper-ready.

## Recommended next action

Stop this run as a proxy early falsification of naive 8-bit state compression; next test should add explicit stabilizers before any GPU/offload-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stabilized CPU-offloaded 8-bit AdamW State Compression
- Success threshold: A stabilized variant has median final loss ratio <= 1.10 versus FP32 AdamW across 3 seeds, maximum relative update error <= 2.0 after warmup, and state compression >= 3x.
- Stop condition: Stop if all stabilization variants still exceed 1.5x FP32 final loss or show max relative update error above 10x on two or more seeds.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-8-bit-optimizer-state-compression-0abd84574d40`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
