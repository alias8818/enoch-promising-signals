# Evidence-Ledger Agent Reliability Framework

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-reliability-framework-78b6379aa010`
Run ID: `evidence-ledger-agent-reliability-framework-78b6379aa010-20260607T225428365244+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fec5ab3734c4

## What looked useful

The ledger gate reduced unsupported answer rate from 25.0% to 0.0% and conflict violation rate from 25.0% to 0.0%, with answer rate falling from 100.0% to 50.0% because the ledger abstained on missing and conflicting evidence.

## Boundaries and scale limits

Synthetic-only, 4,800 generated tasks, no LLM generation, no real tool-use traces, no human grading, exact fact parser, and microbenchmark latency only. This does not validate production agent reliability or publication-grade generality.

## Claim scope

In a deterministic synthetic evidence-use benchmark with atomic extractable facts, a claim-source evidence ledger with abstention gating eliminated unsupported answers and conflict-violating answers relative to a direct retrieval baseline, while preserving correctness on supported tasks.

## Why it stopped

No-paper useful signal: the result supports the mechanism only in a synthetic proxy benchmark, not a full validation of agent reliability.

## Recommended next action

Run a bounded deepen follow-up wrapping the same ledger policy around a small real LLM/tool-use trace benchmark with a strong verifier baseline and support grading.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger gating on real LLM tool-use traces
- Success threshold: Ledger gating achieves at least 30% relative unsupported-claim reduction versus direct answering and at least 10% versus stateless verification, with answered-task accuracy not lower than the strongest baseline and abstention below 40% on answerable cases.
- Stop condition: Stop if ledger gating fails to beat the stateless verifier on unsupported-claim rate, or if abstention exceeds 40% on answerable cases without a compensating accuracy gain.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-reliability-framework-78b6379aa010`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
