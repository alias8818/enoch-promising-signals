# Ternary gradient plus residual for home multi-GPU training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-gradient-plus-residual-for-home-multi-gpu-training-e8bd79ad2c51`
Run ID: `ternary-gradient-plus-residual-for-home-multi-gpu-training-e8bd79ad2c51-20260608T111940575724+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/f51065dc37c2

## What looked useful

Residual error feedback is worthwhile for biased deterministic ternary gradient compression in the tested short-horizon proxy: at 80 steps, threshold ternary alone had 9.88x dense validation loss, while threshold ternary plus residual reached 0.942x dense validation loss with the same estimated 4x practical payload reduction.

## Boundaries and scale limits

No physical multi-GPU all-reduce, no real network or PCIe/NVLink timing, no packed ternary communication kernel, no transformer/GPT-scale model, and no long optimizer-schedule robustness test. Communication savings are payload estimates, not measured end-to-end training speedups.

## Claim scope

In a single-GB10 simulated data-parallel linear-regression proxy with 4 logical workers, deterministic ternary gradient compression with worker-local residual feedback matched dense short-horizon validation loss while using an estimated 4x smaller practical int8 gradient payload; stochastic ternary and long convex runs did not show a clear residual-specific advantage.

## Why it stopped

Proxy-only useful signal; not a full validation of home multi-GPU training speedup or transformer-scale convergence.

## Recommended next action

Run a bounded direct follow-up on either a real 2-GPU bandwidth-limited host with packed ternary communication or a GPT-2-small-class training proxy; require dense-like validation and measured wall-clock or transport-level speedup before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed ternary residual gradients on a real bandwidth-limited 2-GPU training loop
- Success threshold: Ternary plus residual reaches within 2% of dense validation quality and improves median end-to-end step time by at least 10% on a bandwidth-limited 2-GPU setup, with ternary without residual failing at least one of those criteria.
- Stop condition: Stop if packed ternary plus residual is more than 2% worse than dense validation quality after matched training budget, or if measured communication savings fail to improve end-to-end step time by at least 10%.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-gradient-plus-residual-for-home-multi-gpu-training-e8bd79ad2c51`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
