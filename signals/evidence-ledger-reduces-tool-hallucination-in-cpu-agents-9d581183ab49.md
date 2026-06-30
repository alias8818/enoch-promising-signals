# Evidence ledger reduces tool hallucination in CPU agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-reduces-tool-hallucination-in-cpu-agents-9d581183ab49`
Run ID: `evidence-ledger-reduces-tool-hallucination-in-cpu-agents-9d581183ab49-20260605T002004167239+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/cc28ee7c2dd8

## What looked useful

Evidence-only ledger enforcement can mechanically prevent unsupported tool-result claims, but the ledger must be restricted to actual tool observations and missing evidence must produce abstention. A ledger that the finalizer can ignore or poison still permits hallucination.

## Boundaries and scale limits

Synthetic proxy only: no real LLM/Codex agent, no realistic software tasks, no adversarial user context, no long-horizon planning, and the enforced-ledger result is partly guaranteed by construction. Full validation requires real CPU-hosted agent traces with annotated tool evidence and final claims.

## Claim scope

In a deterministic synthetic tool-use harness, constraining final claims to an evidence-only ledger of observed tool outputs reduced unsupported final claims from 25.86% in a transcript-only baseline to 0.00%; a free-form ledger reduced but did not eliminate unsupported claims, and poisoned ledger entries reintroduced unsupported claims.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a synthetic proxy, not direct validation on real CPU agents.

## Recommended next action

Run a bounded real-agent benchmark using the same three controls: transcript-only, free ledger, and evidence-only enforced ledger, with unsupported final claims annotated from actual tool traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent evidence-ledger enforcement benchmark
- Success threshold: At least 50% relative reduction in unsupported final claims versus transcript-only baseline, with Wilson 95% confidence intervals that do not overlap the baseline rate and total abstention or task failure below 20%.
- Stop condition: Stop if enforced ledger reduces task completion below 80%, if unsupported-claim reduction is under 25%, or if annotation cannot reliably map final claims to tool evidence.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-reduces-tool-hallucination-in-cpu-agents-9d581183ab49`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
