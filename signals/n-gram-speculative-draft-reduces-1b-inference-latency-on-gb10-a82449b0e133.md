# N-gram speculative draft reduces 1B inference latency on gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-reduces-1b-inference-latency-on-gb10-a82449b0e133`
Run ID: `n-gram-speculative-draft-reduces-1b-inference-latency-on-gb10-a82449b0e133-20260530T045221043817+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e6f3dc984d66

## What looked useful

Among strict exact-output/exact-length rows, copy-heavy prompts had median 1.77x speedup and best 5.16x, while general prompts had median 1.16x and best 1.71x. However, 22 of 48 speculative attempts had output or length mismatch, so the broad claim is not supported.

## Boundaries and scale limits

Single local GB10, one 1.5B model, batch size 1, 8 prompts, 32 generated tokens, two repeats, Transformers generate path only; no serving stack, batching, quantization, long-context, long-generation, or 7B+ validation.

## Claim scope

On GB10 with Qwen2.5-1.5B-Instruct BF16 batch-1 generation, Transformers prompt n-gram lookup speculative generation can reduce latency for some exact-output 32-token continuations, especially copy-heavy prompts, but the effect is not uniform.

## Why it stopped

No-paper useful signal: direct GB10 evidence shows context-dependent latency gains, but robustness and exact generation parity are insufficient for a positive research conclusion.

## Recommended next action

Run a bounded deepen test with max_new_tokens parity enforcement and accepted-token instrumentation over a larger prompt suite before considering any paper or deployment claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parity-safe n-gram prompt lookup with accepted-token instrumentation on GB10
- Success threshold: All rows maintain exact output and length parity; copy-heavy median speedup is at least 1.5x; general-prompt median speedup is at least 1.0x with p90 slowdown no worse than 5%.
- Stop condition: Stop if parity cannot be enforced without eliminating the speedup, or if copy-heavy median speedup falls below 1.2x after instrumentation.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-reduces-1b-inference-latency-on-gb10-a82449b0e133`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
