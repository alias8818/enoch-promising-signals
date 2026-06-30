# Anchor-KV: keep exact-anchor K/V at FP16, INT4 the rest

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-kv-keep-exact-anchor-k-v-at-fp16-int4-the-rest-3a574f5d7473`
Run ID: `anchor-kv-keep-exact-anchor-k-v-at-fp16-int4-the-rest-3a574f5d7473-20260609T224307885809+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/43b997fa0ab8

## What looked useful

Exact FP16 anchors help when anchors carry attention mass. On GPT-2 activations, 2% anchors reduced relative MSE by 12.8%, 19.5%, and 40.2% across sampled layers at about 5.4% extra memory over all-INT4; 5% anchors reduced error by 36.2%, 44.7%, and 66.2% at about 14.0% extra memory. Synthetic diffuse-attention cases showed only 1-8% improvement, establishing a boundary condition.

## Boundaries and scale limits

No end-to-end perplexity, generation, packed-kernel latency, online anchor policy, larger-model, or long-context serving validation was run. GPT-2 probe used one cached prompt, 512 tokens, and layers 0, 6, and 11.

## Claim scope

Bounded mechanism result: with oracle-selected high-attention anchors, keeping anchor K/V exact in FP16 while quantizing the rest to INT4 reduces attention-output relative MSE versus all-INT4 on synthetic attention-cache probes and a cached GPT-2 activation probe.

## Why it stopped

Closed as no-paper useful signal: the mechanism is supported on direct attention-output metrics, but downstream quality, online anchor selection, and real packed-INT4 performance remain unvalidated.

## Recommended next action

Run a bounded deepen follow-up with an online non-oracle anchor policy inside autoregressive GPT-2 decoding, measuring perplexity, memory, and decode latency against FP16 KV and all-INT4 KV.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Online Anchor-KV GPT-2 decoding validation
- Success threshold: At 2-5% anchors, Anchor-KV should recover at least 50% of the all-INT4 perplexity/NLL degradation versus FP16 while keeping KV memory below 35% of FP16 and adding no more than 15% decode latency versus all-INT4 in the local implementation.
- Stop condition: Stop if online Anchor-KV fails to recover at least 25% of all-INT4 quality loss or if decode latency overhead exceeds 30% before any quality benefit appears.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-kv-keep-exact-anchor-k-v-at-fp16-int4-the-rest-3a574f5d7473`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
