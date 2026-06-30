# N-gram Backoff Speculative Draft for Low-VRAM Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-backoff-speculative-draft-for-low-vram-inference-842e2271f9f6`
Run ID: `n-gram-backoff-speculative-draft-for-low-vram-inference-842e2271f9f6-20260608T122508970589+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f44864991620

## What looked useful

Plain n-gram backoff is low-VRAM and exactly verifiable, but accepted too few target tokens: best saved-call result was 14.06% target-call reduction in the order ablation and 12.11% with a larger order-1 training set, while wall-clock remained slower than cached greedy.

## Boundaries and scale limits

Not tested on 7B+ models, optimized serving kernels, chat/code traces, or production KV-cache scheduling; wall-clock measurements are from a faithful Python verifier loop.

## Claim scope

Bounded local test of CPU n-gram backoff draft tokens for exact greedy speculative verification against distilgpt2 on WikiText-2 prompts.

## Why it stopped

Early bounded falsification: the direct distilgpt2/WikiText-2 proxy showed low exact-match acceptance and no end-to-end speedup, not a full production validation.

## Recommended next action

Stop this naive n-gram backoff line as no-paper evidence; only revisit with a bounded confidence-gated or trace-adapted draft mechanism that must exceed 30% target-call reduction before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Confidence-gated n-gram speculative draft on target decode traces
- Success threshold: At least 30% target-call reduction, zero exact-match failures, CPU draft memory below 10% of target parameter bytes, and wall-clock no slower than cached greedy in the local implementation.
- Stop condition: Stop if target-call reduction remains below 20% or if gating reduces proposal frequency so much that wall-clock cannot match cached greedy.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-backoff-speculative-draft-for-low-vram-inference-842e2271f9f6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
