# Per-layer adaptive gradient checkpointing by activation-recompute cost ratio

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `per-layer-adaptive-gradient-checkpointing-by-activation-recompute-cost-ratio-051f06e9529d`
Run ID: `per-layer-adaptive-gradient-checkpointing-by-activation-recompute-cost-ratio-051f06e9529d-20260619T172447060029+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.2: enoch://research-facility/provider/hf:zai-org/GLM-5.2/ef060c769267

## What looked useful

Across k=2/4/6/8 checkpoint counts, the adaptive ratio policy was never the best memory-per-overhead policy. Cheapest-recompute won efficiency at k=4/6/8, while largest-saved dominated at k=2. Many policies hit the same roughly 5.226% CUDA peak-memory reduction ceiling, showing extra checkpointed layers can add recompute without reducing global peak.

## Boundaries and scale limits

Synthetic 12-block MLP-style model only; no transformer attention, mixed precision, distributed training, full optimizer-state pressure, compiler planner, or long training dynamics.

## Claim scope

On a small heterogeneous CUDA PyTorch model with non-reentrant checkpointing, selecting checkpointed layers by measured saved-activation bytes divided by forward recompute time did not improve the memory/runtime tradeoff over simpler policies at equal checkpoint count.

## Why it stopped

Small direct CUDA benchmark unsupported the proposed ratio heuristic; this is an early bounded falsification, not full-scale validation.

## Recommended next action

Stop this run as a bounded negative/useful-signal result; if pursued, run one transformer-block follow-up under mixed precision and realistic sequence lengths before considering any larger validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer-block validation of checkpoint selection by activation/recompute ratio
- Success threshold: Adaptive ratio must reduce CUDA peak memory at least as much as the best simple baseline while improving saved-MB-per-ms-overhead by at least 15% on two or more transformer-size settings.
- Stop condition: Stop if adaptive ratio is not best or statistically tied for best efficiency on the first two transformer settings, or if peak memory remains dominated by non-activation allocations.

## Evidence references

- Artifact root: `<local-path>/projects/per-layer-adaptive-gradient-checkpointing-by-activation-recompute-cost-ratio-051f06e9529d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
