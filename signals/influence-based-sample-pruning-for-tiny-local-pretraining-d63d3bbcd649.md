# Influence-Based Sample Pruning for Tiny Local Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `influence-based-sample-pruning-for-tiny-local-pretraining-d63d3bbcd649`
Run ID: `influence-based-sample-pruning-for-tiny-local-pretraining-d63d3bbcd649-20260619T043513209001+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fc6676296d4e

## What looked useful

Influence-top pruning reached mean target test loss 0.582 versus random-pruned 3.259, loss-low 4.676, full scored pool 0.834, and influence-bottom 9.019. It selected 77.4% target samples on average versus 26.1% for random, while the anti-influence control selected almost no target samples and failed.

## Boundaries and scale limits

Synthetic corpus only; 3 seeds; 720 candidate sequences per seed; 35% keep fraction; 220 training steps per strategy; tiny 2-layer Transformer; no real text corpus, no tokenizer effects, no GPT-2-small-class validation, no downstream tasks, and no iterative influence recomputation.

## Claim scope

In a controlled synthetic tiny causal-Transformer pretraining task with target, near, distractor, and random domains, one-shot gradient-alignment influence pruning selected substantially more target-domain samples and achieved lower held-out target next-token loss than random pruning, low-initial-loss pruning, and a bottom-influence control under the same training budget.

## Why it stopped

Closed as no-paper useful signal: the mechanism worked in a synthetic proxy, but this is not direct/full validation of local language-model pretraining.

## Recommended next action

Run a bounded real-text deepen test using the same equal-token-budget protocol on a small corpus with a held-out target domain before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text equal-budget validation of influence-based pruning for tiny local pretraining
- Success threshold: Influence-top improves mean target test loss by at least 5% relative to random-pruned and loss-low baselines at matched token budget in both keep fractions, with no catastrophic degradation relative to full-pool training.
- Stop condition: Stop if influence-top fails to beat random-pruned or loss-low in either keep fraction, or if scoring overhead exceeds the saved training time by more than 2x for the tiny setup.

## Evidence references

- Artifact root: `<local-path>/projects/influence-based-sample-pruning-for-tiny-local-pretraining-d63d3bbcd649`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
