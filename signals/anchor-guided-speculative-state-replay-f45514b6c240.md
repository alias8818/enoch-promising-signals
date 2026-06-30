# Anchor-Guided Speculative State Replay

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-guided-speculative-state-replay-f45514b6c240`
Run ID: `anchor-guided-speculative-state-replay-f45514b6c240-20260604T103641107628+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/2322373383a0

## What looked useful

Exact pre-edit anchor replay was correct on 45/45 calibrated edits with mean 3.79x speedup and median 1.93x speedup. Speedup depended strongly on edit position: about 1.10x early, 1.89x middle, and 8.38x late. The unsafe downstream anchor shortcut was faster but failed trace correctness on 45/45 edits.

## Boundaries and scale limits

Single-process CPU benchmark only; no transformer KV-cache, batching, real serving traces, GPU kernels, multi-edit sessions, or anchor maintenance pressure were tested.

## Claim scope

On a deterministic synthetic causal state workload, exact replay from the nearest anchor before a localized edit preserves full-recompute outputs and gives position-dependent speedups; downstream token-hash-guided speculative jumps are incorrect under trace-level validation.

## Why it stopped

Synthetic proxy evidence supports exact pre-edit anchor replay but early-falsifies token-hash-guided downstream speculative replay; this is not full validation on transformer state replay.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should port the exact and unsafe controls to a small causal transformer and compare every suffix logit or hidden state against full recomputation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer KV-Cache Anchor Replay Correctness Probe
- Success threshold: Exact pre-edit anchor replay must match full recomputation at every suffix position within 1e-5 max logit error and show at least 1.5x median speedup for middle/late edits; downstream jumps must either pass the same correctness test with a justified verifier or be rejected.
- Stop condition: Stop if exact pre-edit anchor replay fails correctness on any deterministic edit after numerical tolerance checks, or if median middle/late speedup is below 1.2x after measuring anchor overhead.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-guided-speculative-state-replay-f45514b6c240`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
