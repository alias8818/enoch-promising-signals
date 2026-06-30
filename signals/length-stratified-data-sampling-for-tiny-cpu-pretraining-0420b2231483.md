# Length-stratified data sampling for tiny CPU pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `length-stratified-data-sampling-for-tiny-cpu-pretraining-0420b2231483`
Run ID: `length-stratified-data-sampling-for-tiny-cpu-pretraining-0420b2231483-20260614T003202619805+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/673e4bee7fe3

## What looked useful

Naive equal length-bucket sampling appears to redistribute error toward short examples rather than robustly improving all length buckets. Future tests should preserve token-mass exposure while isolating batch-shape or curriculum effects.

## Boundaries and scale limits

Synthetic corpus only; tiny NumPy n-gram LM only; 5 seeds; 1500 steps per strategy; no real tokenizer, transformer, downstream task, or large-scale pretraining evidence.

## Claim scope

In a bounded synthetic CPU-only tiny neural n-gram LM probe, equal-bucket length-stratified sampling improved short-bucket validation loss and slightly improved mean validation loss, but did not improve long-bucket or worst-bucket validation loss versus a token-mass baseline.

## Why it stopped

Proxy synthetic evidence is mixed: length stratification improved mean and short-bucket loss but slightly worsened worst-bucket and long-bucket loss, so it is not a full validation or paper-positive result.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use a tiny transformer on a real tokenized corpus with token-budget-matched length schedules.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-budget-matched length schedules for a tiny transformer on real text
- Success threshold: Worst-bucket validation perplexity improves by at least 2 percent versus token-mass baseline with no more than 1 percent mean perplexity regression across at least 3 seeds.
- Stop condition: Stop if equal-bucket or token-mass-preserving schedules fail to improve worst-bucket perplexity in 2 consecutive seeds or exceed the local CPU/GPU budget without checkpointed metrics.

## Evidence references

- Artifact root: `<local-path>/projects/length-stratified-data-sampling-for-tiny-cpu-pretraining-0420b2231483`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
