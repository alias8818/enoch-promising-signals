# Small-transformer retrieval validation for anchor-gated KV compression

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `small-transformer-retrieval-validation-for-anchor-gated-kv-4ef41646b1`
Run ID: `small-transformer-retrieval-validation-for-anchor-gated-kv-4ef41646b1-20260527T235103239620+0000`

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

- Parent run decision: Anchor-Gated KV Compression with Exact Retrieval Points: enoch://control-plane/projects/anchor-gated-kv-compression-with-exact-retrieval-points-0719ebfa3002/runs/anchor-gated-kv-compression-with-exact-retrieval-points-0719ebfa3002-20260527T204613450232+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/3b8ae3aeba13

## What looked useful

Full-cache retrieval reached 0.975 mean policy-sweep accuracy, while recent-only compression averaged 0.0683 and anchor-gated compression averaged 0.0750 despite retaining 17.67 tokens on average versus 8.0 for recent-only. Long-distance anchor-gated accuracy stayed near chance.

## Boundaries and scale limits

Single seed, synthetic retrieval data, 12 bindings, one small architecture, one anchor placement, and inference-only pruning after full-cache training; not evidence about compression-aware training or larger pretrained LLMs.

## Claim scope

In a 4-layer 96-dimensional causal transformer trained on a 12-binding synthetic key/value retrieval task, inference-only KV-cache compression that retains all post-binding anchor tokens plus a recent window did not preserve retrieval accuracy.

## Why it stopped

Controlled small direct test falsified the scoped inference-only threshold: anchor-gated retention did not materially beat chance/recent-only compression while full-cache retrieval was high.

## Recommended next action

Stop this inference-only follow-up as a no-paper negative; the next bounded test should train with anchor/cache-dropout compression in the loop before evaluating the same cache policy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compression-aware anchor training for retrievable KV memory cells
- Success threshold: Anchor-gated compression with window 4 or 8 reaches at least 0.80 long-distance accuracy and stays within 10 percentage points of full-cache accuracy while retaining at most 55% of full-cache tokens.
- Stop condition: Stop negative if full-cache accuracy is at least 0.90 but anchor-gated long-distance accuracy remains below 0.50 or fails to beat recent-only by at least 20 percentage points in at least two of three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-retrieval-validation-for-anchor-gated-kv-4ef41646b1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
