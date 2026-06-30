# Real transformer-layer validation of activation-aware outlier residual routing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-transformer-layer-validation-of-activation-aware-outl-2f78afdd99`
Run ID: `real-transformer-layer-validation-of-activation-aware-outl-2f78afdd99-20260621T173302059640+0000`

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

- Parent run decision: Outlier-routed residual quantization with activation-aware channel split: enoch://control-plane/projects/outlier-routed-residual-quantization-with-activation-aware-channel-split-8c45f6f3579d/runs/outlier-routed-residual-quantization-with-activation-aware-channel-split-8c45f6f3579d-20260621T165832127497+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/408262a02f5a

## What looked useful

Activation-aware damped routing reduced mean max hidden norm by 12.7%, but failed the practical threshold: outlier-conditioned validation loss worsened by 1.8% and normal-token loss worsened by 15.6% versus the dense residual baseline.

## Boundaries and scale limits

CPU-only Tier 1 test; 3 seeds, 200 steps, synthetic task, small model, one routing implementation. Not evidence about large pretrained transformers, real corpora, or alternate routing designs.

## Claim scope

A tiny 2-layer causal transformer on a controlled synthetic rare-outlier language task with an activation-norm-gated damped residual route.

## Why it stopped

Direct Tier 1 controlled transformer-layer test failed the predeclared success threshold, so mechanism support is insufficient for a paper-positive result.

## Recommended next action

Stop this paper path; run one bounded deepen follow-up only if testing a parameter-matched bypass/reinjection route rather than damped residual routing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-matched bypass/reinjection routing for transformer activation outliers
- Success threshold: Bypass/reinject route improves outlier-conditioned validation loss by >=5% versus baseline and keeps normal-token loss regression <=2%, with hidden-norm reduction >=10%.
- Stop condition: Stop if the bypass/reinject route misses the loss threshold on this exact task across 3 seeds or only improves activation norms while worsening task loss.

## Evidence references

- Artifact root: `<local-path>/projects/real-transformer-layer-validation-of-activation-aware-outl-2f78afdd99`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
