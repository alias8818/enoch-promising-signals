# Per-Layer FP8 Residual for 2-bit Weight Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-layer-fp8-residual-for-2-bit-weight-quantization-6772fbf3bf2b`
Run ID: `per-layer-fp8-residual-for-2-bit-weight-quantization-6772fbf3bf2b-20260628T172641981213+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ca36c73b2e4f

## What looked useful

A full FP8 residual after 2-bit quantization nearly reconstructs weights, but it costs about 10 effective bits per weight. On 12 distilgpt2 tensors it reduced mean NMSE only from 0.0007041226 for direct FP8 to 0.0006967704 while using 25% more storage, making the literal proposal storage-dominated by direct FP8.

## Boundaries and scale limits

No downstream perplexity, task accuracy, latency, kernel, or calibration-data evaluation. The test uses per-tensor symmetric quantization and treats the FP8 residual as a full stored tensor, so it evaluates the literal residual-storage proposal rather than sparse or learned residual variants.

## Claim scope

Reconstruction-level evaluation of 2-bit symmetric weight quantization plus a full per-weight FP8 E4M3 residual on synthetic tensors and 12 distilgpt2 weight tensors.

## Why it stopped

Proxy reconstruction evidence is an early falsification of the literal full FP8 residual proposal as a compression method, not a full downstream validation.

## Recommended next action

Stop this literal full-residual line as no-paper evidence; if continuing, test a sparse or gated FP8 residual with an explicit storage budget below direct FP8.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Sparse FP8 Residuals Under an 8-bit Storage Budget
- Success threshold: At less than 8 effective bits per weight, sparse residuals reduce downstream degradation versus direct 4-bit or 6-bit controls and approach direct FP8 reconstruction/perplexity within a predeclared tolerance.
- Stop condition: Stop if matched-budget sparse residuals are not better than ordinary 4-bit/6-bit quantization or remain worse than direct FP8 at comparable storage.

## Evidence references

- Artifact root: `<local-path>/projects/per-layer-fp8-residual-for-2-bit-weight-quantization-6772fbf3bf2b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
