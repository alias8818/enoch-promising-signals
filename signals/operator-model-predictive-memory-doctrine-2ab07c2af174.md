# Operator-Model Predictive Memory Doctrine

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `operator-model-predictive-memory-doctrine-2ab07c2af174`
Run ID: `operator-model-predictive-memory-doctrine-2ab07c2af174-20260613T154631078891+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f0a4cc9efb5b

## What looked useful

Across five seeds, the learned operator beat the best non-oracle in-distribution baseline by a mean +0.0363 retention accuracy, but under OOD shift it lost by a mean -0.1662 and performed worse than random reservoir. Predictive memory admission is plausible under stable distributions but unsafe as a general doctrine without adaptation or fallback.

## Boundaries and scale limits

No real language-model training, no real KV-cache/retrieval integration, no long-context benchmark, and no multi-task robustness. The OOD shift is synthetic but directly shows brittleness under reversed marker correlation and recency-dominant utility.

## Claim scope

Synthetic fixed-slot stream memory only: a 1,377-parameter learned write operator improves delayed-query fact retention over non-oracle baselines when train and test streams share the same local feature-to-query distribution.

## Why it stopped

No-paper useful signal: local synthetic evidence supports a narrow stable-distribution mechanism but falsifies robust generality under a simple proxy distribution shift.

## Recommended next action

Run a bounded deepen test adding shift-aware gating or fallback-to-recency/reservoir, and require it to preserve the ID gain while eliminating the OOD collapse.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Shift-Aware Predictive Memory Admission
- Success threshold: Mean ID learned-or-adaptive margin over best non-oracle baseline >= +0.03 and mean OOD margin >= 0.00 across at least five fixed seeds.
- Stop condition: Stop as negative if the adaptive policy still has negative mean OOD margin or sacrifices the ID margin below +0.01.

## Evidence references

- Artifact root: `<local-path>/projects/operator-model-predictive-memory-doctrine-2ab07c2af174`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
