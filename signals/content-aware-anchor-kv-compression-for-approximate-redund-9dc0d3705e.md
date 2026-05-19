# Content-aware anchor KV compression for approximate redundant retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `content-aware-anchor-kv-compression-for-approximate-redund-9dc0d3705e`
Run ID: `content-aware-anchor-kv-compression-for-approximate-redund-9dc0d3705e-20260516T061523254848+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b95f71247f67

## What looked useful

Content-aware anchors beat the best non-content baseline in 16 of 20 scenario/budget cells and roughly halved average relative MSE versus random/recent sampling, but they lost in noisy high- and medium-redundancy settings at 12.5%-25% budgets. Count-weighted anchors were not reliably better than unweighted anchors.

## Boundaries and scale limits

No real transformer KV traces, downstream next-token loss, autoregressive generation quality, GPU kernel implementation, or serving latency were tested. Results are Tier-1 controlled evidence only and do not establish broad LLM-cache performance.

## Claim scope

Small controlled synthetic KV retrieval benchmark with 1024-token redundant memories, 32-96 latent content clusters, 12 seeds, and 3.125%-25% anchor budgets. Content-aware anchors were compared against random, recent, and segment-mean compression using full-attention output relative MSE, output cosine, and top-1 cluster agreement.

## Why it stopped

Tier-1 direct synthetic retrieval found mixed support: useful mechanism signal under redundancy, but enough controlled failures that the idea is not paper-positive and should not be finalized positive.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded action is a real-model KV trace replay on a small GPT-2-class model to test whether the noisy-budget failures persist outside synthetic clusters.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV trace replay for content-aware anchor compression
- Success threshold: Content-aware anchors must beat the best random/recent baseline by at least 25% relative MSE reduction at 3.125%-12.5% budgets on most layers/heads without increasing next-token loss by more than 1%.
- Stop condition: Stop as negative if random or recent eviction matches or beats content-aware anchors on most tested layers/heads, or if compression overhead dominates the memory savings in the replay implementation.

## Evidence references

- Artifact root: `<local-path>/projects/content-aware-anchor-kv-compression-for-approximate-redund-9dc0d3705e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
