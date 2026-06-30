# Real Local-Agent Log Evidence Ledger Audit

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-local-agent-log-evidence-ledger-audit-39d1eb59c7`
Run ID: `real-local-agent-log-evidence-ledger-audit-39d1eb59c7-20260604T130101530993+0000`

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

- Parent run decision: Natural-Language Local-Agent Evidence Ledger Evaluation: enoch://control-plane/projects/natural-language-local-agent-evidence-ledger-evaluation-91cb91e78d/runs/natural-language-local-agent-evidence-ledger-evaluation-91cb91e78d-20260604T082913850197+0000
- Parent run decision: Evidence Ledger for Bounded-Context Local Agents: enoch://control-plane/projects/evidence-ledger-for-bounded-context-local-agents-b7dc402f3430/runs/evidence-ledger-for-bounded-context-local-agents-b7dc402f3430-20260604T054103826787+0000

## What looked useful

Digest-backed evidence records materially improve tamper localization over parser/schema-only checks for content edits and required-key deletions. The hash-chain component was not supported by this corruption family because the no-chain ablation matched the full method.

## Boundaries and scale limits

Single local log, synthetic corruptions on real events, no multi-agent corpus, no adversarial canonicalization attack, no direct sequence deletion/reorder benchmark, and no external/private production audit trail.

## Claim scope

On one real local Codex agent JSONL log with 48 events and fixed-seed labeled content/schema corruptions, per-event SHA-256 digests localized edited events with perfect precision and recall, outperforming a parser/schema/timestamp baseline.

## Why it stopped

Tier 2 local evidence supports digest-based tamper localization but not the broader ledger/chain audit claim or publication readiness.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up that directly tests sequence deletion/reorder and append-only ledger-tip verification across multiple real local-agent logs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sequence-Tamper Evidence Ledger Audit on Multi-Log Local Agent Traces
- Success threshold: Full ledger must improve sequence-tamper detection F1 by at least 0.25 over digest-only and parser/schema baselines while preserving at least 0.95 precision across fixed seeds.
- Stop condition: Stop if digest-only matches full-ledger sequence detection within 0.05 F1 or full-ledger precision falls below 0.90 on any fixed seed.

## Evidence references

- Artifact root: `<local-path>/projects/real-local-agent-log-evidence-ledger-audit-39d1eb59c7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
