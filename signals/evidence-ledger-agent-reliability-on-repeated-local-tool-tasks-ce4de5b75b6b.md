# Evidence-Ledger Agent Reliability on Repeated Local Tool Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-agent-reliability-on-repeated-local-tool-tasks-ce4de5b75b6b`
Run ID: `evidence-ledger-agent-reliability-on-repeated-local-tool-tasks-ce4de5b75b6b-20260619T110752018009+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cfd9f4a57e07

## What looked useful

Across 9000 labeled claims and 1500 evidence entries, the verifier produced 0 false accepts and 0 false rejects for valid, wrong-value, missing-ref, stale-ref, no-evidence, and wrong-kind claim patterns.

## Boundaries and scale limits

Proxy-only local CPU experiment; no live LLM/tool agent, no no-ledger baseline, no natural-language evidence extraction, and no long-horizon or external-tool workload was tested.

## Claim scope

A deterministic evidence-ledger verifier accepted all supported claims and rejected injected unsupported claims across 500 repeated local file/tool trials using wc, sha256sum, and JSON key-count evidence.

## Why it stopped

Closed as proxy-only mechanism evidence, not full validation of repeated local tool agent reliability.

## Recommended next action

Run a bounded live-agent comparison on the same repeated local task suite with and without mandatory ledger citations, then score agent-produced ledgers with the verifier.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-agent evidence-ledger reliability on repeated local tool tasks
- Success threshold: Ledger condition reduces false accepts by at least 50% versus no-ledger baseline without increasing false rejects by more than 10 percentage points on at least 200 live-agent claims.
- Stop condition: Stop if the live agent cannot produce parseable ledgers after a documented prompt repair, or if fewer than 200 scored claims can be collected within the bounded local budget.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-reliability-on-repeated-local-tool-tasks-ce4de5b75b6b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
