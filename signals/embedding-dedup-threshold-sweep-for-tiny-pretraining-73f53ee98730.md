# Embedding-dedup threshold sweep for tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `embedding-dedup-threshold-sweep-for-tiny-pretraining-73f53ee98730`
Run ID: `embedding-dedup-threshold-sweep-for-tiny-pretraining-73f53ee98730-20260614T091200768413+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/665fad9cd7d2

## What looked useful

Exact-ish embedding dedup collapsed a 1740-document duplicate-heavy corpus to 616 retained documents and improved 800-step held-out seen-paraphrase loss from 0.8005 to 0.5775. More aggressive thresholding retained fewer paraphrases and worsened seen-paraphrase loss versus 0.94, with threshold 0.86 reaching 0.6339. Novel-template loss changed only slightly and noisily.

## Boundaries and scale limits

Synthetic corpus only; dependency-free TF-IDF random-projection embeddings rather than neural sentence embeddings; tiny character-level Transformer; 3 matched-seed replicates; maximum 800 training steps; no real web corpus, GPT tokenizer, downstream tasks, or large-scale pretraining.

## Claim scope

In a synthetic tiny-pretraining corpus with exact duplicates, repeated boilerplate, and templated semantic paraphrases, TF-IDF random-projection embedding dedup threshold choice materially changed retained corpus composition and tiny character-Transformer validation losses.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/tiny and supports only a bounded mechanism, not publication-grade validation.

## Recommended next action

Do not write a paper from this run; run a bounded deepen test on a real small corpus using a standard neural embedding model and GPT-style tiny LM to check whether exact-ish dedup still beats no dedup and aggressive dedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus neural-embedding dedup threshold sweep for tiny GPT pretraining
- Success threshold: Exact-ish dedup improves held-out near-duplicate/paraphrase loss or memorization diagnostics versus no dedup without degrading general validation perplexity by more than 1%, and aggressive dedup is measurably worse than exact-ish dedup on at least one target metric.
- Stop condition: Stop if neural embedding dedup does not outperform no dedup on any target validation or memorization metric across matched seeds, or if aggressive and exact-ish thresholds are indistinguishable within replicate variance.

## Evidence references

- Artifact root: `<local-path>/projects/embedding-dedup-threshold-sweep-for-tiny-pretraining-73f53ee98730`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
