# Activation Quantization with Learned Residual Projection Subspace

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-quantization-with-learned-residual-projection-subspace-b4ac8e8e1baa`
Run ID: `activation-quantization-with-learned-residual-projection-subspace-b4ac8e8e1baa-20260621T203532001204+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/59f15e12bd75

## What looked useful

Residual projection is a real narrow mechanism for preserving downstream-sensitive low-dimensional quantization residual directions, but this run argues against broad claims that it is a generally competitive activation quantizer versus spending bits on denser quantization.

## Boundaries and scale limits

Synthetic activations only; no real transformer traces, no task-level quality metrics, no kernel/runtime overhead measurement, dimension 256, 4096 train vectors, 2048 test vectors, 3 seeds.

## Claim scope

Bounded NumPy synthetic activation probe: learned PCA residual projection improves low-rank residual-sensitive downstream output error and usually beats random/activation-PCA residual controls, but does not beat plain higher-bit affine quantization for generic reconstruction or random downstream output under comparable bit budgets.

## Why it stopped

No-paper closure: bounded synthetic evidence is useful and mixed, but it is not direct/full validation; generic reconstruction and random-output metrics were roughly 4x worse than the next dense bit at rank 16.

## Recommended next action

Run a bounded deepen test on real transformer layer activations and actual layer weights, comparing same-bit-budget residual projection against dense b+1 quantization and standard activation quantization baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real transformer layer test for residual projection activation quantization
- Success threshold: Residual projection must reduce actual held-out layer-output relative MSE by at least 10% versus the best same-bit-budget dense/control baseline in two or more layers while not increasing activation reconstruction error by more than 25%.
- Stop condition: Stop if residual projection fails to beat same-budget dense/control baselines on actual layer-output error in the first two evaluated layers, or if real activation traces show no stable low-rank residual subspace.

## Evidence references

- Artifact root: `<local-path>/projects/activation-quantization-with-learned-residual-projection-subspace-b4ac8e8e1baa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
