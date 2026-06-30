# Progressive Channel-wise Quantization with Perplexity-Gated Residuals

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `progressive-channel-wise-quantization-with-perplexity-gated-residuals-928cc75eff01`
Run ID: `progressive-channel-wise-quantization-with-perplexity-gated-residuals-928cc75eff01-20260529T224641036119+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/bb72ed072c12

## What looked useful

Progressive 2/4/8-bit channel allocation reached NLL 2.29833 and PPL 9.95758 versus full precision NLL 2.29408 and PPL 9.91531, with 7.88x output-weight compression. It beat uniform 4-bit NLL 2.30032 at a similar average bit rate. Entropy-gated residuals recovered 5.0% of quantization NLL loss at 10% activation, 36.1% at 25%, 88.7% at 50%, and 100% at full activation.

## Boundaries and scale limits

Single seed, toy character-level one-hidden-layer LM; only output softmax weights were quantized; no transformer blocks, subword benchmark, hardware latency, memory-traffic measurement, or multi-model robustness test.

## Claim scope

On a NumPy character-level Tiny Shakespeare language model, validation-sensitivity-ranked progressive per-output-channel quantization slightly outperformed uniform 4-bit quantization at similar average bit rate, and entropy-gated residual correction recovered most of the quantization NLL penalty only when activated on about half of test tokens.

## Why it stopped

No-paper closure: bounded toy-LM evidence is useful but mixed, because sparse residual gating at 5-10% activation did not recover meaningful loss and the experiment does not directly validate transformer-scale behavior.

## Recommended next action

Run a bounded small-transformer follow-up that quantizes attention and MLP output channels, measures perplexity and latency at matched storage, and treats the current toy result as a mechanism screen rather than validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer validation of entropy-gated residual quantization
- Success threshold: At matched storage, progressive quantization plus <=25% entropy-gated residual activation recovers at least 50% of the uniform int4 perplexity penalty without reducing token throughput by more than 15% versus ungated progressive quantization.
- Stop condition: Stop if <=25% residual activation recovers less than 25% of the int4 perplexity penalty or if residual overhead eliminates any practical compression/throughput advantage.

## Evidence references

- Artifact root: `<local-path>/projects/progressive-channel-wise-quantization-with-perplexity-gated-residuals-928cc75eff01`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
