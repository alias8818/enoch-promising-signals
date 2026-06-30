# Natural-Language Local-Agent Evidence Ledger Evaluation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `natural-language-local-agent-evidence-ledger-evaluation-91cb91e78d`
Run ID: `natural-language-local-agent-evidence-ledger-evaluation-91cb91e78d-20260604T082913850197+0000`

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

- Parent run decision: Evidence Ledger for Bounded-Context Local Agents: enoch://control-plane/projects/evidence-ledger-for-bounded-context-local-agents-b7dc402f3430/runs/evidence-ledger-for-bounded-context-local-agents-b7dc402f3430-20260604T054103826787+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae31537fae7b

## What looked useful

Ledger auditing achieved mean unsupported-claim F1 0.9521 versus 0.6070 for transcript-only auditing across six seeds, with minimum F1 improvement 0.3232 and provenance precision 1.0000.

## Boundaries and scale limits

Six 120-case generated runs only; no real agent logs, human-authored ledgers, LLM auditors, adversarial formatting, or long-horizon production traces were tested.

## Claim scope

In a controlled synthetic local-agent trace benchmark with natural-language evidence items, explicit claim-to-evidence ledgers improved unsupported-claim detection over a transcript-only lexical auditor.

## Why it stopped

Controlled Tier 1 mechanism support only; synthetic generated traces are insufficient for publication-grade validation.

## Recommended next action

Run a deepen follow-up on 50-100 real local-agent logs with human-labeled claim support and the same ledger-vs-transcript metric; stop short of paper claims until real-log evidence agrees.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Local-Agent Log Evidence Ledger Audit
- Success threshold: Ledger unsupported-claim F1 >= 0.80, absolute improvement over transcript-only auditing >= 0.15, and provenance precision >= 0.85 on real local-agent logs.
- Stop condition: Stop if fewer than 50 usable real logs can be labeled, if ledger F1 improvement is below 0.15, or if provenance precision falls below 0.85.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-local-agent-evidence-ledger-evaluation-91cb91e78d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
