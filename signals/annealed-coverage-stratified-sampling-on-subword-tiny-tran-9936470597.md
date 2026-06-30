# Annealed coverage-stratified sampling on subword tiny Transformer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `annealed-coverage-stratified-sampling-on-subword-tiny-tran-9936470597`
Run ID: `annealed-coverage-stratified-sampling-on-subword-tiny-tran-9936470597-20260520T120046665396+0000`

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

- Parent run decision: Real-corpus tiny transformer test of coverage-stratified sampling: enoch://control-plane/projects/real-corpus-tiny-transformer-test-of-coverage-stratified-s-137ab708b3/runs/real-corpus-tiny-transformer-test-of-coverage-stratified-s-137ab708b3-20260520T115514465556+0000
- Parent run decision: Stratified coverage sampling for tiny pretraining: enoch://control-plane/projects/stratified-coverage-sampling-for-tiny-pretraining-8f84a2d6d8f9/runs/stratified-coverage-sampling-for-tiny-pretraining-8f84a2d6d8f9-20260520T114547352371+0000

## What looked useful

Coverage stratification appears useful for rare-subword exposure, but the annealed schedule is not the clean mechanism winner: static coverage beat annealed coverage on rare-token validation loss in 5/5 paired seeds.

## Boundaries and scale limits

Single small public corpus, tiny Transformer, 512-token local BPE tokenizer, 5 fixed seeds, 2,000 training steps per run; not validated on GPT-2-small-class models, broad web/text corpora, external tokenizers, or long training horizons.

## Claim scope

On Tiny Shakespeare with a locally trained 512-token byte-pair subword vocabulary and a tiny 2-layer Transformer, coverage-stratified sampling improved rare-subword validation loss versus uniform sampling under equal token budgets; the tested annealed schedule improved all-token loss but did not beat static coverage on the rare-token target.

## Why it stopped

Tier 2 fixed-seed evidence is mixed: annealed coverage improved versus uniform but failed the stronger ablation against static coverage on the rare-token target metric.

## Recommended next action

Stop this annealed-schedule claim as no-paper; branch only if testing static or schedule-swept coverage stratification on a broader corpus with a larger parameter-matched Transformer.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Static coverage-stratified sampling on broader subword LM validation
- Success threshold: Static or tuned coverage must reduce rare-subword validation loss by at least 0.05 nats versus uniform in at least 4/5 paired seeds while keeping all-token validation loss no worse than +0.01 nats, and must beat the naive annealed schedule on rare-token loss.
- Stop condition: Stop if coverage variants fail to beat uniform rare-token validation loss in at least 3/5 paired seeds or if all-token validation loss degrades by more than 0.02 nats under equal compute.

## Evidence references

- Artifact root: `<local-path>/projects/annealed-coverage-stratified-sampling-on-subword-tiny-tran-9936470597`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
