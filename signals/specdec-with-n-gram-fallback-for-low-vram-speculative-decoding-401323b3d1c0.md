# SpecDec with n-gram fallback for low-VRAM speculative decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `specdec-with-n-gram-fallback-for-low-vram-speculative-decoding-401323b3d1c0`
Run ID: `specdec-with-n-gram-fallback-for-low-vram-speculative-decoding-401323b3d1c0-20260609T172035282114+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2176f6fda42a

## What looked useful

N-gram fallback accepted 20-38 drafted tokens across 384 generated tokens depending on n-gram length; n=2 gave the best target-call reduction at 9.6%. The signal is opportunistic and concentrated in repetitive contexts, but it supports testing prompt-lookup fallback as a low-memory speculative decoding mode.

## Boundaries and scale limits

Small hand-written prompt set, short 48-token generations, one small target model, greedy-only verification, simple no-KV-cache harness, and no forced low-VRAM/OOM condition. Wall-clock speedups are noisy and not the primary claim.

## Claim scope

On 8 short prompts with distilgpt2 greedy decoding, a prompt-local n-gram fallback can exactly preserve greedy output while reducing target verification calls by 5.2-9.6% without loading a second draft model.

## Why it stopped

Useful bounded local evidence was produced, but the run is not paper-ready because it is a small greedy proxy rather than a production-scale or real-corpus validation.

## Recommended next action

Run a medium KV-cache implementation test on real text traces with a larger target model and compare no draft, resident draft model, n-gram fallback, and hybrid fallback triggers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium KV-cache validation of n-gram fallback speculative decoding
- Success threshold: N-gram or hybrid fallback achieves at least 8% target-call reduction and at least 1.05x wall-clock speedup on repetitive strata, with no output divergence under greedy verification and materially lower memory than a resident draft-model setup.
- Stop condition: Stop if target-call reduction is below 3% on real traces or if KV-cache overhead eliminates wall-clock benefit in every stratum.

## Evidence references

- Artifact root: `<local-path>/projects/specdec-with-n-gram-fallback-for-low-vram-speculative-decoding-401323b3d1c0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
