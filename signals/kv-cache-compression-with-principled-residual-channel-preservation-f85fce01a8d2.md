# KV-Cache Compression with Principled Residual Channel Preservation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-compression-with-principled-residual-channel-preservation-f85fce01a8d2`
Run ID: `kv-cache-compression-with-principled-residual-channel-preservation-f85fce01a8d2-20260610T082632093553+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/016e72d87fd6

## What looked useful

Logit/joint sensitivity recovered query-amplified residual channels that variance missed and reduced 3-bit output MSE by 58.5% versus no preservation, but uniform 4-bit quantization had lower MSE than the 3-bit-plus-FP32-preserve scheme despite lower average bits under this accounting.

## Boundaries and scale limits

No real LLM KV traces, no perplexity/task metrics, no latency/kernel measurement, no multi-layer or long-context serving validation. Results are CPU-only NumPy synthetic evidence.

## Claim scope

Synthetic single-query attention probe with injected residual KV channels, per-channel scalar quantization, and exact FP32 preservation of 6.25% of channels. Sensitivity-based preservation improves error within a fixed 3-bit-plus-preserve family, but does not beat uniform 4-bit quantization in the tested regimes.

## Why it stopped

Synthetic mechanism evidence is mixed: channel sensitivity is useful for identifying fragile dimensions, but exact residual preservation failed the stronger practical compression test against uniform 4-bit controls. This is not full validation on real models.

## Recommended next action

Stop this run as a proxy early falsification of the broad same-budget compression claim; if continuing, run the bounded real-trace follow-up comparing residual preservation against uniform and mixed-precision quantization at matched bytes/token.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Matched-Budget KV Residual Preservation Probe
- Success threshold: Residual preservation must reduce next-token KL or perplexity delta by at least 10% versus the best matched-byte uniform or mixed-precision baseline while staying within 5% of its estimated decode bandwidth cost.
- Stop condition: Stop if matched-byte uniform or mixed-precision quantization is better on both quality and estimated bandwidth in two model/layer samples, or if sensitivity-selected channels are not stable across calibration and held-out prompts.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-with-principled-residual-channel-preservation-f85fce01a8d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
