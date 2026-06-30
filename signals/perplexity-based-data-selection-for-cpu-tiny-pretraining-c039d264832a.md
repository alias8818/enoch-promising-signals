# Perplexity-based Data Selection for CPU Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `perplexity-based-data-selection-for-cpu-tiny-pretraining-c039d264832a`
Run ID: `perplexity-based-data-selection-for-cpu-tiny-pretraining-c039d264832a-20260530T070431078286+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/07d3425a146e

## What looked useful

Low-reference-perplexity selection improved test perplexity by 4.0% to 8.3% versus random equal-budget selection across the non-smoke budget sweep; high-perplexity anti-selection was 28.8% to 42.7% worse than low selection. Main budget 120 result: low 12.074 test perplexity, random mean 13.163 +/- 0.203, high 15.654.

## Boundaries and scale limits

The experiment used a character 5-gram count LM, one target domain, obvious public-domain distractors, and short local CPU runs. It does not validate transformer/GPT-style pretraining, large corpora, deduplication-heavy web mixtures, or cross-domain robustness.

## Claim scope

In a CPU-only Tiny Shakespeare mixed-domain character n-gram LM probe, selecting equal-budget pretraining chunks by low perplexity under a small target-domain reference LM reduced held-out target perplexity versus random controls across budgets of 40, 80, 120, and 160 chunks.

## Why it stopped

No-paper useful signal: the mechanism is supported in a direct CPU-tiny n-gram probe, but evidence remains too narrow and model class too simple for publication-grade validation.

## Recommended next action

Run a bounded neural follow-up with a tiny transformer or LSTM LM on the same saved selection splits and compare low-perplexity selection against random, high-perplexity, and simple domain-label baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny neural LM validation of perplexity-ranked CPU data selection
- Success threshold: Low-perplexity selection beats random by at least 3% mean held-out target perplexity at two budgets and is not worse than a simple target-source-label selector by more than 1%.
- Stop condition: Stop as negative if low-perplexity selection fails to beat random by 1% mean held-out target perplexity at both tested budgets or if gains disappear when source balance is controlled.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-based-data-selection-for-cpu-tiny-pretraining-c039d264832a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
