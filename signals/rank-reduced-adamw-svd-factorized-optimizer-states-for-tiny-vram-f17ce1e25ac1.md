# Rank-Reduced AdamW: SVD Factorized Optimizer States for Tiny VRAM

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `rank-reduced-adamw-svd-factorized-optimizer-states-for-tiny-vram-f17ce1e25ac1`
Run ID: `rank-reduced-adamw-svd-factorized-optimizer-states-for-tiny-vram-f17ce1e25ac1-20260620T210510215544+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/57393c8e9a2b

## What looked useful

Direct SVD-factorized AdamW states saved memory at low rank but produced poor update agreement, second-moment instability, early divergence on regression, and roughly 2-3% of dense AdamW throughput in the bounded training probe.

## Boundaries and scale limits

No LLM-scale or GPT-2-small-class training was run. The implementation is an optimistic proxy that materializes dense candidate states before SVD compression; a true tiny-VRAM implementation would have a harder systems problem.

## Claim scope

Bounded proxy tests of direct truncated-SVD factorization of both AdamW first- and second-moment states on synthetic 512x512 moment tracking and a 256x256 single-matrix regression task.

## Why it stopped

Bounded proxy/early falsification: the optimistic direct SVD-state AdamW variant diverged within 6-9 regression steps and did not preserve AdamW update geometry even when memory savings were substantial.

## Recommended next action

Stop this direct both-states SVD path; if continuing locally, test a hybrid that avoids SVD on the second moment, such as low-rank first moment plus block/scalar nonnegative second-moment statistics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid low-rank first moment with nonnegative block second moment
- Success threshold: No divergence in the bounded regression task, final loss within 2x dense AdamW, update cosine above 0.9 on low-rank/drifting-low-rank moment tracking, at least 40% optimizer-state memory reduction, and at least 25% of dense AdamW step throughput.
- Stop condition: Stop if the hybrid diverges on the bounded regression task, update cosine remains below 0.8 at memory-saving ranks, or throughput remains below 10% of dense AdamW.

## Evidence references

- Artifact root: `<local-path>/projects/rank-reduced-adamw-svd-factorized-optimizer-states-for-tiny-vram-f17ce1e25ac1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
