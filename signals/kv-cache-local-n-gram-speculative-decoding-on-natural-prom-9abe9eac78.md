# KV-cache local n-gram speculative decoding on natural prompts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-local-n-gram-speculative-decoding-on-natural-prom-9abe9eac78`
Run ID: `kv-cache-local-n-gram-speculative-decoding-on-natural-prom-9abe9eac78-20260527T111613428607+0000`

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

- Parent run decision: Local N-gram Speculative Decoding with Exact No-Spec Baseline: enoch://control-plane/projects/local-n-gram-speculative-decoding-with-exact-no-spec-baseline-3490cbee010b/runs/local-n-gram-speculative-decoding-with-exact-no-spec-baseline-3490cbee010b-20260527T103611163907+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9e30e000efb9

## What looked useful

Local n-gram replay can exploit locally repetitive prompt/generated prefixes on natural text strongly enough to beat a wrong-context control and pass the predeclared Tier 1 threshold, but the effect is uneven: 17 of 48 prompts had no verifier-call reduction.

## Boundaries and scale limits

This was a Tier 1 small direct call-reduction test, not an integrated serving benchmark. It used one small model, greedy decoding, short natural prompts, and simulated exact verification from generated target continuations. It did not measure end-to-end latency, batching, sampled decoding, larger models, chat workloads, long contexts, or optimized KV-cache verifier kernels.

## Claim scope

On 48 Wikitext-2 natural prompts with distilgpt2 greedy continuations of 96 tokens, a local n-gram draft proposer using only the current prefix reduced simulated target verifier calls for the best tested configuration, with median 2.96x upper-bound call speedup and median 2.25 accepted draft tokens per verifier call.

## Why it stopped

Stopped after Tier 1 useful-signal evidence; this is not paper-ready because it measures verifier-call reduction rather than optimized end-to-end latency.

## Recommended next action

Run a bounded integrated KV-cache speculative decoder benchmark that measures real wall-clock tokens/sec versus greedy decoding and disables drafting with a cheap gate on prompts where local n-gram matches are absent.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated latency benchmark for gated local n-gram speculative decoding
- Success threshold: Median wall-clock throughput at least 1.15x greedy cached decoding, exact greedy output agreement, and local n-gram verifier-call reduction remaining above the wrong-context control.
- Stop condition: Stop if integrated throughput is below 1.05x greedy cached decoding or if proposer/verification overhead erases the verifier-call reduction on the 100-prompt benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-local-n-gram-speculative-decoding-on-natural-prom-9abe9eac78`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
