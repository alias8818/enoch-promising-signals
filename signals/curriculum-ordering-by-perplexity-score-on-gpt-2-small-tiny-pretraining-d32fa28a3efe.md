# Curriculum Ordering by Perplexity-Score on GPT-2-Small Tiny Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `curriculum-ordering-by-perplexity-score-on-gpt-2-small-tiny-pretraining-d32fa28a3efe`
Run ID: `curriculum-ordering-by-perplexity-score-on-gpt-2-small-tiny-pretraining-d32fa28a3efe-20260619T101702138170+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f26d7f39e047

## What looked useful

Random ordering achieved mean test PPL 19.9425, while low_ppl_first reached 24.1215 and high_ppl_first reached 24.7683; the sorted curricula were 20.95% and 24.20% worse than random in the calibrated proxy.

## Boundaries and scale limits

This run did not train GPT-2-small, did not use GPT-2-small as the scorer, used synthetic heterogeneous text, and used a tiny context LM with a smoothed bigram reference scorer.

## Claim scope

In a bounded CPU NumPy tiny-LM proxy, naive monotonic document ordering by a frozen reference perplexity score underperformed random ordering under matched token budgets.

## Why it stopped

Early proxy falsification of the simplest monotonic perplexity-sorted curriculum; insufficient direct GPT-2-small evidence for a paper or broad claim.

## Recommended next action

Stop this run as no-paper proxy evidence; if continuing, run a bounded GPU-backed GPT-2-small-class follow-up with real text, pretrained perplexity scoring, random baseline, and a bucketed/interleaved curriculum arm.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class perplexity curriculum with bucketed interleaving control
- Success threshold: Bucketed/interleaved perplexity curriculum improves mean validation perplexity by at least 3% versus random ordering without worse mean test perplexity across at least three seeds.
- Stop condition: Stop if all perplexity curricula are at least 3% worse than random on mean validation perplexity after matched-token training, or if GPU memory/runtime prevents three completed seeds.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-ordering-by-perplexity-score-on-gpt-2-small-tiny-pretraining-d32fa28a3efe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
