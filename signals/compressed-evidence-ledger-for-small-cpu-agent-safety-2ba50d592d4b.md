# Compressed Evidence Ledger for Small CPU Agent Safety

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `compressed-evidence-ledger-for-small-cpu-agent-safety-2ba50d592d4b`
Run ID: `compressed-evidence-ledger-for-small-cpu-agent-safety-2ba50d592d4b-20260607T223002730597+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/fd8255f1ed89

## What looked useful

Across 1,000 traces x 160 events, the ledger reached 1.000 safety recall and 0.000 false-allow rate at 320 bytes, while recency remained at 0.000 recall and generic summary remained at 0.333 recall. A 500-trace x 320-event stress check reproduced the same curve.

## Boundaries and scale limits

Synthetic retention-only benchmark; no real LLM extraction, adversarial prompt injection, real tool-call enforcement, persistent multi-session state, or deployed CPU-agent workload was tested.

## Claim scope

In deterministic synthetic traces where safety evidence is planted early and later distractor events exceed a small memory budget, a safety-keyed compressed evidence ledger preserves safety facts better than recency memory and a non-safety-aware bounded summary baseline.

## Why it stopped

Synthetic/proxy benchmark supports the retention mechanism but is not direct validation of small CPU agent safety.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next bounded test should add a real small LLM extractor and adversarial ledger-poisoning traces before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-extracted evidence ledger under adversarial trace noise
- Success threshold: At 320-640 bytes, ledger false-allow rate is at least 50% lower than the best baseline with extraction precision at or above 0.90 and p95 per-event update latency below 10 ms on the CPU worker.
- Stop condition: Stop if extraction precision falls below 0.80, ledger false-allow rate is not lower than the best baseline, or p95 update latency exceeds 25 ms at the tested budget.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-evidence-ledger-for-small-cpu-agent-safety-2ba50d592d4b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
