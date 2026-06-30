# Structured evidence ledger for tiny agent tool reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `structured-evidence-ledger-for-tiny-agent-tool-reliability-0a00fd61f864`
Run ID: `structured-evidence-ledger-for-tiny-agent-tool-reliability-0a00fd61f864-20260530T034943513104+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ba852333a41c

## What looked useful

Wrong accepted rate fell from 11.675% single-call and 8.210% same-tool majority to 0.350% with the ledger in the main condition; under correlated session faults it fell from 15.250% and 22.275% to 0.530%. The cost was 21.5-27.9% abstention and lower all-trial accuracy.

## Boundaries and scale limits

Synthetic tasks only; no real LLM agent, real external tool API, real user workflow, or production trace validation. Runs used 40,000 trials per policy per condition and completed on one CPU process.

## Claim scope

In a deterministic synthetic tiny-agent benchmark with noisy tools, a structured evidence ledger requiring independent agreement and contradiction-aware finalization reduced wrong accepted answers versus single-call and same-tool majority baselines.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but is not direct production-agent validation or paper-ready evidence.

## Recommended next action

Run a bounded real-agent follow-up with a small local model or recorded tiny-agent traces, using the same wrong-accepted-answer metric and explicit abstention accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real tiny-agent trace validation of structured evidence ledgers
- Success threshold: Ledger policy achieves at least 50% relative reduction in wrong accepted answers versus the strongest non-ledger baseline, with abstention rate below 35% and no more than 20% relative increase in mean tool calls.
- Stop condition: Stop as unsupported if wrong accepted answer reduction is below 25%, abstention exceeds 50%, or ledger failures are dominated by model inability to maintain the schema.

## Evidence references

- Artifact root: `<local-path>/projects/structured-evidence-ledger-for-tiny-agent-tool-reliability-0a00fd61f864`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
