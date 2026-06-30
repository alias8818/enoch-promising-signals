# Real-corpus learned vs heuristic filtering for tiny decoder pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-corpus-learned-vs-heuristic-filtering-for-tiny-decode-e44827e011`
Run ID: `real-corpus-learned-vs-heuristic-filtering-for-tiny-decode-e44827e011-20260613T161811237916+0000`

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

- Parent run decision: Heuristic vs Learned Quality Filtering for Tiny Pretraining: enoch://control-plane/projects/heuristic-vs-learned-quality-filtering-for-tiny-pretraining-10d6b6c66dc4/runs/heuristic-vs-learned-quality-filtering-for-tiny-pretraining-10d6b6c66dc4-20260613T155243132078+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8c652a0ea698

## What looked useful

The learned scorer selected far more target-domain sci.space chunks than random or heuristic baselines, but produced worse held-out sci.space decoder loss than random and the best heuristic. This suggests target-domain concentration alone can reduce useful diversity for tiny decoder pretraining.

## Boundaries and scale limits

Single corpus, one target domain, character-level tiny Transformer, 420k-character selected subsets, 700 training steps, three seeds. Not a test of web-scale filtering, tokenizer-level GPT-class pretraining, larger decoders, human quality labels, or long training.

## Claim scope

In a controlled Tier 1 real-corpus 20 Newsgroups test targeting held-out sci.space text, a small supervised learned domain filter did not improve tiny causal decoder validation loss over the best hand-coded heuristic or random selection at matched byte and training budgets.

## Why it stopped

Direct Tier 1 threshold failed: learned mean final validation loss was 2.6220 versus 2.5769 for the best heuristic and 2.5599 for random; learned margin versus best heuristic was -0.0451 nats/token, below the required +0.02.

## Recommended next action

Stop this hypothesis as a no-paper Tier 1 negative; if continuing, run a bounded diversity-constrained learned-filter follow-up that must beat both random and the best heuristic across at least two target domains.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Diversity-constrained learned filtering for tiny decoder pretraining
- Success threshold: Diversity-constrained learned filtering beats both random and the best heuristic by at least 0.02 nats/token mean final validation loss on each target domain across three seeds.
- Stop condition: Stop if diversity-constrained learned filtering fails to beat random or the best heuristic on either target domain under the matched budget.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-learned-vs-heuristic-filtering-for-tiny-decode-e44827e011`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
