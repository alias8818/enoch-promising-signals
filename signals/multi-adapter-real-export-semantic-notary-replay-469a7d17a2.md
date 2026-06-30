# Multi-adapter real-export semantic notary replay

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `multi-adapter-real-export-semantic-notary-replay-469a7d17a2`
Run ID: `multi-adapter-real-export-semantic-notary-replay-469a7d17a2-20260522T035635112742+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Held-out realistic ledger mutation benchmark for semantic notary fingerprints: enoch://control-plane/projects/held-out-realistic-ledger-mutation-benchmark-for-semantic-66ffaff727/runs/held-out-realistic-ledger-mutation-benchmark-for-semantic-66ffaff727-20260522T003742717609+0000
- Parent run decision: Real-export ledger mutation replay for semantic notary fingerprints: enoch://control-plane/projects/real-export-ledger-mutation-replay-for-semantic-notary-fin-e414683962/runs/real-export-ledger-mutation-replay-for-semantic-notary-fin-e414683962-20260522T022446317338+0000

## What looked useful

Semantic notary achieved TP 24, TN 60, FP 0, FN 0 across 84 adapter cases, while byte hash and surface parsed-object baselines false-rejected benign re-encodes and weak ID validation missed all semantic drift controls.

## Boundaries and scale limits

Records were generated fixtures and adapters were implemented inside one benchmark harness; no third-party production exports, independent parser implementations, adversarial parser fuzzing, concurrent service workload, or production key-management path was validated.

## Claim scope

A semantic notary using canonicalized record semantics and an HMAC collection manifest verified replay equivalence across locally generated real-format JSON, CSV, SQLite, and vCard exports with 1.68M replayed records, accepting benign re-encodes and rejecting five injected semantic drift classes.

## Why it stopped

Bounded validation supports the mechanism but the real-export claim is not closed because production export corpora and independently maintained adapters were not tested.

## Recommended next action

Run one bounded deepen study on actual public or consented app exports with independent adapters and withheld corruptions; do not write a paper from the current generated-fixture evidence alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Independent real-export corpus semantic notary replay
- Success threshold: Across at least 300 real-export replay cases, semantic notary has zero critical false accepts, at least 0.95 benign replay acceptance, and at least a 50% reduction in benign false rejects versus byte hashing.
- Stop condition: Stop if independently parsed actual exports cannot be canonicalized without manual semantic labeling for more than one third of systems, or if semantic notary has any critical false accept on withheld corruptions.

## Evidence references

- Artifact root: `<local-path>/projects/multi-adapter-real-export-semantic-notary-replay-469a7d17a2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
