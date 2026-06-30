# Small Transformer Learned-Route Adapter Retention Test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-transformer-learned-route-adapter-retention-test-b70bae4e6d`
Run ID: `small-transformer-learned-route-adapter-retention-test-b70bae4e6d-20260522T034522711990+0000`

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

- Parent run decision: Local-Serving Data-Route Bounded Fine-Tuning: enoch://control-plane/projects/local-serving-data-route-bounded-fine-tuning-1c114cdf5ae1/runs/local-serving-data-route-bounded-fine-tuning-1c114cdf5ae1-20260521T202028084148+0000
- Parent run decision: Neural Adapter Route-Bounded Fine-Tuning Probe: enoch://control-plane/projects/neural-adapter-route-bounded-fine-tuning-probe-1d5d50ae8c/runs/neural-adapter-route-bounded-fine-tuning-probe-1d5d50ae8c-20260522T033630004041+0000

## What looked useful

Learned-route adapters achieved mean route0 retention accuracy 0.9860 +/- 0.0313 after route1-only updating, with route1 new accuracy 1.0000. Dense fine-tuning retained 0.4215 +/- 0.1815 and shared adapter retained 0.0117 +/- 0.0262. Swapping learned-route experts reduced route0 retention to 0.1039 +/- 0.0877, supporting route-specific adapter isolation as the mechanism.

## Boundaries and scale limits

One 40k-parameter one-block transformer, synthetic key-to-answer mappings, explicit route labels, CPU-only local validation, no natural language workload, no GPT-2-small-class model, no replay/EWC/LoRA robustness suite, and no ambiguous or latent route cues.

## Claim scope

In a synthetic short-context small-transformer continual-learning task with explicit route tokens, learned route-specific adapters retained an untouched route mapping while learning a changed route mapping better than dense fine-tuning and a shared always-on adapter over 5 fixed seeds.

## Why it stopped

Medium synthetic validation supports the mechanism but remains too scoped and artificial for publication readiness.

## Recommended next action

Stop this run as no-paper useful signal; next, run a GPT-2-small-class or similarly realistic language-model retention benchmark with explicit route/domain cues, matched LoRA/shared-adapter/dense baselines, and no-replay plus replay controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class learned-route adapter retention benchmark
- Success threshold: Learned-route adapters must improve old-domain retention by at least 20 percentage points in accuracy or reduce perplexity regression by at least 25% relative to the best non-replay baseline while matching at least 95% of its new-domain adaptation metric across at least 3 fixed seeds.
- Stop condition: Stop if learned-route adapters fail to beat the best matched non-replay baseline on old-domain retention in 2 of 3 seeds, or if the route-swap/no-route ablations show no meaningful dependence on route-specific adapter selection.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-learned-route-adapter-retention-test-b70bae4e6d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
