# N-Gram Target-Draft Speculative Decoding on 10GB GPUs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-target-draft-speculative-decoding-on-10gb-gpus-05e9c51fbe22`
Run ID: `n-gram-target-draft-speculative-decoding-on-10gb-gpus-05e9c51fbe22-20260529T023943333047+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bc97cb3bdc1b

## What looked useful

Repeat-heavy prompts showed 4.60x median speedup on Qwen2.5-0.5B and 6.23x on Qwen2.5-1.5B with about 8x median target-forward reduction; open-ended controls stayed near parity at 1.00x and 1.03x median speedup. Requested greedy prefixes matched in all calibrated cases, but the native prompt-lookup path sometimes generated extra accepted tokens beyond max_new_tokens.

## Boundaries and scale limits

Only two small cached Qwen targets, seven handcrafted prompts, greedy decoding, single-process local benchmarking, no serving engine, no quantized backend, no production traces, and no 7B+ strict-VRAM validation.

## Claim scope

On a GB10 host with Transformers 4.57.6, native n-gram prompt lookup speculative decoding accelerated greedy generation for exact-reuse repeat-heavy prompts on Qwen2.5-0.5B and Qwen2.5-1.5B, while preserving the requested greedy prefix.

## Why it stopped

Bounded local evidence supports the mechanism only for exact-repeat workloads and exposes a strict token-budget caveat; it is not broad or robust enough for a paper.

## Recommended next action

Stop this run as no-paper useful signal; next, implement or wrap strict max-token n-gram speculative decoding and evaluate it on real repeated-context RAG/code-edit traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Strict-Length N-Gram Speculative Decoding on Real Repeated-Context Traces
- Success threshold: Requested outputs exactly match normal greedy decoding with no extra tokens, median speedup is at least 1.5x on repeated-context traces, and median slowdown on controls is no worse than 5%.
- Stop condition: Stop if strict length control removes most of the speedup, if real traces have too few exact reusable spans for at least 1.2x median speedup, or if controls slow down by more than 10%.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-target-draft-speculative-decoding-on-10gb-gpus-05e9c51fbe22`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
