# Tool-Use Evidence Ledger for Small Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tool-use-evidence-ledger-for-small-agents-b86bd3f70daa`
Run ID: `tool-use-evidence-ledger-for-small-agents-b86bd3f70daa-20260525T213451140058+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e860e91d93dc

## What looked useful

Across 20,000 confirmation tasks per policy, baseline unsupported final claims were 30.51% with 65.19% exact accuracy. Ledger-abstain reduced unsupported final claims to 0% at 63.88% accuracy and 36.12% abstention. Ledger-repair reduced unsupported final claims to 0% and reached 100% exact accuracy with mean 1.4279 tool calls versus 1.1028 for baseline. Sensitivity runs preserved the zero-unsupported ledger result across low/default/high skip/wrong/arithmetic-error regimes.

## Boundaries and scale limits

No real LLM-generated traces, no open-domain tools, no ambiguous evidence, and no natural-language claim/evidence parser were tested. The 100% repair accuracy depends on known task schemas and deterministic tool results.

## Claim scope

In a closed synthetic catalog QA benchmark with schema-known required evidence and deterministic tools, an evidence-ledger gate eliminated unsupported final claims; a repair variant also restored exact answers by fetching missing evidence and recomputing.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a synthetic/proxy mechanism test, not direct validation on real small-agent LLM traces.

## Recommended next action

Run a bounded deepen follow-up with an actual small instruction model producing tool traces, then wrap the same tasks with ledger-abstain and ledger-repair policies to measure unsupported claims, accuracy, and repair failures.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM Trace Validation for Evidence-Ledger Tool Use
- Success threshold: Unsupported final-claim rate drops by at least 80% versus baseline, exact accuracy does not fall by more than 5 percentage points for abstain or improves for repair, and repair overhead remains below 0.75 extra tool calls per task.
- Stop condition: Stop if ledger gates fail to reduce unsupported final claims by at least 50% on a 200-task smoke set or if claim/evidence parsing cannot be made reliable enough to score traces without manual judgment.

## Evidence references

- Artifact root: `<local-path>/projects/tool-use-evidence-ledger-for-small-agents-b86bd3f70daa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
