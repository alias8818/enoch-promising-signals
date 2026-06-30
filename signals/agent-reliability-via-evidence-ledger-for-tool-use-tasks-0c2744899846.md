# Agent reliability via evidence ledger for tool-use tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-reliability-via-evidence-ledger-for-tool-use-tasks-0c2744899846`
Run ID: `agent-reliability-via-evidence-ledger-for-tool-use-tasks-0c2744899846-20260605T121344028119+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/0ecc541d5ba8

## What looked useful

Evidence ledgers are useful only when citations are checked against task-bound provenance/tool arguments as well as output values; value-only checking can accept distractor evidence when a wrong answer matches an irrelevant observation.

## Boundaries and scale limits

No live LLM, natural-language entailment, external tools, public benchmark, human grading, long-horizon planning, or adversarial prompt-injection traces were tested. Results are a mechanistic local proxy, not a production-agent validation.

## Claim scope

On synthetic structured account-query tool-use tasks, a task-bound evidence ledger verifier eliminated unsupported presented answer fields in 10,000 default tasks and a 25,000-task fabrication-rate sweep, while increasing refusals and lowering exact-answer coverage.

## Why it stopped

Synthetic proxy produced a useful mechanism signal but is not direct enough for a paper-positive agent reliability claim.

## Recommended next action

Run a bounded deepen follow-up using a real LLM tool-use benchmark with mandatory field-level citations and task-bound ledger verification.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Task-bound evidence ledger on real LLM tool-use traces
- Success threshold: At least 50% relative reduction in unsupported final claims versus baseline, refusal rate under 30%, and task success drop no greater than 10 percentage points on at least 200 real LLM tool-use tasks.
- Stop condition: Stop if the ledger cannot parse field-level citations reliably after a prompt/wrapper smoke test, or if a 50-task pilot shows unsupported-claim reduction below 20% with refusal rate above 40%.

## Evidence references

- Artifact root: `<local-path>/projects/agent-reliability-via-evidence-ledger-for-tool-use-tasks-0c2744899846`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
