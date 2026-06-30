# Real-corpus bounded comparison of small-LM perplexity filtering against keyword filtering

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-corpus-bounded-comparison-of-small-lm-perplexity-filt-93433d88d6`
Run ID: `real-corpus-bounded-comparison-of-small-lm-perplexity-filt-93433d88d6-20260622T001631022344+0000`

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

- Parent run decision: Small-LM perplexity filter vs heuristic keyword filter for tiny pretraining: enoch://control-plane/projects/small-lm-perplexity-filter-vs-heuristic-keyword-filter-for-tiny-pretraining-64ef6248ecee/runs/small-lm-perplexity-filter-vs-heuristic-keyword-filter-for-tiny-pretraining-64ef6248ecee-20260621T235856481026+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ef97128d263b

## What looked useful

Primary 40-keyword run: LM mean AP 0.2902 vs keyword 0.2198 (+0.0704), equal-budget F1 0.3308 vs 0.2213 (+0.1095), wins 20/20 trials on both metrics. Keyword-count sensitivity preserved the LM advantage at 80 and 160 keywords, though the margin narrowed.

## Boundaries and scale limits

Single corpus family, four target categories, topic labels as relevance labels, simple seed-derived keyword baselines only, no BM25/query-expansion baseline, no pretrained transformer LM perplexity, and no human-labeled noisy web corpus.

## Claim scope

On a bounded 20 Newsgroups real-corpus topic-filtering task with four target topics, 60 positive seed documents per target, and equal held-out review budgets, a tiny add-smoothed word trigram LM ranked target documents better than a same-seed keyword-hit filter.

## Why it stopped

Tier 1 direct real-corpus evidence supports the mechanism but is not publication-grade because it is one corpus family with simple lexical baselines.

## Recommended next action

Run a bounded deepen test on at least one additional real corpus with stronger lexical baselines such as BM25/query expansion and TF-IDF centroid/logistic classifiers before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-corpus stronger-baseline check for positive-seed perplexity filtering
- Success threshold: Across corpora/tasks, small-LM or transformer perplexity filtering must beat the strongest lexical baseline by at least +0.03 mean AP and +0.03 equal-budget F1, with wins on at least 70% of task/repeat trials.
- Stop condition: Stop as no-paper evidence if the LM advantage disappears against stronger lexical baselines or fails to replicate on the added corpus.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-bounded-comparison-of-small-lm-perplexity-filt-93433d88d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
