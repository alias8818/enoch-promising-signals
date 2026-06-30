# Active Pretraining: Dynamic Data Selection via Loss Probing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `active-pretraining-dynamic-data-selection-via-loss-probing-7511ebb5644b`
Run ID: `active-pretraining-dynamic-data-selection-via-loss-probing-7511ebb5644b-20260524T204037209437+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/94333ccb4b8d

## What looked useful

Naive loss-only active pretraining is unsafe in mixed-quality corpora: high-loss probing sampled noise 93.48% of the time and raised target validation loss by 218.39% versus uniform. A robustified loss-band selector reduced target loss by 6.39% versus uniform, suggesting that loss probing needs irreducible-noise or outlier controls before real pretraining tests.

## Boundaries and scale limits

Tiny GRU, synthetic token streams, 5 seeds, 500 training steps per policy. This is not evidence for large-scale pretraining, real web data, tokenizer effects, or GPT-scale optimization dynamics.

## Claim scope

Synthetic four-domain language-modeling proxy with target, near-target, easy distractor, and irreducible-noise streams. Under equal token budget, naive high-current-loss probing is worse than uniform because it overselects irreducible noise; a simple loss-band outlier rejection control is modestly better than uniform on target validation.

## Why it stopped

No-paper closure: proxy evidence falsifies naive high-loss probing as a standalone rule and only supports a bounded follow-up for robust loss probing, not a publication-grade active pretraining claim.

## Recommended next action

Run a bounded deepen follow-up on a small real text mixture with a GPT-2-small-class or parameter-matched model, comparing uniform, high-loss probing, and explicit irreducible-noise/outlier rejection under equal tokens.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robust loss-probing selection on a small real-text pretraining mixture
- Success threshold: Outlier-rejected loss probing beats uniform target validation loss by at least 3% mean over seeds without reducing throughput by more than 10%, while naive high-loss probing fails or selects substantially more noisy data.
- Stop condition: Stop if robust loss probing does not beat uniform by 3% mean target validation loss over at least 3 seeds, or if gains disappear when source/noise fractions are varied.

## Evidence references

- Artifact root: `<local-path>/projects/active-pretraining-dynamic-data-selection-via-loss-probing-7511ebb5644b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
