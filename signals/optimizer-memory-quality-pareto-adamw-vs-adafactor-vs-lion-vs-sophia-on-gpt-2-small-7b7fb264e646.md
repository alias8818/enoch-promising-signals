# Optimizer memory-quality Pareto: AdamW vs Adafactor vs Lion vs Sophia on GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `optimizer-memory-quality-pareto-adamw-vs-adafactor-vs-lion-vs-sophia-on-gpt-2-small-7b7fb264e646`
Run ID: `optimizer-memory-quality-pareto-adamw-vs-adafactor-vs-lion-vs-sophia-on-gpt-2-small-7b7fb264e646-20260619T044026459442+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2209144b07fc

## What looked useful

Adafactor sharply reduced optimizer state memory and was the only optimizer with a strong positive eval-loss delta in this bounded GPT-2-small-geometry probe. Lion provided the expected half-AdamW state footprint but did not improve quality under the tested configuration.

## Boundaries and scale limits

Not a full GPT-2-small full-vocabulary or real-corpus validation; no multi-seed statistics; no optimizer learning-rate sweep; Sophia implementation is a simplified Sophia-G style gradient-squared diagonal EMA rather than a full paper-faithful Hessian refresh pipeline.

## Claim scope

On a GB10 CUDA run using GPT-2-small depth/width/head geometry with reduced 2048-token vocabulary, context length 128, deterministic synthetic next-token data, and one fixed hyperparameter setting per optimizer, Adafactor had the best measured memory-quality Pareto: about 1.04 MiB optimizer state and 0.1058 eval-loss improvement over 400 steps. AdamW improved less with about 661.68 MiB optimizer state, while Lion and the simplified Sophia-G implementation did not improve.

## Why it stopped

Closed as no-paper useful signal: the result is direct for local optimizer memory/runtime and synthetic quality movement, but it is proxy evidence rather than full real-corpus GPT-2-small validation.

## Recommended next action

Run a bounded real-corpus GPT-2-small confirmation with full vocabulary or a documented tokenizer subset, multiple seeds, and a small learning-rate sweep for AdamW, Adafactor, and Lion before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus GPT-2-small optimizer Pareto confirmation
- Success threshold: Adafactor must match or beat AdamW validation loss within 1 percent while using at least 4x less optimizer state memory, or Lion must recover AdamW-like validation loss while using about half the optimizer state.
- Stop condition: Stop if none of the lower-memory optimizers reaches within 3 percent of AdamW validation loss after the bounded token budget and reasonable learning-rate sweep.

## Evidence references

- Artifact root: `<local-path>/projects/optimizer-memory-quality-pareto-adamw-vs-adafactor-vs-lion-vs-sophia-on-gpt-2-small-7b7fb264e646`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
