# Evidence-Ledger Constraint for Tiny Tool Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-constraint-for-tiny-tool-agents-a6577f515e83`
Run ID: `evidence-ledger-constraint-for-tiny-tool-agents-a6577f515e83-20260605T042204538298+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/9386228f9296

## What looked useful

At 5,000 tasks with budget 4, ledger accuracy was 0.9864 versus 0.8808 baseline, paired delta +0.1056 with 95% bootstrap CI [0.0960, 0.1148]. Unsupported task rate fell from 0.4882 to 0.0136, while mean tool calls rose by 0.884. A 3-seed budget sweep showed negative accuracy deltas at budgets 2 and 3, and positive deltas of about +0.103 to +0.112 at budgets 4 to 6.

## Boundaries and scale limits

Evidence is simulator-only, CPU-only, and does not test real LLM tool use, natural-language ambiguity, adversarial evidence, production latency, or human utility of abstention versus stale guesses. Budgets 2 and 3 reduced unsupported claims but hurt exact-answer accuracy.

## Claim scope

In a synthetic database-tool benchmark for tiny heuristic agents whose main failure mode is incomplete evidence gathering, an evidence-ledger audit/repair wrapper improves exact-answer accuracy when the tool budget is at least the number of required lookups plus minimal retry margin.

## Why it stopped

No-paper closure because the current evidence is synthetic and mixed: it supports the mechanism under sufficient budget but exposes a budget cliff, so it is not publication-grade direct evidence.

## Recommended next action

Run a bounded deepen follow-up with an actual tiny local or API small-model tool agent on the same task family, comparing baseline prompting to ledger-constrained prompting under budgets 3, 4, and 5.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Tiny Tool-Agent Ledger Budget Cliff Test
- Success threshold: Ledger-constrained real-agent accuracy improves by at least 0.05 at budget 4 or 5, unsupported task rate drops by at least 0.20, and mean extra tool calls stay at or below 2.0; budgets below required evidence should reproduce the accuracy/abstention tradeoff.
- Stop condition: Stop if ledger-constrained real-agent accuracy delta is below 0.02 at budgets 4 and 5, or if extra tool calls exceed 2.0 without accuracy gain, even if unsupported claim rate falls.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-constraint-for-tiny-tool-agents-a6577f515e83`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
