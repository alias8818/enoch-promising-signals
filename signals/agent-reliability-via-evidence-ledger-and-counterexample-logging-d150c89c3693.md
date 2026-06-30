# Agent reliability via evidence ledger and counterexample logging

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-reliability-via-evidence-ledger-and-counterexample-logging-d150c89c3693`
Run ID: `agent-reliability-via-evidence-ledger-and-counterexample-logging-d150c89c3693-20260605T161915922832+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/7be7d2f361d0

## What looked useful

Across 20 seeds and 5,000 tasks per seed, ledger+counterexample logging reduced false supported claims to 0.67% versus 12.2% for a recent-context baseline and 5.34% for ledger-only, with 98.49% coverage and 99.11% accuracy when answered.

## Boundaries and scale limits

Synthetic tasks only; binary answers; hand-specified evidence semantics; no real LLM agent, retrieval system, human evidence labels, or long-horizon tool-use traces were tested.

## Claim scope

In a deterministic synthetic binary evidence-stream benchmark with delayed contradictions, persistent evidence ledgers plus explicit counterexample logging reduce false supported final claims versus a recent-context baseline and a ledger-only ablation.

## Why it stopped

No-paper useful signal from a synthetic proxy; this is not full validation of real agent reliability.

## Recommended next action

Run a bounded real LLM-agent trace replay comparing no-ledger, ledger-only, and ledger+counterexample protocols under equal context budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real trace replay for evidence ledger and counterexample logging
- Success threshold: Ledger+counterexample logging reduces false supported final answers by at least 30% relative to ledger-only without lowering answered-task accuracy by more than 5 percentage points.
- Stop condition: Stop if the intervention fails to beat ledger-only on false supported claims in two independent trace sets or if context overhead makes coverage fall below 80%.

## Evidence references

- Artifact root: `<local-path>/projects/agent-reliability-via-evidence-ledger-and-counterexample-logging-d150c89c3693`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
