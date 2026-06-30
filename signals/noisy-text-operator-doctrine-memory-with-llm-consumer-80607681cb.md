# Noisy Text Operator-Doctrine Memory With LLM Consumer

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `noisy-text-operator-doctrine-memory-with-llm-consumer-80607681cb`
Run ID: `noisy-text-operator-doctrine-memory-with-llm-consumer-80607681cb-20260611T185931971670+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Operator-Doctrine Memory: Learning Reusable Behaviors Beyond Fact Recall: enoch://control-plane/projects/operator-doctrine-memory-learning-reusable-behaviors-beyond-fact-recall-883b87d1d055/runs/operator-doctrine-memory-learning-reusable-behaviors-beyond-fact-recall-883b87d1d055-20260611T182818517684+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/64970e5b76f9

## What looked useful

Across 23,040 per-query records, operator-noisy memory produced zero character-mode nonzero-noise wins of at least 10 percentage points versus clean memory and was worse at the highest query-noise levels; word/bigram retrieval also showed no positive deltas and degraded by up to 10.6 percentage points.

## Boundaries and scale limits

Synthetic 40-rule doctrine corpus, deterministic retrieval consumers, 12 seeds, CPU-only run under 15 minutes; no real LLM generation, no production RAG stack, and no large natural corpus.

## Claim scope

Controlled synthetic Tier 1 doctrine-memory retrieval test: expanding doctrine memory with noisy text operator variants did not improve top-1 doctrine/action recovery over clean memory under query corruption.

## Why it stopped

Controlled Tier 1 direct mechanism test falsified the success threshold; this is an early falsification of the memory-expansion mechanism, not full LLM validation.

## Recommended next action

Stop this line as a no-paper useful signal unless a future real LLM/RAG test can directly show noisy doctrine variants improve answer accuracy by at least 10 percentage points at multiple realistic corruption levels.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/noisy-text-operator-doctrine-memory-with-llm-consumer-80607681cb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
