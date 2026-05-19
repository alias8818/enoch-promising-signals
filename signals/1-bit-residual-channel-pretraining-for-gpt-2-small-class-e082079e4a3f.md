# 1-Bit Residual Channel Pretraining for GPT-2-Small Class

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `1-bit-residual-channel-pretraining-for-gpt-2-small-class-e082079e4a3f`
Run ID: `1-bit-residual-channel-pretraining-for-gpt-2-small-class-e082079e4a3f-20260518T103815996526+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b7309050a869

## What looked useful

Across three seeds, dense residuals reached mean validation loss 2.2578 nats, fixed-scale 1-bit residuals reached 2.5855 (+0.3277), and learned-scale 1-bit residuals reached 3.1367 (+0.8788), with similar throughput and identical parameter count.

## Boundaries and scale limits

This was a 3.2M-parameter Tiny Shakespeare character-level probe, plus one partial 10.7M-parameter seed-0 run. It was not GPT-2-small BPE pretraining, not full-token-budget training, and not a packed-kernel hardware efficiency test.

## Claim scope

Naive straight-through 1-bit residual-channel bottlenecks, applied after attention and MLP residual additions in a small GPT-like character-level language model, underperform dense residuals at matched model shape over 200-step multi-seed local training.

## Why it stopped

Proxy early falsification rather than full validation: the local small GPT-like training comparison found a large validation-loss penalty for both tested 1-bit residual variants and no throughput benefit in this non-packed implementation.

## Recommended next action

Stop this naive 1-bit residual-channel pretraining variant as a proxy early falsification; only revisit after a cheap-scale mechanism change closes the validation-loss gap against dense residuals.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-preserving 1-bit bottleneck with dense bypass gate
- Success threshold: At 500 steps, the gated/annealed 1-bit variant must be within 0.10 nats of the dense baseline mean validation loss while retaining at least 75% of residual channels through the 1-bit path.
- Stop condition: Stop if the gated/annealed variant remains more than 0.20 nats worse than dense by 500 steps, or if diagnostics show the bypass stays effectively dense.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-residual-channel-pretraining-for-gpt-2-small-class-e082079e4a3f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
