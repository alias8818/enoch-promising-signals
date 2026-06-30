# KV-Cache Anchor Compression with Exact Recall

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-anchor-compression-with-exact-recall-e5456422bb47`
Run ID: `kv-cache-anchor-compression-with-exact-recall-e5456422bb47-20260619T222921985679+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1c8068b079c9

## What looked useful

At 25.6x fewer resident cache items and ~9.2% exact-token read fraction, centroid anchors reached 0.816 clustered, 0.916 drift, and 0.907 adversarial-body mean top-16 recall, but only 0.135 on random keys. First-token anchors collapsed to 0.016 recall in the adversarial regime.

## Boundaries and scale limits

No pretrained LLM traces, no end-to-end generation quality, no optimized retrieval kernel, no batch serving latency measurement, and no datacenter-scale validation were run.

## Claim scope

Synthetic/proxy KV traces show that centroid block summaries can select exact K/V blocks containing many full-cache top-attended tokens when keys are coherent within blocks, while naive first-token anchors and unstructured key regimes fail.

## Why it stopped

Proxy evidence is useful but insufficient for a paper; it early-falsifies naive first-token anchor exact recall and supports only a scoped centroid-summary mechanism under coherent synthetic KV geometry.

## Recommended next action

Run the same candidate-recall benchmark on real pretrained transformer K/Q traces across layers and heads before considering any paper or serving prototype.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV trace candidate recall for centroid anchor exact retrieval
- Success threshold: Mean top-16 recall >= 0.80 and top-1 hit rate >= 0.90 at <=10% exact-token read fraction on at least half of tested attention heads, with failure cases characterized.
- Stop condition: Stop if centroid anchors remain below 0.50 mean top-16 recall at <=10% read fraction across most layers/heads or do not beat random blocks by at least 3x.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-anchor-compression-with-exact-recall-e5456422bb47`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
