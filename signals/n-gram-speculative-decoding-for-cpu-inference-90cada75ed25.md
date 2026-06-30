# N-Gram Speculative Decoding for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-for-cpu-inference-90cada75ed25`
Run ID: `n-gram-speculative-decoding-for-cpu-inference-90cada75ed25-20260524T000702984357+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/12311a2acc01

## What looked useful

N-gram speculation reduced verifier calls slightly on natural text but low draft acceptance made the measured CPU cost model slower. On highly repetitive synthetic code it reduced calls sharply, but speedup appeared only when fixed per-call overhead was added.

## Boundaries and scale limits

No real Transformer/LLM was run; tokenizer, KV-cache behavior, attention cost, sampling distribution effects, optimized BLAS kernels, and production serving overhead were not directly measured.

## Claim scope

Bounded proxy test of exact n-gram speculative decoding control flow on regex-tokenized Tiny Shakespeare and synthetic repetitive code, combined with a local CPU dense-layer verification-cost model.

## Why it stopped

Proxy early falsification of the broad speedup claim: natural text slowed down under the measured CPU cost model, while synthetic gains depended on high fixed per-call overhead rather than lower verifier token compute.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next test is a bounded real CPU LLM benchmark with prompt-lookup/ngram drafting on repetitive long-context and natural-text prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM Prompt-Lookup Benchmark for Repetitive Contexts
- Success threshold: At least 1.20x wall-clock speedup on the repetitive/code workload with no more than 5% slowdown on natural text, measured over at least 10,000 generated tokens per condition.
- Stop condition: Stop if repetitive/code workloads fail to exceed 1.05x speedup or if natural-text slowdown exceeds 10% for all tested gamma values.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-for-cpu-inference-90cada75ed25`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
