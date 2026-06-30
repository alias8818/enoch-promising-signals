# Influence pruning on a real-corpus tiny transformer pretraining budget

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `influence-pruning-on-a-real-corpus-tiny-transformer-pretra-299295f84b`
Run ID: `influence-pruning-on-a-real-corpus-tiny-transformer-pretra-299295f84b-20260619T084731077836+0000`

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

- Parent run decision: Influence-Function Data Pruning for Tiny Local Pretraining: enoch://control-plane/projects/influence-function-data-pruning-for-tiny-local-pretraining-b44ab1ad09a1/runs/influence-function-data-pruning-for-tiny-local-pretraining-b44ab1ad09a1-20260619T083111473886+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8977943e21b7

## What looked useful

Influence-style LM-head gradient alignment consistently rejected harmful bottom-scored examples and strongly beat the anti-influence control; it is a useful mechanism signal but not a paper-positive validation of full tiny transformer pretraining.

## Boundaries and scale limits

This did not train all transformer weights end to end; the available worker lacked PyTorch/Transformers and tinygrad CPU compilation required missing clang, while the pure Python backend was too slow. Corpus, model, and seed count are small.

## Claim scope

In a three-seed Tiny Shakespeare Tier-1 run using a frozen tiny causal self-attention feature extractor with a trainable next-token LM head, pruning the bottom 25% of examples by validation-gradient alignment improved validation loss versus dense training on all seeds and versus random pruning on two of three seeds.

## Why it stopped

Closed as no-paper useful signal: direct real-corpus evidence supports the pruning mechanism in a narrowed LM-head setting, but full end-to-end tiny transformer pretraining was not validated and random pruning was not uniformly beaten.

## Recommended next action

Run a bounded deepen follow-up on a worker with a compiled autodiff backend, training all weights of a parameter-matched tiny transformer with the same dense/random/anti-influence controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end tiny transformer influence pruning on real text
- Success threshold: Influence-pruned training has lower mean validation loss than dense and random-pruned controls and wins at least 4 of 5 seeds; anti-influence is worse than influence on at least 4 of 5 seeds.
- Stop condition: Stop as negative if influence pruning fails to beat random pruning on validation loss in at least 3 of 5 seeds or if anti-influence is not consistently worse, because that would undermine the scoring mechanism.

## Evidence references

- Artifact root: `<local-path>/projects/influence-pruning-on-a-real-corpus-tiny-transformer-pretra-299295f84b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
