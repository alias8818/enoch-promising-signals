# Serving endpoint prompt-lookup latency distribution on natural repeated-context workloads

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `serving-endpoint-prompt-lookup-latency-distribution-on-nat-057e7fad9b`
Run ID: `serving-endpoint-prompt-lookup-latency-distribution-on-nat-057e7fad9b-20260523T092544597224+0000`

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

- Parent run decision: N-Gram/Prompt-Lookup Speculative Decoding for Home Inference: enoch://control-plane/projects/n-gram-prompt-lookup-speculative-decoding-for-home-inference-dd02225429a6/runs/n-gram-prompt-lookup-speculative-decoding-for-home-inference-dd02225429a6-20260523T052814500746+0000
- Parent run decision: Integrated prompt-lookup latency benchmark on a local 3B-8B serving model: enoch://control-plane/projects/integrated-prompt-lookup-latency-benchmark-on-a-local-3b-8-5724d3b8eb/runs/integrated-prompt-lookup-latency-benchmark-on-a-local-3b-8-5724d3b8eb-20260523T072915198369+0000

## What looked useful

Across seeds 17, 42, and 2025 with 2000 lookups per seed/workload/capacity, repeated natural contexts reached a 0.5958 prefix hit rate at cache capacity 2048 while shuffled controls reached 0.0008 and exact full-prompt caching reached 0.0. The rolling anchor prefix index matched the naive scan's threshold hit rate and reduced repeated-workload p99 lookup latency from 526.4 us to 51.5 us.

## Boundaries and scale limits

Local Python benchmark only; regex tokenization; synthetic repeated-context construction from Project Gutenberg text; no production inference server, real model tokenizer, concurrent serving, KV-cache allocation, TTFT, or private traffic trace validation.

## Claim scope

In a local CPU-side benchmark using fixed seeds and natural public-domain text assembled into repeated-context serving prompts, prefix lookup finds reusable prompt prefixes that exact full-prompt caching misses; a rolling anchor prefix index preserves the 128-token reuse hit rate while cutting p99 lookup latency by about 10x versus naive longest-prefix scanning at 2048 cached prompts.

## Why it stopped

Medium local evidence supports the prefix-lookup mechanism but does not provide production-serving or end-to-end latency evidence required for a paper.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next bounded test is to replay model-tokenized natural repeated-context prompts through a real serving stack or close equivalent instrumentation and measure lookup p99 plus TTFT under concurrency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-tokenized serving replay for prompt-prefix lookup latency
- Success threshold: Repeated workload prefix hit rate >= 0.30, shuffled-control hit rate <= 0.05, p99 lookup latency at least 5x lower than naive scan, and no TTFT p99 regression greater than 5% versus exact-cache baseline at the same traffic rate.
- Stop condition: Stop if model-tokenized repeated workloads do not produce at least 0.15 prefix hit rate or if indexed lookup overhead erases TTFT benefit under concurrency.

## Evidence references

- Artifact root: `<local-path>/projects/serving-endpoint-prompt-lookup-latency-distribution-on-nat-057e7fad9b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
