# 1.58-bit Ternary Weights with Importance-Scored FP8 Residual Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-58-bit-ternary-weights-with-importance-scored-fp8-residual-channels-3baff9829456`
Run ID: `1-58-bit-ternary-weights-with-importance-scored-fp8-residual-channels-3baff9829456-20260609T063542770329+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/58d8e0541c11

## What looked useful

Across 72 synthetic cases, activation-scored residual channels reduced relative output MSE by 18.94% on average versus pure ternary and beat random selection in every case. Across 48 GPT-2-small layer/budget cases, activation scoring reduced MSE by 51.17% on average and beat random and row-norm controls in every case, but benefits varied by layer and were weak for diffuse normal synthetic weights.

## Boundaries and scale limits

Tested only short synthetic probes and GPT-2-small layer-output reconstruction with captured activations; no perplexity, finetuning, packed-kernel benchmark, larger model, or datacenter-scale validation was run.

## Claim scope

Activation-scored FP8 residual output channels reduce dense-linear output reconstruction error after 1.58-bit ternary quantization on synthetic linear layers and sampled GPT-2-small projection layers; the strongest observed signal is layer-local output MSE reduction, not end-to-end model quality or throughput.

## Why it stopped

Bounded local evidence supports the layer reconstruction mechanism, but this is not full validation because end-to-end perplexity, training stability, packed storage, and kernel throughput were not tested.

## Recommended next action

Run a bounded GPT-2-small perplexity evaluation with layerwise activation-scored residual budgets and compare against pure ternary plus a same-bit mixed-precision baseline; stop this run because current evidence is layer-local and not paper-ready.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small perplexity test for activation-scored FP8 residual ternary weights
- Success threshold: At the same estimated bit budget, activation-scored residual channels reduce perplexity degradation by at least 25% relative to pure ternary and outperform random residual-channel selection on every tested seed or calibration split.
- Stop condition: Stop if activation-scored residual channels fail to beat random residual selection or a same-bit mixed-precision baseline on validation perplexity.

## Evidence references

- Artifact root: `<local-path>/projects/1-58-bit-ternary-weights-with-importance-scored-fp8-residual-channels-3baff9829456`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
