# Replay EvLedger on real repeated tool-agent traces with paraphrase drift

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `replay-evledger-on-real-repeated-tool-agent-traces-with-pa-1d10529862`
Run ID: `replay-evledger-on-real-repeated-tool-agent-traces-with-pa-1d10529862-20260619T214300934539+0000`

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

- Parent run decision: EvLedger: Minimal Evidence Ledger for Agent Reliability on Repeated Tasks: enoch://control-plane/projects/evledger-minimal-evidence-ledger-for-agent-reliability-on-repeated-tasks-0e1f06d6e21d/runs/evledger-minimal-evidence-ledger-for-agent-reliability-on-repeated-tasks-0e1f06d6e21d-20260619T211210112448+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e5d886975975

## What looked useful

EvLedger reached 5/5 top-1 retrieval accuracy versus 2/5 for the best non-EvLedger baseline on the same small real trace replay, suggesting normalized event memory can help with paraphrase drift.

## Boundaries and scale limits

Single worker trace, five hand-scoped sanitized probes, deterministic canonical terms, no independent held-out multi-session corpus, no autonomous extraction-quality test, and no confidence intervals.

## Claim scope

On one local sanitized real Codex command-execution trace slice with 12 pre-evaluator events and 5 deterministic paraphrase-drift probes, an EvLedger-style normalized event ledger retrieved the correct prior event for all probes and exceeded raw transcript/flat retrieval baselines.

## Why it stopped

Tier 1 controlled small direct test completed; evidence supports the mechanism locally but is too small and too scaffolded for publication readiness.

## Recommended next action

Stop this run as no-paper useful signal; next run should evaluate the same script on at least 50 independent real repeated tool-agent sessions with held-out paraphrase probes and an autonomous canonical-term extractor.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out multi-session EvLedger paraphrase replay
- Success threshold: EvLedger improves top-1 retrieval accuracy by at least 10 percentage points over the best baseline with a bootstrap 95% confidence interval excluding zero, and does not regress exact-reference retrieval by more than 2 percentage points.
- Stop condition: Stop as unsupported if EvLedger's improvement over the best baseline is below 5 percentage points or if autonomous extraction errors account for more than 25% of misses.

## Evidence references

- Artifact root: `<local-path>/projects/replay-evledger-on-real-repeated-tool-agent-traces-with-pa-1d10529862`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
