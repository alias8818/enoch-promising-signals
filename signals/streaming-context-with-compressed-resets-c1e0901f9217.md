# Streaming Context with Compressed Resets

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `streaming-context-with-compressed-resets-c1e0901f9217`
Run ID: `streaming-context-with-compressed-resets-c1e0901f9217-20260605T031121048823+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a52a6c210eec

## What looked useful

Compressed resets recovered beyond-window facts that a fixed window could not recover, but only when the compressed state had enough slots. With 256 slots for 512 keys, compressed accuracy was 0.6431 versus 0.4928 for the sliding window, and long-query accuracy was 0.3794 versus 0.0. At 64 and 128 slots, collision pressure erased much or all of the total-accuracy benefit.

## Boundaries and scale limits

No trained language model, natural text, KV-cache implementation, latency benchmark, or GPT-2-small-class baseline was tested. The strongest positive condition with 512+ slots is an upper-bound sanity check rather than a compressed setting.

## Claim scope

Synthetic streaming key-value recall with 512 keys, 32 values, 512-event reset/window cadence, and bounded hashed key-value compressed state.

## Why it stopped

Synthetic proxy evidence supports the mechanism under sufficient memory budget but is not direct/full validation for language-model streaming context.

## Recommended next action

Stop this worker run as a proxy useful signal; run a bounded trained-transformer follow-up on the same long-range recall structure before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer Compressed-Reset Recall
- Success threshold: At equal parameter scale, compressed-reset model improves beyond-window recall by at least 20 percentage points and total accuracy by at least 5 percentage points without more than 20% inference latency overhead.
- Stop condition: Stop if the compressed-reset model fails to beat the fixed-window baseline on beyond-window recall after matched training budget across two seeds, or if latency/memory overhead dominates the accuracy gain.

## Evidence references

- Artifact root: `<local-path>/projects/streaming-context-with-compressed-resets-c1e0901f9217`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
