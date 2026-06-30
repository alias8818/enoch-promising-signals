# Evidence Ledger for Small-Agent Tool-Use Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-small-agent-tool-use-reliability-749929c07dd7`
Run ID: `evidence-ledger-for-small-agent-tool-use-reliability-749929c07dd7-20260609T014342066735+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/93e550780a82

## What looked useful

Ledger checks convert unsupported proposals into abstentions; bounded repair calls produce the accuracy gain; faulty tools remain an accuracy limit because the ledger verifies support rather than truth.

## Boundaries and scale limits

Synthetic proxy only; no live LLMs, real APIs, multi-step planning, natural-language tool parsing, latency modeling, or external tool-use benchmark validation.

## Claim scope

In a local stochastic synthetic single-tool task harness, ledger-gated finalization eliminated unsupported final answers and, with one repair call, improved accuracy by about 16.5-17.0 percentage points at default injected error rates.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic proxy evidence, not direct publication-grade validation on real agents.

## Recommended next action

Run a bounded real-agent follow-up using the same ledger protocol on a small model tool-use benchmark with hidden ground truth and matched token/tool-call budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-model evidence ledger benchmark
- Success threshold: Unsupported final answers drop by at least 80% relative while accuracy improves by at least 5 absolute percentage points and mean tool-call overhead stays below 30%.
- Stop condition: Stop if unsupported answers do not fall by at least 50% or if the ledger policy's tool-call overhead exceeds 50% without an accuracy gain.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-agent-tool-use-reliability-749929c07dd7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
