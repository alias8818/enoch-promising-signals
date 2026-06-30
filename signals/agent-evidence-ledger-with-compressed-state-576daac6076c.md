# Agent Evidence Ledger with Compressed State

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-evidence-ledger-with-compressed-state-576daac6076c`
Run ID: `agent-evidence-ledger-with-compressed-state-576daac6076c-20260609T054402296474+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/df7ee48e93fd

## What looked useful

Compressed summaries alone forgot 39-95% of audit queries across 5k-60k char budgets and had zero revision evidence recall, while ledger_plus_summary achieved 100% latest-value accuracy, 100% evidence accuracy, and 100% revision evidence recall with the same compressed-summary budgets plus explicit ledger storage.

## Boundaries and scale limits

Synthetic traces only; no live LLM agent, no noisy extraction, no approximate retrieval, no adversarial evidence, and an exact external ledger whose storage grew to about 229k chars for 5000 events.

## Claim scope

In a deterministic synthetic state-management benchmark with lossy compressed working summaries, an append-only keyed evidence ledger preserved latest-value answers, latest evidence citations, and immediately prior revision evidence across 20 seeds and four summary budgets.

## Why it stopped

Closed as no-paper useful signal: the mechanism is supported in a synthetic deterministic benchmark, but end-to-end agent evidence is missing.

## Recommended next action

Run a bounded live-agent follow-up with LLM-extracted observations and retrieval-indexed ledger queries under a fixed context budget; do not write a paper from this synthetic-only result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-agent evidence ledger under noisy LLM extraction
- Success threshold: Ledger condition improves citation accuracy and contradiction recall by at least 20 percentage points over the strongest baseline while keeping answer accuracy non-inferior within 5 percentage points and reporting storage/latency overhead.
- Stop condition: Stop if ledger retrieval misses or extraction noise reduce citation accuracy below the strongest baseline, or if overhead exceeds a documented practical budget without accuracy gain.

## Evidence references

- Artifact root: `<local-path>/projects/agent-evidence-ledger-with-compressed-state-576daac6076c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
