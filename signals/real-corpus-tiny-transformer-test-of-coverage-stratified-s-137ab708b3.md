# Real-corpus tiny transformer test of coverage-stratified sampling

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-corpus-tiny-transformer-test-of-coverage-stratified-s-137ab708b3`
Run ID: `real-corpus-tiny-transformer-test-of-coverage-stratified-s-137ab708b3-20260520T115514465556+0000`

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

- Parent run decision: Stratified coverage sampling for tiny pretraining: enoch://control-plane/projects/stratified-coverage-sampling-for-tiny-pretraining-8f84a2d6d8f9/runs/stratified-coverage-sampling-for-tiny-pretraining-8f84a2d6d8f9-20260520T114547352371+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b491ee72200a

## What looked useful

Coverage-stratified sampling increased minimum rare-token exposure from 0.0 to 3.7 and reduced rare-token validation loss by 0.804 nats on average, but increased overall validation loss by 0.0124 nats and sampled fewer unique training windows. Mechanism support is present, but broad training benefit is mixed.

## Boundaries and scale limits

Character-level Tiny Shakespeare only; 65-token vocabulary; 2-layer width-64 Transformer; 716,800 training tokens per trial; 3 seeds; no subword tokenization, GPT-2-small-class baseline, larger corpus, or long convergence test.

## Claim scope

In a 3-seed Tier 1 direct test on Tiny Shakespeare with a 2-layer character-level causal Transformer trained for 350 steps, coverage-stratified sampling improved rare-token exposure and rare-token validation loss but slightly worsened overall validation loss versus uniform random sampling.

## Why it stopped

Tier 1 direct evidence produced a useful no-paper signal: rare-token coverage improved, but the overall validation-loss penalty prevents a positive paper decision.

## Recommended next action

Run a bounded medium confirmation with a subword-tokenized real corpus and an annealed coverage sampler, requiring rare-token loss gains without an overall validation-loss penalty before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Annealed coverage-stratified sampling on subword tiny Transformer
- Success threshold: Annealed coverage reduces rare-token validation loss by at least 5% versus random and keeps overall validation loss within +0.002 nats of random or better across at least 5 matched seeds.
- Stop condition: Stop if annealed coverage still increases overall validation loss by more than 0.002 nats or fails to improve rare-token validation loss by 5% under matched training-token budget.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-tiny-transformer-test-of-coverage-stratified-s-137ab708b3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
