# Per-Head KV Clustering for Cache Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-head-kv-clustering-for-cache-compression-770b3885eed6`
Run ID: `per-head-kv-clustering-for-cache-compression-770b3885eed6-20260605T050241077483+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/f39d9fa0999d

## What looked useful

Per-head clustering appears to fix a real weakness of shared layer-level codebooks, but the standalone clustering approach is not practically competitive in this proxy because recent/stride retention had lower reconstruction error and much lower selection cost.

## Boundaries and scale limits

Six repeated local text prompts, sequence length 128, all 12 GPT-2-small layers, 4,320 head-query comparisons, no downstream perplexity/generation evaluation, no long-context serving kernel, no larger model validation.

## Claim scope

On a bounded GPT-2-small attention-output reconstruction proxy, per-head joint KV k-means preserved attention outputs better than an equal-total-budget layer-shared k-means codebook at 1/8 and 1/4 cache ratios, but it did not outperform a simple recent-plus-stride retention baseline.

## Why it stopped

Bounded direct attention-output proxy produced mixed evidence: per-head clustering beat shared clustering but failed against the practical retention control, so this is no-paper useful signal rather than a positive validation.

## Recommended next action

Do not write a paper from this standalone result; run one bounded deepen test of a hybrid cache that keeps recent tokens exactly and clusters only older tokens per head.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid Recent-Exact Plus Per-Head Older-Token KV Clustering
- Success threshold: Hybrid method reduces mean and P90 attention-output error by at least 20% versus recent/stride at the same occupied-entry budget while keeping compression cost within 3x of recent/stride selection or showing a clear amortization path.
- Stop condition: Stop if the hybrid fails to beat recent/stride on either mean or P90 attention-output error at both tested ratios, or if clustering cost remains more than 10x retention without a plausible amortization mechanism.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-kv-clustering-for-cache-compression-770b3885eed6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
