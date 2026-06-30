# Layered Memory Architecture for Operator Doctrine

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-memory-architecture-for-operator-doctrine-e606b7b53b65`
Run ID: `layered-memory-architecture-for-operator-doctrine-e606b7b53b65-20260610T061059602657+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b5322e31cb5c

## What looked useful

Across 20 seeds and 3,600 total cases, layered_routed reached 0.936 mean action accuracy and 1.000 target-rule recall@5. Flat TF-IDF reached 0.018 accuracy and 0.446 recall@5 under conflicting episodic distractors; randomizing layer labels dropped layered accuracy to 0.075, indicating the benefit depends on meaningful layer semantics.

## Boundaries and scale limits

Synthetic schema only; no real doctrine corpus, no human/operator evaluation, no LLM planner, no long-horizon agent runs, and no full-scale deployment workload. Full validation would require real doctrine/task traces and model-in-the-loop plan scoring.

## Claim scope

In a deterministic synthetic operator-doctrine retrieval benchmark with lexically similar episodic distractors, a routed layered memory policy with explicit doctrine, episodic, and preference layers improved target-rule recall and action selection over equal-budget flat retrieval and random-label controls.

## Why it stopped

Proxy-only synthetic evidence supports the mechanism but does not validate real operator doctrine use or LLM planning behavior.

## Recommended next action

Stop this run as a no-paper useful signal; deepen with a bounded model-in-the-loop evaluation on real or semi-real doctrine passages before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-in-the-loop layered doctrine memory evaluation
- Success threshold: At least 15 percentage points absolute improvement in doctrine-consistent final action accuracy over flat retrieval, with randomized-layer control within 5 percentage points of the flat baseline and no more than 10% relative latency/context overhead.
- Stop condition: Stop if layered memory fails to beat flat retrieval by 5 percentage points on doctrine-consistent final action accuracy or if gains vanish under randomized mission seeds.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-architecture-for-operator-doctrine-e606b7b53b65`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
