# Hidden-State Router for Local Model Cascades

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `hidden-state-router-for-local-model-cascades-f23fbbd38941`
Run ID: `hidden-state-router-for-local-model-cascades-f23fbbd38941-20260526T082441048732+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/12a892dcebd7

## What looked useful

Hidden-state error AUC averaged 0.8691 vs 0.8271 for confidence; hidden-state AP averaged 0.4788 vs 0.3966; routing 20% of examples recovered 61.9% of cheap-model errors vs 54.6% for confidence and improved oracle cascade accuracy from 0.9318 to 0.9436.

## Boundaries and scale limits

Synthetic data only; tiny classifier only; oracle larger-model assumption; no real local LLM pair, no generative QA, no serving latency/cost measurement, and no public natural-language benchmark result because the public model/dataset smoke path stalled before producing metrics.

## Claim scope

In a controlled synthetic shifted-distribution sequence-classification benchmark with a tiny local Transformer, a linear router over the cheap model's final hidden state predicts cheap-model errors better than max-softmax confidence and improves oracle cascade routing at 20% routed examples on average across five seeds.

## Why it stopped

No-paper closure: the positive result is a synthetic/proxy mechanism signal, not full validation of hidden-state routing for real local model cascades.

## Recommended next action

Run a bounded real-model follow-up using a cached or predownloaded small local LLM routed to a larger local model on labeled QA, comparing hidden-state routers against calibrated confidence with actual larger-model outputs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Local LLM Hidden-State Router on Labeled QA
- Success threshold: Hidden-state routing improves error AUC by at least 0.03 and cascade accuracy by at least 1 percentage point over calibrated confidence at a fixed routed fraction of 20%, with actual larger-model outputs.
- Stop condition: Stop if hidden-state routing fails to beat calibrated confidence on error AUC or cascade accuracy in two independent real-data splits, or if model/dataset access again prevents a valid real-model run.

## Evidence references

- Artifact root: `<local-path>/projects/hidden-state-router-for-local-model-cascades-f23fbbd38941`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
