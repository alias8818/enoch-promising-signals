# Natural-language repeated-agent memory benchmark with metadata-aware flat baselines

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `natural-language-repeated-agent-memory-benchmark-with-meta-e3e8cc7b25`
Run ID: `natural-language-repeated-agent-memory-benchmark-with-meta-e3e8cc7b25-20260612T085159531192+0000`

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

- Parent run decision: Layered memory vs flat retrieval on repeated agent tasks: enoch://control-plane/projects/layered-memory-vs-flat-retrieval-on-repeated-agent-tasks-b65ff39fa88d/runs/layered-memory-vs-flat-retrieval-on-repeated-agent-tasks-b65ff39fa88d-20260611T163801785554+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/17d687b72f1b

## What looked useful

Metadata-aware flat baselines are a necessary control for repeated-agent memory benchmarks. Exact metadata filtering solved the controlled current-fact task, while text-only BM25 and soft metadata reranking remained brittle under stale-value and distractor collisions.

## Boundaries and scale limits

Tier 1 controlled synthetic test only: 30 main seeds, 10 agents, 6 keys, 5 repeated updates, 80 distractors per seed; oracle query metadata and exact value matching; no real traces, learned extraction, embeddings, LLM answering, or long-horizon deployment.

## Claim scope

In a deterministic synthetic repeated-agent latest-fact memory benchmark, exact agent/key/time metadata filtering in a flat memory table reached 100% accuracy and exceeded text-only flat lexical retrieval by 93.72 percentage points in the metadata-only-agent condition.

## Why it stopped

The Tier 1 direct test supports the mechanism but is synthetic and oracle-metadata-dependent, so it is no-paper useful signal rather than paper-positive evidence.

## Recommended next action

Run a bounded deepen test with noisy metadata extraction and paraphrased queries before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy metadata extraction for repeated-agent memory baselines
- Success threshold: Across at least 20 seeds or an equivalent held-out trace split, practical metadata-aware retrieval reaches >=85% exact answer accuracy and >=30 percentage point absolute gain over the best text-only flat retrieval baseline.
- Stop condition: Stop as negative if metadata extraction errors reduce the practical metadata-aware baseline below 70% accuracy or below a 10 percentage point gain over text-only retrieval in two independently generated trace sets.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-repeated-agent-memory-benchmark-with-meta-e3e8cc7b25`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
