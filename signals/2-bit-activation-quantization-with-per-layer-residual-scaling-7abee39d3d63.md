# 2-bit Activation Quantization with Per-Layer Residual Scaling

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-activation-quantization-with-per-layer-residual-scaling-7abee39d3d63`
Run ID: `2-bit-activation-quantization-with-per-layer-residual-scaling-7abee39d3d63-20260629T174112603706+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/66965a9ddd71

## What looked useful

Fixed residual interpolation recovered a small mean +0.0078125 accuracy over strict 2-bit across 8 seeds; learned residual scaling recovered only +0.0036621 and stayed below FP32 by -0.0227051. The mechanism is weak and depends on retaining non-2-bit residual information.

## Boundaries and scale limits

No real transformer/LLM, no hardware kernel, no external dataset, no full activation memory implementation, and no publication-grade benchmark. Residual-scaled variants forward scaled full-precision residual information, so they are not strict 2-bit activation-storage evidence.

## Claim scope

Bounded NumPy synthetic teacher-student MLP probe of dynamic 2-bit ReLU activation quantization with fixed or learned per-layer residual interpolation.

## Why it stopped

Proxy evidence was sufficient for a no-paper useful signal: residual scaling gave only small, variance-sensitive gains and the improvement came from forwarding scaled full-precision residual information rather than preserving a strict 2-bit activation path.

## Recommended next action

Do not write a paper from this run; run one bounded direct transformer or vision QAT test with explicit activation-memory accounting before considering any follow-up claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded direct QAT test for residual-scaled 2-bit activations with memory accounting
- Success threshold: At least +1.5 percentage points accuracy or equivalent perplexity improvement over strict 2-bit while retaining at least 3x activation memory reduction versus FP32, with the gain positive on most paired runs.
- Stop condition: Stop if residual-scaled variants fail to exceed strict 2-bit by more than run-to-run variance, or if the residual path eliminates the claimed activation memory savings.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-activation-quantization-with-per-layer-residual-scaling-7abee39d3d63`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
