# Embedding-diversity subsampling vs random for tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `embedding-diversity-subsampling-vs-random-for-tiny-pretraining-ed4df9b72903`
Run ID: `embedding-diversity-subsampling-vs-random-for-tiny-pretraining-ed4df9b72903-20260619T201432989350+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b904a67997da

## What looked useful

Embedding diversity selected 22.8 rare documents on average versus 16.2 for random and reduced validation NLL from 3.3394 to 3.3019; rare-topic NLL improved from 3.3922 to 3.3281, with improvement in 5/5 paired seeds.

## Boundaries and scale limits

Synthetic corpus only; TF-IDF document embeddings only; tiny NumPy neural LM only; 5 seeds; no real natural-language corpus, transformer, GPT-2-small-class baseline, or long/full-scale pretraining.

## Claim scope

On a deterministic synthetic imbalanced multi-topic corpus, TF-IDF embedding-diversity subsampling of 84/420 documents improved a small NumPy next-token LM's held-out NLL versus random sampling across 5 paired seeds, especially on rare-topic validation text.

## Why it stopped

Closed as no-paper useful signal because the local evidence is synthetic/proxy-scale, not a full validation of embedding-diversity subsampling for real tiny pretraining.

## Recommended next action

Run a bounded direct follow-up on a real small text corpus with a transformer-class tiny LM, paired seeds, matched token budget, and both production-matched and rare-balanced validation splits.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny-transformer check for embedding-diversity subsampling
- Success threshold: Diversity improves mean overall validation NLL by at least 0.02 or is non-worse within 0.01 while improving predefined rare-slice NLL by at least 0.04 in at least 4/5 paired seeds.
- Stop condition: Stop as unsupported if diversity is worse than random by more than 0.01 overall NLL in 3 or more paired seeds or if rare-slice improvement is below 0.02 mean NLL.

## Evidence references

- Artifact root: `<local-path>/projects/embedding-diversity-subsampling-vs-random-for-tiny-pretraining-ed4df9b72903`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
