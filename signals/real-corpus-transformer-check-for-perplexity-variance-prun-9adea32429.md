# Real-Corpus Transformer Check for Perplexity-Variance Pruning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-corpus-transformer-check-for-perplexity-variance-prun-9adea32429`
Run ID: `real-corpus-transformer-check-for-perplexity-variance-prun-9adea32429-20260526T163211234633+0000`

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

- Parent run decision: Perplexity-Variance Data Pruning for Tiny Pretraining: enoch://control-plane/projects/perplexity-variance-data-pruning-for-tiny-pretraining-80deeb56be0d/runs/perplexity-variance-data-pruning-for-tiny-pretraining-80deeb56be0d-20260526T091531005044+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/026a37900b96

## What looked useful

Low variance of per-window loss damage is a real safety correlate for head pruning versus random selection, but the added variance criterion did not improve held-out perplexity over directly ranking by mean loss damage.

## Boundaries and scale limits

Single pretrained GPT-2 model, WikiText-2 only, 48 calibration windows and 64 held-out test windows, runtime head masking rather than structural pruning, no post-pruning fine-tuning, no MLP/block pruning, and no deployment speed measurement.

## Claim scope

Tier 1 controlled direct test of GPT-2 attention-head masking on WikiText-2: per-window loss-delta variance selects heads that are safer than random to prune, but it does not outperform a lowest absolute mean-damage control at 10%, 25%, or 50% pruning budgets.

## Why it stopped

Tier 1 direct evidence is mixed and no-paper: variance pruning beat random but failed the stricter practical threshold against a direct mean-damage pruning control.

## Recommended next action

Stop paper escalation for this run; if continuing, run a bounded robustness follow-up that tests whether variance adds residual predictive value beyond mean loss damage across multiple GPT-2-family models and corpora.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robustness Check for Variance Residual Value Beyond Mean-Damage Pruning
- Success threshold: Variance-based or variance-plus-mean pruning must reduce held-out loss damage versus mean-damage pruning in at least two of three model/corpus pairs at both 10% and 25% budgets, while remaining far better than random.
- Stop condition: Stop if mean-damage pruning matches or beats variance-based pruning on two model/corpus pairs, because the residual value claim is not supported.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-transformer-check-for-perplexity-variance-prun-9adea32429`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
