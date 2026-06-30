# Embedding-diversity data selection for 2x faster tiny pretraining convergence

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `embedding-diversity-data-selection-for-2x-faster-tiny-pretraining-convergence-8573b08f074c`
Run ID: `embedding-diversity-data-selection-for-2x-faster-tiny-pretraining-convergence-8573b08f074c-20260604T125051113643+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6ed8e4d03c38

## What looked useful

Pure embedding-diversity acted as topic-coverage reweighting: it helped when validation was balanced across topics, hurt or slowed slightly when validation followed the natural long-tail distribution, and anti-diverse centroid selection failed badly.

## Boundaries and scale limits

Synthetic data, TF-IDF proxy embeddings, bigram LM only, 8 seeds per validation mode, 600 selected documents per run; no neural transformer, real corpus, or full pretraining validation.

## Claim scope

In a synthetic multi-topic corpus with a NumPy online smoothed bigram LM, greedy TF-IDF embedding-diversity selection improved balanced validation NLL versus random but did not achieve 2x faster convergence and did not improve natural-frequency validation.

## Why it stopped

Proxy direct-LM evidence did not support 2x faster convergence: balanced validation showed only 1.33x speedup, while natural validation showed 0.916x speedup versus random.

## Recommended next action

Stop this run as a proxy early falsification of the broad 2x claim; the bounded next test is distribution-aware embedding diversity on a tiny neural LM.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Distribution-aware embedding diversity for tiny neural LM pretraining
- Success threshold: Distribution-aware embedding diversity reaches the same natural-validation loss as random with at least 1.5x fewer tokens while matching or improving balanced validation loss, with no seed showing a large regression.
- Stop condition: Stop if distribution-aware selection fails to beat random by at least 1.2x on natural validation or loses the balanced-validation advantage in the first bounded neural run.

## Evidence references

- Artifact root: `<local-path>/projects/embedding-diversity-data-selection-for-2x-faster-tiny-pretraining-convergence-8573b08f074c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
