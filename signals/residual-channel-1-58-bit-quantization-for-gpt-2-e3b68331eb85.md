# Residual-Channel 1.58-bit Quantization for GPT-2

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-1-58-bit-quantization-for-gpt-2-e3b68331eb85`
Run ID: `residual-channel-1-58-bit-quantization-for-gpt-2-e3b68331eb85-20260525T103441008432+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7766e9134d7c

## What looked useful

On 32k WikiText-2 validation tokens, baseline GPT-2-small perplexity was 31.61. Plain ternary PTQ gave 15,814.82 perplexity at 1.62 effective bits per quantized weight. The best residual-channel variant kept 5% of output channels in higher precision and improved perplexity to 6,096.83 at 2.33 effective bits, still 192.9x worse than baseline. Larger residual fractions of 10% and 20% did not improve further.

## Boundaries and scale limits

Direct evidence is limited to GPT-2-small, WikiText-2 validation subsets up to 32k tokens, inference-only post-training quantization, simple per-output-channel ternary scaling, and residual fractions up to 20%. It does not test quantization-aware fine-tuning, training from scratch, activation quantization, custom kernels, larger models, or full benchmark suites.

## Claim scope

Naive post-training residual-channel ternary quantization of GPT-2-small weights was tested on WikiText-2 validation subsets. Residual channels reduce perplexity collapse versus pure ternary PTQ, but the best measured configuration remains unusably far from the float baseline.

## Why it stopped

Moderate-strength direct GPT-2-small PTQ evidence shows a useful recovery mechanism but early-falsifies the naive residual-channel 1.58-bit quantization claim; the best residual result remains about 193x worse in perplexity than the float baseline and exceeds the nominal 1.58-bit budget when residual channels and scales are counted.

## Recommended next action

Stop this naive PTQ line as no-paper evidence; only pursue a bounded deepen follow-up if it uses quantization-aware fine-tuning or training-aware residual selection with an explicit success threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantization-aware residual-channel ternary fine-tuning for GPT-2-small
- Success threshold: At <=2.5 effective bits per quantized weight, residual-channel QAT should reduce validation perplexity by at least 5x versus pure ternary PTQ and reach within 2x of the float GPT-2-small baseline on the same validation slice.
- Stop condition: Stop if QAT residual-channel perplexity remains more than 5x worse than the float baseline after a bounded fine-tuning budget, or if storage accounting exceeds 2.5 effective bits per quantized weight.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-1-58-bit-quantization-for-gpt-2-e3b68331eb85`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
