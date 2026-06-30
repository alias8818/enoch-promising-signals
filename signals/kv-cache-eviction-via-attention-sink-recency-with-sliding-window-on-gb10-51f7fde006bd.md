# KV-cache eviction via attention-sink + recency with sliding window on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-eviction-via-attention-sink-recency-with-sliding-window-on-gb10-51f7fde006bd`
Run ID: `kv-cache-eviction-via-attention-sink-recency-with-sliding-window-on-gb10-51f7fde006bd-20260628T192607818839+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b7567edcb0a4

## What looked useful

In the constrained 4096-token synthetic run with budget 128 and sink_mass 0.35, sink+recency increased retained attention mass by 0.018978 and reduced sink-local output MSE to 25.7% of recency-only MSE. In mid-retrieval scenarios, MSE remained effectively unchanged versus recency-only, showing the policy's expected failure mode.

## Boundaries and scale limits

No real language model perplexity, downstream task accuracy, multi-layer/multi-head serving stack, batching, quantized KV cache, paged attention, or long-context retrieval benchmark was tested. Sequence length was 4096, hidden dimension 256, single-process PyTorch CUDA, synthetic attention distributions only.

## Claim scope

On synthetic autoregressive attention distributions run on GB10, a fixed-budget cache that preserves a small sink prefix plus recent tokens approximates full attention better than recency-only when attention mass is actually sink-plus-local; it provides little benefit when the recency window already captures the mass and does not recover non-sink mid-context retrieval.

## Why it stopped

No-paper useful signal: the mechanism is supported only in synthetic attention and the direct real-model evidence required for a paper was not produced in this run.

## Recommended next action

Run a bounded real-model follow-up using a small decoder model and real text to compare recency-only, sink+recency, and heavy-hitter KV eviction on perplexity plus retained per-head attention mass.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model validation of sink-plus-recency KV eviction
- Success threshold: At the same KV budget, sink+recency must reduce perplexity or loss versus recency-only by at least 2% relative on two real-text evaluations while preserving at least 95% of full-cache decode quality and showing attention-mass diagnostics consistent with sink retention.
- Stop condition: Stop if sink+recency fails to beat recency-only by 2% relative on real-model loss/perplexity, or if retained attention diagnostics show no meaningful sink mass in the tested model/layers.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-eviction-via-attention-sink-recency-with-sliding-window-on-gb10-51f7fde006bd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
