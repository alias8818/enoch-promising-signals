# Direct GB10 paged-KV eviction test in a real serving stack

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `direct-gb10-paged-kv-eviction-test-in-a-real-serving-stack-1135178c4d`
Run ID: `direct-gb10-paged-kv-eviction-test-in-a-real-serving-stack-1135178c4d-20260605T173519525655+0000`

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

- Parent run decision: KV-cache eviction under GB10 queue pressure: enoch://control-plane/projects/kv-cache-eviction-under-gb10-queue-pressure-5c40b653ada2/runs/kv-cache-eviction-under-gb10-queue-pressure-5c40b653ada2-20260605T145139376639+0000
- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/0eb48d708acf

## What looked useful

vLLM initialized on GB10 with explicit paged-KV cache sizing and reported 896 KV-cache tokens at 16 MB. In a clean run, an 89-token anchor prompt had 80 cached-token hits on immediate repeat; after 24 unique-front prompts totaling 5712 prompt tokens, the same anchor had 0 cached-token hits, then recovered to 80 hits on the next repeat. This directly supports cache eviction under independent prefix pressure in a real serving stack.

## Boundaries and scale limits

Single host, single small model, short run, eager mode, no concurrent load sweep, no larger 7B-class model, no production traffic trace, and no repeated statistical ablation across cache sizes or prompt distributions.

## Claim scope

Tier 1 controlled direct test on one GB10 host using vLLM 0.22.1 OpenAI-compatible serving, distilgpt2, prefix caching enabled, block size 16, max model length 256, and explicit 16 MB KV cache cap. Independent prompt pressure evicted an earlier anchor prefix from the local prefix/KV cache.

## Why it stopped

Tier 1 direct evidence was obtained, but it is a small single-model serving test and not publication-grade validation.

## Recommended next action

Run a bounded medium confirmation on the same GB10 with two cache caps, at least two prompt distributions, concurrent requests, and repeated trials to quantify eviction thresholds and hit-rate/latency impact.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GB10 vLLM paged-KV eviction threshold sweep with concurrent prompt pressure
- Success threshold: Across at least three trials per condition, anchor cached-token hits drop to zero or below 10 percent of hot-cache hits only after independent pressure exceeds the configured KV token capacity, while immediate repeats recover the expected hot-cache hits.
- Stop condition: Stop if vLLM cannot keep the server stable under modest concurrency on GB10, or if cache-hit loss does not correlate with configured KV capacity in repeated controlled trials.

## Evidence references

- Artifact root: `<local-path>/projects/direct-gb10-paged-kv-eviction-test-in-a-real-serving-stack-1135178c4d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
