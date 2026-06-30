# Real serving benchmark for CPU n-gram speculation on code completion

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-serving-benchmark-for-cpu-n-gram-speculation-on-code-8009abcea3`
Run ID: `real-serving-benchmark-for-cpu-n-gram-speculation-on-code-8009abcea3-20260524T051813081053+0000`

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

- Parent run decision: CPU N-gram cache speculative decoding: enoch://control-plane/projects/cpu-n-gram-cache-speculative-decoding-3a42783731c4/runs/cpu-n-gram-cache-speculative-decoding-3a42783731c4-20260524T042712943688+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9b19fa4a73f3

## What looked useful

Prompt lookup n-gram speculation frequently proposed candidate tokens and materially improved decode wall time in a real target-model generation loop, but exactness and acceptance-rate evidence is mixed across dtype/model controls and is not sufficient for a paper claim.

## Boundaries and scale limits

Small local Tier 1 benchmark only: handcrafted prompts, one small non-code-specialized main model, batch size 1, no production server scheduler, no concurrency, no latency percentiles, no large code benchmark corpus, and incomplete local cache for the intended Qwen2.5-Coder checkpoint.

## Claim scope

On a local GB10 using Hugging Face Transformers prompt lookup assisted generation with Qwen/Qwen3-0.6B on 24 code-completion-style prompts, CPU n-gram prompt lookup reduced single-request greedy decode wall time by 1.62x in float32 while preserving greedy prefixes for the requested token budget. A bf16 run was 1.67x faster and reached 20.1% accepted/proposed draft tokens but had one greedy-prefix divergence.

## Why it stopped

Tier 1 direct test produced useful but mixed evidence: exact float32 run was fast but below the 20% accepted/proposed threshold, while bf16 met the threshold but had one greedy-prefix divergence.

## Recommended next action

Stop this run as no-paper useful signal; next run should use a complete code-specialized model in a real serving harness with concurrency, latency percentiles, exactness checks, and n-gram/proposal-length ablations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production-style serving benchmark for prompt lookup speculation on a complete code model
- Success threshold: Exact greedy-prefix preservation on 100% of tested prompts, at least 20% p50 and p95 latency reduction versus greedy baseline, no throughput regression greater than 5%, and accepted/proposed draft-token rate at or above 20%.
- Stop condition: Stop as negative if exactness fails on any deterministic prompt without an implementation fix, or if p95 latency improves by less than 10% after n-gram/proposal-length tuning.

## Evidence references

- Artifact root: `<local-path>/projects/real-serving-benchmark-for-cpu-n-gram-speculation-on-code-8009abcea3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
