# GPT-2-Small-Class Neural Embedding Shard Selection With Rarity Ablation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gpt-2-small-class-neural-embedding-shard-selection-with-ra-55a4d794f7`
Run ID: `gpt-2-small-class-neural-embedding-shard-selection-with-ra-55a4d794f7-20260607T195203939148+0000`

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

- Parent run decision: Embedding-Guided Shard Selection for Tiny Pretraining: enoch://control-plane/projects/embedding-guided-shard-selection-for-tiny-pretraining-dc545f8168ad/runs/embedding-guided-shard-selection-for-tiny-pretraining-dc545f8168ad-20260607T153416234749+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/74bd16827ba8

## What looked useful

Rarity features produced consistent routing specialization across seeds: rare/common shard-mass L1 rose from 0.0205 to 0.0686 mean. The primary performance threshold failed: rare-context loss changed from 2.11799 to 2.11895 mean, a +0.00096 nat worsening rather than the required at least 0.05 nat improvement.

## Boundaries and scale limits

Small synthetic controlled setting only: 2048-token vocabulary, 96 hidden size, 2 Transformer layers, 1200 train steps, 3 seeds. No natural-text GPT-2-small run, no dense embedding baseline, no hard top-k/capacity-constrained router, and no long training-scale validation.

## Claim scope

In a controlled 2-layer causal Transformer with 4 soft-mixture embedding shards on a Zipfian Markov language, adding explicit rarity features to the neural shard selector increases rare/common routing separation but does not improve rare-context validation loss versus the same selector without rarity features.

## Why it stopped

Tier 1 controlled direct test failed the predeclared rare-context improvement threshold. This is an early component-level falsification for the tested soft selector, not a full GPT-2-small natural-text validation.

## Recommended next action

Stop this run as a no-paper useful signal; the bounded next test should replace the soft mixture with hard or capacity-constrained shard selection and require a rare-context loss gain before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard Capacity Rarity-Aware Embedding Shard Selection
- Success threshold: Rarity-aware hard/capacity-constrained routing improves rare-context loss by at least 0.03 nats on the controlled task and does not degrade overall loss by more than 0.02 nats, with the effect positive in at least 2 of 3 seeds.
- Stop condition: Stop if hard/capacity-constrained rarity routing again changes routing specialization without improving rare-context loss, or if it degrades overall validation loss by more than 0.02 nats.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-neural-embedding-shard-selection-with-ra-55a4d794f7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
