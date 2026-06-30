# Cross-layer KV head clustering for long-context inference on 10GB

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cross-layer-kv-head-clustering-for-long-context-inference-on-10gb-36db4c04e5e5`
Run ID: `cross-layer-kv-head-clustering-for-long-context-inference-on-10gb-36db4c04e5e5-20260604T212300940696+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/33ebd991a77f

## What looked useful

At 50% KV reduction, distilgpt2 clustered attention output cosine was 0.451 mean with 1.88 relative L2; synthetic long-context timing was slower than baseline from 1024 to 4096 tokens despite modeled KV byte savings. Fidelity only approached 0.899 mean cosine at 8.3% KV reduction, still with a negative worst-head cosine.

## Boundaries and scale limits

Real-model evidence is limited to distilgpt2 at 256 tokens and last-token attention-output reconstruction. Timing evidence is a synthetic PyTorch attention proxy at sequence lengths up to 4096, not fused production serving or 7B+ end-to-end generation.

## Claim scope

Naive cross-layer/head KV cache centroid sharing, clustered by mean key/value trajectories and tested on distilgpt2 plus synthetic long-context GB10 decode-attention tensors, does not preserve attention outputs at useful compression ratios and does not improve the tested decode-attention proxy.

## Why it stopped

Proxy and small-model evidence provide an early falsification of the simple cross-layer KV-head clustering hypothesis, not a full validation of all possible learned or fused variants.

## Recommended next action

Stop this naive centroid-sharing path; the next bounded test should add a learned per-head correction or constrain clustering to heads with verified attention-output equivalence before any larger serving experiment.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated KV-head clustering with per-head correction gates
- Success threshold: At least 15% KV byte reduction with mean attention-output cosine >= 0.98, no negative per-head cosine, perplexity delta <= 2%, and no decode-latency regression at 2048+ tokens.
- Stop condition: Stop if calibrated grouping cannot reach 0.98 mean cosine at 15% KV reduction on GPT-2-small-class models or if latency remains slower than exact KV attention.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-kv-head-clustering-for-long-context-inference-on-10gb-36db4c04e5e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
