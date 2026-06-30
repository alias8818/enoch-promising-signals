# Gradient-Gated Sparse Optimizer: Train Top-k% Parameters by Gradient Signal

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-gated-sparse-optimizer-train-top-k-parameters-by-gradient-signal-7fb674a3e80b`
Run ID: `gradient-gated-sparse-optimizer-train-top-k-parameters-by-gradient-signal-7fb674a3e80b-20260526T173311361295+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/31d6205bf9bc

## What looked useful

EMA(abs(gradient)) top-k matched dense two-moons accuracy at 10% per-step density (0.978906 vs dense 0.978516 mean accuracy over 5 seeds) while touching 0.233 of parameters; at 1% density it still reached 0.975879 accuracy while touching 0.037 of parameters. Random-k controls reached only 0.847266 at 10% and 0.539844 at 1%. On sparse regression, 1% EMA top-k had MSE 0.007682 versus dense 0.004405, while 1% random-k failed with MSE 14.178483.

## Boundaries and scale limits

No transformer, real dataset, AdamW, long-run, kernel-speed, or production optimizer-state memory validation was run. The implementation measures algorithmic update selection, not deployable sparse optimizer throughput.

## Claim scope

Small synthetic tasks show that gradient-signal top-k parameter-entry updates can preserve dense-like task quality at 10% and even 1% per-step update density, while random-k controls fail badly at low density. The claim is limited to the implemented SGD-with-momentum probe on sparse linear regression and two-moons MLP classification.

## Why it stopped

Local synthetic evidence supports the mechanism but is not direct enough for a paper; closure is no-paper useful signal rather than full validation.

## Recommended next action

Run one bounded deepen follow-up on a real small language-model or vision task with AdamW-style dense, EMA top-k, instant top-k, random-k, and static-mask controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: AdamW Gradient-Gated Top-k on a Real Small Model Task
- Success threshold: EMA top-k must match dense validation metric within 2% relative degradation at 10% update density and outperform random-k and static-mask controls by a clear margin at 5% or lower density across at least 3 seeds.
- Stop condition: Stop if EMA top-k degrades more than 5% relative to dense at 10% density or fails to beat random-k/static controls on the primary validation metric.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-gated-sparse-optimizer-train-top-k-parameters-by-gradient-signal-7fb674a3e80b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
