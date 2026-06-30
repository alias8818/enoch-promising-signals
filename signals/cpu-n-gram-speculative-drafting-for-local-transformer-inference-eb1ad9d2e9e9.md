# CPU n-gram speculative drafting for local transformer inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-drafting-for-local-transformer-inference-eb1ad9d2e9e9`
Run ID: `cpu-n-gram-speculative-drafting-for-local-transformer-inference-eb1ad9d2e9e9-20260527T215003306608+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/72faf9de0682

## What looked useful

A 1-6 byte n-gram drafter accepted the next held-out byte 54% of the time, but emitted tokens per verifier call saturated near 1.54 for K=2 and 2.03-2.29 for K=4-16. Default-thread 2048-dim NumPy calibration made K=2 look potentially useful at 1.48x no-draft upper speedup, but single-thread 4096-dim calibration made all K values lose badly at 0.26x-0.38x. The idea is therefore verifier-kernel-sensitive and likely only worth testing with very small K on an actual runtime.

## Boundaries and scale limits

No real transformer, tokenizer, KV cache, quantized runtime, or sampling loop was benchmarked. Corpus was 6.7 MB of public-domain English text; primary acceptance run used 100,000 positions and a cached sensitivity run used 200,000 positions. Matrix multiplication is an imperfect proxy for transformer verification.

## Claim scope

Bounded CPU-only proxy test of byte-level n-gram speculative drafting on held-out public-domain English text, combined with local NumPy GEMV/GEMM verifier-cost calibration. The result supports only an acceptance/cost tradeoff signal, not an actual local transformer serving claim.

## Why it stopped

Closed as no-paper useful signal because current evidence is proxy-only and mixed: acceptance is measurable, but speedup depends on verifier chunk cost and was negative in the cleaner single-thread sensitivity run.

## Recommended next action

Run a bounded direct benchmark in llama.cpp or another local transformer runtime with the target tokenizer, comparing baseline generation against K=2 and K=4 CPU n-gram drafting on identical prompts and reporting acceptance, verifier latency, and end-to-end tokens/sec.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct local-transformer benchmark for K=2/K=4 CPU n-gram drafting
- Success threshold: At least 1.10x end-to-end tokens/sec improvement over baseline on 3 or more prompt sets, with non-overlapping latency confidence intervals and no quality-affecting decoding change.
- Stop condition: Stop if K=2 and K=4 both fail to reach 1.00x tokens/sec or if verifier chunk latency exceeds the measured mean emitted-token gain by more than 10% on two prompt sets.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-drafting-for-local-transformer-inference-eb1ad9d2e9e9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
