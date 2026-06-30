# Cascaded retrieval-then-rerank agent memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cascaded-retrieval-then-rerank-agent-memory-823412608276`
Run ID: `cascaded-retrieval-then-rerank-agent-memory-823412608276-20260621T040542557419+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b5f990dbbbaa

## What looked useful

Cascaded rerank achieved 0.9995 mean accuracy versus 0.2997 for flat retrieval and 0.2147 for transcript search, with similar sub-millisecond local latency. The 2 cascaded failures were candidate-retrieval misses, indicating retrieval recall, not rerank selection, is the next bottleneck in this bounded setup.

## Boundaries and scale limits

3,750 synthetic replay tasks, 5 seeds, 3 noise levels, 13 memories per task, top_k=10, CPU-only in-memory Python. Does not validate real agent transcripts, learned embeddings, noisy metadata extraction, production latency, privacy constraints, long-horizon memory compaction, or LLM answer quality.

## Claim scope

In a deterministic synthetic repeated-agent memory benchmark with controlled entity/slot metadata, stale same-pair memories, same-entity and same-slot distractors, and noisy lexical overlap, cascaded sparse retrieval followed by structured reranking selected the intended current memory much more accurately than no-memory, transcript sparse search, or flat sparse retrieval baselines.

## Why it stopped

No-paper closure: this is useful synthetic mechanism evidence, but it relies on generated oracle-like metadata and small corpora, so it is not direct/full validation of an agent memory system.

## Recommended next action

Run a bounded deepen follow-up using noisy metadata extracted from realistic replay transcripts and include top-k, corpus-size, and extraction-error ablations before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy metadata cascaded memory rerank on realistic replay transcripts
- Success threshold: At least 15 percentage-point accuracy improvement over flat retrieval on realistic/noisy replay tasks with candidate hit rate reported and no more than 2x local retrieval latency at the tested scale.
- Stop condition: Stop as negative if cascaded rerank improves accuracy by less than 5 percentage points over flat retrieval or if most errors are caused by metadata extraction failures that the reranker cannot recover from.

## Evidence references

- Artifact root: `<local-path>/projects/cascaded-retrieval-then-rerank-agent-memory-823412608276`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
