# Likelihood-filtered synthetic data vs raw synthetic vs human-only tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `likelihood-filtered-synthetic-data-vs-raw-synthetic-vs-human-only-tiny-pretraining-dee73be2bf96`
Run ID: `likelihood-filtered-synthetic-data-vs-raw-synthetic-vs-human-only-tiny-pretraining-dee73be2bf96-20260619T114938599581+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3dedabb33ff9

## What looked useful

Filtering raised the good-synthetic fraction from 0.64-0.67 to 0.74-0.80 and improved mean held-out NLL from 2.8474 for raw synthetic to 2.8317 for likelihood-filtered synthetic. Human-only remained best at 2.7817 mean NLL.

## Boundaries and scale limits

Three seeds, controlled stochastic corpus, controlled synthetic corruption process, smoothed bigram likelihood filter, 2-layer tiny Transformer, 320 optimizer steps per condition; no natural-language corpus, no real LLM-generated synthetic data, no GPT-2-small-class scale, and no downstream transfer tasks.

## Claim scope

In a controlled toy language-modeling benchmark, likelihood filtering of mixed-quality synthetic sequences enriched human-like samples and modestly improved held-out human-distribution NLL versus raw synthetic pretraining, but did not beat the human-only baseline.

## Why it stopped

No-paper useful signal: the local toy result supports the filtering mechanism versus raw synthetic data but is not direct or large enough for a paper and does not outperform human-only pretraining.

## Recommended next action

Run a bounded natural-language follow-up using a small real corpus, actual LLM-generated synthetic continuations, a neural likelihood filter, and the same fixed-token comparison against raw synthetic and human-only baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language likelihood filtering probe for tiny pretraining
- Success threshold: Likelihood-filtered synthetic improves mean held-out NLL over raw synthetic by at least 0.02 across three seeds while retaining at least 80% of human-only distinct-4 diversity and not worsening by more than 0.03 NLL versus human-only.
- Stop condition: Stop as unsupported if filtered synthetic fails to beat raw synthetic mean held-out NLL by 0.01 or if filtering causes substantial diversity collapse despite NLL gains.

## Evidence references

- Artifact root: `<local-path>/projects/likelihood-filtered-synthetic-data-vs-raw-synthetic-vs-human-only-tiny-pretraining-dee73be2bf96`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
