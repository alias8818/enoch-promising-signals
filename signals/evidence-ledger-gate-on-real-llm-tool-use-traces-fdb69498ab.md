# Evidence Ledger Gate on Real LLM Tool-Use Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-gate-on-real-llm-tool-use-traces-fdb69498ab`
Run ID: `evidence-ledger-gate-on-real-llm-tool-use-traces-fdb69498ab-20260605T102953732773+0000`

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

- Parent run decision: Agent Reliability via Evidence Ledger for Tool Use: enoch://control-plane/projects/agent-reliability-via-evidence-ledger-for-tool-use-cf3926f9566e/runs/agent-reliability-via-evidence-ledger-for-tool-use-cf3926f9566e-20260605T054044068601+0000
- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/28a3c5acb135

## What looked useful

Evidence ids alone are not enough: citation-only accepted unsupported in-ledger mutations, while a ledger gate that checks typed predicates against the cited evidence rejected all controlled unsupported cases in two bounded runs.

## Boundaries and scale limits

Test used 500 evidence entries from recent local Codex traces plus a 200-entry repeat run. Claims were deterministic structured templates and controlled mutations, not unconstrained model-generated summaries or human-adjudicated free-form claims.

## Claim scope

On bounded local Codex JSONL traces, a typed evidence-ledger gate accepted supported structured claims and rejected controlled unsupported mutations about real tool-call exit codes and tool names better than a citation-only baseline.

## Why it stopped

Tier 1 direct mechanism test succeeded on real traces, but evidence remains a structured controlled test rather than publication-grade validation on noisy LLM-generated claims.

## Recommended next action

Run a bounded deepen follow-up on real assistant final-answer claims with typed evidence annotations and independent adjudication; do not write a paper from this template-mutation result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence Ledger Gate on Free-Form Assistant Claims
- Success threshold: On at least 100 adjudicated free-form claims from real traces, reject at least 80% of unsupported claims with no more than 10% supported-claim false rejections, and beat citation-only gating by at least 30 percentage points on unsupported rejection.
- Stop condition: Stop as negative if typed evidence annotation cannot be produced reliably from real assistant claims or if unsupported rejection is less than 50% at more than 20% supported false rejection.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-gate-on-real-llm-tool-use-traces-fdb69498ab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
