# Embedding and LLM answerer check for layered doctrine memory

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `embedding-and-llm-answerer-check-for-layered-doctrine-memo-6920be59ed`
Run ID: `embedding-and-llm-answerer-check-for-layered-doctrine-memo-6920be59ed-20260620T080700415523+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Semantic Operator Doctrine vs Flat Vector Memory: enoch://control-plane/projects/semantic-operator-doctrine-vs-flat-vector-memory-300142d613e8/runs/semantic-operator-doctrine-vs-flat-vector-memory-300142d613e8-20260620T073742135582+0000
- Parent run decision: Realistic Trace Doctrine Memory vs Filtered Vector Retrieval: enoch://control-plane/projects/realistic-trace-doctrine-memory-vs-filtered-vector-retriev-b6b4f37b6a/runs/realistic-trace-doctrine-memory-vs-filtered-vector-retriev-b6b4f37b6a-20260620T075102478722+0000

## What looked useful

Layered doctrine memory reached 1.000 answer accuracy, but transcript_search and flat_retrieval also reached 1.000. Layered minus flat accuracy was 0.000 with bootstrap 95% CI [0.000, 0.000]. Removing query routing dropped accuracy to 0.797, but removing conflict resolution caused no drop, so the targeted layered mechanism was not supported beyond key-routing value.

## Boundaries and scale limits

Synthetic replay only; no production LLM, neural embedding model, private/operator transcript corpus, or adversarial paraphrase stress set. The corrected benchmark is easy enough that explicit current doctrine records are recovered perfectly by simple baselines.

## Claim scope

On a 360-task fixed-seed synthetic repeated-agent doctrine replay with direct exact-answer scoring, lexical embedding retrieval, and an extractive answerer, layered doctrine memory did not improve answer accuracy over transcript_search or flat_retrieval baselines.

## Why it stopped

Corrected Tier-2 local benchmark directly falsified the success threshold: layered_doctrine_memory did not beat flat_retrieval by the required 0.15 absolute margin and the conflict-resolution ablation did not reduce accuracy.

## Recommended next action

Stop this run as a no-paper useful negative; if continued, run a bounded hard-replay follow-up with paraphrased queries, sparse current restatements, neural embeddings or a real LLM answerer, and the same flat/transcript baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard replay check for layered doctrine memory under paraphrase and sparse updates
- Success threshold: Layered doctrine memory improves exact-answer accuracy over the best real baseline by at least 0.15 absolute with paired bootstrap 95% CI lower bound above 0 and both ablations reduce accuracy by at least 0.05.
- Stop condition: Stop as unsupported if transcript_search or flat_retrieval matches layered accuracy within 0.05 absolute or if the conflict-resolution ablation again shows no measurable drop.

## Evidence references

- Artifact root: `<local-path>/projects/embedding-and-llm-answerer-check-for-layered-doctrine-memo-6920be59ed`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
