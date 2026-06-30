# Proof-of-Work Validation for Volunteer Training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `proof-of-work-validation-for-volunteer-training-78c6641ac977`
Run ID: `proof-of-work-validation-for-volunteer-training-78c6641ac977-20260614T025948447409+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b55635fe84fe

## What looked useful

Skippers who performed zero training passed the PoW gate at essentially the same rate as honest volunteers across modeled difficulties; increasing difficulty only increased common friction rather than adding training-completion evidence.

## Boundaries and scale limits

Evidence is limited to a local SHA-256 PoW implementation, measured CPU throughput, and a deterministic synthetic honest-vs-skipper simulation. It does not include human-subject data, real volunteer devices, or a curriculum-bound PoW design.

## Claim scope

A curriculum-detached, session-bound proof-of-work gate proves compute after a challenge but does not validate volunteer training completion or learning.

## Why it stopped

Proxy/local early falsification: the tested PoW signal is independent of training completion, so it cannot validate volunteers by itself; full validation would require a curriculum-bound design and human/deployment evidence.

## Recommended next action

Stop this line as a validation mechanism unless a new design cryptographically binds work to non-transferable curriculum interactions or assessment evidence.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Curriculum-bound proof-of-engagement challenge for volunteer training
- Success threshold: At least 50% lower skipper false-acceptance than plain session PoW with honest volunteer pass rate at or above 90% and median added friction under 30 seconds in the bounded test.
- Stop condition: Stop if curriculum-bound work can still be solved without observing or answering training content, or if honest pass rate falls below 90% at the difficulty required for the false-acceptance target.

## Evidence references

- Artifact root: `<local-path>/projects/proof-of-work-validation-for-volunteer-training-78c6641ac977`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
