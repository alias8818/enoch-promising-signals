# Multi-run independent replay validation for anchored evidence ledgers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `multi-run-independent-replay-validation-for-anchored-evide-ca7c909dd0`
Run ID: `multi-run-independent-replay-validation-for-anchored-evide-ca7c909dd0-20260527T025954046939+0000`

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

- Parent run decision: Real-log replay for anchored structured evidence ledgers: enoch://control-plane/projects/real-log-replay-for-anchored-structured-evidence-ledgers-007c5da79c/runs/real-log-replay-for-anchored-structured-evidence-ledgers-007c5da79c-20260526T202601175686+0000
- Parent run decision: Falsifiable Evidence Ledger via Structured Log Provenance: enoch://control-plane/projects/falsifiable-evidence-ledger-via-structured-log-provenance-8e7b5d1f7865/runs/falsifiable-evidence-ledger-via-structured-log-provenance-8e7b5d1f7865-20260525T072140990464+0000

## What looked useful

External anchoring, not local hash manifests, is the key integrity boundary. A forced final anchor or known latest checkpoint is required; periodic anchors without a final/latest check miss tail edits. Periodic anchoring did not beat a terminal external anchor for whole-ledger tamper detection in this bounded test.

## Boundaries and scale limits

Synthetic ledgers only; no production transparency log; no real CI/research-agent traces; one verifier implementation; no online partial-replay or localization benchmark.

## Claim scope

In a deterministic synthetic multi-run replay protocol with attacker-rewritable local metadata, independent external anchors detected all tested rehashed ledger tampering while chain-only and local-manifest baselines did not; terminal external anchoring matched periodic anchoring for whole-ledger integrity.

## Why it stopped

Tier 2 fixed-seed validation produced useful mechanism evidence but not paper-positive novelty because the real terminal-anchor baseline matched periodic anchoring on whole-ledger integrity.

## Recommended next action

Run a bounded deepen test on real agent/CI evidence traces with a real transparency-log-style anchor backend and compare terminal-only versus periodic anchors on partial replay and fault localization.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace partial replay and localization benchmark for periodic evidence anchors
- Success threshold: Periodic anchoring must match terminal anchoring at >=99.9% whole-ledger tamper detection and 0 benign false rejects, while reducing median partial-replay or localization work by at least 3x on real traces.
- Stop condition: Stop if terminal anchoring again matches periodic anchoring on all direct metrics or if real traces cannot be obtained/emulated without changing the threat model.

## Evidence references

- Artifact root: `<local-path>/projects/multi-run-independent-replay-validation-for-anchored-evide-ca7c909dd0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
