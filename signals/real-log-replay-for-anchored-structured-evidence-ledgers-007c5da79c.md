# Real-log replay for anchored structured evidence ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-log-replay-for-anchored-structured-evidence-ledgers-007c5da79c`
Run ID: `real-log-replay-for-anchored-structured-evidence-ledgers-007c5da79c-20260526T202601175686+0000`

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

- Parent run decision: Falsifiable Evidence Ledger via Structured Log Provenance: enoch://control-plane/projects/falsifiable-evidence-ledger-via-structured-log-provenance-8e7b5d1f7865/runs/falsifiable-evidence-ledger-via-structured-log-provenance-8e7b5d1f7865-20260525T072140990464+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/111b44975757

## What looked useful

Real local logs can be replayed through an anchored structured evidence ledger with deterministic clean verification and detection of payload edit, event deletion, adjacent reorder, tail truncation, and anchor flip controls.

## Boundaries and scale limits

Single project, four local log files, 68,369 input bytes, 28 events, one implementation, no external timestamp service, no concurrent append stress, no independent verifier, and no production-scale adversarial model.

## Claim scope

Tier 1 local direct test: 28 real Enoch/Codex log events from this project were normalized into structured records, anchored in a SHA-256 hash-chain ledger, and replay-verified with 5/5 deterministic mutation controls detected.

## Why it stopped

Closed as no-paper useful signal: the direct small replay supports the mechanism, but the corpus and implementation diversity are too limited for publication-grade evidence.

## Recommended next action

Run a bounded deepen validation over at least 20 independent real Enoch runs with an independently written verifier, append-only persistence checks, and external timestamp anchors before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-run independent replay validation for anchored evidence ledgers
- Success threshold: Clean replay succeeds on every unmodified corpus; independent verifier reproduces 100% of ledger roots; all injected mutation classes are detected with zero false clean replays; throughput remains above 50,000 events/s on commodity CPU for corpora up to 100,000 events.
- Stop condition: Stop if any unmodified corpus cannot be replayed deterministically, if the independent verifier disagrees on a ledger root without an implementation bug fix, or if any mutation class yields a false clean replay.

## Evidence references

- Artifact root: `<local-path>/projects/real-log-replay-for-anchored-structured-evidence-ledgers-007c5da79c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
