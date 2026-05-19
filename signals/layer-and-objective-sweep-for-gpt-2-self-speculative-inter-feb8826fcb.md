# Layer and objective sweep for GPT-2 self-speculative intermediate heads

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layer-and-objective-sweep-for-gpt-2-self-speculative-inter-feb8826fcb`
Run ID: `layer-and-objective-sweep-for-gpt-2-self-speculative-inter-feb8826fcb-20260516T171322955301+0000`

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

- Internal Enoch project: Layer and objective sweep for GPT-2 self-speculative intermediate heads: internal_generated:layer-and-objective-sweep-for-gpt-2-self-speculative-inter-feb8826fcb

## What looked useful

KL-distilled intermediate heads consistently improved target distribution-overlap acceptance over untrained tied heads and shuffled-label controls; best acceptance was layer 9 KL at 0.2617 mean overlap and 0.4077 greedy match over two seeds.

## Boundaries and scale limits

No saved head checkpoints, no actual multi-token speculative decoding loop, no wall-clock generation throughput benchmark, no larger models or datasets, and only 200 head-training steps per comparable chunk.

## Claim scope

Frozen GPT-2 small on Wikitext-2 with single linear auxiliary heads at hidden-state indices 3, 6, and 9; two fixed seeds; direct one-token draft-target distribution-overlap and greedy-match metrics.

## Why it stopped

Medium local evidence supports the mechanism but absolute acceptance is modest and direct end-to-end speculative decoding speedup was not tested, so this is useful no-paper evidence rather than publication-grade validation.

## Recommended next action

Run a bounded deepen study that saves layer 9 KL heads and measures exact speculative decoding acceptance and wall-clock throughput on Wikitext-2 prompts before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Checkpointed GPT-2 intermediate KL heads for actual speculative decoding throughput
- Success threshold: At least 1.05x wall-clock tokens/sec improvement over dense GPT-2 on the same hardware with acceptance >= 0.35 for a nontrivial draft length and no output-equivalence failures under the chosen decoding mode.
- Stop condition: Stop if layer 9 KL heads fail to reach 0.35 acceptance or 1.05x speedup under exact verification, or if control heads match the trained head throughput within measurement noise.

## Evidence references

- Artifact root: `<local-path>/projects/layer-and-objective-sweep-for-gpt-2-self-speculative-inter-feb8826fcb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
