# Contradiction Detection in Agent Memory for Long-Horizon Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `contradiction-detection-in-agent-memory-for-long-horizon-tasks-17b4da2c6d86`
Run ID: `contradiction-detection-in-agent-memory-for-long-horizon-tasks-17b4da2c6d86-20260609T213326343202+0000`

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

Structured normalized memory slots achieved F1 0.924 on 20,000 synthetic events, versus 0.259 for lexical retrieval top-k and 0.781 for exact canonical-name tracking. The largest practical gains appeared on opaque aliases, long gaps, and paraphrased statements.

## Boundaries and scale limits

The evidence is synthetic and rule-based. It does not validate real LLM-agent memory, human-labeled traces, ambiguous temporal scope, source reliability, negation, uncertainty, multi-hop contradictions, or downstream task completion.

## Claim scope

In a controlled synthetic long-horizon memory benchmark with entity/attribute/value statements, paraphrases, opaque aliases, and contradiction gaps up to roughly 100 events, normalized active slot tracking detects contradictions more accurately than lexical retrieval over raw memory text or exact canonical-name tracking.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is not direct or broad enough for a publication-grade claim.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should test the same detector families on real or LLM-generated agent traces with human-labeled contradictions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evaluate normalized contradiction memory on labeled agent traces
- Success threshold: Structured normalized tracking improves F1 by at least 0.10 over lexical retrieval and at least 0.05 over exact-name tracking, while maintaining precision at or above 0.85 on labeled real or LLM-generated traces.
- Stop condition: Stop if structured tracking fails to improve F1 over exact-name tracking by 0.05 or if precision falls below 0.80 on realistic labeled traces.

## Evidence references

- Artifact root: `<local-path>/projects/contradiction-detection-in-agent-memory-for-long-horizon-tasks-17b4da2c6d86`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
