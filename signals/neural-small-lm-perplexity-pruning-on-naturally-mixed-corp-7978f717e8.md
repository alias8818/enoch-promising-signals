# Neural small-LM perplexity pruning on naturally mixed corpus shards

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `neural-small-lm-perplexity-pruning-on-naturally-mixed-corp-7978f717e8`
Run ID: `neural-small-lm-perplexity-pruning-on-naturally-mixed-corp-7978f717e8-20260619T192231423500+0000`

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

- Parent run decision: Perplexity-Guided Pruning of Tiny Pretraining Corpus: enoch://control-plane/projects/perplexity-guided-pruning-of-tiny-pretraining-corpus-ba8d1898ee42/runs/perplexity-guided-pruning-of-tiny-pretraining-corpus-ba8d1898ee42-20260619T185602098454+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/86b6ef8f5ec2

## What looked useful

Mechanism support exists for perplexity as an off-target shard filter, but the controlled downstream perplexity gain did not meet the predeclared 3% threshold.

## Boundaries and scale limits

Small CPU-only character LM, ASCII normalization, Project Gutenberg English target plus Spanish/French/German mixed shards, limited random replicates, no transformer/BPE model and no broad web-corpus validation.

## Claim scope

On a bounded public-domain natural-text mixture of 731 character shards, a small NumPy neural character-LM scorer filtered off-target multilingual shards but improved held-out target LM perplexity by only 0.7-1.8% versus same-budget random controls across 25%, 50%, and 75% retention.

## Why it stopped

Direct Tier 1 controlled test and retention sweep failed the 3% improvement threshold; this is useful mechanism evidence, not full validation or paper-positive evidence.

## Recommended next action

Run one bounded transformer/BPE follow-up on the same shard manifest with language-ID or quality-filter baselines; stop if it still fails to reach a 3% held-out perplexity gain over random-budget controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer/BPE check for perplexity pruning on the same natural shard manifest
- Success threshold: At least 3% lower held-out target perplexity than random-budget mean and better than simple language/quality-filter baselines.
- Stop condition: Stop if the transformer/BPE run improves held-out perplexity by less than 3% or fails to beat simple language/quality-filter controls.

## Evidence references

- Artifact root: `<local-path>/projects/neural-small-lm-perplexity-pruning-on-naturally-mixed-corp-7978f717e8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
