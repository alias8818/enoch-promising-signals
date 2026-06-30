# Ephemeral Gradient Accumulation: Zero-Optimizer-State Training for Tiny VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ephemeral-gradient-accumulation-zero-optimizer-state-training-for-tiny-vram-8fd24839a39e`
Run ID: `ephemeral-gradient-accumulation-zero-optimizer-state-training-for-tiny-vram-8fd24839a39e-20260607T060958300982+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/8b1a34cc0646

## What looked useful

Ephemeral online SGD can remove optimizer slots and persistent accumulated gradients, reducing persistent memory from about 4x parameter bytes for AdamW and 2x for accumulated SGD to about 1x parameter bytes in the tested harness. One-step diagnostics show it changes the optimization trajectory rather than preserving exact accumulated gradients.

## Boundaries and scale limits

Synthetic easy task, single seed, small model, short 40-step run, no real corpus, no GPT-2-small-class baseline, no actual tiny-GPU OOM boundary, no mixed-precision or activation-checkpointing interaction tests.

## Claim scope

On a 1.8M-parameter CUDA transformer LM synthetic next-token task, stateless per-microbatch SGD with immediate gradient clearing reduced persistent training memory to parameter bytes only, but it was not equivalent to exact gradient accumulation.

## Why it stopped

No-paper closure: bounded synthetic evidence produced a useful memory mechanism signal, but the method is not exact gradient accumulation and the run is too small and synthetic for a publication-grade training claim.

## Recommended next action

Run a bounded deepen test on a real small language-modeling corpus under an explicit VRAM cap, comparing tuned ephemeral online SGD against accumulated SGD and AdamW for OOM/pass and validation loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-VRAM Real-Corpus Ephemeral Online SGD Boundary Test
- Success threshold: Ephemeral online SGD must be the only or lowest-memory method that completes under the cap while ending within 10% validation perplexity of the best feasible stateless baseline after equal tokens.
- Stop condition: Stop if ephemeral online SGD either OOMs at the same or lower model size as accumulated SGD, or requires more than 10% validation perplexity degradation after reasonable learning-rate tuning.

## Evidence references

- Artifact root: `<local-path>/projects/ephemeral-gradient-accumulation-zero-optimizer-state-training-for-tiny-vram-8fd24839a39e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
