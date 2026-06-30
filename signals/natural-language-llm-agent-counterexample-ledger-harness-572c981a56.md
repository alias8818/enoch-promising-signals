# Natural-language LLM-agent counterexample ledger harness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `natural-language-llm-agent-counterexample-ledger-harness-572c981a56`
Run ID: `natural-language-llm-agent-counterexample-ledger-harness-572c981a56-20260605T211255185218+0000`

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

- Parent run decision: Agent reliability via evidence ledger with counterexamples: enoch://control-plane/projects/agent-reliability-via-evidence-ledger-with-counterexamples-891798f8cbe2/runs/agent-reliability-via-evidence-ledger-with-counterexamples-891798f8cbe2-20260605T153409056113+0000
- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/0797ab292fce

## What looked useful

Baseline accuracy was 0.60, calibrated ledger accuracy was 0.90, irrelevant-ledger control stayed at 0.60, repeated-failure rate fell from 1.00 to 0.25, and harmful false overrides were 0 on 20 held-out cases.

## Boundaries and scale limits

Small synthetic dataset; deterministic non-LLM agent; no stochastic multi-step tool use; no naturally occurring production traces; no robustness test for noisy or contradictory ledgers.

## Claim scope

In a controlled 20-case natural-language routing harness with a deterministic agent policy, a retrieved counterexample ledger reduced repeated exception failures versus baseline and an irrelevant-ledger control.

## Why it stopped

Tier 1 controlled test produced a useful mechanism signal, but the result is not paper-positive because actual LLM-agent behavior was proxied by a deterministic policy.

## Recommended next action

Run a bounded direct LLM-agent replication using the same baseline/relevant-ledger/irrelevant-ledger controls before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded LLM-agent replication of counterexample ledger harness
- Success threshold: Relevant ledger improves accuracy by at least 20 percentage points or reduces repeated failures by at least 40% versus no-ledger, while irrelevant and stale/contradictory controls do not match the gain and harmful overrides stay below 5 percentage points.
- Stop condition: Stop if the relevant ledger fails to beat both no-ledger and irrelevant-ledger controls by at least 10 percentage points on the first 50 held-out cases, or if harmful overrides exceed 10 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-llm-agent-counterexample-ledger-harness-572c981a56`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
