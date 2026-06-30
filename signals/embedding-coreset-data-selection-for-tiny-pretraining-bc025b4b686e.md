# Embedding Coreset Data Selection for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `embedding-coreset-data-selection-for-tiny-pretraining-bc025b4b686e`
Run ID: `embedding-coreset-data-selection-for-tiny-pretraining-bc025b4b686e-20260608T180946409046+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7039c70da27b

## What looked useful

K-center embedding coreset selection increased mean max-cosine coverage from 0.5000 for random to 0.5371 and reduced mean validation loss from 2.58933 to 2.58527; centroid and longest baselines had lower coverage and worse validation loss, indicating the selection objective matters.

## Boundaries and scale limits

Toy character-level model, WikiText-2 only, 260-step fits, one selected subset per deterministic method, three model seeds, no BPE/GPT-2-small-class pretraining, no downstream transfer tasks, and no larger-corpus or multi-budget scaling validation.

## Claim scope

On a bounded WikiText-2 character-level tiny-transformer pretraining probe with a fixed 180k-character selection budget and 260 optimizer steps per fit, stable hashed TF-IDF k-center document selection improved embedding coverage and slightly reduced validation loss versus three random-subset seeds; centroid and longest-document selections were worse than random.

## Why it stopped

Bounded local evidence supports only a small mechanism signal, not publication-grade validation of embedding coreset data selection for tiny pretraining.

## Recommended next action

Stop this run as no-paper useful signal; run a medium token-level follow-up with a GPT-2-small-class or parameter-matched BPE transformer, multiple budget fractions, and random confidence intervals before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium BPE-LM Validation of K-Center Embedding Coresets
- Success threshold: K-center must reduce mean held-out perplexity by at least 1 percent versus random at two or more budget fractions with confidence intervals that do not overlap random, without losing to the heuristic baseline.
- Stop condition: Stop if k-center fails to beat random by 1 percent at two budget fractions or if gains disappear on the second corpus.

## Evidence references

- Artifact root: `<local-path>/projects/embedding-coreset-data-selection-for-tiny-pretraining-bc025b4b686e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
