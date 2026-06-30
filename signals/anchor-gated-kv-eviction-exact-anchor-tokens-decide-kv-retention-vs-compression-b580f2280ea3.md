# Anchor-Gated KV Eviction: exact-anchor tokens decide KV retention vs compression

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-gated-kv-eviction-exact-anchor-tokens-decide-kv-retention-vs-compression-b580f2280ea3`
Run ID: `anchor-gated-kv-eviction-exact-anchor-tokens-decide-kv-retention-vs-compression-b580f2280ea3-20260528T170411368504+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f6f0cc80afa4

## What looked useful

Across 500 trials per cell, clean anchor-gated retention reached top1_hit 1.000 when budget covered 64 true anchors while best non-full baseline was 0.014. With 1% false-positive anchors, anchor-gated top1_hit was 0.600 at budget 64 and 0.914 at budget 96. With 25% false negatives, anchor-gated saturated near 0.74-0.75, matching the expected missing-anchor failure mode.

## Boundaries and scale limits

No real LLM serving path, no learned anchor predictor, no generation-quality metric, no multi-layer KV cache, and no production latency or memory measurement. Dense softmax output-vector metrics were not discriminative; top-1 retrieval is the meaningful local mechanism metric.

## Claim scope

Synthetic attention-retrieval simulator with exact anchor labels, fixed exact-KV budget, and block-average compression shows anchor-gated exact retention improves target-token top-1 retrieval versus recency, random, key-norm, and compress-all baselines.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic mechanism support, not direct model-serving or generation-quality validation.

## Recommended next action

Run a bounded direct-evidence follow-up with a small transformer or GPT-2-small-class model on synthetic long-context key-value QA, measuring answer accuracy plus latency and memory under the same cache budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer anchor-gated KV retention on synthetic long-context QA
- Success threshold: At the same KV memory budget, anchor-gated retention improves answer accuracy by at least 20 percentage points over the best non-full baseline and recovers at least 80% of full-exact accuracy in the clean-anchor condition, without worse latency than compress-all by more than 25%.
- Stop condition: Stop if anchor-gated retention fails to beat the best non-full baseline by at least 5 percentage points in clean-anchor answer accuracy or if anchor metadata overhead removes the memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-gated-kv-eviction-exact-anchor-tokens-decide-kv-retention-vs-compression-b580f2280ea3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
