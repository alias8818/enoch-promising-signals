# Agent Reliability via Compressed State Evidence Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-reliability-via-compressed-state-evidence-ledger-5a70361f2ff8`
Run ID: `agent-reliability-via-compressed-state-evidence-ledger-5a70361f2ff8-20260607T185008380296+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/4965522b9dfe

## What looked useful

Structured evidence ledgers preserve provenance far better than raw recency after hard cutover, but a simple flat compact summary outperformed this ledger format at 400 and 800 tokens. The failure mode is budget-sensitive ledger admission and metadata overhead; at 1200 tokens the ledger reached 0.9923 both-accuracy versus 0.9429 for flat summary.

## Boundaries and scale limits

No real LLM traces, no natural-language compaction, no production agent workflows, and no model-in-the-loop recovery. The main run used 300 synthetic trials, 400-step traces, 60 entities, 120 questions, and token budgets of 400, 800, and 1200.

## Claim scope

Synthetic schema-generated hard-cutover traces with latest-fact questions and exact evidence-id scoring. The evidence ledger beat raw recency at all budgets and beat flat summary only when the ledger mostly fit within the 1200-token budget.

## Why it stopped

Mixed synthetic evidence: the ledger wins against raw recency and wins when it fits, but loses the primary 800-token comparison to a simpler flat summary, so this is not a full validation.

## Recommended next action

Stop this run as no-paper useful signal; test an adaptive ledger eviction policy against flat summary on real or LLM-generated agent traces before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Evidence Ledger Admission for Tight Context Budgets
- Success threshold: At both 400 and 800 token budgets, adaptive ledger both_accuracy exceeds flat_summary by at least 0.05 absolute with overlapping token usage and evidence_accuracy no worse than value_accuracy by more than 0.02.
- Stop condition: Stop if adaptive ledger fails to beat flat_summary at either tight budget after 300 trials, or if the gain comes only from using more tokens than the flat baseline.

## Evidence references

- Artifact root: `<local-path>/projects/agent-reliability-via-compressed-state-evidence-ledger-5a70361f2ff8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
