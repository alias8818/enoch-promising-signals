# Perplexity-Filtered Mini-Pretraining Subset

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-filtered-mini-pretraining-subset-082884f15240`
Run ID: `perplexity-filtered-mini-pretraining-subset-082884f15240-20260608T001112803201+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/51f62cf8b7b9

## What looked useful

The practical signal is to avoid selecting the high-perplexity tail; low-perplexity-only filtering did not reliably improve over random in this bounded mini-pretraining test.

## Boundaries and scale limits

Small public corpus, proxy scorer rather than pretrained LM perplexity, 240 optimizer steps per run, three seeds, tiny model, and early token-efficiency only; no web-scale corpus, no GPT-2-small-class baseline, and no convergence or downstream evaluation.

## Claim scope

On WikiText-2 with GPT-2 tokenization, a smoothed unigram proxy-perplexity scorer, and a tiny GPT-style causal LM trained for a fixed 120k-token budget across three seeds, low-perplexity-only subset selection was effectively tied with random, while high-perplexity-tail selection was consistently worse.

## Why it stopped

No-paper closure: bounded local evidence mixed the original hypothesis, with low-perplexity selection not reliably better than random despite a consistent negative control for high-perplexity selection.

## Recommended next action

Run a bounded deepen test comparing random, low-only, high-tail-excluded, and quantile-mixture policies using a stronger pretrained-LM scorer on a noisier medium corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tail-exclusion versus low-only perplexity filtering on a noisier corpus
- Success threshold: High-tail-excluded selection improves mean validation loss versus random by at least 0.03 nats and beats low-only selection in at least 4 of 5 paired seeds.
- Stop condition: Stop if high-tail-excluded does not beat random in mean validation loss or if low-only remains statistically indistinguishable from random after the planned fixed-token-budget runs.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-filtered-mini-pretraining-subset-082884f15240`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
