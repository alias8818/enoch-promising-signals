# Extreme INT4 Quantization with Principled Residual Channel Preservation in Feed-Forward Layers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `extreme-int4-quantization-with-principled-residual-channel-preservation-in-feed-forward-layers-ddf368569742`
Run ID: `extreme-int4-quantization-with-principled-residual-channel-preservation-in-feed-forward-layers-ddf368569742-20260605T175255143897+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e4ac61a90de1

## What looked useful

Quantization-error proxy selection won 12 of 16 non-oracle synthetic case/budget comparisons and 8 of 12 GPT-2-small layer/budget comparisons. It averaged 22.5% synthetic and 27.2% GPT-2 MLP relative-output-MSE improvement over unpreserved INT4, close to the 22.6% synthetic oracle proxy average.

## Boundaries and scale limits

No end-to-end perplexity, task accuracy, full-corpus calibration, multi-model validation, deployable INT4 kernel, or latency/memory-bandwidth measurement was run. GPT-2 evidence used three MLP layers and eight local prompts only.

## Claim scope

A small high-precision residual set selected by activation-aware and quantization-error-aware channel scores reduces INT4 feed-forward layer output reconstruction error in synthetic FFN probes and GPT-2-small MLP layer probes.

## Why it stopped

Closed as no-paper useful signal: the local evidence supports the FFN reconstruction mechanism but lacks direct end-to-end model-quality and systems evidence required for a paper.

## Recommended next action

Run a bounded real-model follow-up on all GPT-2-small MLP layers with WikiText or C4 calibration/evaluation, reporting both layer-output MSE and perplexity against matched random, activation-only, and downstream-weight-only controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: All-layer GPT-2 INT4 residual-channel preservation with perplexity validation
- Success threshold: At 1-5% preserved FFN channels, quantization-error proxy reduces INT4 perplexity degradation by at least 20% versus unpreserved INT4 and beats activation-only and random controls in most layers or budgets.
- Stop condition: Stop if quantization-error proxy fails to improve perplexity degradation by at least 10% versus activation-only at any tested budget or if layer-output MSE gains do not translate into perplexity gains.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-int4-quantization-with-principled-residual-channel-preservation-in-feed-forward-layers-d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
