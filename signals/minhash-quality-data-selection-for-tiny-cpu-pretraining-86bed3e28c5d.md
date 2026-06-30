# MinHash+Quality Data Selection for Tiny CPU Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `minhash-quality-data-selection-for-tiny-cpu-pretraining-86bed3e28c5d`
Run ID: `minhash-quality-data-selection-for-tiny-cpu-pretraining-86bed3e28c5d-20260620T082825199992+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ef9e9a368dd1

## What looked useful

MinHash+quality achieved validation perplexity 13.1806 versus 14.7418 for random, 13.2787 for quality-only, and 14.4352 for MinHash-only. Quality filtering was the main effect; MinHash added a small incremental gain over quality-only by selecting more clean unique documents.

## Boundaries and scale limits

Single seed; synthetic corpus; 120 selected documents; 60 validation documents; neural bigram LM only; no transformer/GPT-2-small-class run; no real corpus; no large-corpus LSH throughput validation.

## Claim scope

On a deterministic synthetic 420-document corpus with clean, noisy, off-domain, and near-duplicate documents, a fixed-document-budget MinHash+quality selector produced the best held-out in-domain perplexity for a tiny NumPy neural bigram LM.

## Why it stopped

No-paper closure: the result is a useful synthetic proxy signal, but not direct or robust enough for publication-grade validation.

## Recommended next action

Run a bounded multi-seed deepen test on a semi-real duplicated/noisy corpus with a tiny transformer or GPT-2-small-class CPU-feasible baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-seed semi-real MinHash+quality selection for tiny transformer pretraining
- Success threshold: MinHash+quality improves mean validation perplexity over quality-only by at least 1% with no worse than 1 of 5 seeds regressing, while also beating random and MinHash-only.
- Stop condition: Stop if MinHash+quality fails to beat quality-only in at least 3 of 5 seeds or if the effect is below 0.5% mean perplexity improvement.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-quality-data-selection-for-tiny-cpu-pretraining-86bed3e28c5d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
