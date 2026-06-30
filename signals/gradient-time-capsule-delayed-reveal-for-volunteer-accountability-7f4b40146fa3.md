# Gradient-Time Capsule: Delayed Reveal for Volunteer Accountability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-time-capsule-delayed-reveal-for-volunteer-accountability-7f4b40146fa3`
Run ID: `gradient-time-capsule-delayed-reveal-for-volunteer-accountability-7f4b40146fa3-20260608T163213714501+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/fc88751159c5

## What looked useful

Distance-to-full-gradient detection had 0.0 lazy detection across all lazy fractions while false positives were about 5-8%; replay detection had 1.0 lazy detection for naive copying in both delayed_commit and immediate_public modes. The run weakens the naive delayed-reveal accountability claim but identifies replay/audit design as the key mechanism to test next.

## Boundaries and scale limits

Toy/proxy simulation only: 100 trials per lazy fraction, 4096 samples, 64 dimensions, 32 volunteers, 80 rounds. Does not test real volunteer behavior, adaptive adversaries, cryptographic implementation, Sybil resistance, privacy, non-IID production data, or large-scale federated learning.

## Claim scope

In a synthetic linear-regression volunteer-gradient simulation with naive lazy copying, exact replay-style accountability detects copied aggregate submissions, but generic gradient-distance accountability fails and delayed reveal is not uniquely better than immediate public reveal.

## Why it stopped

Bounded toy/proxy evidence is mixed: delayed reveal catches naive stale replay, but the same replay heuristic catches immediate copying and the generic gradient-distance detector fails completely, so the unique delayed-reveal accountability hypothesis is not supported enough for a paper.

## Recommended next action

Stop this run as no-paper useful signal; next run should test adaptive lazy volunteers that add calibrated noise to evade replay detection while preserving training utility.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Noise Evasion for Gradient-Time Capsule Accountability
- Success threshold: A delayed-reveal-plus-audit variant achieves at least 0.80 lazy detection at no more than 0.05 honest false-positive rate while keeping final loss delta below 1% versus the honest baseline, and immediate_public without the audit fails that threshold.
- Stop condition: Stop if adaptive noise reduces delayed-reveal detection below 0.60 at 5% false-positive rate or if all variants are equivalently detectable, because delayed reveal would not provide a distinct accountability mechanism in this model.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-time-capsule-delayed-reveal-for-volunteer-accountability-7f4b40146fa3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
