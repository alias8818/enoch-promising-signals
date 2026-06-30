# 1.58-bit KV cache with residual summary vectors

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-58-bit-kv-cache-with-residual-summary-vectors-5ecd285b237f`
Run ID: `1-58-bit-kv-cache-with-residual-summary-vectors-5ecd285b237f-20260522T112506015784+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4286aa1c5b71

## What looked useful

Residual summary vectors strongly improve pure ternary KV only when quantization residuals are locally correlated: AR(1) median rel-MSE ratio was 0.0336 versus ternary, but Gaussian and sparse-outlier controls were 0.9142 and 0.9405. This supports the mechanism conditionally and falsifies a broad synthetic claim that block-mean residual summaries generally recover ternary KV quality.

## Boundaries and scale limits

No real language-model KV traces, perplexity, downstream quality, packed-cache kernel, decode throughput, or long-context serving benchmark was run. Storage accounting is approximate and includes fp16 scale and summary overhead, so the tested implementation exceeds a strict 1.58-bit-per-element budget.

## Claim scope

Synthetic CUDA attention-fidelity probe for ternary KV quantization plus block-mean residual key/value summaries at sequence lengths 512-2048, block sizes 8-64, and Gaussian, AR(1), and sparse-outlier activation regimes.

## Why it stopped

Proxy-only synthetic evidence is mixed: the mechanism works for locally correlated residuals but barely helps independent Gaussian or sparse outlier controls, so this is useful no-paper evidence rather than publication-grade validation.

## Recommended next action

Run a bounded real-model GPT-2-small-class KV trace or perplexity test before any packing or kernel work; stop if block-mean residual summaries fail to reduce output/logit KL by at least 25% over ternary KV at no more than 3 effective bits per element.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV trace test for ternary cache residual summaries
- Success threshold: At block sizes with estimated total storage at or below 3 bits per element, residual summaries reduce median output/logit KL by at least 25% versus pure ternary KV without increasing perplexity beyond an agreed small-model tolerance.
- Stop condition: Stop after the real-model trace if residual summaries improve KL by less than 10% at all block sizes under 3 effective bits per element, or if storage overhead required for improvement exceeds the target budget.

## Evidence references

- Artifact root: `<local-path>/projects/1-58-bit-kv-cache-with-residual-summary-vectors-5ecd285b237f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
