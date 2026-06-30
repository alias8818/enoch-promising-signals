# Real-Agent Strict Evidence Ledger Audit Benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-strict-evidence-ledger-audit-benchmark-e0579a535c`
Run ID: `real-agent-strict-evidence-ledger-audit-benchmark-e0579a535c-20260610T194531942641+0000`

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

- Parent run decision: Evidence Ledger Falsifiability Protocol for Agent Reliability: enoch://control-plane/projects/evidence-ledger-falsifiability-protocol-for-agent-reliability-297fd8b4eb2d/runs/evidence-ledger-falsifiability-protocol-for-agent-reliability-297fd8b4eb2d-20260610T133944366191+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f040bdbdf971

## What looked useful

Strict claim-level evidence checks caught missing citations, absent evidence IDs, metric mismatches, failed-command overclaims, unsupported source references, malformed citations, and partial metric overclaims that the lenient baseline missed.

## Boundaries and scale limits

Cases were deterministic fixtures generated inside this run, not independent live-agent transcripts; evaluation used one small suite and no blinded human adjudication.

## Claim scope

In a controlled 12-case benchmark of agent-style reports with durable local evidence records, a strict evidence-ledger auditor detected unsupported or contradicted claims with F1 1.0 and outperformed a citation-presence baseline by 0.40 F1.

## Why it stopped

Tier 1 controlled direct mechanism test passed, but this is no-paper evidence because the agent reports were controlled fixtures rather than diverse live real-agent outputs.

## Recommended next action

Run a bounded deepen follow-up on live Codex/agent transcripts from small repository tasks and compare strict-auditor labels against blinded human adjudication.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-Agent Evidence Ledger Audit on Small Repository Tasks
- Success threshold: Strict auditor improves unsupported-claim F1 by at least 0.15 over citation-presence baseline and keeps false-positive rate under 10% on at least 20 live-agent transcripts.
- Stop condition: Stop if live transcripts cannot be produced with claim-level evidence ledgers, if human adjudication disagrees below usable reliability, or if strict auditor margin over baseline is below 0.05 after 20 transcripts.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-strict-evidence-ledger-audit-benchmark-e0579a535c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
