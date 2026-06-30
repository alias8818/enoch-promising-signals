# KV-cache latency validation for prompt-suffix speculative drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-latency-validation-for-prompt-suffix-speculative-5823d3d5c8`
Run ID: `kv-cache-latency-validation-for-prompt-suffix-speculative-5823d3d5c8-20260529T122531094802+0000`

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

- Parent run decision: Suffix N-Gram Speculative Drafting: enoch://control-plane/projects/suffix-n-gram-speculative-drafting-6aed72d8cf20/runs/suffix-n-gram-speculative-drafting-6aed72d8cf20-20260529T083200938613+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5c0c56bfae25

## What looked useful

Controlled small direct test supports the KV-cache latency mechanism for prompt-suffix drafting: long reusable prefixes make cached suffix evaluation substantially faster than full-context prefill, with low candidate-count amortization. The evidence is useful for deciding to run an end-to-end follow-up, but not enough for a paper.

## Boundaries and scale limits

Single GPT-2-class model, synthetic random-token prompts, microbenchmark forward passes only, no end-to-end speculative drafting loop, no real serving scheduler, no multi-model or multi-dataset robustness. Strict max-logit equivalence threshold was not met, though mean logit differences were small and top-1 agreement was high.

## Claim scope

On a GB10 GPU with Hugging Face GPT-2 forward passes over random token IDs, reusing a prefix KV cache reduced median suffix-evaluation latency by 53.8% to 70.8% for prefix lengths >=512 and suffix length <=64 compared with recomputing full prefix+suffix prefill; prefix-cache build cost amortized after about 1.3 to 1.6 candidate suffixes in the strongest cases.

## Why it stopped

No-paper useful signal: direct latency threshold was met, but the run is a single-model synthetic-token microbenchmark and strict max-logit equivalence was not met, so it is mechanism support rather than paper-positive validation.

## Recommended next action

Stop the paper gate here; run a bounded deepen follow-up that measures end-to-end prompt-suffix speculative drafting on real prompt/suffix traces with acceptance and quality controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end prompt-suffix speculative drafting with prefix KV reuse
- Success threshold: For prefix length >=512 and suffix length <=64, end-to-end cached-prefix suffix drafting must reduce median latency by at least 25% versus full prefill while preserving acceptance/top-k agreement at >=99% or showing no measurable output-quality regression.
- Stop condition: Stop if scheduler/tokenizer/cache overhead reduces median latency savings below 10% in two representative local models or if acceptance/top-k agreement falls below 95%.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-latency-validation-for-prompt-suffix-speculative-5823d3d5c8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
