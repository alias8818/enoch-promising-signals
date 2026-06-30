# 8-bit AdamW Blockwise for Sub-100M Models

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `8-bit-adamw-blockwise-for-sub-100m-models-38d163321912`
Run ID: `8-bit-adamw-blockwise-for-sub-100m-models-38d163321912-20260621T110702205274+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/e2df2029c8a7

## What looked useful

Blockwise 8-bit moment state appears mechanically viable for sub-100M GPU training in bounded probes, with large optimizer-state savings and no observed short-run convergence penalty; it is not paper-ready without real-corpus, longer-horizon validation.

## Boundaries and scale limits

Synthetic Markov-token data only; 100-200 training steps; models far below 100M parameters; no real-corpus pretraining, long-horizon stability, downstream evaluation, mixed-precision production setup, or fused optimizer kernel validation.

## Claim scope

On two short synthetic causal language-modeling probes at 1.81M and 10.71M parameters on NVIDIA GB10, a local blockwise uint8 AdamW moment-state implementation reduced optimizer-state bytes to about 25.4-25.6% of AdamW while matching short-run eval loss within +0.00069 on the 3-seed small probe and -0.01244 on the larger single-seed probe.

## Why it stopped

Closed as a no-paper useful signal: local synthetic GPU evidence supports the mechanism, but the result is proxy-only and too short for publication-grade validation.

## Recommended next action

Run a bounded real-corpus deepen test on a 10M-50M parameter transformer for matched-token validation loss/perplexity against AdamW before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus sub-100M validation for blockwise 8-bit AdamW
- Success threshold: At matched tokens, 8-bit AdamW final validation perplexity is within 1% of AdamW while optimizer-state bytes are at least 70% lower and throughput is no worse than 25% slower.
- Stop condition: Stop if 8-bit AdamW exceeds AdamW validation perplexity by more than 3% after warmup on two matched checkpoints, diverges, or fails to deliver at least 60% optimizer-state memory reduction.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adamw-blockwise-for-sub-100m-models-38d163321912`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
