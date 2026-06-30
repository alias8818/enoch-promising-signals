# Public-Quiz Benchmark Gating for CPU Sparse Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `public-quiz-benchmark-gating-for-cpu-sparse-volunteer-training-15ff0dd421ed`
Run ID: `public-quiz-benchmark-gating-for-cpu-sparse-volunteer-training-15ff0dd421ed-20260613T031302196624+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/908164cba090

## What looked useful

Public quiz gating improved over no gating but accepted 100% of public-overfit sparse updates and had worse test loss than hidden/oracle gating. Public-only gates should be treated as gameable unless paired with private or rotating holdouts.

## Boundaries and scale limits

Synthetic 10-seed NumPy simulation only; no real volunteer network, no language model, no real public quiz corpus, and no large-scale sparse training.

## Claim scope

In a deterministic CPU proxy for sparse volunteer logistic-regression training, a fixed public quiz was not sufficient as the only update gate under public benchmark leakage; a hidden holdout gate rejected the public-overfit attack.

## Why it stopped

Proxy evidence is enough to falsify the strong public-quiz-only gate sufficiency claim, but not enough for publication-grade claims about real volunteer sparse training.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should replace the logistic proxy with a small real sparse model/task and a rotating hidden holdout.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Rotating Holdout Gate on a Small Real Sparse Training Task
- Success threshold: Rotating hidden gate rejects at least 90% of benchmark-aware harmful updates while retaining at least 80% of the honest-only oracle's held-out improvement and outperforming fixed public gating on hidden loss.
- Stop condition: Stop if fixed public gating and rotating hidden gating have indistinguishable hidden metrics across seeds or if the real task cannot reproduce public-overfit admission.

## Evidence references

- Artifact root: `<local-path>/projects/public-quiz-benchmark-gating-for-cpu-sparse-volunteer-training-15ff0dd421ed`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
