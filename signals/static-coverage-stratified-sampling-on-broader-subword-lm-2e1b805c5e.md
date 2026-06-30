# Static coverage-stratified sampling on broader subword LM validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `static-coverage-stratified-sampling-on-broader-subword-lm-2e1b805c5e`
Run ID: `static-coverage-stratified-sampling-on-broader-subword-lm-2e1b805c5e-20260520T121110062749+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-corpus tiny transformer test of coverage-stratified sampling: enoch://control-plane/projects/real-corpus-tiny-transformer-test-of-coverage-stratified-s-137ab708b3/runs/real-corpus-tiny-transformer-test-of-coverage-stratified-s-137ab708b3-20260520T115514465556+0000
- Parent run decision: Annealed coverage-stratified sampling on subword tiny Transformer: enoch://control-plane/projects/annealed-coverage-stratified-sampling-on-subword-tiny-tran-9936470597/runs/annealed-coverage-stratified-sampling-on-subword-tiny-tran-9936470597-20260520T120046665396+0000

## What looked useful

Coverage stratification improved aggregate paired absolute NLL error versus uniform with mean improvement 0.00543, median improvement 0.00341, 60.9% win rate, and one-sided paired Wilcoxon p=0.00273 across 192 comparisons. At 512 windows it had the best mean absolute error, 0.00871 vs 0.01717 for uniform, with 75.0% paired win rate. However, the no-rare ablation often performed better, indicating the rare-token coverage mechanism is mixed.

## Boundaries and scale limits

Three GPT-2-family checkpoints, two corpora, sequence length 128, up to 4096 windows per corpus/model, 8 fixed sampling seeds. Tokenizer diversity was limited because cached Pythia/TinyStories model snapshots lacked usable local weights and online loading stalled. This does not test training-time model selection or large multi-domain validation suites.

## Claim scope

On a bounded local sweep of distilgpt2, gpt2, and gpt2-medium over Wikitext-2 and TinyStories validation windows, static tokenizer-derived stratification can reduce subset-estimator absolute NLL error versus uniform random sampling, especially at 512 validation windows.

## Why it stopped

Moderate direct estimator evidence supports a scoped mechanism, but it is mixed and not paper-ready because the no-rare ablation often beats full coverage stratification and tokenizer/model diversity remains limited.

## Recommended next action

Stop this run as no-paper useful signal; if continuing within the campaign, run a bounded deepen test focused on feature ablations and tokenizer-diverse checkpoints rather than scaling only.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Feature-ablation and tokenizer-diverse validation of static LM subset stratification
- Success threshold: Across tokenizer-diverse model/corpus cells, the best static coverage-feature method achieves at least 25% lower mean absolute NLL estimation error than uniform, at least 60% paired win rate, and no degradation in checkpoint-ranking preservation relative to length-only stratification.
- Stop condition: Stop if no static coverage-feature method beats both uniform and length-only controls by at least 10% mean absolute error reduction or if gains disappear on non-GPT-2 tokenizer families.

## Evidence references

- Artifact root: `<local-path>/projects/static-coverage-stratified-sampling-on-broader-subword-lm-2e1b805c5e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
