# 2-bit KV-cache with per-head residual channel for long context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-kv-cache-with-per-head-residual-channel-for-long-context-f5a35fddd84c`
Run ID: `2-bit-kv-cache-with-per-head-residual-channel-for-long-context-f5a35fddd84c-20260619T163352218318+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ebfb3f457883

## What looked useful

At T=8192, energy-selected residual channels reduced normalized output MSE by 63.6% for fixed outliers and 72.3% for late fixed outliers, while random residuals were near zero. Benefit was only 8.9% on Gaussian tensors and 14.2% on drifting outliers. Memory reduction versus fp16 remains about 83.0% including fp16 min/max scales.

## Boundaries and scale limits

No real transformer KV traces, no perplexity or task metrics, no serving kernel, no latency measurement, no layer-wise calibration, and no validation beyond 8192-token synthetic tensors with 8 heads and head dimension 64.

## Claim scope

Synthetic attention probe shows that preserving one high-energy K channel and one high-energy V channel per head can reduce 2-bit KV quantization attention-output distortion when heads contain stable or late high-impact outlier channels.

## Why it stopped

Synthetic proxy produced useful but mixed mechanism evidence; it is not full validation of long-context model quality or serving performance.

## Recommended next action

Run a bounded direct-evidence follow-up on real transformer KV traces with layer/head residual selection and perplexity or long-context retrieval metrics; do not claim paper-ready validation from this synthetic probe.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-KV trace validation for 2-bit cache residual channels
- Success threshold: Energy-selected residual channels improve the primary model-level metric by at least 25% of the gap between plain 2-bit and fp16 KV while retaining at least 80% KV memory reduction versus fp16 and outperforming random residual selection.
- Stop condition: Stop if residual selection is not consistently better than random residuals, if the model-level metric gain is below 10% of the 2-bit-to-fp16 gap, or if residual overhead reduces compression below 80% versus fp16.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-per-head-residual-channel-for-long-context-f5a35fddd84c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
