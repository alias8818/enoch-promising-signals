# Seed-robust GPT-2 residual-channel INT4 preservation validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `seed-robust-gpt-2-residual-channel-int4-preservation-valid-b7df82d9c6`
Run ID: `seed-robust-gpt-2-residual-channel-int4-preservation-valid-b7df82d9c6-20260605T215358898456+0000`

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

- Parent run decision: Extreme INT4 Quantization with Principled Residual Channel Preservation in Feed-Forward Layers: enoch://control-plane/projects/extreme-int4-quantization-with-principled-residual-channel-preservation-in-feed-forward-layers-ddf368569742/runs/extreme-int4-quantization-with-principled-residual-channel-preservation-in-feed-forward-layers-ddf368569742-20260605T175255143897+0000
- Parent run decision: All-layer GPT-2 INT4 residual-channel preservation with perplexity validation: enoch://control-plane/projects/all-layer-gpt-2-int4-residual-channel-preservation-with-pe-c1f61b833c/runs/all-layer-gpt-2-int4-residual-channel-preservation-with-pe-c1f61b833c-20260605T203225281143+0000

## What looked useful

Direct GPT-2-small WikiText-2 validation showed full precision PPL 35.69, plain INT4 PPL 1864.75, top-activation preserved INT4 mean PPL 90.98 +/- 0.75 across three calibration seeds, random preserved mean PPL 1789.39, and low-activation preserved mean PPL 1826.34. Top-channel selection was seed-stable with mean Jaccard overlaps 0.859 and 0.901 over 48 modules.

## Boundaries and scale limits

Single model size (GPT-2-small), single dataset (WikiText-2), one preservation ratio (2%), one simple per-channel symmetric INT4 quantizer, no lm_head quantization, and no comparison against established PTQ baselines such as GPTQ, AWQ, SmoothQuant, or parameterized channel-mixing controls.

## Claim scope

For pretrained GPT-2-small on WikiText-2 validation, preserving the top 2% activation-magnitude input channels in transformer projection weights during simple symmetric INT4 post-training quantization recovers most of the perplexity damage versus plain INT4 and same-budget random or low-activation channel preservation across calibration seeds 11, 23, and 37.

## Why it stopped

Tier 2 direct evidence supports the scoped mechanism, but the result is not publication-grade because it lacks broader model/dataset coverage and established quantization baselines.

## Recommended next action

Stop this run as no-paper useful evidence; next, run a bounded deepen follow-up against GPTQ/AWQ/SmoothQuant-style baselines and a preservation-ratio sweep on GPT-2-small and GPT-2-medium before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2 residual-channel preservation against established INT4 PTQ baselines
- Success threshold: Activation-top preservation must beat same-budget random and low-activation controls in mean NLL on both model sizes and remain competitive with at least one established INT4 PTQ baseline without relying on a single preservation ratio.
- Stop condition: Stop if activation-top preservation fails to beat random preservation by at least 10% of the plain-INT4-to-FP NLL gap on either model size, or if established PTQ baselines eliminate the observed advantage.

## Evidence references

- Artifact root: `<local-path>/projects/seed-robust-gpt-2-residual-channel-int4-preservation-valid-b7df82d9c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
