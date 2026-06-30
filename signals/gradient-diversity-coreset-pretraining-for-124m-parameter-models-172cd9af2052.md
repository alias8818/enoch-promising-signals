# Gradient-diversity coreset pretraining for 124M-parameter models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-diversity-coreset-pretraining-for-124m-parameter-models-172cd9af2052`
Run ID: `gradient-diversity-coreset-pretraining-for-124m-parameter-models-172cd9af2052-20260607T114219824645+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/de5906dc8f62

## What looked useful

Across 7 seeds, grad_diverse validation NLL was slightly worse than random (4.158860 vs 4.158669; paired mean delta +0.000191, positive is worse), while topic-loss standard deviation was lower (0.000168 vs 0.001932), suggesting a balancing effect rather than an aggregate pretraining-loss win in this proxy.

## Boundaries and scale limits

No 124M-parameter model, transformer architecture, real text corpus, GPU run, long-horizon training, or wall-clock-normalized large-model per-example-gradient overhead measurement was performed.

## Claim scope

In a small NumPy next-token proxy with synthetic skewed-topic data, greedy output-gradient-diverse batch selection did not improve balanced validation loss over random sampling under an equal token budget, but it reduced across-topic validation-loss spread.

## Why it stopped

Proxy evidence is mixed and no-paper: it gives an early mechanism signal for distribution balancing but does not support the stronger 124M-parameter pretraining-improvement claim.

## Recommended next action

Run a bounded GPT-2-small-class real-corpus experiment with random, hard-loss, and gradient-diverse selectors, measuring held-out perplexity, domain-balanced loss, and selector overhead under equal token and equal wall-clock budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small real-corpus gradient-diversity selector validation
- Success threshold: Gradient-diverse selection must improve domain-balanced validation loss or reduce domain-loss spread by at least 10% versus random while keeping aggregate validation NLL no worse than random by more than 0.5% and staying within a documented overhead budget.
- Stop condition: Stop if two independent seeds show aggregate validation NLL degradation greater than 0.5% versus random without at least a 10% domain-balance improvement, or if selector overhead makes equal-wall-clock performance worse than random.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-diversity-coreset-pretraining-for-124m-parameter-models-172cd9af2052`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
