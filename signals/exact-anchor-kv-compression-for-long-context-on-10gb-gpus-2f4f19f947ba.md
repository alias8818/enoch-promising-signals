# Exact-Anchor KV Compression for Long Context on 10GB GPUs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-compression-for-long-context-on-10gb-gpus-2f4f19f947ba`
Run ID: `exact-anchor-kv-compression-for-long-context-on-10gb-gpus-2f4f19f947ba-20260523T183705027569+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/613e7ca7ee3d

## What looked useful

Exact-anchor retention produced low anchor-query output error at 4096/8192/16384 tokens (0.029/0.066/0.109 mean relative error) while uniform pooling at similar KV size produced high error (0.867/0.939/0.974). The same policy failed for non-anchor old-token retrieval, with about 1.0 relative error, showing the mechanism is useful only when important old tokens are correctly anchored.

## Boundaries and scale limits

No real LLM inference, no learned or task-derived anchor selection, no generation-quality evaluation, no latency benchmark, and no actual 10GB full-model serving measurement. KV memory is estimated from retained entry counts using a 7B-style fp16 KV layout.

## Claim scope

Synthetic CUDA attention probe up to 16384 tokens: exact retention of stride-512 anchor KV entries plus a 512-token local window and pooled non-anchor KV preserves anchor-targeted attention outputs much better than budget-matched uniform pooling or recent-only controls.

## Why it stopped

No-paper useful signal: the result is a synthetic/proxy mechanism confirmation with an explicit failure mode, not a full validation of long-context inference on 10GB GPUs.

## Recommended next action

Run a bounded real-decoder follow-up with a small transformer and deterministic anchor positions on a long-context retrieval task, comparing full KV, recent-only, uniform pooling, and exact-anchor compression on accuracy, logit KL, latency, and actual GPU memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Decoder Exact-Anchor KV Compression on Long-Context Retrieval
- Success threshold: At a cache budget below 25% of full KV, exact-anchor compression retains at least 90% of full-KV retrieval accuracy and beats both recent-only and uniform-pooling controls by at least 20 percentage points absolute, without increasing latency by more than 25% versus the strongest compressed baseline.
- Stop condition: Stop if exact-anchor compression loses more than 20 percentage points of retrieval accuracy versus full KV or fails to outperform budget-matched controls on two independent prompt seeds.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-for-long-context-on-10gb-gpus-2f4f19f947ba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
