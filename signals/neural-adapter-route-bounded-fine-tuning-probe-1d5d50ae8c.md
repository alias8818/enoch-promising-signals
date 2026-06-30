# Neural Adapter Route-Bounded Fine-Tuning Probe

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `neural-adapter-route-bounded-fine-tuning-probe-1d5d50ae8c`
Run ID: `neural-adapter-route-bounded-fine-tuning-probe-1d5d50ae8c-20260522T033630004041+0000`

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
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f42e89d1099e

## What looked useful

Across 12 seeds with a matched-total-rank global adapter baseline, route-bounded adapters achieved 0.3802 target-route accuracy gain versus 0.4021 for global adapters, while non-target accuracy forgetting was 0.0000 versus 0.1693 for global adapters.

## Boundaries and scale limits

Synthetic binary classification over frozen nonlinear features; explicit oracle route IDs; no learned router, transformer, language modeling, GPT-2-small-class baseline, or real dataset validation.

## Claim scope

In a controlled synthetic multi-route neural adapter probe with explicit route IDs, route-bounded fine-tuning preserved unchanged routes while adapting the changed target route nearly as well as a matched-total-rank global adapter.

## Why it stopped

Tier 1 direct mechanism test succeeded, but evidence remains synthetic and structurally route-isolated, so this run is no-paper useful signal rather than publication-grade validation.

## Recommended next action

Run a bounded deepen test in a small transformer-class setting with learned or model-derived routes before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Transformer Learned-Route Adapter Retention Test
- Success threshold: Route-bounded fine-tuning has non-target forgetting at least 50% lower than the matched baseline while preserving at least 90% of baseline target adaptation on real or semi-real sequence tasks.
- Stop condition: Stop if learned/noisy routing eliminates the retention advantage or target adaptation falls below 80% of the matched baseline in the small transformer setting.

## Evidence references

- Artifact root: `<local-path>/projects/neural-adapter-route-bounded-fine-tuning-probe-1d5d50ae8c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
