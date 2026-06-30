# Multi-source real transcript evidence-ledger robustness suite

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `multi-source-real-transcript-evidence-ledger-robustness-su-c79dc2d017`
Run ID: `multi-source-real-transcript-evidence-ledger-robustness-su-c79dc2d017-20260619T235502568188+0000`

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

- Parent run decision: Evidence Ledger Format Robustness on CPU Agent Tasks: enoch://control-plane/projects/evidence-ledger-format-robustness-on-cpu-agent-tasks-bffa24a48a89/runs/evidence-ledger-format-robustness-on-cpu-agent-tasks-bffa24a48a89-20260619T231252956198+0000
- Parent run decision: Real Transcript Evidence-Ledger Format Robustness: enoch://control-plane/projects/real-transcript-evidence-ledger-format-robustness-295b5adb96/runs/real-transcript-evidence-ledger-format-robustness-295b5adb96-20260619T232855801719+0000

## What looked useful

Quote anchoring alone had 40% false-positive rate, while removing speaker or claim-source checks each left 20% false-positive rate. The robust turn/source/speaker/quote verifier reached 100% accuracy and 0% false-positive rate on the bounded generated suite.

## Boundaries and scale limits

Claims were templated and corruptions were seeded controls over real transcript turns; open-ended agent-written claims, paraphrases, ambiguous speaker attribution, partial quotes, and multi-evidence synthesis were not validated.

## Claim scope

On a deterministic 360-case suite generated from 4 public real transcript sources, a verifier requiring source, speaker, turn-id, and exact quote consistency eliminated false accepts that remained in schema-only, quote-only, no-speaker, and no-claim-source baselines.

## Why it stopped

No-paper useful signal: the mechanism is supported on real transcript turns with fixed seeds, baselines, and ablations, but the evidence is generated and bounded rather than independent publication-grade validation.

## Recommended next action

Run the same verifier family on independently authored agent or human transcript claims with adjudicated labels before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Independent transcript-claim adjudication for evidence-ledger verifier robustness
- Success threshold: Robust verifier false-positive rate at least 20 percentage points below the strongest baseline while maintaining at least 0.90 recall on supported claims.
- Stop condition: Stop if robust recall falls below 0.80 or false-positive reduction versus the strongest baseline is under 10 percentage points on the adjudicated set.

## Evidence references

- Artifact root: `<local-path>/projects/multi-source-real-transcript-evidence-ledger-robustness-su-c79dc2d017`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
