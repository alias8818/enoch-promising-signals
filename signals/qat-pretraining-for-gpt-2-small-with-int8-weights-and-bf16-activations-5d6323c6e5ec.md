# QAT Pretraining for GPT-2-Small with INT8 Weights and BF16 Activations

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `qat-pretraining-for-gpt-2-small-with-int8-weights-and-bf16-activations-5d6323c6e5ec`
Run ID: `qat-pretraining-for-gpt-2-small-with-int8-weights-and-bf16-activations-5d6323c6e5ec-20260607T235527457806+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e3a7643c1d8a

## What looked useful

QAT replaced 48 GPT-2-small projection modules, trained without NaNs, and reduced loss from about 8.01 to 0.2545 over 200 measured steps. The BF16 baseline reached 0.1007 final loss under the same settings. QAT throughput was 1,445.5 tokens/s versus 1,742.7 tokens/s baseline, about 0.829x.

## Boundaries and scale limits

This was not full GPT-2-small pretraining: corpus was a repeated public-domain excerpt, no held-out validation perplexity was measured, only one seed was run, embeddings and the tied LM head were not quantized, and fake quantization did not use real packed INT8 kernels.

## Claim scope

A bounded CUDA probe of GPT-2-small architecture training from scratch showed that straight-through fake INT8 quantization of attention and MLP projection weights with BF16 activations is numerically stable for 200 measured steps on a repeated-text objective, but it did not outperform the BF16 baseline.

## Why it stopped

No-paper closure: this proxy/medium local probe supports stability but not a publication-grade claim, and QAT ended with worse overfit loss and slower training than the BF16 baseline.

## Recommended next action

Run a bounded real-corpus follow-up with held-out validation perplexity, 3 seeds, delayed-QAT and always-QAT variants, and actual INT8 inference export metrics before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus GPT-2-small INT8-weight QAT validation with held-out perplexity
- Success threshold: QAT validation perplexity within 2 percent of BF16 baseline at matched sequence-item budget, no divergence across seeds, and exported INT8 inference showing a concrete memory or latency benefit.
- Stop condition: Stop if QAT diverges in 2 or more seeds, validation perplexity remains more than 5 percent worse than BF16 after basic LR/delayed-QAT tuning, or exported INT8 inference provides no measurable deployment benefit.

## Evidence references

- Artifact root: `<local-path>/projects/qat-pretraining-for-gpt-2-small-with-int8-weights-and-bf16-activations-5d6323c6e5ec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
