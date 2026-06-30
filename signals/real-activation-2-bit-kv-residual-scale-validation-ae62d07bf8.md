# Real-Activation 2-bit KV Residual Scale Validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-activation-2-bit-kv-residual-scale-validation-ae62d07bf8`
Run ID: `real-activation-2-bit-kv-residual-scale-validation-ae62d07bf8-20260621T030757583454+0000`

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

- Parent run decision: 2-bit KV Cache with Channel-Wise Residual Scale Factors: enoch://control-plane/projects/2-bit-kv-cache-with-channel-wise-residual-scale-factors-51d100d45729/runs/2-bit-kv-cache-with-channel-wise-residual-scale-factors-51d100d45729-20260621T024922030928+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bc4ce748255b

## What looked useful

Residual-derived 2-bit KV scaling produced a stable direct mechanism signal: residual/static attention-output NMSE ratio averaged 0.3488 over three seed splits, residual/oracle ratio averaged 0.8980, and residual key-scale relative MAE averaged 0.1474.

## Boundaries and scale limits

Small model, embedded short-text corpus, max length 64, no end-to-end perplexity/logit/task metric, no long-context decode replay, no 7B-class model, no production throughput measurement, and no comparison to stronger learned scale predictors or published KV quantization systems.

## Claim scope

In a Tier 1 direct small-model test on distilgpt2 real natural-language activations, residual-stream RMS with calibrated coefficients selected 2-bit KV scales that beat static calibration on causal attention-output NMSE across three seed splits and stayed within 1.5x of the absmax oracle reconstruction-scale reference.

## Why it stopped

Tier 1 direct validation produced a useful mechanism signal, but the evidence is small-model and not publication-grade.

## Recommended next action

Run a bounded deepen follow-up on a stronger causal LM and held-out corpus with logit KL/perplexity and long-context decode replay metrics before considering paper escalation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium-model residual-scale 2-bit KV validation with logit and perplexity metrics
- Success threshold: Residual-derived 2-bit KV scaling must beat static calibration on logit KL or cross-entropy delta in all seed splits, remain within 1.5x of oracle attention-output NMSE, and show no catastrophic layer/head outliers.
- Stop condition: Stop if residual-derived scaling fails to beat static calibration on logit KL or cross-entropy in two or more seed splits, or if long-context replay shows unstable error growth.

## Evidence references

- Artifact root: `<local-path>/projects/real-activation-2-bit-kv-residual-scale-validation-ae62d07bf8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
