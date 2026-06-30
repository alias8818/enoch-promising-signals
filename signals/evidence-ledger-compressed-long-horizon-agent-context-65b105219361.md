# Evidence-Ledger Compressed Long-Horizon Agent Context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-compressed-long-horizon-agent-context-65b105219361`
Run ID: `evidence-ledger-compressed-long-horizon-agent-context-65b105219361-20260611T144058986306+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fd9129181108

## What looked useful

Corrected benchmark aggregate answer/support accuracy was 0.5980 for evidence_ledger versus 0.1388 random, 0.0709 recency, and 0.0550 latest_summary; ledger beat the best baseline by 0.4592 absolute accuracy. Long traces exposed a limitation: global source-ranked retention saturates near 0.5 accuracy because budget is spent on non-query high-quality claims.

## Boundaries and scale limits

Evidence is synthetic and schema-aware only. It does not validate natural-language extraction, LLM summarization errors, real agent trajectories, semantic retrieval baselines, or downstream task success. Corrected main run covered 300 episodes per condition, trace lengths up to 4096 events, and budgets up to 2048 token-proxy units.

## Claim scope

On a deterministic synthetic long-horizon trace benchmark with schema-aware events, sparse target facts, fixed token-proxy budgets, and optional later lower-quality conflicts, a source-ranked evidence ledger preserved answer/support facts substantially better than recency, random, and latest-value summary baselines.

## Why it stopped

Proxy synthetic mechanism test only; it supports the structured-ledger mechanism but does not provide direct/full evidence for real long-horizon agents.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should test an extraction-plus-ledger pipeline on realistic natural-language agent traces against semantic retrieval and summarization baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-Language Agent Trace Evidence Ledger Evaluation
- Success threshold: At least 10 percentage points absolute improvement in answer accuracy and support accuracy over the best matched-budget baseline on realistic traces, with extraction F1 reported and no more than 2x latency overhead versus semantic retrieval.
- Stop condition: Stop if extraction F1 is below 0.70 or if ledger retrieval fails to beat the best matched-budget baseline by at least 5 absolute points on a 100-trajectory pilot.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-compressed-long-horizon-agent-context-65b105219361`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
