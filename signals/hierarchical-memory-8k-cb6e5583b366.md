# Hierarchical Memory 8k

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-memory-8k-cb6e5583b366`
Run ID: `hierarchical-memory-8k-cb6e5583b366-20260531T095619802153+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3158d7e70227

## What looked useful

Dense retrieval stayed at 1.0000 accuracy through noise 0.10, and oracle true-block retrieval also stayed at 1.0000, but mean top-8 block summaries reached only 0.2720 at noise 0.10 and LSH-16-slot top-8 reached only 0.4043 while scanning 12.5% of tokens. The bottleneck is robust target-block selection, not local retrieval within the block.

## Boundaries and scale limits

Single synthetic benchmark, 2048 trials per noise level, 8192-token memories, random vector keys, no language-model training, no learned memory writer/router, no natural text evaluation, and no optimized kernel implementation.

## Claim scope

On a synthetic 8k sparse associative-recall task, non-learned hierarchical block summaries were not robust enough to replace dense retrieval under mild query noise, although an LSH-slot selector gave a useful no-noise signal and oracle-block retrieval showed local retrieval is not the bottleneck.

## Why it stopped

Proxy early falsification: simple mean and LSH-slot hierarchical summaries did not meet a practical sparse-recall threshold under mild query noise, so this is useful no-paper evidence rather than a full validation or publication-grade result.

## Recommended next action

Stop this run as a proxy early falsification of simple hierarchical summaries; the next bounded test is a learned or noise-robust block router on the same 8k task with dense and oracle controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned 8k Block Router for Sparse Associative Recall
- Success threshold: At noise 0.10, held-out accuracy and target-block recall at or above 0.95 while scanning no more than 12.5% of tokens, with dense retrieval at or near 1.0 and oracle-block retrieval confirming local retrieval is not limiting.
- Stop condition: Stop as negative if the learned router remains below 0.80 accuracy at noise 0.10 after a bounded training budget or only succeeds by scanning more than 25% of tokens.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-memory-8k-cb6e5583b366`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
