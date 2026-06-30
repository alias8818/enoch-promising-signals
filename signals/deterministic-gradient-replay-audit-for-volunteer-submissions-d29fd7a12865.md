# Deterministic Gradient Replay Audit for Volunteer Submissions

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `deterministic-gradient-replay-audit-for-volunteer-submissions-d29fd7a12865`
Run ID: `deterministic-gradient-replay-audit-for-volunteer-submissions-d29fd7a12865-20260620T104431943061+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/addb2b44e416

## What looked useful

Salted challenge-response auditing added detection power beyond passive duplicate hashing: passive duplicate checks detected 25% of attack submissions, while challenge-response checks detected 100% of the synthetic replay/forgery submissions with 0% honest false positives.

## Boundaries and scale limits

Synthetic CPU-only proxy with one task, 200 submissions, 32-dimensional logistic-regression gradients, and no real volunteer submissions, large-model traces, hardware nondeterminism study, privacy-preserving verification, or adaptive adversary that computes the salted challenge.

## Claim scope

In a deterministic synthetic logistic-regression replay benchmark, recomputing salted challenge gradients separates honest submissions from deterministic, cyclic, noisy, and norm-only replay/forgery submissions with 0/40 false positives and 160/160 detected attacks.

## Why it stopped

Proxy-only synthetic evidence supports the mechanism but is not direct/full validation on real volunteer submissions.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same salted audit on a small real framework training trace with signed salts and hardware/float nondeterminism controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real framework salted-gradient replay audit with nondeterminism controls
- Success threshold: At least 95% replay detection with at most 1% honest false positives on the real framework trace, with documented tolerance for hardware floating-point nondeterminism.
- Stop condition: Stop if honest nondeterminism alone exceeds the replay threshold or if replay detection drops below 90% after threshold calibration.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-gradient-replay-audit-for-volunteer-submissions-d29fd7a12865`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
