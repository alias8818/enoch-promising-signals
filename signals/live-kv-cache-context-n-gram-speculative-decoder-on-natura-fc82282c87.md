# Live KV-Cache Context N-Gram Speculative Decoder on Natural Long-Context Corpora

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-kv-cache-context-n-gram-speculative-decoder-on-natura-fc82282c87`
Run ID: `live-kv-cache-context-n-gram-speculative-decoder-on-natura-fc82282c87-20260529T020611061234+0000`

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

- Parent run decision: Context-Local N-Gram Speculative Drafting with Zero Extra VRAM: enoch://control-plane/projects/context-local-n-gram-speculative-drafting-with-zero-extra-vram-0da0a6edfc9d/runs/context-local-n-gram-speculative-drafting-with-zero-extra-vram-0da0a6edfc9d-20260528T232933276261+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/792c980d2760

## What looked useful

Best config min_n=4,max_n=6,proposal=8 matched greedy on all 9 prompts, accepted 692/1030 proposed tokens, reduced target decode forwards by 47.8% on average, and achieved 1.80x mean wall-clock speedup. The mechanism is supported locally but not paper-ready.

## Boundaries and scale limits

One 0.5B model, three public-domain books, nine sampled prompt endpoints, greedy decoding only, Python/Hugging Face implementation with deepcopy cache rollback, no batching, no 7B+ models, no broad corpus or production-serving validation.

## Claim scope

In a controlled Tier 1 direct test with Qwen2.5-0.5B-Instruct on one GB10 GPU, 1536-token Project Gutenberg prompts, greedy decoding, and 128-token continuations, a live context n-gram proposer with KV-cache verification preserved exact greedy outputs and reduced target decode forwards/wall-clock time for all tested configurations.

## Why it stopped

Tier 1 direct validation produced useful mechanism evidence but is too small and implementation-specific for publication readiness.

## Recommended next action

Run a medium direct confirmation with optimized cache rollback, at least two model families, hundreds of natural long-context prompt endpoints, and the same exact-greedy equivalence check.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Confirmation of Context N-Gram Speculative Decoding with Optimized KV Rollback
- Success threshold: At least 1.25x mean wall-clock speedup and at least 25% target decode forward reduction on two model families with exact greedy equivalence on all samples.
- Stop condition: Stop if any implementation cannot preserve exact greedy equivalence, or if optimized rollback yields less than 1.10x mean speedup on both model families despite at least 300 prompt endpoints.

## Evidence references

- Artifact root: `<local-path>/projects/live-kv-cache-context-n-gram-speculative-decoder-on-natura-fc82282c87`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
