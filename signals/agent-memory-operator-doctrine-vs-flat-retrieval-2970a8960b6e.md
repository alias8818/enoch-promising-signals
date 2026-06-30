# Agent Memory: Operator Doctrine vs Flat Retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-memory-operator-doctrine-vs-flat-retrieval-2970a8960b6e`
Run ID: `agent-memory-operator-doctrine-vs-flat-retrieval-2970a8960b6e-20260611T030030425085+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1c2cf98124c5

## What looked useful

Operator doctrine was data-hungry and underperformed flat retrieval by 19-30 accuracy points at 40-160 training episodes, but at 320 episodes it beat the best flat baseline by 2.1-6.2 points while using fewer stored condition items and roughly 9-11x faster query-time prediction.

## Boundaries and scale limits

No LLM agents, embeddings, vector store, natural-language traces, online memory writes, or real multi-step tasks were tested. The largest condition used 320 training episodes and 1000 test episodes per seed.

## Claim scope

Bounded synthetic structured-memory proxy: transparent conjunction-rule doctrine induced from episodic records was compared with flat nearest-neighbor retrieval on hidden-policy action prediction across 96 local runs.

## Why it stopped

Proxy evidence is useful but mixed and not direct enough for a paper; sparse-memory results falsify any broad automatic-superiority claim for operator doctrine over flat retrieval.

## Recommended next action

Run a bounded deepen follow-up with natural-language synthetic agent traces, a doctrine extractor, and an embedding/vector retrieval baseline under a fixed context budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language trace doctrine versus vector retrieval under fixed context budget
- Success threshold: At medium memory size, doctrine reaches at least the vector retrieval accuracy within a 2 percentage point margin or better, with at least 5x lower retrieved context footprint and no worse than 20% degradation on minority action classes.
- Stop condition: Stop if doctrine remains more than 5 accuracy points below vector retrieval at medium memory size or if extraction errors erase the latency/context advantage.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-operator-doctrine-vs-flat-retrieval-2970a8960b6e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
