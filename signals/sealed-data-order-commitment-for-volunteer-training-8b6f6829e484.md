# Sealed Data-Order Commitment for Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sealed-data-order-commitment-for-volunteer-training-8b6f6829e484`
Run ID: `sealed-data-order-commitment-for-volunteer-training-8b6f6829e484-20260613T081701720217+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5d4162bfe9c9

## What looked useful

Sealed random commitment reduced mean early-window bias from 20.46 percentage points under unsealed cherry-picking to 0.02 percentage points and detected all tested tampering attacks; a naive stratified variant improved bias but had worse group exposure deviation than sealed random.

## Boundaries and scale limits

Synthetic mechanism probe only: 200 trials, 240 tasks per trial, no real volunteers, no secure external timestamp service, no real task identifiers, no human learning or retention measurement, and no full model training.

## Claim scope

In a deterministic synthetic volunteer-task stream, publishing a sealed precommitment to task order before outcome-relevant information is used detects tested swap/delete/duplicate tampering and removes early-window score inflation from post-hoc easy-first ordering.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a synthetic protocol/mechanism probe rather than direct volunteer-training validation.

## Recommended next action

Run a small prospective volunteer or human-in-the-loop replay study with timestamped order roots, opaque task IDs, audited metadata balance, and held-out outcome metrics before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prospective timestamped sealed-order volunteer-training pilot
- Success threshold: Compared with the unsealed/control condition, early-window score inflation is reduced by at least 75%, final held-out outcome is not worse by more than 2 percentage points, and all attempted or injected order mutations are detected.
- Stop condition: Stop if timestamped commitments cannot be recorded before reveal, opaque task IDs cannot be enforced, or the pilot shows more than 5 percentage points final held-out outcome degradation versus control.

## Evidence references

- Artifact root: `<local-path>/projects/sealed-data-order-commitment-for-volunteer-training-8b6f6829e484`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
