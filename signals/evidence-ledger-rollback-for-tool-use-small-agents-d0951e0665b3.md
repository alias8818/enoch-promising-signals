# Evidence-ledger rollback for tool-use small agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-rollback-for-tool-use-small-agents-d0951e0665b3`
Run ID: `evidence-ledger-rollback-for-tool-use-small-agents-d0951e0665b3-20260529T065032674876+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2ce92ee43bde

## What looked useful

Across three 5,000-episode sweeps, rollback matched latest-facts recomputation accuracy and reduced mean absolute error versus append-only scratchpad: at p_error 0.05, accuracy 0.6924 vs 0.3000 and MAE 2.0118 vs 5.3886; at p_error 0.18, accuracy 0.2676 vs 0.0312 and MAE 5.5898 vs 11.6330; at p_error 0.35, accuracy 0.0984 vs 0.0222 and MAE 8.4294 vs 15.9734.

## Boundaries and scale limits

The run used symbolic synthetic episodes only: 24 item values, grouped subtotals, fixed tool error rates, and deterministic correction handling. It did not test real LLM agents, natural-language traces, real tools, planner failures, long-context pressure, or production memory stores.

## Claim scope

In a deterministic synthetic tool-use aggregation task, dependency-aware evidence-ledger rollback prevents stale derived claims from contaminating final answers after verifier corrections, matching full recomputation and outperforming an append-only scratchpad baseline.

## Why it stopped

Synthetic mechanism evidence supports rollback over append-only stale claim retention, but the evidence is not direct enough for a paper about real tool-use small agents.

## Recommended next action

Stop this run as no-paper useful signal; next concrete step is a bounded real small-agent harness using LLM-generated tool traces and the same correction protocol.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger rollback in a real small-agent tool-trace harness
- Success threshold: Rollback should improve final-answer accuracy by at least 10 percentage points over append-only memory, reduce stale evidence citations by at least 50%, and stay within 20% of full recomputation accuracy while using fewer active context tokens.
- Stop condition: Stop if rollback fails to beat append-only by 5 percentage points in accuracy or if most observed failures come from LLM instruction-following rather than stale evidence retention.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-for-tool-use-small-agents-d0951e0665b3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
