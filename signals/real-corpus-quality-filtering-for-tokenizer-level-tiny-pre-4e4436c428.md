# Real-corpus quality filtering for tokenizer-level tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-corpus-quality-filtering-for-tokenizer-level-tiny-pre-4e4436c428`
Run ID: `real-corpus-quality-filtering-for-tokenizer-level-tiny-pre-4e4436c428-20260621T091024464568+0000`

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

- Parent run decision: Quality-filtered data selection for tiny pretraining: enoch://control-plane/projects/quality-filtered-data-selection-for-tiny-pretraining-039806429081/runs/quality-filtered-data-selection-for-tiny-pretraining-039806429081-20260621T085457906431+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/094f0ceaee0d

## What looked useful

Filtered training reached clean validation loss 7.5520 versus 7.6741 for the random control, a -0.1221 loss delta that exceeded the predefined -0.02 Tier 1 threshold; random validation also improved slightly by -0.0157.

## Boundaries and scale limits

Single seed, one corpus shard, one short tiny-model run, no component ablations, no downstream tasks, no GPT-2-small-class or long-horizon validation.

## Claim scope

On one 2,500-document FineWeb sample-10BT slice, a GPT-2-tokenizer quality filter improved 180-step tiny GPT-style LM clean-validation loss versus a random real-corpus control at the same 120,576 blocked-token training budget.

## Why it stopped

Tier 1 direct test met the threshold, but evidence remains too narrow for publication-grade claims.

## Recommended next action

Run a bounded deepen follow-up with at least 5 seeds, 3 independent FineWeb shards, longer training, and score-component ablations; do not write a paper from this single Tier 1 signal.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-seed FineWeb tokenizer-quality filtering confirmation
- Success threshold: Mean filtered clean-validation loss improves by at least 0.05 over random control with no worse than +0.02 random-validation loss, and at least 4 of 5 seeds show clean-validation improvement on each shard.
- Stop condition: Stop if the mean clean-validation improvement is below 0.02 after the planned seeds/shards or if ablations show the full filter is indistinguishable from random selection.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-quality-filtering-for-tokenizer-level-tiny-pre-4e4436c428`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
