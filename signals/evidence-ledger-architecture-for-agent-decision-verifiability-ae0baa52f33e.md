# Evidence Ledger Architecture for Agent Decision Verifiability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-architecture-for-agent-decision-verifiability-ae0baa52f33e`
Run ID: `evidence-ledger-architecture-for-agent-decision-verifiability-ae0baa52f33e-20260610T013233094599+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/bc71408406bd

## What looked useful

Unforged ledgers detected 100% of tested tampering cases across both 1,000-episode runs, while plain semantic traces detected about 44-45%. When an attacker could rewrite and rehash the full unanchored ledger, detection fell to about 62-63% and reordered histories were never detected.

## Boundaries and scale limits

Tested only synthetic single-agent threshold-policy episodes: 2,000 total episodes across two seeds, 6 evidence documents per episode, four tamper classes, no real LLM agent, no database, no key management, and no external append-only anchor.

## Claim scope

In a small synthetic deterministic agent-decision trace, a hash-chained evidence ledger with evidence content hashes detects ordinary post-hoc tampering that a plain semantic JSONL trace misses, with about 1.8x serialized size and about 0.022 ms verification time per episode.

## Why it stopped

No-paper closure: the synthetic probe supports the mechanism for ordinary tamper evidence but early-falsifies the stronger architecture claim under full-chain rewrite without an external trust anchor.

## Recommended next action

Run a bounded anchored-ledger follow-up using signed checkpoints or a transparency-log-style external anchor, then repeat the forged-chain rewrite attacks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored Evidence Ledger Forgery Resistance
- Success threshold: Anchored verifier detects at least 99% of forged-chain reorder and deletion attacks while adding less than 5 ms verification overhead per episode at the same synthetic scale.
- Stop condition: Stop if forged-chain reorder attacks still pass after checkpoint verification, or if the design requires trusted local mutable state equivalent to the original unanchored ledger.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-architecture-for-agent-decision-verifiability-ae0baa52f33e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
