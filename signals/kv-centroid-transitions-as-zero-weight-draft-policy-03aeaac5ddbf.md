# KV centroid transitions as zero-weight draft policy

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-centroid-transitions-as-zero-weight-draft-policy-03aeaac5ddbf`
Run ID: `kv-centroid-transitions-as-zero-weight-draft-policy-03aeaac5ddbf-20260601T052700859040+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e2ed0cb03f27

## What looked useful

Centroid target-greedy match improved from 0.2065 at 64 clusters to 0.2469 at 1024 clusters and beat unigram/random controls, but the previous-token bigram control reached 0.2603 target-greedy match and higher mean target probability of drafted tokens.

## Boundaries and scale limits

Single target model, one dataset, deterministic one-token draft proxy, hidden-state centroid proxy rather than exact layer-wise KV centroids, no wall-clock speculative decoding implementation, one seed for the cluster sweep.

## Claim scope

On distilgpt2 with WikiText-2 held-out contexts, last-layer hidden-state centroid tables contain draft-useful transition signal above unigram and randomized-cluster controls, but a centroid-only zero-weight draft policy does not beat a previous-token bigram table.

## Why it stopped

Bounded proxy evidence shows real centroid signal but early practical falsification of the stronger centroid-only zero-weight draft policy claim because a simpler previous-token table outperformed it.

## Recommended next action

Stop this centroid-only policy as no-paper evidence; the bounded next test is a residual centroid-over-bigram policy with direct speculative acceptance metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual centroid-over-bigram zero-weight draft policy
- Success threshold: Residual centroid policy improves target-greedy match or deterministic expected acceptance by at least 10% relative over previous-token bigram and shows a positive accepted-token throughput proxy without increasing lookup cost beyond a small table.
- Stop condition: Stop if residual centroid features fail to beat previous-token bigram on held-out target-greedy match and mean target probability across the stability checks.

## Evidence references

- Artifact root: `<local-path>/projects/kv-centroid-transitions-as-zero-weight-draft-policy-03aeaac5ddbf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
