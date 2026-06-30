# Anchored KV-cache eviction policy on CPU inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchored-kv-cache-eviction-policy-on-cpu-inference-32e083f4281b`
Run ID: `anchored-kv-cache-eviction-policy-on-cpu-inference-32e083f4281b-20260620T234620476581+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/982c005a47ec

## What looked useful

Anchored sliding at capacity 1024 with 64 protected anchors reached 0.7578 mean accuracy versus 0.2169 for sliding, with anchor accuracy 1.0000 and recent accuracy 1.0000. A structural heavy baseline reached 0.7611 accuracy but had higher update time in this simulator. Middle-context accuracy stayed near zero for anchored sliding, marking a clear boundary.

## Boundaries and scale limits

Synthetic mechanism test only: 16 seeds, sequence length 8192, 1024 queries per seed, capacities 128-1024, no real transformer inference, no perplexity or end-to-end generation quality measurement, and no production CPU kernel integration.

## Claim scope

In a deterministic synthetic CPU KV-cache trace with prefix-anchor, middle-context, and recent targets, anchored sliding retention strongly improves anchor-heavy retrieval accuracy over pure sliding-window eviction at matched cache capacities, but does not solve arbitrary middle-context retention and only roughly matches a structural heavy-hitter baseline at the largest tested cache.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic mechanism evidence, not direct real-LLM inference validation.

## Recommended next action

Run a bounded real-transformer CPU replay using a small model and long-context prefix-anchor tasks, comparing anchored sliding against sliding and structural heavy-hitter eviction at matched KV budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-transformer CPU replay for anchored KV-cache eviction
- Success threshold: Anchored sliding improves prefix-anchor task accuracy by at least 20 percentage points over sliding while staying within 10 percent of structural heavy-hitter accuracy and using lower update overhead on matched CPU runs.
- Stop condition: Stop if anchored sliding fails to beat sliding by at least 10 percentage points on real-model prefix-anchor tasks or if its anchor budget causes more than a 10 percentage point loss on recency-dominant tasks.

## Evidence references

- Artifact root: `<local-path>/projects/anchored-kv-cache-eviction-policy-on-cpu-inference-32e083f4281b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
