# Agent Reliability via Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-reliability-via-evidence-ledger-22bcef5c1581`
Run ID: `agent-reliability-via-evidence-ledger-22bcef5c1581-20260605T083550941440+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/d8e1b158b562

## What looked useful

On 5,000 synthetic cases at 0.75 conflict rate, baseline unsupported answer rate was 0.3692, ledger-without-recency unsupported rate was 0.0910, and latest-reliable evidence ledger unsupported rate was 0.0000. Conflict-rate sweeps at 0.25, 0.50, and 0.90 preserved the same ordering.

## Boundaries and scale limits

Evidence is symbolic and synthetic. The run does not test LLM extraction errors, retrieval noise, natural-language ambiguity, long-horizon planning, API/tool failures, or real user tasks.

## Claim scope

In a deterministic synthetic conflicting-evidence harness, an evidence ledger with relevance filtering, minimum source reliability, and recency-based conflict resolution reduced unsupported final answers versus a first-match baseline and a ledger-without-recency ablation.

## Why it stopped

Synthetic/proxy-only mechanism support is not direct publication-grade evidence for real agent reliability.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should wrap the ledger contract around a real LLM on a bounded fact-verification or QA benchmark with adversarial stale evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM Evidence Ledger on Adversarial Stale-Evidence QA
- Success threshold: Ledger agent lowers unsupported answer rate by at least 30% relative to scratchpad baseline while reducing exact answer rate by no more than 5 percentage points and keeping abstention below 15%.
- Stop condition: Stop if ledger extraction/citation validity is below 90% on a 100-case audit or if unsupported answer reduction is below 10% on the first 300 labeled cases.

## Evidence references

- Artifact root: `<local-path>/projects/agent-reliability-via-evidence-ledger-22bcef5c1581`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
