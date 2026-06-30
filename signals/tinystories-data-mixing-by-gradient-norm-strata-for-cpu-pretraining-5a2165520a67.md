# TinyStories data mixing by gradient norm strata for CPU pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tinystories-data-mixing-by-gradient-norm-strata-for-cpu-pretraining-5a2165520a67`
Run ID: `tinystories-data-mixing-by-gradient-norm-strata-for-cpu-pretraining-5a2165520a67-20260524T201135573763+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5cef9dde20c1

## What looked useful

Balanced low/mid/high gradient-norm strata produced a small mean validation-loss improvement over uniform (+0.0095 loss delta across 3 seeds), but high-gradient weighted sampling and gradient-proportional sampling were consistently worse than uniform. High-gradient examples were not the synthetic hard examples, indicating an unsafe confound for naive gradient-norm mixing.

## Boundaries and scale limits

Not real TinyStories, not transformer-scale, not long pretraining, and no downstream generation-quality evaluation. Gradient norm was not length-normalized.

## Claim scope

Bounded synthetic TinyStories-style CPU probe with a tiny GRU language model, 3 seeds, per-example gradient-norm stratification after short warmup, and equal-step policy comparisons.

## Why it stopped

Proxy/local evidence is mixed and no-paper: balanced strata is a useful signal, but naive high-gradient mixing is an early falsification of the broad upweight-by-gradient-norm hypothesis rather than a full validation.

## Recommended next action

Run a bounded deepen test on a real TinyStories subset using length-normalized gradient norm, balanced-strata sampling, and a transformer baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Length-normalized gradient-norm strata on real TinyStories subset
- Success threshold: Balanced length-normalized gradient strata beats uniform by at least 0.02 validation loss on average across 3 seeds with no seed worse than uniform by more than 0.005, and high-gradient-only is not required for the gain.
- Stop condition: Stop if balanced length-normalized strata fails to beat uniform in at least 2 of 3 seeds or if gradient norm remains primarily a length/easiness proxy.

## Evidence references

- Artifact root: `<local-path>/projects/tinystories-data-mixing-by-gradient-norm-strata-for-cpu-pretraining-5a2165520a67`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
