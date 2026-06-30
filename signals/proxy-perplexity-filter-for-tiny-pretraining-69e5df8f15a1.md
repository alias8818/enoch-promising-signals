# Proxy perplexity filter for tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `proxy-perplexity-filter-for-tiny-pretraining-69e5df8f15a1`
Run ID: `proxy-perplexity-filter-for-tiny-pretraining-69e5df8f15a1-20260609T080913756306+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/482d9398fb58

## What looked useful

Proxy-best selection improved held-out BPC versus random at all tested budgets. Broad clean/noise deltas were -0.78 to -0.35 BPC; balanced clean-vs-shuffle deltas were -0.21 to -0.12 BPC. Worst-ranked controls were consistently worse than random.

## Boundaries and scale limits

Not a neural transformer pretraining result; target and proxy are n-gram LMs, contaminants are synthetic, corpora are small public-domain books, and no GPT-2-small-class or realistic web-scale validation was run.

## Claim scope

In a bounded character n-gram benchmark using Project Gutenberg English plus synthetic contaminants, a cheap proxy-perplexity filter enriches useful chunks and improves held-out BPC for an equal-budget tiny character LM versus random selection.

## Why it stopped

Evidence is a bounded proxy/mechanism validation, not direct neural pretraining or publication-grade validation.

## Recommended next action

Stop this worker run as a no-paper useful signal; next, run the same selection protocol with a tiny neural LM and a realistic small corpus mixture.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny neural LM validation for proxy-perplexity data filtering
- Success threshold: Proxy-filtered training improves held-out validation loss by at least 3% versus random and beats simple heuristic filtering in at least two of three seeds without reducing effective token diversity.
- Stop condition: Stop if proxy filtering fails to beat random by 1% validation loss in two independent seeds or if gains disappear when compared against simple quality/dedup heuristics.

## Evidence references

- Artifact root: `<local-path>/projects/proxy-perplexity-filter-for-tiny-pretraining-69e5df8f15a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
