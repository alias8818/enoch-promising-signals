# Embedding diversity sampling for local pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `embedding-diversity-sampling-for-local-pretraining-ea183f059123`
Run ID: `embedding-diversity-sampling-for-local-pretraining-ea183f059123-20260609T075320822497+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/482d9398fb58

## What looked useful

Across five corpus seeds, embedding_diversity was worse than random on balanced validation by +0.0928 NLL and worse on in-distribution validation by +0.1538 NLL, losing to random on 5/5 seeds for both splits. Oracle topic balancing improved balanced validation but hurt in-distribution validation, indicating a coverage-density tradeoff rather than a simple diversity win.

## Boundaries and scale limits

Synthetic corpus, TF-IDF embeddings, count-based LM, small document budget, and CPU-only local runs; no neural transformer pretraining, learned embeddings, natural corpus, tokenizer study, or large-scale validation was performed.

## Claim scope

In a controlled local proxy with 2400 imbalanced synthetic topic documents, TF-IDF document embeddings, greedy farthest-first diversity selection, a 240-document fixed subset budget, and a fixed-vocabulary bigram next-token LM, naive embedding-diversity sampling did not improve held-out NLL over random sampling.

## Why it stopped

Proxy evidence consistently falsified the simple embedding-diversity selector against random; this is not full validation, but it is sufficient no-paper evidence for the scoped local mechanism test.

## Recommended next action

Stop this run as a proxy early falsification of naive max-min embedding diversity; if continuing, test a distribution-constrained diversity selector with a small neural LM and real public text before considering any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Distribution-constrained embedding diversity for small neural local pretraining
- Success threshold: Hybrid selector beats random by at least 0.03 NLL on balanced validation while staying within 0.01 NLL of random on in-distribution validation across at least 3 seeds.
- Stop condition: Stop if pure or hybrid diversity loses to random on both balanced and in-distribution validation in at least 3 seeds, or if the neural run cannot finish within the local CPU/GPU budget.

## Evidence references

- Artifact root: `<local-path>/projects/embedding-diversity-sampling-for-local-pretraining-ea183f059123`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
