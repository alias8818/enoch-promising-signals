# Layerwise Adaptive 4-Bit Group Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layerwise-adaptive-4-bit-group-quantization-8106df0d8a5f`
Run ID: `layerwise-adaptive-4-bit-group-quantization-8106df0d8a5f-20260527T195913368085+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/80d69c8860f5

## What looked useful

Per-tensor reconstruction MSE is not a sufficient objective for adaptive 4-bit group-size assignment in this setup: adaptive MSE selection reduced weighted MSE from 0.0003424 to 0.0003309 while using 97.9% of the uniform-g128 scale groups, but held-out loss was slightly worse than uniform g128. A calibration-loss chooser was better than MSE adaptation in the 256-window confirmation run but still did not beat uniform g128.

## Boundaries and scale limits

Single small pretrained model, WikiText-2 fixed-window evaluation, fake quantized fp16 weights rather than packed int4 kernels, no downstream task suite, no 7B-class model, and no joint/Hessian-aware assignment search.

## Claim scope

On distilgpt2 non-embedding matrix weights with fake symmetric int4 quantization and WikiText-2 held-out windows, layer/tensor-level adaptive group-size selection under a uniform-g128 scale-count budget did not improve language-model loss over uniform g128, even though MSE-based adaptation slightly reduced weighted reconstruction MSE.

## Why it stopped

Bounded local evidence failed the target LM-loss success criterion for layerwise adaptive group-size selection at the same metadata budget; this is an early scoped negative/useful-signal result, not a full validation of all adaptive quantization methods.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should test joint activation/Hessian-aware group-size assignment on GPT-2-small-class and OPT-125M-class models before considering scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-Aware Joint Group-Size Assignment for 4-Bit Quantization
- Success threshold: Adaptive assignment must reduce held-out loss versus uniform g128 by at least 0.02 loss on both tested models while using no more scale groups than uniform g128, and must not rely on doubled metadata like uniform g64.
- Stop condition: Stop if the activation/Hessian-aware adaptive policy fails to beat uniform g128 on either model or if the improvement disappears when calibration and evaluation windows are disjoint.

## Evidence references

- Artifact root: `<local-path>/projects/layerwise-adaptive-4-bit-group-quantization-8106df0d8a5f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
