# KV-cache serving benchmark for n-gram draft-free speculative decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-serving-benchmark-for-n-gram-draft-free-speculati-fba5b4b00b`
Run ID: `kv-cache-serving-benchmark-for-n-gram-draft-free-speculati-fba5b4b00b-20260525T131701548243+0000`

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

- Parent run decision: N-gram Context Cache for Draft-Free Speculative Decoding: enoch://control-plane/projects/n-gram-context-cache-for-draft-free-speculative-decoding-a9342d684a1e/runs/n-gram-context-cache-for-draft-free-speculative-decoding-a9342d684a1e-20260525T080315117310+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/31aa1832cda5

## What looked useful

A real causal-LM KV-cache benchmark supports the mechanism: context n-gram candidates can be verified in one main-model forward pass, accepted tokens reduce model calls, rejected-token KV entries can be cropped, and float32 GPT-2 outputs can remain exactly greedy-equivalent. Tiny-gpt2 showed overhead can dominate, and fp16 GPT-2 showed exactness sensitivity on one prompt family.

## Boundaries and scale limits

Not validated for production serving, batching, paged KV caches, non-greedy sampling, fp16/bf16 exactness, 7B+ models, long contexts, or real traffic traces. Python/Hugging Face overhead and synthetic prompt repetition may inflate local speedups.

## Claim scope

Tier 1 controlled small direct test: GPT-2 float32 greedy decoding on one GB10 GPU, single request, synthetic repeated log/code/natural prompts, Hugging Face KV cache. Best n-gram draft-free speculative settings exactly matched greedy output and improved local generated-token throughput by 3.79x to 6.17x on repeated-context prompts.

## Why it stopped

Tier 1 direct mechanism evidence is useful but insufficient for publication-grade serving claims because it is small, synthetic, single-request, and precision-sensitive.

## Recommended next action

Run a bounded follow-up in an actual batched serving runtime or a closer mock with paged KV and fp16/bf16 exactness guards; do not write a paper from this single-request synthetic Tier 1 result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Batched fp16/bf16 KV-cache n-gram speculative serving test
- Success threshold: All tested requests exactly match greedy output, no rejected draft token remains in the retained KV cache, and repeated-context requests achieve at least 1.5x throughput with no more than 10% p95 latency regression on low-repeat controls.
- Stop condition: Stop as negative if fp16/bf16 exactness cannot be preserved without falling back to sequential verification, or if batched scheduler/KV overhead reduces repeated-context throughput gain below 1.2x.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-serving-benchmark-for-n-gram-draft-free-speculati-fba5b4b00b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
