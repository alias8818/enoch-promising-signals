# Real-model latency benchmark for n-gram fallback speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-model-latency-benchmark-for-n-gram-fallback-speculati-19e352e5b3`
Run ID: `real-model-latency-benchmark-for-n-gram-fallback-speculati-19e352e5b3-20260608T124131310871+0000`

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

- Parent run decision: Corpus benchmark for n-gram fallback speculative decoding: enoch://control-plane/projects/corpus-benchmark-for-n-gram-fallback-speculative-decoding-ff48ad6f26/runs/corpus-benchmark-for-n-gram-fallback-speculative-decoding-ff48ad6f26-20260608T082835229100+0000
- Parent run decision: Spec-Decoding with N-gram Fallback: enoch://control-plane/projects/spec-decoding-with-n-gram-fallback-6bfdcae87d4c/runs/spec-decoding-with-n-gram-fallback-6bfdcae87d4c-20260607T230436323963+0000

## What looked useful

Mechanism support is real but workload-dependent: prompt lookup strongly helps copy/repetition-heavy prompts by reducing target forward calls, while gpt2 natural prompts were slower than cached greedy despite fewer calls. Exactness checks found first-48-token greedy matches in 60/72 prompt-seed groups per prompt-lookup variant and boundary overshoot up to 54 generated tokens for a 48-token request.

## Boundaries and scale limits

Only GPT-2-class models, single-request GPU generation, 48 requested new tokens, 12 local prompts, deterministic decoding, and the Transformers 4.57.6 prompt lookup implementation were tested. No 7B+ models, batching, production serving stack, or large realistic RAG/code workload suite was evaluated.

## Claim scope

On GB10 with distilgpt2 and gpt2, Hugging Face prompt n-gram lookup speculative decoding can reduce target forward calls and improve median tokens/s by about 2.0x-3.6x on repetition-heavy prompts, but it is not consistently faster than cached greedy on natural prompts and does not always preserve exact greedy output/token-budget behavior.

## Why it stopped

Moderate direct evidence is mixed: latency improves on favorable repetitive prompts, but the method is not robustly faster than cached greedy on natural prompts and the tested implementation has output-equivalence/token-boundary limitations.

## Recommended next action

Stop paper escalation for this run; next useful work is an exactness-preserving prompt-lookup benchmark on longer realistic copy-heavy RAG/code workloads before considering scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact prompt-lookup speculative decoding on realistic copy-heavy workloads
- Success threshold: For exact first-N greedy-equivalent output, median tokens/s is at least 1.5x cached greedy on copy-heavy workloads with no more than 5% slowdown on natural controls across at least two model sizes.
- Stop condition: Stop if exact output preservation cannot be achieved locally or if copy-heavy workloads fail to reach 1.2x median speedup versus cached greedy on GPT-2-class models.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-latency-benchmark-for-n-gram-fallback-speculati-19e352e5b3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
