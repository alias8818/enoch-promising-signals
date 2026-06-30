# Gradient-Norm Data Selection for 125M Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `gradient-norm-data-selection-for-125m-pretraining-e933408f8860`
Run ID: `gradient-norm-data-selection-for-125m-pretraining-e933408f8860-20260630T014828710556+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/4d70856a2150

## What looked useful

Naive high-gradient-norm top-k selection behaved like an outlier/noise selector in this bounded proxy: selected noise rate was 45.75% versus random 29.51%, and final clean validation loss was 2.1203 versus random 2.0232. Bottom GradNorm selected 10.42% noise and improved clean validation to 1.8788, while low-loss selection reached 1.7998.

## Boundaries and scale limits

Test used a tiny GPT-like model, synthetic grammar/noise data, static one-time selection, 768 scored candidates per seed, 384 selected examples per seed, and 160 training steps. It did not test 125M parameters, real web data, tokenizer effects, long-horizon pretraining, adaptive online reselection, downstream tasks, or optimizer-aware gradient utility.

## Claim scope

In a three-seed synthetic mixed-quality causal-LM proxy, static early top-k per-example gradient-norm selection enriched noisy examples and worsened clean validation loss versus random selection under an equal training budget.

## Why it stopped

Proxy evidence is an early falsification of naive top-k GradNorm for clean pretraining efficiency, not a full 125M-scale validation; close this run as no-paper useful signal.

## Recommended next action

Run a bounded real-text follow-up using a GPT-2-small-class or otherwise parameter-matched model on a deliberately mixed-quality corpus, comparing top/bottom GradNorm, loss filters, random, and a direction-aware gradient control on held-out perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text bounded validation of GradNorm noise attraction
- Success threshold: Top GradNorm is considered unsupported if it selects at least 10 percentage points more noisy data than random and has worse mean clean held-out loss than random across seeds; direction-aware control earns continuation if it beats random by at least 0.03 clean loss without increasing selected noise rate.
- Stop condition: Stop after three seeds if top GradNorm is consistently worse than random or if the direction-aware control fails to beat random; do not escalate to longer training unless a selector improves clean held-out loss with stable selected-data quality.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-data-selection-for-125m-pretraining-e933408f8860`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
