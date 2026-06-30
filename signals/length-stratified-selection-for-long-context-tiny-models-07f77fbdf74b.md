# Length-stratified selection for long-context tiny models

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `length-stratified-selection-for-long-context-tiny-models-07f77fbdf74b`
Run ID: `length-stratified-selection-for-long-context-tiny-models-07f77fbdf74b-20260604T120213978378+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b57543c984e7

## What looked useful

Length stratification consumed over twice the training tokens of the short-skew baseline but had lower long-bin macro accuracy: 0.0692 versus 0.0770. Uniform length sampling also failed to improve long-bin accuracy at 0.0762.

## Boundaries and scale limits

This run used a synthetic retrieval task, one tiny architecture, fixed optimizer steps, and local GB10 compute. It did not train a real language model, use natural text, enforce equal-token/equal-FLOP budgets, or evaluate standard long-context benchmarks.

## Claim scope

In a synthetic associative-retrieval probe with a 2-layer 64-dimension tiny transformer trained for 5,000 steps across 3 seeds, naive length-stratified selection did not improve held-out long-context retrieval compared with a short-heavy selector.

## Why it stopped

Proxy/early falsification: the direct synthetic mechanism test did not show a long-context gain from naive length-stratified selection, so the claim is not supported without stronger direct evidence.

## Recommended next action

Stop this run as a no-paper early falsification; if pursued, run an equal-token/equal-FLOP small language-model follow-up before any larger validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Equal-token length stratification for a small long-context language model
- Success threshold: Length-stratified selection improves long-bucket accuracy or perplexity by at least 5% relative without more than 1% short-bucket regression across at least 3 seeds under equal token/FLOP budget.
- Stop condition: Stop if equal-budget length stratification does not beat the non-stratified baseline on long buckets after 3 seeds, or if gains disappear when short-context regression is constrained.

## Evidence references

- Artifact root: `<local-path>/projects/length-stratified-selection-for-long-context-tiny-models-07f77fbdf74b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
