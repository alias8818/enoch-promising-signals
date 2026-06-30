# Natural-language doctrine memory replay with inferred update semantics

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `natural-language-doctrine-memory-replay-with-inferred-upda-94da3d695d`
Run ID: `natural-language-doctrine-memory-replay-with-inferred-upda-94da3d695d-20260629T014616125618+0000`

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

- Parent run decision: Operator-Doctrine Memory vs Flat Retrieval on Repeated Tasks: enoch://control-plane/projects/operator-doctrine-memory-vs-flat-retrieval-on-repeated-tasks-dfa1d509765c/runs/operator-doctrine-memory-vs-flat-retrieval-on-repeated-tasks-dfa1d509765c-20260629T012802002978+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ed5246c3b5cb

## What looked useful

Layered doctrine memory reached 1.000 mean/min accuracy across 30 seeds versus 0.6667 for the best non-layered baseline, exceeding the predefined 0.95 min-accuracy and 0.15 margin thresholds.

## Boundaries and scale limits

Synthetic corpus only: 6 doctrine threads, 30 shuffled seeds, 30 no-op noise events per seed, 12 queries per seed, deterministic parser, no LLM extraction, no real operator traces, and no long-horizon production memory integration.

## Claim scope

A deterministic layered memory that infers add/replace/delete/exception/noop semantics from controlled natural-language doctrine updates outperformed no-memory, transcript-search, and flat-retrieval baselines on a small synthetic replay benchmark.

## Why it stopped

Synthetic bounded mechanism probe produced useful signal but not publication-grade or real-trace evidence.

## Recommended next action

Run a bounded deepen follow-up with held-out paraphrased doctrine updates and model-assisted extraction, preserving the same baselines and success thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Paraphrase-robust doctrine update semantics replay
- Success threshold: Layered memory minimum accuracy >= 0.90 and mean margin over the best non-layered baseline >= 0.15 on held-out paraphrase updates.
- Stop condition: Stop if layered memory falls below 0.80 mean accuracy or its margin over the best baseline is below 0.05 after operation-inference bug fixes are disallowed.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-doctrine-memory-replay-with-inferred-upda-94da3d695d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
