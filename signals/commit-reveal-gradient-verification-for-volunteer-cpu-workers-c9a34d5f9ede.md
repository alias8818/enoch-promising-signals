# Commit-Reveal Gradient Verification for Volunteer CPU Workers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `commit-reveal-gradient-verification-for-volunteer-cpu-workers-c9a34d5f9ede`
Run ID: `commit-reveal-gradient-verification-for-volunteer-cpu-workers-c9a34d5f9ede-20260628T233344862110+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4b5657fb2df5

## What looked useful

Known-audit spot checks detected 0% of adaptive malicious submissions, while commit-reveal spot checks detected 65.87% at 32/512 audited coordinates and 16/512 corrupted coordinates, close to the 64.96% theoretical blind-sampling rate. A sweep from 8 to 128 audited coordinates was monotonic and theory-aligned.

## Boundaries and scale limits

No real volunteer workers, neural-network training loop, distributed scheduling, network overhead, Sybil/collusion behavior, delayed reveal handling, incentive design, or convergence impact was tested.

## Claim scope

In a local synthetic 512-dimensional linear-gradient simulation, commit-before-audit prevents adaptive known-audit coordinate evasion and makes spot-check detection match blind random sampling probabilities for fixed-coordinate corruptions.

## Why it stopped

No-paper useful signal: the mechanism is supported locally, but the evidence is synthetic/proxy and not sufficient for a paper or deployment claim.

## Recommended next action

Run a bounded deepen test on a small neural-network training loop with realistic gradient tensors, measuring detection, accepted-corruption impact on convergence, bandwidth, and verifier CPU overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural-gradient commit-reveal verification with convergence impact
- Success threshold: Commit-reveal spot checking should match blind-sampling detection within 5 percentage points, keep honest false rejects below 1%, and show materially lower convergence degradation than known-audit checking at the same audit budget.
- Stop condition: Stop if commit-reveal detection deviates from blind-sampling theory by more than 10 percentage points without an explained implementation cause, false rejects exceed 1%, or accepted corruptions cause convergence collapse at audit budgets below 25%.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-gradient-verification-for-volunteer-cpu-workers-c9a34d5f9ede`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
