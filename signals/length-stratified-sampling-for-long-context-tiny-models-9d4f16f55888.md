# Length-Stratified Sampling for Long-Context Tiny Models

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `length-stratified-sampling-for-long-context-tiny-models-9d4f16f55888`
Run ID: `length-stratified-sampling-for-long-context-tiny-models-9d4f16f55888-20260525T061031403733+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4f52e446edcb

## What looked useful

Long examples already consumed about one-third of tokens under the 70/20/10 natural example distribution. Equal example stratification raised long-token share above 62%, reduced optimizer updates, and failed to improve long accuracy; at 20M tokens uniform_natural reached 48.9% long accuracy while stratified_equal remained at 11.7%.

## Boundaries and scale limits

Synthetic retrieval only; one tiny transformer architecture; max sequence length 114 tokens; three seeds at 5M tokens plus one 20M-token persistence seed; not a natural-language pretraining or downstream long-context benchmark.

## Claim scope

In a synthetic online key-value retrieval task with a 118k-parameter causal transformer and matched training-token budgets, naive example-level length stratification did not improve long-context accuracy over a natural length sampler and was much worse in a 20M-token seed-0 persistence check.

## Why it stopped

Proxy synthetic evidence falsified the tested naive length-stratified sampling mechanism under matched token budgets; this is not a full natural-language validation.

## Recommended next action

Stop this run as a no-paper bounded negative; if continuing locally, test a token-mass-aware curriculum rather than naive example-count length stratification.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-mass-aware length curriculum for tiny long-context retrieval
- Success threshold: Token-mass-aware or staged curriculum improves long-bucket accuracy by at least 5 absolute percentage points over uniform_natural without reducing short or medium accuracy by more than 2 absolute percentage points at the same token budget.
- Stop condition: Stop if the token-aware curriculum is not better than uniform_natural on mean long accuracy over three seeds or if gains require materially more tokens/updates.

## Evidence references

- Artifact root: `<local-path>/projects/length-stratified-sampling-for-long-context-tiny-models-9d4f16f55888`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
