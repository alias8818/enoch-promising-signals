# Tiered Exact-Anchor KV Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiered-exact-anchor-kv-compression-97529bdf3095`
Run ID: `tiered-exact-anchor-kv-compression-97529bdf3095-20260523T143406479403+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f4aa93715e73

## What looked useful

Exact-anchor interpolation fails badly on iid and moderate-change KV traces and trails 4-bit quantization by 4.4x to 24.9x relative attention-output L2 at 12.5% memory. It only barely matches 4-bit quantization on an artificially very-smooth trace while using 25% memory, where 8-bit quantization at the same memory is still 22.7x lower error.

## Boundaries and scale limits

No trained transformer was run; KV traces were synthetic, single-layer style arrays with 2048 tokens, 64 dimensions, 256 queries, 3 seeds, and CPU-only NumPy evaluation. End-to-end perplexity, decode latency, multi-head/layer behavior, and real KV distributions remain untested.

## Claim scope

On synthetic autoregressive KV traces with direct attention-output evaluation, standalone tiered exact-anchor reconstruction is measurable on very smooth traces but is not competitive with simple uniform KV quantization at matched or lower FP32-equivalent memory.

## Why it stopped

Moderate synthetic attention-output evidence is an early proxy falsification of standalone tiered exact-anchor KV compression, not a full model-serving validation.

## Recommended next action

Stop this standalone exact-anchor line as no-paper evidence; only revisit via a bounded real-KV follow-up that adds residual quantization or learned reconstruction and beats 4-bit/8-bit KV quantization at matched memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-KV residual exact-anchor compression versus quantized KV baselines
- Success threshold: At 12.5% to 25% FP32-equivalent memory, residual exact-anchor compression must reduce mean attention-output error or perplexity degradation by at least 20% versus 4-bit KV quantization on real KV traces across most layers/heads.
- Stop condition: Stop if real KV traces show the same pattern as this run: anchor reconstruction or residual-anchor variants fail to beat 4-bit quantization at matched memory in mean attention-output error.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-exact-anchor-kv-compression-97529bdf3095`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
