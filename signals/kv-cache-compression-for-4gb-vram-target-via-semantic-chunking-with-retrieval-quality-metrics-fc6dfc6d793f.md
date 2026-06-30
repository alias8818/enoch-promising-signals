# KV cache compression for 4GB VRAM target via semantic chunking with retrieval quality metrics

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-compression-for-4gb-vram-target-via-semantic-chunking-with-retrieval-quality-metrics-fc6dfc6d793f`
Run ID: `kv-cache-compression-for-4gb-vram-target-via-semantic-chunking-with-retrieval-quality-metrics-fc6dfc6d793f-20260614T015727418699+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b71a2bd1b483

## What looked useful

At a 4.0 GiB estimated KV budget retaining 256/512 chunks, semantic selection reached 0.724 recall in the noisy/distractor proxy versus 0.520 recency, 0.498 stride, and 0.488 random. At aggressive 2-20% budgets, semantic remained better than controls but absolute recall was only 0.067-0.378. In a clean upper-bound condition, semantic recall rose to 0.974 at 50% retention.

## Boundaries and scale limits

No real transformer KV tensors were modified, no generation-quality metric was measured, and the 4GB target accounts only for estimated KV memory, not model weights or runtime overhead. Synthetic embeddings proxy semantic separability and same-topic distractors.

## Claim scope

Synthetic chunk-retention proxy for a 65,536-token document using llama-7b-gqa8 fp16 KV memory estimates. Semantic chunk selection improved target retention over recency, stride, and random controls at all tested budgets, but did not provide reliable retrieval under noisy same-topic distractors.

## Why it stopped

Closed as no-paper useful signal because the proxy supports the mechanism but also shows unreliable recall under noisy same-topic distractors; this is not direct/full validation of 4GB VRAM KV-cache compression.

## Recommended next action

Run a bounded deepen experiment with real document embeddings and real long-context QA/needle examples, keeping the same 4GB KV memory accounting and comparing semantic chunk retention against full-context, recency, stride, random, and at least one published KV-compression baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-embedding semantic chunk retention for 4GB KV-budget long-context retrieval
- Success threshold: At the 4GB estimated KV budget, semantic retention must reach at least 0.90 target-chunk recall or answer exact-match within 5 percentage points of full context, while exceeding all simple controls by at least 20 percentage points.
- Stop condition: Stop negative if semantic retention misses more than 10% of targets at the 4GB budget or fails to beat the strongest simple control by at least 10 percentage points on real examples.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-for-4gb-vram-target-via-semantic-chunking-with-retrieval-quality-metrics-fc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
