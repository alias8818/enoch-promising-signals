# Mixed-Precision Draft-Verifier Cascade on gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `mixed-precision-draft-verifier-cascade-on-gb10-72dca04d8ebd`
Run ID: `mixed-precision-draft-verifier-cascade-on-gb10-72dca04d8ebd-20260614T120501973802+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d3101b0c3e95

## What looked useful

Draft top-k containment can be high when verifier logits are mostly explained by the draft subspace, but the measured cascade was consistently slower than full BF16 projection on GB10. Best cascade speedup was 0.244x and worst was 0.106x across 32 medium cases; PyTorch FP8 addmm failed for both float8_e4m3fn and float8_e5m2.

## Boundaries and scale limits

Not an end-to-end LLM serving run; no trained draft model; no full transformer forward pass; low-precision draft used quantize/dequantize BF16 because native PyTorch FP8 addmm was unavailable; candidate verifier was implemented with ordinary PyTorch gather plus batched matmul rather than a fused custom kernel.

## Claim scope

Synthetic GB10 projection benchmark comparing full BF16 verifier logits against a quantized lower-dimensional draft projection plus BF16 top-k candidate verification using PyTorch CUDA operations.

## Why it stopped

Proxy/synthetic GB10 evidence early-falsified the practical speed claim for a naive PyTorch mixed-precision draft-verifier cascade; it is not a full end-to-end validation.

## Recommended next action

Stop this run as a no-paper useful signal; the only bounded next test worth running is a fused candidate-verifier kernel or production backend experiment that must beat full BF16 projection on the same GB10 shapes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused Candidate Verifier Kernel for GB10 Draft Cascades
- Success threshold: Cascade total mean latency at least 1.25x faster than full BF16 projection with at least 99% exact top-1 agreement for tail_scale <= 0.25 on both vocabulary sizes.
- Stop condition: Stop if the fused candidate verifier remains slower than full BF16 projection or if top-1 agreement falls below 99% in the low-tail correlated cases.

## Evidence references

- Artifact root: `<local-path>/projects/mixed-precision-draft-verifier-cascade-on-gb10-72dca04d8ebd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
