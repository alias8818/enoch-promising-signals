# Real-model KV trace validation for exact-anchor compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-model-kv-trace-validation-for-exact-anchor-compressio-ede3c23200`
Run ID: `real-model-kv-trace-validation-for-exact-anchor-compressio-ede3c23200-20260608T081051528599+0000`

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

- Parent run decision: Exact-Anchor KV Compression: enoch://control-plane/projects/exact-anchor-kv-compression-84dcf37efd77/runs/exact-anchor-kv-compression-84dcf37efd77-20260608T032817364487+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/de208cd5fa47

## What looked useful

Anchor+centroid compression produced a bounded mechanism signal but failed the exactness threshold: stride 4 used 0.519 mean stored-slot ratio with rel RMSE 0.490 and cosine 0.848; stride 8 used 0.292 ratio with rel RMSE 0.602 and cosine 0.764; stride 16 used 0.184 ratio with rel RMSE 0.692 and cosine 0.682. Same-stride anchor-only controls were worse, but the remaining error is too high.

## Boundaries and scale limits

8 hand-written prompts, <=128 input tokens, distilgpt2 only, per-layer attention-context reconstruction only; no patched-cache generation, no perplexity/logit-drift evaluation, no learned/adaptive compression, no larger model or long-context validation.

## Claim scope

Small direct real-model KV-trace test on distilgpt2: periodic exact anchors plus one log-count-biased centroid per non-anchor block improves layerwise attention-context reconstruction versus anchor-only controls, but does not meet the <=0.25 mean relative RMSE and >=0.95 mean cosine threshold at <=0.50 stored-slot ratio.

## Why it stopped

Controlled small direct real-model KV-trace validation failed the explicit Tier 1 exactness threshold, although it showed a mechanism improvement over anchor-only controls.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen test with adaptive or learned per-head summary slots only if it must meet the same <=0.25 rel RMSE and >=0.95 cosine threshold on real K/V traces before any larger-scale work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive per-head summary slots for exact-anchor KV trace compression
- Success threshold: At <=0.50 mean stored-slot ratio, adaptive exact-anchor compression must achieve mean rel RMSE <=0.25 and mean cosine >=0.95 on held-out real-model K/V traces, while beating fixed-centroid and same-slot controls.
- Stop condition: Stop if held-out mean rel RMSE remains >0.25 or mean cosine remains <0.95 after adaptive summaries, or if gains over fixed centroids are less than 10% relative error reduction.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-kv-trace-validation-for-exact-anchor-compressio-ede3c23200`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
