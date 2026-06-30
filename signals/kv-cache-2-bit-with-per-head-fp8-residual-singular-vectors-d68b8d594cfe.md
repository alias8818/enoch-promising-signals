# KV-Cache 2-bit with Per-Head FP8 Residual Singular Vectors

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-2-bit-with-per-head-fp8-residual-singular-vectors-d68b8d594cfe`
Run ID: `kv-cache-2-bit-with-per-head-fp8-residual-singular-vectors-d68b8d594cfe-20260629T162000768939+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/10d46b4777d6

## What looked useful

Rank-8 residuals improved aggregate attention relative MSE from 3.94 to 0.165 at about 3.52 estimated bits/element, but plain 4-bit reached 0.071 at 4.0 bits/element. Rank-16 matched 4-bit-like aggregate attention error only after rising to about 5.03 bits/element. V reconstruction dominated the remaining failure mode.

## Boundaries and scale limits

Single small GPT-2-family model, 8 text prompts, reconstruction and isolated attention-output metrics only; no end-to-end perplexity, generation-quality, decoding-throughput, or larger-model validation.

## Claim scope

On distilgpt2 activations with 8 prompts at sequence length 128, per-head affine 2-bit KV quantization plus FP8 low-rank residual SVD factors substantially reduces reconstruction and causal attention-output error versus plain 2-bit, but does not beat a plain 4-bit KV baseline at equal-or-lower estimated storage.

## Why it stopped

No-paper useful signal: the bounded direct activation probe supports the residual mechanism but shows the FP8 SVD factor overhead erases the nominal 2-bit advantage against a simple 4-bit baseline.

## Recommended next action

Stop paper path for this variant; run a bounded deepen follow-up that compares against per-token/per-channel 2-bit and 4-bit KV quantization with end-to-end perplexity before considering any larger validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end KV quantization comparison with stronger per-token baselines
- Success threshold: At equal-or-lower effective bits per element than 4-bit KV, the residual 2-bit method must match or improve next-token loss/perplexity while keeping attention-output relative MSE no worse than the 4-bit baseline.
- Stop condition: Stop if the residual method needs more than 4 effective bits per element to match 4-bit perplexity/attention error, or if V reconstruction remains more than 25% worse than 4-bit at equal storage.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-2-bit-with-per-head-fp8-residual-singular-vectors-d68b8d594cfe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
