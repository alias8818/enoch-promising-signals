# Counterexample-Mining Step Before Agent Action Commit

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `counterexample-mining-step-before-agent-action-commit-5e2a791d51f7`
Run ID: `counterexample-mining-step-before-agent-action-commit-5e2a791d51f7-20260630T123003136304+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6535d1d4d6f9

## What looked useful

Mean hidden failure rate across tasks dropped from 0.4417 at budget 0 to 0.1072 at budget 2, 0.0337 at budget 4, 0.0023 at budget 16, and 0.000083 at budget 128. This supports the mechanism that concrete counterexamples before commit can prevent bad toy program-action commits.

## Boundaries and scale limits

This did not test real LLM agents, real tool/API side effects, natural-language critique quality, adversarial environments, or multi-step action plans. Candidate revisions and oracles were hand-authored. The benchmark ran for 200 trials per task per budget with 200 hidden cases per trial.

## Claim scope

On a 12-task toy program-action benchmark with oracle-generated inputs and hand-authored candidate revisions, a bounded counterexample-mining step before commit reduced hidden post-commit failure rates versus immediately committing the first candidate.

## Why it stopped

No-paper closure: the result is a controlled toy mechanism signal, not direct evidence for deployed agents or LLM-generated action commits.

## Recommended next action

Run a bounded deepen follow-up on real LLM-generated candidate code actions for 30-50 HumanEval-style tasks, comparing no pre-commit mining against oracle/property-test counterexample mining with fixed budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pre-commit counterexample mining on real LLM code-action candidates
- Success threshold: At least 50% reduction in mean hidden failure rate with no more than 2x candidate/action evaluation cost, and improvement on at least 70% of tasks with nonzero baseline failures.
- Stop condition: Stop if the miner finds counterexamples on fewer than 20% of failing baseline candidates or if hidden failure reduction is under 25% after 30 tasks.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-mining-step-before-agent-action-commit-5e2a791d51f7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
