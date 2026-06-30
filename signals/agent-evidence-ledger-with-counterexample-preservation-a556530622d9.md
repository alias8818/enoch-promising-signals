# Agent Evidence Ledger with Counterexample Preservation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-evidence-ledger-with-counterexample-preservation-a556530622d9`
Run ID: `agent-evidence-ledger-with-counterexample-preservation-a556530622d9-20260609T145825244524+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7d6a4a111bc8

## What looked useful

Counterexample preservation retained 76.6% of injected counterexamples in the main run versus 0.0% for compressed summary and 6.35% for recency, and reduced final error to 0.3632 versus 0.4194 and 0.4394. A budget sweep showed the benefit is conditional: the ledger lost to compressed summary at very tight memory and tied recency at larger memory.

## Boundaries and scale limits

No real LLM agents, real tool-use traces, human-authored evidence, production retrieval, or external grading were tested. Runs were CPU-only synthetic simulations under 10 seconds, with 40-80 seeds depending on condition.

## Claim scope

In a deterministic synthetic bounded-memory evidence-stream benchmark with misleading early consensus and rare high-reliability corrections, explicit counterexample preservation increased counterexample retention and improved final belief error at mid memory budgets, but not at all tested budgets.

## Why it stopped

No-paper closure: evidence is synthetic and mixed across memory budgets, so it is useful for mechanism selection but not direct publication-grade validation.

## Recommended next action

Run a bounded real-agent trace benchmark with externally graded claims to test whether preserved counterexamples improve later answer correction under fixed context/token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent counterexample ledger trace benchmark
- Success threshold: Ledger improves correction-after-counterexample rate by at least 5 percentage points over both baselines without reducing final answer accuracy by more than 1 percentage point or increasing token cost by more than 15%.
- Stop condition: Stop if the ledger fails to improve correction-after-counterexample rate over either baseline in two independently seeded task batches, or if token/context overhead exceeds 25%.

## Evidence references

- Artifact root: `<local-path>/projects/agent-evidence-ledger-with-counterexample-preservation-a556530622d9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
