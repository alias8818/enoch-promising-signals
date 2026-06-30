# Evidence-Ledger Rollback for Tiny Tool-Use Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-rollback-for-tiny-tool-use-agents-b710d357ba05`
Run ID: `evidence-ledger-rollback-for-tiny-tool-use-agents-b710d357ba05-20260525T083241001331+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8a852442b9b4

## What looked useful

Across three 10,000-episode settings, ledger rollback had zero accuracy gap versus full recompute, improved accuracy over patch-only/no-rollback by 0.1577 to 0.4036, saved 30.3% to 44.1% of recomputations versus full recompute, and eliminated stale cached-answer failures seen in the patch-only control.

## Boundaries and scale limits

Tested only on rule-based synthetic integer-fact tasks: one cached derived answer, 10 facts, arity 4, 30,000 total medium-run episodes across three noise/audit settings. No real LLM, real tool API, long-context scratchpad, adversarial tool output, or multi-branch agent trace was evaluated.

## Claim scope

In a deterministic synthetic tiny-agent harness with noisy fact lookups and later audited corrections, dependency-aware evidence-ledger rollback matched full-recompute final-answer accuracy while avoiding recomputation for irrelevant corrected evidence.

## Why it stopped

No-paper closure: bounded synthetic mechanism evidence is useful but not a full validation of tiny LLM tool-use agents.

## Recommended next action

Run a bounded deepen experiment on actual small local-model or replayed ReAct-style tool traces with injected tool corrections, comparing append-only scratchpad, full recompute, and evidence-ledger rollback on identical tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger rollback on real tiny tool-use traces
- Success threshold: Ledger rollback matches full-recompute accuracy within 1 percentage point, reduces stale-answer rate by at least 50% versus append-only/no-rollback, and saves at least 20% recomputations versus full recompute on 200 or more real/replayed traces.
- Stop condition: Stop if rollback fails to improve stale-answer rate by at least 10 percentage points over append-only/no-rollback or if trace instrumentation cannot reliably identify evidence dependencies.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-for-tiny-tool-use-agents-b710d357ba05`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
