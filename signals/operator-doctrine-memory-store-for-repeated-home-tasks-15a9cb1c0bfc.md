# Operator-Doctrine Memory Store for Repeated Home Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-store-for-repeated-home-tasks-15a9cb1c0bfc`
Run ID: `operator-doctrine-memory-store-for-repeated-home-tasks-15a9cb1c0bfc-20260620T230542004011+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/65f84ab55b3d

## What looked useful

Doctrine memory reached 0.9169 full-task success and 0.9332 fact-match rate on 3600 varied-surface episodes, versus 0.2019/0.2713 for a 24-fact raw recency baseline. A 1024-fact raw recency control improved to 0.6989 full success but used about 10x mean memory bytes and still trailed doctrine by 0.2181 absolute full-success rate.

## Boundaries and scale limits

Synthetic operators, synthetic doctrine facts, deterministic feedback, no live LLM extraction, no real household traces, no human acceptance or privacy evaluation, and no long-term deployment study.

## Claim scope

In a deterministic synthetic repeated-home-task benchmark, a compact canonical operator-doctrine memory store improved pre-feedback task correctness over stateless and raw recency baselines under paraphrased task references and finite memory.

## Why it stopped

No-paper closure: useful proxy evidence supports the mechanism, but this is not a full validation of real home-task operation, LLM extraction quality, privacy behavior, or human acceptance.

## Recommended next action

Run a bounded direct-evidence follow-up using natural-language correction traces and an LLM or parser extraction layer, comparing canonical doctrine memory against vector/raw retrieval baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-Language Correction Trace Test for Operator-Doctrine Memory
- Success threshold: Doctrine memory improves held-out full-task success by at least 15 absolute percentage points over the best retrieval baseline with no worse than 5 percentage points higher extraction/privacy error and lower inspectable memory size.
- Stop condition: Stop if extraction F1 is below 0.80 on corrections or if doctrine memory fails to beat the best retrieval baseline by at least 5 absolute percentage points on held-out full-task success.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-store-for-repeated-home-tasks-15a9cb1c0bfc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
