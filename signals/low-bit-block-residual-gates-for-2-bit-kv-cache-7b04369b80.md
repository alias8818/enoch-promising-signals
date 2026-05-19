# Low-bit block residual gates for 2-bit KV cache

Status: `useful_signal`
Project ID: `low-bit-block-residual-gates-for-2-bit-kv-cache-7b04369b80`
Run ID: `low-bit-block-residual-gates-for-2-bit-kv-cache-7b04369b80-20260519T155907238606+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b8ef7195f471

## What looked useful

Block residual gates almost eliminated attention-output error when 2-bit KV quantization damage was localized to token blocks, but failed the predefined threshold on Gaussian and distributed Laplace regimes. The mechanism is useful only as a localized-error signal, not as broad validation.

## Boundaries and scale limits

Synthetic K/V distributions only; no real transformer activations, no low-bit residual encoding, no fused decode kernel, no throughput measurement, no perplexity or generation-quality evaluation, and no 7B-scale validation.

## Claim scope

Controlled NumPy attention/KV-cache test with synthetic K/V regimes, 8 heads, sequence length 256, head dimension 64, 2-bit blockwise quantization, and 12.5% exact residual block gates selected from calibration queries.

## Why it stopped

Tier 1 controlled direct test produced mixed evidence: strong support for block-localized errors, but the predefined success threshold was met in only 1 of 3 regimes and all K/V tensors were synthetic.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is to repeat the same gate/control protocol on real GPT-2-small or TinyLlama KV activation traces and require the 12.5% gate budget to reduce held-out attention-output MSE by at least 25% in a majority of layers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-LM KV trace test for 2-bit residual block gates
- Success threshold: At 12.5% gated head-blocks, calibration residual gates achieve mean held-out relative MSE <= 0.75 and beat random gates in at least two thirds of evaluated layers, with a plausible residual encoding overhead no worse than 2.0x over pure 2-bit KV.
- Stop condition: Stop negative if real KV traces show calibration gate relative MSE > 0.85 or fail to beat random gates in a majority of evaluated layers.

## Evidence references

- Artifact root: `<local-path>/projects/low-bit-block-residual-gates-for-2-bit-kv-cache-7b04369b80`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
