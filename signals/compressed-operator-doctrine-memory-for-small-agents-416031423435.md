# Compressed Operator Doctrine Memory for Small Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `compressed-operator-doctrine-memory-for-small-agents-416031423435`
Run ID: `compressed-operator-doctrine-memory-for-small-agents-416031423435-20260620T122542415482+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0e65086e62ef

## What looked useful

Layered doctrine memory scored 1.000 accuracy and 0.000 doctrine violation rate at the primary 96-token budget, while the best baseline scored 0.000 accuracy; across a 20-run budget/noise sweep, layered memory stayed at 1.000 and the best baseline ranged from 0.000 to 0.625.

## Boundaries and scale limits

Synthetic rule-based small-agent proxy only; no real LLM, no learned retrieval, no held-out natural operator data, and no production traces were tested.

## Claim scope

In a deterministic synthetic replay benchmark with 8 operator-doctrine scenarios, tight memory budgets, stale doctrine, and noisy retrieval, a compressed precedence-aware doctrine memory achieved higher exact-action accuracy than no memory, raw transcript search, and flat retrieval.

## Why it stopped

This run produced a useful synthetic mechanism signal but not direct evidence for real small agents, so it is finalized as no-paper evidence rather than a paper-positive result.

## Recommended next action

Run a bounded real small-LLM replay evaluation using the same strategies, fixed decoding, held-out task variants, and a recency-aware retrieval baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Small-LLM Replay Test for Compressed Doctrine Memory
- Success threshold: Layered doctrine memory improves exact-action accuracy by at least 15 percentage points over the best retrieval baseline and lowers doctrine violation rate without increasing prompt tokens by more than 25%.
- Stop condition: Stop if layered memory fails to beat the best retrieval baseline by at least 5 percentage points on the first held-out real-model run or if failures are dominated by prompt ambiguity rather than memory strategy.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-operator-doctrine-memory-for-small-agents-416031423435`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
