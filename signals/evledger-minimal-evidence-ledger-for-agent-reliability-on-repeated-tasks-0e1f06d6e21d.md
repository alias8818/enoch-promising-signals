# EvLedger: Minimal Evidence Ledger for Agent Reliability on Repeated Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evledger-minimal-evidence-ledger-for-agent-reliability-on-repeated-tasks-0e1f06d6e21d`
Run ID: `evledger-minimal-evidence-ledger-for-agent-reliability-on-repeated-tasks-0e1f06d6e21d-20260619T211210112448+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e5d886975975

## What looked useful

The ledger gate reduced false accepts on injected drift/trap cases from 32/32 for the naive baseline to 0/32 while preserving 8/8 clean repeats, suggesting the mechanism is worth testing on real repeated agent traces.

## Boundaries and scale limits

Synthetic cases only; no real LLM agent traces, no tool-use execution logs, no paraphrase/semantic verifier, no adversarial prompt variation, and no long-horizon repeated production task data.

## Claim scope

In a deterministic 40-case synthetic repeated-task proxy, a minimal ledger requiring evidence refs, observation hashes, staleness checks, and supported-claim hashes rejected injected drift/trap cases that a naive accept-latest baseline accepted.

## Why it stopped

Proxy mechanism evidence is positive but not direct enough for a paper or broad reliability claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should validate the same ledger gate on real or replayed tool-using agent traces with paraphrased claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay EvLedger on real repeated tool-agent traces with paraphrase drift
- Success threshold: Ledger false accept rate at least 50% lower than baseline with clean-repeat false reject rate at or below 10%.
- Stop condition: Stop if ledger false rejects exceed 25% on clean repeats or if required claim/evidence digests cannot be generated from realistic traces.

## Evidence references

- Artifact root: `<local-path>/projects/evledger-minimal-evidence-ledger-for-agent-reliability-on-repeated-tasks-0e1f06d6e21d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
