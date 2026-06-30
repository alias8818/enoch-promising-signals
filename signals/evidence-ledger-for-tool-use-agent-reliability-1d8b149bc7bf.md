# Evidence Ledger for Tool-Use Agent Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-tool-use-agent-reliability-1d8b149bc7bf`
Run ID: `evidence-ledger-for-tool-use-agent-reliability-1d8b149bc7bf-20260609T171317283126+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3e789731a7f3

## What looked useful

A simple evidence ledger can mechanically prevent unsupported answers when evidence metadata is available, but it does not solve wrong trusted evidence and it reduces answer coverage as noise increases.

## Boundaries and scale limits

No LLM was run, no real tool traces were used, and the ledger relied on oracle-style observation labels for current/stale/trusted status. Results do not establish reliability gains for deployed agents.

## Claim scope

In a deterministic synthetic tool-observation benchmark with explicit current/stale/trusted/conflicting evidence labels, a ledger-gated finalizer eliminated unsupported final claims across 125000 tasks while trading off coverage.

## Why it stopped

Closed as no-paper useful signal: local synthetic evidence supports the mechanism, but direct agent evidence is required before any publication-grade claim.

## Recommended next action

Run a bounded LLM/tool-trace follow-up where the same ledger gate is applied to real or model-generated tool-use trajectories and measured against unsupported-answer reduction and coverage loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence Ledger on Real Tool-Use Agent Traces
- Success threshold: At least 50% relative reduction in unsupported final answers versus the ungated baseline, ledger unsupported rate below 5%, and coverage loss no worse than 35 percentage points on the same traces.
- Stop condition: Stop if ledger gating reduces unsupported answers by less than 25% or requires more than 50 percentage points coverage loss on the bounded trace set.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-tool-use-agent-reliability-1d8b149bc7bf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
