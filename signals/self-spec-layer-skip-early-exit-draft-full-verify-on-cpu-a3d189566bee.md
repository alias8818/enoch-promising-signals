# Self-Spec Layer Skip: Early-Exit Draft, Full Verify on CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-spec-layer-skip-early-exit-draft-full-verify-on-cpu-a3d189566bee`
Run ID: `self-spec-layer-skip-early-exit-draft-full-verify-on-cpu-a3d189566bee-20260620T023032376944+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/91fd014e8fb9

## What looked useful

Across 100 CPU proxy conditions, no actual drafting condition beat full-only decoding. The best overall 1.000x condition drafted zero tokens; the best actual drafting condition reached 0.994x with only 9 drafted tokens; the best ungated drafting condition reached 0.752x despite 93.2% raw early/full top-1 agreement because contiguous speculative-prefix acceptance was much lower.

## Boundaries and scale limits

Not tested on trained transformer language models, real corpora, KV-cache kernels, production CPU inference stacks, or quality-preserving decoding. The result is an early/proxy falsification of the naive mechanism, not a universal self-speculative decoding result.

## Claim scope

Bounded synthetic CPU proxy for self-speculative layer skipping: early residual-network exits draft greedy token blocks and full-depth logits verify them under a measured NumPy CPU latency model.

## Why it stopped

Bounded CPU proxy found no speedup for actual drafting; the only baseline-matching policy disabled drafting entirely. This is proxy evidence, not full-scale validation.

## Recommended next action

Stop this run as a proxy/early falsification; only revisit with a trained small transformer plus an explicit objective or calibration method that improves contiguous accepted-prefix length.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train shallow exits for contiguous speculative-prefix acceptance
- Success threshold: At least 1.15x wall-clock tokens/s over dense full-only CPU decoding at matched greedy outputs or matched task quality, with gains reproduced across at least two seeds or datasets.
- Stop condition: Stop if trained/calibrated exits fail to reach 1.0x wall-clock speedup or if quality-equivalent acceptance remains too low to offset draft and verification overhead.

## Evidence references

- Artifact root: `<local-path>/projects/self-spec-layer-skip-early-exit-draft-full-verify-on-cpu-a3d189566bee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
