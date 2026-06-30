# Rank-1 Second-Moment Factorization for Adam Optimizer Memory Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `rank-1-second-moment-factorization-for-adam-optimizer-memory-reduction-6a0d2a9b6856`
Run ID: `rank-1-second-moment-factorization-for-adam-optimizer-memory-reduction-6a0d2a9b6856-20260526T102640968393+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1a4d425f5a56

## What looked useful

The memory mechanism works but the maximum reduction is roughly half of Adam optimizer state when dense first moments are retained. Update diagnostics show substantial distortion versus Adam, and medium synthetic training showed a roughly 3.06 percentage point mean final-accuracy regression on the rank1_friendly condition.

## Boundaries and scale limits

Evidence is limited to small synthetic MLP runs, 180 optimizer steps, 3 seeds, float32 PyTorch, and one favorable rank-1 reconstruction. It does not validate transformer-scale language modeling, long-horizon training, mixed precision, distributed optimizer sharding, or real memory-pressure behavior.

## Claim scope

On small CUDA MLP synthetic teacher-label tasks, replacing Adam's dense second-moment tensors for 2D parameters with row/column rank-1 EMAs reduces measured optimizer-state memory by about 49.6% while preserving final accuracy on IID and anisotropic tasks but regressing on one controlled rank1_friendly task.

## Why it stopped

Bounded local evidence is mixed: optimizer-state memory reduction is directly supported, but Adam-like behavior is not consistently preserved and the evidence is too synthetic and short-horizon for a paper-positive claim.

## Recommended next action

Stop this worker run as a no-paper useful signal; the next concrete test would be a bounded small decoder-only language-model run comparing validation loss, memory, throughput, and stability against AdamW.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Decoder LM Validation of Rank-1 Second-Moment Adam
- Success threshold: Rank-1 variant reaches validation loss within 2% of AdamW across at least 2 of 3 seeds, reduces optimizer-state memory by at least 45%, and has less than 15% throughput regression.
- Stop condition: Stop if rank-1 validation loss is more than 5% worse than AdamW after the planned budget, diverges in two seeds, or throughput regression exceeds 25% without a compensating memory result.

## Evidence references

- Artifact root: `<local-path>/projects/rank-1-second-moment-factorization-for-adam-optimizer-memory-reduction-6a0d2a9b6856`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
