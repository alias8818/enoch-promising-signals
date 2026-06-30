# Outlier-Aware INT8 KV Cache with FP16 Outlier Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `outlier-aware-int8-kv-cache-with-fp16-outlier-channels-78508ff7a2b4`
Run ID: `outlier-aware-int8-kv-cache-with-fp16-outlier-channels-78508ff7a2b4-20260613T232251962974+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e0f0c362574a

## What looked useful

On synthetic heavy-tail KV cases, hybrid INT8+FP16-outlier storage reduced relative L2 attention-output error by a mean 60.53% versus plain INT8 at a mean 57.28% of FP16 KV storage. On no-outlier controls, mean error reduction was only 3.89%, showing the method needs real outlier structure or a gating criterion.

## Boundaries and scale limits

No GPU, fused kernel, real model KV trace, perplexity, long-context serving, or production decode throughput evidence. CPU latency is not favorable in this unfused NumPy implementation.

## Claim scope

CPU NumPy synthetic attention proxy: preserving detected high-energy KV channels in FP16 can substantially reduce attention-output error versus per-channel INT8 when the KV distribution has true heavy-tail outlier channels, while retaining roughly 43% storage savings versus full FP16 KV.

## Why it stopped

No-paper closure: this is a CPU synthetic proxy that supports the error-reduction mechanism under heavy-tail channels but does not validate real-model quality or GPU serving performance.

## Recommended next action

Run a bounded real-model trace replay: capture K/V activations from a small transformer, compare FP16, INT8, and hybrid caches on attention error and downstream logits/perplexity, and only then consider a fused GPU decode prototype.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV trace replay for INT8 cache with FP16 outlier channels
- Success threshold: Hybrid cache reduces attention-output or logit relative error by at least 30% versus plain INT8 at no more than 65% of FP16 KV storage, with perplexity degradation no worse than plain INT8.
- Stop condition: Stop if real-model KV traces do not show repeatable outlier-channel structure, if hybrid error is within 10% of plain INT8, or if perplexity/logit degradation is worse than plain INT8 at comparable storage.

## Evidence references

- Artifact root: `<local-path>/projects/outlier-aware-int8-kv-cache-with-fp16-outlier-channels-78508ff7a2b4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
