# Quality+Perplexity Scored Data Selection for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quality-perplexity-scored-data-selection-for-tiny-pretraining-27e74ec447cd`
Run ID: `quality-perplexity-scored-data-selection-for-tiny-pretraining-27e74ec447cd-20260611T171517937338+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/33572c430bc7

## What looked useful

Across 10 seeds, combined selection had mean final validation loss 0.8052 versus 0.8169 for perplexity-only, 0.8390 for quality-only, and 0.9874 for random. Combined won 7/10 seeds overall and beat perplexity-only in 8/10 paired seed comparisons, but the margin over perplexity-only was small.

## Boundaries and scale limits

Synthetic text only; generator-provided quality scores; 2-layer 96-dim tiny transformer; 650 selected examples per seed; 220 optimizer steps; no GPT-2-small-class model, real web corpus, downstream benchmark, or long-run scaling validation.

## Claim scope

In a controlled synthetic mixed-corpus tiny-pretraining probe, equal-weight quality plus target trigram perplexity selection produced lower held-out target validation loss than random, quality-only, and perplexity-only selection under the same example budget.

## Why it stopped

No-paper closure: the run produced a useful bounded synthetic mechanism signal, but the evidence is not real-corpus or scale-robust enough for paper-positive validation.

## Recommended next action

Run a bounded real-corpus deepen follow-up using the same baselines on a small WikiText/OpenWebText-style slice with a learned or rule-based quality score and stop unless combined beats perplexity-only by at least 1% relative mean validation loss across at least 5 seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus Quality+Perplexity Selection Probe for Tiny Pretraining
- Success threshold: Combined selection beats perplexity-only by at least 1% relative mean target validation loss and wins at least 4/5 paired seeds while also beating quality-only and random.
- Stop condition: Stop as no-paper negative if combined fails to beat perplexity-only by 1% relative mean validation loss or wins fewer than 4/5 paired seeds.

## Evidence references

- Artifact root: `<local-path>/projects/quality-perplexity-scored-data-selection-for-tiny-pretraining-27e74ec447cd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
