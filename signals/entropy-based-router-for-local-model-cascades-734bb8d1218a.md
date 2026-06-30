# Entropy-Based Router for Local Model Cascades

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-based-router-for-local-model-cascades-734bb8d1218a`
Run ID: `entropy-based-router-for-local-model-cascades-734bb8d1218a-20260604T192813953967+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae645af88749

## What looked useful

Entropy routing improved cheap-model accuracy and saved about 81% measured cost on digits while beating random same-fraction routing in every seed. On synthetic data it needed about 97% escalation, saved only about 2.4% cost, and beat random same-fraction routing in only half the seeds.

## Boundaries and scale limits

Tested only small sklearn classifiers on digits and synthetic multiclass classification across 8 seeds. Not tested on LLM generation, GPU serving, batching, KV-cache behavior, production traces, or 7B+ local models.

## Claim scope

Bounded CPU-local sklearn proxy evidence shows entropy routing can save strong-model calls when the cheap model is competent and entropy separates errors, but it degenerates to near-always-strong routing on harder settings with a weak cheap model.

## Why it stopped

Bounded proxy evidence is mixed: it supports the routing mechanism in favorable conditions but falsifies a broad claim that entropy alone reliably yields efficient local cascades.

## Recommended next action

Stop this run as no-paper useful signal; next run should sweep cheap-model strength and entropy-error AUROC to identify when uncertainty routing earns real cost savings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cheap-model competence threshold for entropy cascade savings
- Success threshold: Identify a reproducible operating region across at least two datasets where entropy routing saves at least 50% measured cost versus always-strong inference with no more than 1 percentage point held-out accuracy loss, and entropy beats random same-fraction routing by at least 2 standard deviations.
- Stop condition: Stop if no cheap-model capacity setting across the sweep satisfies the cost and accuracy threshold, or if entropy-error AUROC remains below 0.75 in all settings.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-based-router-for-local-model-cascades-734bb8d1218a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
