# Adversarial Self-Critique Ledger on Tool-Use Outputs

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adversarial-self-critique-ledger-on-tool-use-outputs-f1ff8262c33b`
Run ID: `adversarial-self-critique-ledger-on-tool-use-outputs-f1ff8262c33b-20260611T014729479930+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cd48ab272cb1

## What looked useful

Explicit tool-output ledgers are most useful when the error depends on temporal state or negative evidence, such as stale values after revised tool calls or final answers that cite failed tools as successful. In this benchmark, adversarial ledger F1 was 0.999 versus 0.935 for simple evidence matching and 0.000 for answer-only checks.

## Boundaries and scale limits

Synthetic deterministic traces only; no real LLM self-critique, no open-ended natural language robustness, no real external APIs, and no full agent benchmark.

## Claim scope

On a 1,200-case structured synthetic benchmark of tool-use transcripts, a latest-fact ledger with adversarial checks detected stale revisions and ignored tool failures that answer-only critique and simple evidence matching missed.

## Why it stopped

No-paper closure: the run produced a useful synthetic mechanism signal, but it is proxy evidence rather than direct LLM self-critique validation.

## Recommended next action

Run a bounded direct LLM-agent follow-up where a model produces tool-use answers and critiques under matched token budgets, using the same ledger rubric and held-out trace tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LLM comparison of adversarial ledgers versus prompted self-critique
- Success threshold: Adversarial ledger improves recall by at least 10 percentage points over the strongest non-ledger baseline while keeping precision at or above 0.90.
- Stop condition: Stop if ledger precision falls below 0.80 or if recall gain over the strongest non-ledger baseline is under 5 percentage points after 200 labeled traces.

## Evidence references

- Artifact root: `<local-path>/projects/adversarial-self-critique-ledger-on-tool-use-outputs-f1ff8262c33b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
