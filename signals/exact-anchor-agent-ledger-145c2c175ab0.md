# Exact Anchor Agent Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-agent-ledger-145c2c175ab0`
Run ID: `exact-anchor-agent-ledger-145c2c175ab0-20260604T195815541691+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e92de2eb0aa4

## What looked useful

Exact anchor ledgers gave the best bounded verifier result: accuracy 0.8571 and false accept rate 0.1667 versus 0.5714/0.5000 for span-without-revision, 0.4286/0.6667 for quote-substring, and 0.2857/0.8333 for revision-only. The remaining exact-ledger false accepts came from repeated identical text where the claim depended on occurrence identity.

## Boundaries and scale limits

The run used synthetic traces only: 1,000 generated documents and 14,000 generated ledger entries. It did not test deployed agents, human citation behavior, natural-language entailment, large mutable corpora, or long-running production ledgers.

## Claim scope

On deterministic synthetic agent-ledger traces, exact byte offsets plus document revision hashes and ledger-entry hashes reduce false accepts for wrong offsets, stale revisions, edited quotes, hallucinated quotes, and tampered ledger entries compared with substring, span-only, and revision-only checks.

## Why it stopped

No-paper useful signal: synthetic bounded evidence supports the mechanism as a guardrail but also shows byte-exact anchoring alone is insufficient for repeated-text occurrence semantics.

## Recommended next action

Run a bounded real-trace replay with occurrence or retrieval-event ids added to the ledger, then compare against this exact-byte baseline on observed agent citation failures.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Occurrence-aware exact anchor ledger replay on real agent traces
- Success threshold: On at least 1,000 real or recorded agent claims, occurrence-aware exact anchors should reduce repeated-text false accepts to zero while keeping total false accept rate below 5% and p95 verification latency below 1 ms per entry.
- Stop condition: Stop if occurrence-aware anchors still accept repeated-text wrong-occurrence cases or if real traces do not contain enough anchor/citation failures to measure the mechanism.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-agent-ledger-145c2c175ab0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
