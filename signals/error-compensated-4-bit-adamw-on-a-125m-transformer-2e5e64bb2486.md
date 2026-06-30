# Error-Compensated 4-bit AdamW on a 125M Transformer

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `error-compensated-4-bit-adamw-on-a-125m-transformer-2e5e64bb2486`
Run ID: `error-compensated-4-bit-adamw-on-a-125m-transformer-2e5e64bb2486-20260621T044102196121+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/41fa2e2055c3

## What looked useful

Naive tensorwise 4-bit moment quantization is numerically fragile; second-moment zeros caused NaNs until a positive-bin floor was added. Plain 4-bit moments reduced theoretical state to about 25% of AdamW but had 4-6x worse final loss. Full-precision residual error compensation used 2.25x AdamW state and diverged at both 3e-4 and 1e-4 learning rates.

## Boundaries and scale limits

Not tested at 125M parameters, on real text, with packed/fused kernels, across multiple seeds, or over long training horizons. The result is an early proxy falsification of this optimizer formulation, not a full-scale validation.

## Claim scope

On a 3.24M-parameter synthetic transformer proxy on GB10 CUDA, the tested tensorwise 4-bit AdamW variants did not match AdamW: plain 4-bit moments trained much worse, and full-residual error compensation diverged while using more optimizer state than AdamW.

## Why it stopped

Proxy/early falsification: the tested error-compensated 4-bit AdamW variant diverged or underperformed AdamW, and the full-residual implementation eliminated the memory-saving premise.

## Recommended next action

Stop this exact formulation; before any 125M run, test blockwise 4-bit moment quantization with bounded or compressed residuals on the same proxy and require AdamW-adjacent loss plus real state savings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blockwise bounded-residual 4-bit AdamW on the transformer proxy
- Success threshold: Across three seeds, mean tail loss within 20% of AdamW, no divergence, optimizer-state bytes below 60% of AdamW, and runtime no worse than 1.5x AdamW in the unfused prototype.
- Stop condition: Stop if any variant diverges in two of three seeds, exceeds AdamW optimizer-state bytes, or remains more than 2x AdamW tail loss after a small learning-rate sweep.

## Evidence references

- Artifact root: `<local-path>/projects/error-compensated-4-bit-adamw-on-a-125m-transformer-2e5e64bb2486`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
