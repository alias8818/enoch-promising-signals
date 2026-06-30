# Dynamic KV-cache eviction via attention-score thresholding for longer context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-kv-cache-eviction-via-attention-score-thresholding-for-longer-context-5395ff4d5869`
Run ID: `dynamic-kv-cache-eviction-via-attention-score-thresholding-for-longer-context-5395ff4d5869-20260605T132645255705+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/4be1fc6fa736

## What looked useful

Full cache reached 1.000 retrieval accuracy. Recency-24/48 fell to 0.070/0.078 after evicting all old pair tokens. Attention threshold 0.005 kept 1.000 accuracy but retained the full 102-token cache. Attention threshold 0.010 compressed to 81.9 tokens but fell to 0.516 accuracy; threshold 0.020 compressed to 40.4 tokens but fell to 0.430 accuracy; a 48-token threshold budget gave 0.406 accuracy. The observed failure mode is that low-attention tokens during filler spans can become essential at a later query.

## Boundaries and scale limits

Synthetic 8-key/8-value task, 4 stored pairs, 96 filler tokens, 128 evaluation examples, toy PyTorch model and harness-level cache eviction; not a production LLM or broad long-context benchmark.

## Claim scope

Toy synthetic delayed key-value retrieval with a trained 3-layer causal transformer: online current-attention threshold eviction only preserved accuracy when it preserved essentially the full cache; thresholds or budget caps that compressed the cache evicted old key-value tokens and sharply reduced answer accuracy.

## Why it stopped

Early direct mechanism test found no useful accuracy/compression tradeoff for simple online attention-score thresholding; this is a proxy/tiny-model result, not a full production-LLM validation.

## Recommended next action

Stop this run as a bounded no-paper mechanism result; test a heavy-hitter plus recency-pinning eviction variant on the same delayed retrieval harness before any larger-scale LLM trace work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Heavy-hitter plus recency pinning for delayed KV retrieval
- Success threshold: At least one hybrid policy achieves >=0.90 retrieval accuracy with >=40% mean KV-cache reduction on the delayed retrieval harness across three seeds.
- Stop condition: Stop if all compressed policies remain below 0.80 accuracy or if the only accurate settings retain more than 80% of the full cache.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-kv-cache-eviction-via-attention-score-thresholding-for-longer-context-5395ff4d5869`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
