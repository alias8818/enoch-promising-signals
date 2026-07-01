# CPU-Budgeted Data Selection for Tiny Local Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-budgeted-data-selection-for-tiny-local-pretraining-cf22c401268c`
Run ID: `cpu-budgeted-data-selection-for-tiny-local-pretraining-cf22c401268c-20260613T100528273706+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/a19fd55a048f

## What looked useful

Similarity selection beat random and anti-similarity in 5/5 seeds, with mean random-minus-similarity target validation NLL of 0.8081 and mean relative NLL reduction of 16.71%.

## Boundaries and scale limits

Synthetic corpus, five seeds, tiny n-gram neural LM, no transformer, no real web/code corpus, no downstream evaluation.

## Claim scope

In a controlled synthetic mixed-domain corpus, cheap lexical similarity selection improved target-validation NLL for the same fixed sequence-item budget and tiny NumPy neural n-gram LM.

## Why it stopped

No-paper useful signal: the result supports the selection mechanism locally, but it is proxy/synthetic evidence rather than direct real-corpus transformer pretraining validation.

## Recommended next action

Run a bounded real-corpus follow-up using the same selector-vs-random design with a tiny transformer or GPT-2-small-class baseline before making any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny-transformer validation for CPU-budgeted lexical data selection
- Success threshold: Similarity selection must beat random on held-out target perplexity in at least 3/3 seeds by at least 5% relative perplexity reduction without materially higher wall-clock or memory.
- Stop condition: Stop if similarity does not beat random in at least two seeds, if preprocessing leakage is found, or if CPU-only runtime exceeds the deployment budget without producing checkpointed partial metrics.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-budgeted-data-selection-for-tiny-local-pretraining-cf22c401268c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
