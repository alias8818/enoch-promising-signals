# Real-model 32k residual-selector benchmark for 2-bit KV cache

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `real-model-32k-residual-selector-benchmark-for-2-bit-kv-ca-0b3922cc18`
Run ID: `real-model-32k-residual-selector-benchmark-for-2-bit-kv-ca-0b3922cc18-20260621T125431594725+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: 2-bit KV Cache with Principled Residual Stream for 32k Context: enoch://control-plane/projects/2-bit-kv-cache-with-principled-residual-stream-for-32k-context-1b3c39f49238/runs/2-bit-kv-cache-with-principled-residual-stream-for-32k-context-1b3c39f49238-20260621T113732149475+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2f909791b33b

## What looked useful

A direct 32k real-model benchmark found large target-NLL deltas and zero top-1 preservation across all selectors and residual budgets tested. At 1024 residual tokens random was best but still added 11.78 nats target NLL; at 4096 residual tokens recent was best but still added 3.32 nats; at 8192 residual tokens key-similarity was best but still added 9.31 nats. KV norm was consistently poor, and raw KV relative MSE did not predict logit preservation.

## Boundaries and scale limits

Single cached 0.6B real model, one deterministic repeated technical-text prompt family, one naive 2-bit quantizer, no true attention-hook selector, no multi-model or dataset robustness sweep.

## Claim scope

On Qwen/Qwen3-0.6B at 32768 tokens with a naive per-token/per-head 2-bit affine KV quantizer, the tested simple residual selectors (recent, random, KV norm, and key-similarity proxy) did not preserve next-token behavior.

## Why it stopped

Direct Tier 1 32k real-model tests falsified the practical threshold for the tested residual selectors: none preserved top-1 behavior and all produced large next-token NLL distortion.

## Recommended next action

Stop this branch as no-paper useful negative evidence; only reopen with a calibrated 2-bit KV quantizer and true attention/loss-aware residual selector that first passes this same 32k benchmark with top-1 preservation and target-NLL delta below 0.5 nats.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-model-32k-residual-selector-benchmark-for-2-bit-kv-ca-0b3922cc18`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
