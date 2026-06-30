# Gradient Coreset Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-coreset-tiny-pretraining-35b3fce77422`
Run ID: `gradient-coreset-tiny-pretraining-35b3fce77422-20260523T050704378417+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bb1f540afb65

## What looked useful

Gradient-space diversity avoided the severe skew and degradation of high-loss selection and selected more balanced domains, but its mean test-loss gain over random was only -0.011 with paired seed stdev 0.059 and one of three seeds regressed.

## Boundaries and scale limits

Synthetic corpus only, three seeds, tiny Transformer, 768 training sequences per seed, 260 subset-training steps, LM-head gradient embeddings only, no natural-language corpus or GPT-2-small-class validation.

## Claim scope

On a synthetic heterogeneous character pretraining task with a tiny 2-layer causal Transformer and 25% subset budget, LM-head gradient k-center selection slightly improved mean test loss versus random but the paired effect was small and not robust across three seeds; high-loss selection was worse than random.

## Why it stopped

Proxy/small-scale synthetic evidence is insufficient for a positive claim: gradient k-center was only marginally better than random on average and not robust across seeds, although it falsified naive high-loss selection and produced a concrete follow-up target.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded medium follow-up on a real text corpus with a GPT-2-small-class or parameter-matched tiny baseline, at least five seeds/shards, and a predeclared success threshold of >=0.03 held-out loss improvement over random without domain regressions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Real-Corpus Gradient Coreset Validation
- Success threshold: Mean held-out loss improvement versus random of at least 0.03 with paired improvement on at least 4 of 5 seeds/shards and no severe rare-domain regression.
- Stop condition: Stop if gradient coreset fails to beat random by 0.03 mean held-out loss, regresses on more than one seed/shard, or the apparent gain is explained by a simpler domain-balancing baseline.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-coreset-tiny-pretraining-35b3fce77422`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
