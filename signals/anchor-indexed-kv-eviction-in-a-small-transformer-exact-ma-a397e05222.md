# Anchor-indexed KV eviction in a small transformer exact-match retrieval task

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-indexed-kv-eviction-in-a-small-transformer-exact-ma-a397e05222`
Run ID: `anchor-indexed-kv-eviction-in-a-small-transformer-exact-ma-a397e05222-20260529T211017566277+0000`

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

- Parent run decision: Anchor-Indexed KV Compression with Exact Recall Probes: enoch://control-plane/projects/anchor-indexed-kv-compression-with-exact-recall-probes-e60184c4c634/runs/anchor-indexed-kv-compression-with-exact-recall-probes-e60184c4c634-20260529T174221008055+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ece0442c89b7

## What looked useful

Anchor-indexed retention produced a large controlled retrieval benefit over recency-only eviction when the target memory pair was old, and controls showed the value token adjacent to the matched key is necessary.

## Boundaries and scale limits

Synthetic exact-match task only; one small architecture; 24-pair sequences; three seeds; evaluation emulates cache availability with attention masks at the answer-producing row rather than a real streaming KV-cache implementation; no latency, memory-overhead, natural-language, long-context, or larger-model validation.

## Claim scope

In a 0.999M-parameter, 3-layer synthetic causal transformer trained on BOS K_i V_i ... QUERY K_target -> V_target exact-match retrieval with 24 key/value pairs, retaining the queried key's indexed key/value pair plus a recent window preserved held-out answer accuracy at 0.9979-1.0000 across cache budgets 4, 8, 16, and 32 over three seeds, while recency-only, key-only, and random-pair controls did not.

## Why it stopped

Tier 1 controlled direct test supports the mechanism, but the evidence is synthetic and uses masked attention as a cache proxy, so it is not a full validation or paper-positive result.

## Recommended next action

Stop this worker run as no-paper useful signal; next concrete step is a true incremental decoding implementation with online key-position indexing and overhead measurements on the same task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Streaming implementation of anchor-indexed KV eviction on exact-match retrieval
- Success threshold: For budgets where recency-only accuracy is below 70%, anchor-indexed streaming cache must reach at least 95% answer accuracy and beat recency-only by at least 30 percentage points in all seeds, with overhead reported.
- Stop condition: Stop as negative if the full-cache model cannot reach at least 95% held-out accuracy, if anchor-indexed streaming accuracy is within 5 percentage points of recency-only in two seeds, or if index overhead exceeds the retained-cache savings in the tested regime.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-indexed-kv-eviction-in-a-small-transformer-exact-ma-a397e05222`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
