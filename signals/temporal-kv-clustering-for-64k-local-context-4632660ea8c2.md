# Temporal KV Clustering for 64K Local Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `temporal-kv-clustering-for-64k-local-context-4632660ea8c2`
Run ID: `temporal-kv-clustering-for-64k-local-context-4632660ea8c2-20260523T144934442292+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/954a3eae6345

## What looked useful

Temporal KV clustering should be treated as a redundancy compressor rather than a safe exact-recall cache: it reached 0.852 all-target cosine on bursty 64K contexts versus 0.351 for recency, but only 0.009 cosine on iid far targets despite 100% centroid representation.

## Boundaries and scale limits

Synthetic single-layer attention only; no real transformer KV tensors, downstream language-model metrics, learned clustering, multi-layer/head analysis, serving kernel benchmark, or production latency validation.

## Claim scope

On a synthetic 64K full-attention approximation probe, temporal chunk clustering of older KV entries improves approximation over recency, stride, and random retention when keys are temporally redundant, but it fails as an exact old-token retrieval mechanism on iid keys.

## Why it stopped

No-paper useful signal: the local synthetic evidence is enough to define the mechanism boundary, but not enough for a publication-grade 64K language-model cache claim.

## Recommended next action

Run a bounded real-transformer KV follow-up on a small pretrained model, comparing temporal centroids against recency and a salience-preserving cluster variant on long retrieval and perplexity metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-KV temporal clustering with salience-preserving centroids
- Success threshold: Temporal clustering or its salience-preserving variant must improve long-range retrieval or log-likelihood over recency by at least 10% relative while keeping recent-token quality within 2% and avoiding the iid-style far-token collapse.
- Stop condition: Stop if real KV metrics reproduce iid-style far-token collapse without a downstream gain over recency, or if gains appear only on synthetic/bursty proxies and not on real prompts.

## Evidence references

- Artifact root: `<local-path>/projects/temporal-kv-clustering-for-64k-local-context-4632660ea8c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
