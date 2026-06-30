# INT2 weights with learned FP8 residual channels on GPT-2-small-class transformer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-weights-with-learned-fp8-residual-channels-on-gpt-2-small-class-transformer-8622e5d6b179`
Run ID: `int2-weights-with-learned-fp8-residual-channels-on-gpt-2-small-class-transformer-8622e5d6b179-20260621T160105066321+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/588e49d9c221

## What looked useful

Across all 48 GPT-2 transformer Conv1D matrices, 12.5% top-error FP8 residual rows reduced mean INT2 weight relative MSE from 0.3250 to 0.2351 and output relative MSE from 0.3262 to 0.2356 at nominal 3.0 bits/weight. Random residual rows at the same budget only reached 0.2823 weight relative MSE. In a local forward-loss probe, dense loss was 5.8484, INT2-only was 8.7865, top-error residual was 7.9224, and random residual was 8.6335.

## Boundaries and scale limits

No benchmark perplexity, fine-tuning/recovery training, packed-kernel throughput, or hardware serving measurement was run. The forward-loss check used a local 209-token text sample and is not a language-model benchmark. Learned residuals did not materially beat directly fitted static FP8 residuals.

## Claim scope

On pretrained GPT-2-small Conv1D transformer weights, per-row INT2 plus FP8 residual rows on the highest INT2-error output channels reduces reconstruction and random-activation output error versus INT2-only, and improves a small deterministic forward-loss probe versus INT2-only and random residual channels.

## Why it stopped

Closed as no-paper useful signal because the proxy and small forward evidence support a mechanism but do not validate benchmark LM quality, recovery training, or packed INT2/FP8 systems performance.

## Recommended next action

Run a bounded deepen experiment on a real LM validation set: GPT-2-small INT2-only versus top-error FP8 residual rows versus random rows versus static fitted residual rows, with optional short recovery training and perplexity as the primary metric.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small perplexity recovery with top-error FP8 residual rows
- Success threshold: At 12.5% residual rows, top-error INT2+FP8 residuals recover at least half of the INT2-only perplexity degradation versus dense and outperform random residual rows by at least 20% relative degradation reduction on the same validation set.
- Stop condition: Stop if top-error residual rows fail to improve perplexity degradation versus INT2-only by at least 20% relative on a real validation set, or if static fitted residuals fully match learned residuals and no training-specific advantage appears.

## Evidence references

- Artifact root: `<local-path>/projects/int2-weights-with-learned-fp8-residual-channels-on-gpt-2-small-class-transformer-8622e5d6b179`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
