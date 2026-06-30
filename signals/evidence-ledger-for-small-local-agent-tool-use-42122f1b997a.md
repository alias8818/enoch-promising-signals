# Evidence Ledger for Small Local Agent Tool-Use

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-small-local-agent-tool-use-42122f1b997a`
Run ID: `evidence-ledger-for-small-local-agent-tool-use-42122f1b997a-20260604T065814075277+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8ecf6cd3b5fd

## What looked useful

Task-context binding is necessary: a fact-only ledger missed 8 of 340 wrong-observation corruptions, while a task-bound ledger rejected 340 of 340 wrong-observation corruptions and 1,761 of 1,761 total injected corruptions.

## Boundaries and scale limits

Synthetic traces only; structured claim syntax; no real LLM agent, natural-language claim extraction, adversarial prompting, concurrent tools, or long-horizon workflows were tested.

## Claim scope

In a 5,000-task synthetic local-tool harness with structured claims, a task-context-bound evidence ledger rejected all injected unsupported-answer corruptions with no observed false positives and sub-10-microsecond p95 verification time.

## Why it stopped

No-paper useful signal: the mechanism is supported in a synthetic structured proxy, but direct real-agent evidence is missing.

## Recommended next action

Run the task-bound ledger on real small local-agent traces with natural-language answers and citation extraction before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Task-Bound Evidence Ledger on Real Local-Agent Traces
- Success threshold: At least 95% unsupported-claim rejection recall, at most 2% false-positive rejection on valid answers, and under 1 ms median verification overhead per final answer.
- Stop condition: Stop if real-trace recall falls below 85% or valid-answer false positives exceed 5% after extractor tuning, because the structured synthetic result would not transfer.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-local-agent-tool-use-42122f1b997a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
