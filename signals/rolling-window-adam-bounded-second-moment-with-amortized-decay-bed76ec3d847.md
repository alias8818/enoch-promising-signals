# Rolling-Window Adam: Bounded Second Moment with Amortized Decay

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `rolling-window-adam-bounded-second-moment-with-amortized-decay-bed76ec3d847`
Run ID: `rolling-window-adam-bounded-second-moment-with-amortized-decay-bed76ec3d847-20260526T180341257390+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/31d6205bf9bc

## What looked useful

The amortized tail-removal recurrence is numerically exact and bounded; W=100 returned v_hat to ~1.0 at step 101 while Adam remained at 95.13, and rolling W=100 recovered after the optimization shock in 127.7 mean steps versus Adam's 453.1. However, all rolling windows tested ended with worse mean final loss around 0.040-0.041 versus Adam's 0.0115.

## Boundaries and scale limits

Evidence is CPU-only NumPy, synthetic trace plus small convex stochastic optimization. No neural-network training, AdamW weight decay, large-batch behavior, transformer-scale gradients, or broad hyperparameter robustness was tested.

## Claim scope

On an exact second-moment trace and a 30-seed stochastic diagonal quadratic with a controlled gradient shock, rolling-window Adam exactly removes stale squared-gradient contributions after the configured window and recovers faster after shocks than Adam, but converges to worse final loss under the tested settings.

## Why it stopped

Mixed local evidence: mechanism supported and useful, but practical optimizer quality is not strong enough for a paper because rolling windows improved shock recovery while worsening final loss on the direct small benchmark.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should test a hybrid floor or long-tail blend that preserves the shock recovery benefit without the observed final-loss degradation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid Rolling Adam With Adam-Floor Second Moment
- Success threshold: Hybrid variant has mean recovery steps at least 2x faster than Adam while final loss is within 20% of Adam on the 30-seed quadratic benchmark; if a neural task is run, validation loss must be within 1% of AdamW while preserving faster post-shock recovery diagnostics.
- Stop condition: Stop if no hybrid variant meets both the recovery and final-loss thresholds on the quadratic benchmark, or if the benefit disappears under a basic learning-rate sweep.

## Evidence references

- Artifact root: `<local-path>/projects/rolling-window-adam-bounded-second-moment-with-amortized-decay-bed76ec3d847`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
