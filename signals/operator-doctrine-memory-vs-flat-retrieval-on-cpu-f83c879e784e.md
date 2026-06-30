# Operator-Doctrine Memory vs. Flat Retrieval on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-vs-flat-retrieval-on-cpu-f83c879e784e`
Run ID: `operator-doctrine-memory-vs-flat-retrieval-on-cpu-f83c879e784e-20260620T220441983650+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a2accbf205cf

## What looked useful

Primary full run: flat retrieval accuracy 0.5775 with 365 stale-rule errors; layered doctrine memory accuracy 1.0000 with zero errors. Five-seed sweep: mean flat accuracy 0.5861, mean layered accuracy 1.0000, minimum accuracy delta 0.3576.

## Boundaries and scale limits

Synthetic corpus only; no real operator data, no LLM-in-the-loop agent, no embedding or ANN baseline, and no robustness test for missing or noisy metadata. Full primary run covered 864 tasks and 14688 memory items; five-seed sweep covered 288 tasks per seed.

## Claim scope

On a deterministic synthetic repeated-agent replay benchmark with explicit operator/rule/version metadata, layered operator-doctrine memory selected current doctrine more accurately than flat lexical retrieval under stale transcript and scratchpad noise.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is proxy-only and not broad or publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should test semi-natural replay tasks with imperfect metadata plus an embedding or LLM retrieval baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Semi-natural operator-doctrine memory benchmark with imperfect metadata
- Success threshold: Layered doctrine memory improves accuracy by at least 10 percentage points over the best flat baseline while not increasing stale-rule errors, across at least five seeds.
- Stop condition: Stop if the layered advantage falls below 5 percentage points or errors are dominated by metadata/key extraction failures that the current design does not address.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-flat-retrieval-on-cpu-f83c879e784e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
