# Trace-based counter-example ledger validation for LLM tool retries

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `trace-based-counter-example-ledger-validation-for-llm-tool-95c1f788de`
Run ID: `trace-based-counter-example-ledger-validation-for-llm-tool-95c1f788de-20260612T211432090781+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-agent counter-example ledger on repeated tool-use failures: enoch://control-plane/projects/real-agent-counter-example-ledger-on-repeated-tool-use-fai-796c9749e3/runs/real-agent-counter-example-ledger-on-repeated-tool-use-fai-796c9749e3-20260611T204151375882+0000
- Parent run decision: Automatic counter-example ledger on randomized retry/fallback tool tasks: enoch://control-plane/projects/automatic-counter-example-ledger-on-randomized-retry-fallb-c25b9c88c7/runs/automatic-counter-example-ledger-on-randomized-retry-fallb-c25b9c88c7-20260611T213845263711+0000

## What looked useful

Counterexample ledger achieved 0.991963 mean solve rate versus 0.735676 for error_hint_repair, reduced invalid retries per episode from 1.952031 to 0.804347, and eliminated repeated static invalid retries in the simulator. The no-block ablation slightly outsolved the full blocking ledger, indicating transient-state blocking needs care.

## Boundaries and scale limits

Synthetic replay only: 16 fixed seeds, 200000 episodes per seed, five retry strategies, max three retries. No live LLM generation, no production trace corpus, and no human/operator trace data were used.

## Claim scope

In deterministic generated tool-retry replay traces across five failure families, a trace-based counter-example ledger improves solve rate and reduces invalid retry waste versus an error-hint-only retry baseline.

## Why it stopped

No-paper useful signal: direct retry metrics support the mechanism in synthetic replay, but evidence remains proxy-only for real LLM/tool deployments.

## Recommended next action

Run a bounded real-trace replay on held-out LLM tool-call logs with transient-state annotations before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace replay validation for counter-example ledger tool retries
- Success threshold: At least 30% lower invalid repeated retries than error_hint_repair, solve rate no more than 2 percentage points below the best non-oracle baseline, and no transient-state false-blocking cluster above 5% of transient cases.
- Stop condition: Stop as negative if the ledger fails to reduce invalid repeated retries by 15% or if false blocking lowers solve rate by more than 5 percentage points on real traces.

## Evidence references

- Artifact root: `<local-path>/projects/trace-based-counter-example-ledger-validation-for-llm-tool-95c1f788de`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
