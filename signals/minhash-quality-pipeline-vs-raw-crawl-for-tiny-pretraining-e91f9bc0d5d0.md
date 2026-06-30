# MinHash-quality pipeline vs raw crawl for tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `minhash-quality-pipeline-vs-raw-crawl-for-tiny-pretraining-e91f9bc0d5d0`
Run ID: `minhash-quality-pipeline-vs-raw-crawl-for-tiny-pretraining-e91f9bc0d5d0-20260527T173811088493+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1399af805d1d

## What looked useful

Combined quality + MinHash filtering improved mean held-out BPC from 3.2119 to 2.9661 across 10 synthetic raw-crawl seeds, winning 10/10 trials. Quality-only and MinHash-only ablations also helped, while a no-corruption clean control showed only 0.00058 BPC mean improvement.

## Boundaries and scale limits

The evidence uses synthetic corruption, one public literary source, a character 5-gram LM, and 10 seeds. It does not validate real web-crawl distributions, tokenizer effects, neural tiny transformer pretraining, downstream tasks, or larger scale.

## Claim scope

In a bounded synthetic raw-crawl corruption test built from Tiny Shakespeare, a simple document quality filter plus MinHash near-deduplication improved held-out character 5-gram LM bits-per-character versus training on the unfiltered raw crawl under an equal character budget.

## Why it stopped

This run is a useful proxy/mechanism result, not a full validation or paper-ready result, because it used synthetic corruption and a character n-gram LM instead of real crawl pretraining.

## Recommended next action

Run a bounded direct-evidence follow-up using a real crawl slice and a small neural LM with raw, quality-only, MinHash-only, and combined-pipeline ablations under matched token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-crawl tiny neural LM ablation for quality and MinHash filtering
- Success threshold: Combined filtering improves neural validation loss by at least 3% relative to raw and outperforms both single-stage ablations on at least 3 of 5 seeds without reducing the usable token budget below 60% of raw.
- Stop condition: Stop as unsupported if combined filtering fails to beat raw on mean neural validation loss or if most gains are explained by a single-stage ablation.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-quality-pipeline-vs-raw-crawl-for-tiny-pretraining-e91f9bc0d5d0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
