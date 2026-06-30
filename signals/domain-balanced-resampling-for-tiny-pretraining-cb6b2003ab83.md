# Domain-balanced resampling for tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `domain-balanced-resampling-for-tiny-pretraining-cb6b2003ab83`
Run ID: `domain-balanced-resampling-for-tiny-pretraining-cb6b2003ab83-20260604T123029133210+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b57543c984e7

## What looked useful

Balanced sampling improved equal-domain mean validation loss from 1.3178 to 1.0946 and worst-domain loss from 1.8820 to 1.1230, while worsening majority-domain encyclopedic loss from 0.3859 to 1.1230. This supports the tradeoff mechanism: balanced resampling improves minority/worst-domain coverage when evaluation weights domains equally.

## Boundaries and scale limits

Synthetic template corpus only; 500 steps per policy per seed; no direct public-corpus pretraining, no tokenizer ablation, no downstream evaluation, no large-token or larger-model validation.

## Claim scope

In a deterministic three-domain synthetic tiny-pretraining proxy with an 875,777-parameter byte-level Transformer, balanced domain sampling lowered equal-domain mean and worst-domain validation loss relative to an 80/10/10 imbalanced sampler across three seeds.

## Why it stopped

Proxy-only synthetic result: mechanism is supported, but direct real-corpus tiny-pretraining evidence is required before any paper-ready claim.

## Recommended next action

Stop this worker run as no-paper useful-signal evidence; run a bounded public-corpus follow-up using cached or predownloaded Wikitext/AG News/IMDB-style domains before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Public-corpus confirmation of balanced domain resampling for tiny pretraining
- Success threshold: Balanced sampling reduces mean worst-domain validation loss by >=10% and equal-domain mean loss by >=5% across at least three seeds without increasing variance enough to erase the effect.
- Stop condition: Stop if public-corpus balanced sampling fails to improve worst-domain loss by 5% in a three-seed bounded run or if dataset acquisition remains the dominant blocker after a predownload/cache step.

## Evidence references

- Artifact root: `<local-path>/projects/domain-balanced-resampling-for-tiny-pretraining-cb6b2003ab83`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
