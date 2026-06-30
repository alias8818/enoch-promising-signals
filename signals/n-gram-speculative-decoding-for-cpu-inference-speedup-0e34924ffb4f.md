# N-Gram Speculative Decoding for CPU Inference Speedup

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-for-cpu-inference-speedup-0e34924ffb4f`
Run ID: `n-gram-speculative-decoding-for-cpu-inference-speedup-0e34924ffb4f-20260607T232211179779+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/fd8255f1ed89

## What looked useful

Simple n-gram drafting accepted few draft tokens on natural text. At 50k and 100k prompt tokens, optimistic proxy speedups were 1.46x and 1.40x because batched block verification was much cheaper than single-token verification, but a conservative floor model reduced the best speedups to 1.04x and 1.02x; at 20k prompt tokens the result was negative at 0.97x.

## Boundaries and scale limits

No real Transformer or LLM runtime was benchmarked; target verification was proxied by a NumPy float32 MLP-like kernel, acceptance was teacher-forced on one natural-text corpus, and results may not transfer to KV-cache attention, tokenizer overhead, sampling, or production CPU inference kernels.

## Claim scope

Bounded CPU proxy probe on Tiny Shakespeare token traces: online n-gram prompt/history drafting combined with measured NumPy matrix-heavy block verification suggests context-sensitive benefit only when long prompts and favorable batched CPU kernels are present.

## Why it stopped

This run produced useful proxy evidence but not direct paper-ready validation; the positive result depends on an implementation-specific batched-kernel advantage and the conservative speedup is only a few percent.

## Recommended next action

Run a bounded real CPU LLM benchmark, such as llama.cpp prompt-lookup or equivalent n-gram speculative decoding on a quantized small model, and require at least 1.10x wall-clock tokens/s improvement with exact greedy output equivalence before considering a deeper validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU LLM n-gram prompt-lookup speculative decoding benchmark
- Success threshold: >=1.10x tokens/s on repeated-context prompts with exact greedy output equivalence and <=5% slowdown on non-repeated controls.
- Stop condition: Stop as negative if real-model speedup is <1.05x on repeated-context prompts, if outputs diverge in greedy mode, or if non-repeated controls regress by >5%.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-for-cpu-inference-speedup-0e34924ffb4f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
