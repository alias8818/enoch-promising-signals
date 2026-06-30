# 4-bit KV-cache with attention-sink preservation for 2x effective context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-kv-cache-with-attention-sink-preservation-for-2x-effective-context-7908d23f0ee6`
Run ID: `4-bit-kv-cache-with-attention-sink-preservation-for-2x-effective-context-7908d23f0ee6-20260620T205334737756+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fffce6da15c8

## What looked useful

The memory-quality premise for int4 KV is useful: full-context int4 had mean NLL delta +0.018 vs full FP16 while half-context FP16 truncation had +6.171. The sink-preservation add-on was not supported: 4, 16, and 32 preserved sink tokens gave slightly worse paired NLL than all-token int4 with only tiny inconclusive KL changes.

## Boundaries and scale limits

Single GPT-2-small-class model, 1024-token native context, next-token loss only, fake dequantized int4 tensors rather than packed kernels, no real >1024 long-context serving, no retrieval or passkey task, and no diagnosed sink-head selection.

## Claim scope

On 64 WikiText-2 GPT-2 samples at native 1024-token context, fake int4 full-context KV cache preserved next-token behavior much better than half-context FP16 truncation, but preserving first-token attention sinks in FP16 did not improve mean NLL over all-token int4.

## Why it stopped

Proxy evidence supports 4-bit KV compression but early falsifies the specific attention-sink preservation benefit in this GPT-2 setting; this is not a full validation and not paper-ready.

## Recommended next action

Run a bounded deepen test on a small native long-context model with attention-head diagnostics, real retrieval-beyond-window examples, and per-head/per-layer sink preservation before spending effort on packed int4 kernels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Diagnosed sink-head preservation on a native long-context small model
- Success threshold: Sink-preserved int4 must improve paired mean NLL or task accuracy over all-token int4 with a 95% confidence interval excluding zero while retaining the full-context advantage over half-context FP16 truncation.
- Stop condition: Stop if diagnosed sink preservation fails to beat all-token int4 on paired NLL/task accuracy or if memory overhead exceeds the 2x-context KV budget.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-kv-cache-with-attention-sink-preservation-for-2x-effective-context-7908d23f0ee6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
