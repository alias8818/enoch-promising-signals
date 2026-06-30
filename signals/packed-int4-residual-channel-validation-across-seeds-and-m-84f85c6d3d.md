# Packed INT4 Residual-Channel Validation Across Seeds and Models

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `packed-int4-residual-channel-validation-across-seeds-and-m-84f85c6d3d`
Run ID: `packed-int4-residual-channel-validation-across-seeds-and-m-84f85c6d3d-20260605T220335951521+0000`

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

- Parent run decision: Extreme INT4 Quantization with Principled Residual Channels: enoch://control-plane/projects/extreme-int4-quantization-with-principled-residual-channels-5fe8780180e7/runs/extreme-int4-quantization-with-principled-residual-channels-5fe8780180e7-20260605T210208292221+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/87c976834bf7

## What looked useful

Selected sparse residual channels beat plain packed INT4 on NLL and logit RMSE in 6/6 model-seed runs and beat same-budget random residual channels in 6/6 runs; mean selected-minus-plain NLL delta was -6.3530 and mean selected-minus-plain logit RMSE delta was -3.0472.

## Boundaries and scale limits

Built-in small synthetic text corpus, sequence length 128, 8 calibration and 8 eval windows per model-seed, GPT-2-family checkpoints only, correctness-oriented packed INT4 dequantization rather than optimized kernels, no serving throughput or large-model validation.

## Claim scope

Small direct validation on distilgpt2 and gpt2 across three seeds each: activation/error-selected 1.56% residual input channels in packed INT4 weight-only projections reduced held-out NLL and logit RMSE versus plain packed INT4 and same-budget random residual channels.

## Why it stopped

Tier 1 controlled small direct test completed and produced a useful mechanism signal, but the evidence is too narrow for paper-positive closure.

## Recommended next action

Run a bounded deepen test on a standard held-out corpus such as WikiText-2 or WikiText-103 validation with at least three checkpoint families and include plain INT4, random residual, error-only residual, and activation/error residual controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Standard-Corpus Residual-Channel Packed INT4 Validation
- Success threshold: Activation/error residual beats plain INT4 and same-budget random residual on NLL and logit RMSE in at least 80% of model-seed cases, with negative mean deltas for both metrics and no model family showing consistent regression.
- Stop condition: Stop if selected residual fails to beat random residual on either NLL or logit RMSE in more than 40% of cases, or if improvement only appears on one checkpoint family.

## Evidence references

- Artifact root: `<local-path>/projects/packed-int4-residual-channel-validation-across-seeds-and-m-84f85c6d3d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
