# Hash-Chain Evidence Ledger for Agent Decision Replay Integrity

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hash-chain-evidence-ledger-for-agent-decision-replay-integrity-146232d734ad`
Run ID: `hash-chain-evidence-ledger-for-agent-decision-replay-integrity-146232d734ad-20260601T053711995256+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/017d756bc23d

## What looked useful

Anchored hash-chain evidence ledgers are a viable integrity mechanism for replayable decision traces under the tested faults, with median build throughput of 48,701.66 events/s, median verify throughput of 73,727.04 events/s, and 1.4388x median storage overhead versus plain JSONL. A hash chain alone is insufficient against suffix rewrite when anchors are not retained outside the rewritten ledger.

## Boundaries and scale limits

Synthetic deterministic policy and synthetic evidence only; no real LLM agent traces, tool artifacts, external evidence store, append-only infrastructure, key management, crash recovery, concurrent writers, or external timestamp/transparency anchor were tested.

## Claim scope

In a deterministic synthetic agent replay benchmark of 100,000 events across 5 repeats, a canonical hash-chain evidence ledger with saved anchors detected evidence mutation, decision mutation, entry deletion, entry reorder, and recomputed suffix rewrite attempts at the next saved anchor; the same hash chain without saved anchors did not detect a recomputed suffix rewrite.

## Why it stopped

No-paper closure: local synthetic evidence supports the mechanism but also shows the unanchored suffix-rewrite limitation, and real-agent/direct anchoring evidence is required before a publication-grade claim.

## Recommended next action

Run a bounded deepen test on real agent traces with externally persisted anchors and injected tamper cases; stop treating the synthetic result as paper-ready until real trace replay and anchoring behavior are measured.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored Hash-Chain Ledger on Real Agent Tool Traces
- Success threshold: All anchored tamper classes are rejected, unanchored suffix rewrite remains explicitly identified as out of scope, replay verification succeeds after restart, storage overhead is below 2x, and trace-capture wall-clock overhead is below 10%.
- Stop condition: Stop if real trace replay cannot be made deterministic enough to distinguish ledger failure from nondeterministic agent behavior, or if anchored capture overhead exceeds 2x storage or 25% wall-clock on the bounded trace set.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chain-evidence-ledger-for-agent-decision-replay-integrity-146232d734ad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
