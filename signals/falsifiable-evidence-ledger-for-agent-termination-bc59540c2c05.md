# Falsifiable Evidence Ledger for Agent Termination

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `falsifiable-evidence-ledger-for-agent-termination-bc59540c2c05`
Run ID: `falsifiable-evidence-ledger-for-agent-termination-bc59540c2c05-20260602T172039532720+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/77930d8ad634

## What looked useful

A latest-evidence ledger that requires non-stale passing evidence and explicit falsifiers for every required claim eliminated synthetic unsupported terminations across a 5,000-trace main run and four 3,000-trace adversarial-rate sweeps; the closest baseline, latest_pass, still false-terminated at 0.0382 in the main run.

## Boundaries and scale limits

Evidence is synthetic/proxy-only: no live LLM agent runs, no real tool logs, no human-labeled termination benchmark, no cryptographic tamper-resistance test, and no production cost/latency measurement.

## Claim scope

On synthetic multi-claim termination traces with explicit evidence states, a falsifiable evidence ledger policy matched the oracle and prevented unsupported termination cases that affected DONE-flag, checklist-count, and latest-pass baselines.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but is not a full validation of deployed agent termination.

## Recommended next action

Stop this run as no-paper useful signal; next run should replay real or semi-real agent traces with injected missing, stale, contradictory, and non-falsifiable evidence under an independently labeled termination oracle.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Trace Replay for Falsifiable Evidence Ledger Termination
- Success threshold: Falsifiable ledger false termination rate at least 50% lower than latest-pass baseline with false stop rate <= 5% and median decision overhead under 100 ms per termination check on the replay corpus.
- Stop condition: Stop if the ledger fails to reduce false terminations versus latest-pass by at least 20%, or if false stop rate exceeds 10% on independently labeled justified terminations.

## Evidence references

- Artifact root: `<local-path>/projects/falsifiable-evidence-ledger-for-agent-termination-bc59540c2c05`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
