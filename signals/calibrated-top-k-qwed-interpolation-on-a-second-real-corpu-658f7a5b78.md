# Calibrated top-k QWED interpolation on a second real corpus

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `100`
Project ID: `calibrated-top-k-qwed-interpolation-on-a-second-real-corpu-658f7a5b78`
Run ID: `calibrated-top-k-qwed-interpolation-on-a-second-real-corpu-658f7a5b78-20260518T203133566410+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `100`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Calibrated top-k QWED interpolation on a second real corpus: internal_generated:calibrated-top-k-qwed-interpolation-on-a-second-real-corpu-658f7a5b78

## What looked useful

QWED top-k improved mean test NLL by -0.0995 on WikiText-2 and -0.0582 on TinyStories versus distilgpt2, with all six corpus/seed cells improving NLL and mean top-1 accuracy deltas of +0.0015 and +0.0055. It also beat unweighted, random, and shuffled-target top-k controls by mean NLL on both corpora.

## Boundaries and scale limits

Single small GPT-2-family model, two English corpora, 32-token contexts, inference-only probability interpolation, no generation-quality evaluation, no larger-model validation, no long-context validation, no decode-time integration, and no bootstrap confidence intervals over query windows.

## Claim scope

On distilgpt2 next-token prediction with 32-token contexts, 30k retrieval candidates, 2k validation/test windows per seed, three fixed seeds, and two real corpora (WikiText-2 and TinyStories), validation-calibrated top-4 QWED interpolation improved test NLL versus the dense LM baseline without top-1 accuracy degradation.

## Why it stopped

No-paper useful-signal closure: the parent direct threshold was met on two real corpora with controls, but the evidence remains scoped to distilgpt2 inference-only probability smoothing rather than broad generation or larger-model validation.

## Recommended next action

Do not write a paper from this run; run one capped robustness follow-up only if testing whether the NLL and no-top1-drop signal persists on GPT-2-small-class scale, more corpora, top-k sensitivity, and bootstrap confidence intervals.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Depth-4 robustness validation of top-k QWED interpolation on GPT-2-small-class models
- Success threshold: Across at least three corpora, calibrated QWED top-k on GPT-2-small-class scale must improve mean test NLL by at least 0.02 versus dense LM, have a bootstrap 95% CI excluding zero for NLL delta on at least two corpora, have no corpus mean top-1 accuracy drop worse than 0.005, and beat unweighted/random/shuffled controls by mean NLL.
- Stop condition: Stop the QWED interpolation line as no-paper if the larger-model run fails the 0.02 mean NLL threshold on any corpus, if top-1 drops by more than 0.005 on any corpus, or if unweighted top-k matches QWED within bootstrap uncertainty.

## Evidence references

- Artifact root: `<local-path>/projects/calibrated-top-k-qwed-interpolation-on-a-second-real-corpu-658f7a5b78`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
