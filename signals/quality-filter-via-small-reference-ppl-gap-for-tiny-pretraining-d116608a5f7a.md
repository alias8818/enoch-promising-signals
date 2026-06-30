# Quality filter via small-reference PPL-gap for tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quality-filter-via-small-reference-ppl-gap-for-tiny-pretraining-d116608a5f7a`
Run ID: `quality-filter-via-small-reference-ppl-gap-for-tiny-pretraining-d116608a5f7a-20260620T033631609169+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bd9b07e16388

## What looked useful

Top PPL-gap was best in 3/3 bounded seeds. Mean final validation loss was 7.8465 for top-gap versus 8.1509 for random, 10.3195 for low 70M-reference loss, and 10.6927 for bottom-gap. Top-gap had a mean 0.3044 lower validation loss and about 26% lower held-out perplexity than random.

## Boundaries and scale limits

Candidate pool was 960 documents per seed with synthetic corruptions; target models were 11.45M-parameter GPT-2-style LMs trained for 160 steps on 24k selected tokens; evaluation was Wikitext validation perplexity only. This does not validate real web-crawl filtering, GPT-2-small-class or larger targets, duplicate/contamination handling, downstream tasks, or long pretraining.

## Claim scope

In a bounded controlled tiny-pretraining probe using cached Wikitext and TinyStories mixed with deterministic corruptions, selecting documents by top loss gap between EleutherAI/pythia-14m and EleutherAI/pythia-70m produced lower held-out Wikitext validation loss than random, low-single-reference-loss, and bottom-gap selectors across 3 seeds.

## Why it stopped

No-paper closure: this run produced a useful bounded mechanism signal, but the evidence is controlled and small-scale rather than a publication-grade validation.

## Recommended next action

Run a bounded deepen experiment on a real noisy crawl shard without synthetic corruptions, with at least 3 seeds, a GPT-2-small-class target or parameter-matched baseline, and the same selector controls before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-crawl PPL-gap filtering for GPT-2-small-class tiny pretraining
- Success threshold: Top-gap must beat random by at least 0.10 validation loss or 5% perplexity in at least 2/3 seeds and must not underperform a simple heuristic-quality baseline by more than 2%.
- Stop condition: Stop as negative if top-gap fails to beat random in 2 or more seeds, selects obvious domain artifacts, or the improvement disappears when synthetic corruptions are removed.

## Evidence references

- Artifact root: `<local-path>/projects/quality-filter-via-small-reference-ppl-gap-for-tiny-pretraining-d116608a5f7a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
