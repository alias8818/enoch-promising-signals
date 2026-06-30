# Evidence ledger for small CPU agent reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-small-cpu-agent-reliability-d2e6750b2b3a`
Run ID: `evidence-ledger-for-small-cpu-agent-reliability-d2e6750b2b3a-20260608T003135348502+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4dc5f69bcaa8

## What looked useful

Evidence ledgers appear useful as a safety gate for small CPU agents when source records are hashable and derived claims can be mechanically checked. Retries recovered liveness: ledger acceptance rose from 43.38% with no retries to 81.57% with two retries while maintaining 0 accepted wrong completions in the measured runs.

## Boundaries and scale limits

The test used synthetic tasks and a simulated fault model, not a live LLM or real production agent. The ledger auditor has access to source records and stable hashes; results do not prove robustness against adversarial sources, colluding tools, ambiguous natural-language evidence, or larger multi-step agent workflows.

## Claim scope

In a deterministic synthetic CPU-agent record-summarization harness with injected read, arithmetic, citation, and write-receipt faults, a strict evidence ledger with source hashes, citation completeness, derivation checks, and up to two retries reduced accepted wrong completions from 53.0% for an unchecked baseline and 52.48% for transcript-only checking to 0/20000 accepted wrong completions.

## Why it stopped

Synthetic evidence supports the mechanism but is not direct enough for a paper or broad reliability claim.

## Recommended next action

Stop as no-paper useful signal; next concrete step is a bounded direct-agent follow-up using real tool traces rather than this synthetic fault model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence ledger on real small-agent file and calculation tasks
- Success threshold: Ledger-audited accepted wrong rate at least 50% lower than transcript-only with Wilson 95% intervals not overlapping materially, and ledger acceptance rate at least 70%.
- Stop condition: Stop if ledger auditing reduces accepted wrong completions by less than 25%, if acceptance falls below 50%, or if most errors are uncheckable from available evidence.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-cpu-agent-reliability-d2e6750b2b3a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
