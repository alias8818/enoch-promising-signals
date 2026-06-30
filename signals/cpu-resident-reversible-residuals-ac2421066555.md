# CPU-Resident Reversible Residuals

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-resident-reversible-residuals-ac2421066555`
Run ID: `cpu-resident-reversible-residuals-ac2421066555-20260602T152200979572+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1969124219c8

## What looked useful

Reversible residual reconstruction is numerically viable in the bounded test and gives depth-proportional activation residency reduction; CPU copy bandwidth on this host was only about 4.8-5.0 GB/s for 16-256 MiB buffers, so naive CPU-resident activation offload is likely bandwidth-sensitive without reducing transferred states.

## Boundaries and scale limits

No GPU-to-CPU transfer path, no PyTorch/autograd implementation, no optimizer training loop, no transformer attention/MLP block, and no large-model or long-run validation were tested.

## Claim scope

On a CPU-only NumPy additive-coupling residual stack, reversible backward reconstruction matched stored-activation backward within float32 tolerance and reduced analytic activation residency from L+1 full states to about two full states for depths 4-64.

## Why it stopped

No-paper useful signal: this run directly tested the reversible reconstruction mechanism and CPU memory bandwidth, but CPU-resident GPU offload and training outcomes were only proxied.

## Recommended next action

Run a single-GPU PyTorch benchmark comparing ordinary residuals, activation checkpointing, CPU offload, reversible reconstruction, and reversible-plus-CPU-resident offload on identical transformer-block shapes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Single-GPU CPU-Offload Benchmark for Reversible Residual Blocks
- Success threshold: Reversible-plus-offload achieves at least 2x lower peak GPU activation memory than standard residuals and at least 20% better step time than naive CPU offload while maintaining gradient/loss parity in a short run.
- Stop condition: Stop if reversible-plus-offload is slower than naive CPU offload by more than 20%, fails gradient parity, or does not reduce peak GPU memory beyond ordinary activation checkpointing.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-resident-reversible-residuals-ac2421066555`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
