# AnchorKV: Exact-Anchor Preserving KV Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchorkv-exact-anchor-preserving-kv-compression-9fd6427af3ed`
Run ID: `anchorkv-exact-anchor-preserving-kv-compression-9fd6427af3ed-20260621T072954778952+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/37227f7a15f9

## What looked useful

Exact preservation guarantees anchor KV availability but does not preserve the full-cache attention distribution after eviction and softmax renormalization. Sparse anchors can help in a narrow anchor-critical setting, suggesting any future method needs attention-mass correction or better non-anchor fill selection.

## Boundaries and scale limits

No real LLM, no multi-layer/head cache, no generation benchmark, no accepted KV compression baseline implementation, no GPU throughput measurement, and no quantization or positional-cache interactions were tested.

## Claim scope

CPU-only synthetic single-layer attention probes over 4096-token KV caches show exact-anchor-preserving norm retention is not a robust standalone KV compression rule; it won only one sparse-anchor, anchor-critical budget setting and failed in dense-anchor settings even with perfect target-anchor retention.

## Why it stopped

No-paper mixed proxy result: exact-anchor preservation alone was best in only 1 of 24 synthetic scenario-budget settings and failed as a robust compression rule despite perfect target-anchor retention in dense-anchor workloads.

## Recommended next action

Deepen with a small real-transformer test of sparse exact anchors plus attention-mass correction or decoding-query-aware fill selection against norm retention and a standard KV compression baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sparse exact anchors with attention-mass-corrected KV retention
- Success threshold: At matched cache budgets on a small real transformer, sparse exact-anchor plus correction improves task metric or perplexity versus norm retention and the selected KV baseline while not increasing cache size, with the gain persisting across at least two anchor densities.
- Stop condition: Stop if corrected sparse anchors fail to beat norm retention on attention-output error or generation metric in the first small real-transformer benchmark, or if anchor density sensitivity makes the method require impractically rare anchors.

## Evidence references

- Artifact root: `<local-path>/projects/anchorkv-exact-anchor-preserving-kv-compression-9fd6427af3ed`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
