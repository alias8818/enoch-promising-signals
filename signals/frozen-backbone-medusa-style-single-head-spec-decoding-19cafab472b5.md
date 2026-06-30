# Frozen-backbone Medusa-style single-head spec decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `frozen-backbone-medusa-style-single-head-spec-decoding-19cafab472b5`
Run ID: `frozen-backbone-medusa-style-single-head-spec-decoding-19cafab472b5-20260628T041333422987+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/65b34aa17811

## What looked useful

A frozen-backbone single Medusa-style head is trainable and beats a unigram baseline on corpus future-token prediction for early offsets, but its target-greedy rollout agreement is low: mean exact prefix 0.3047/4 over 128 contexts after the longer run.

## Boundaries and scale limits

Single backbone, Wikitext-2 only, offsets 1..4, short 600-step head training, corpus-future labels rather than target-rollout distillation, no actual speculative acceptance or latency benchmark, no multi-head Medusa control.

## Claim scope

On a frozen distilgpt2 backbone with Wikitext-2, one shared offset-conditioned head learns measurable future-token prediction signal for offsets 1-3 and marginal signal for offset 4, but target-greedy draft agreement remains too weak to support a speculative decoding speedup claim.

## Why it stopped

No-paper useful signal: bounded local evidence supports partial mechanism viability, but direct speculative decoding acceptance and speedup evidence were not produced and the target-greedy proxy remains weak.

## Recommended next action

Run a bounded direct speculative-decoding follow-up: train the single head on target-model rollout labels and compare verifier acceptance/throughput against a parameter-matched multi-head Medusa baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Target-rollout-trained single-head versus multi-head Medusa acceptance
- Success threshold: Single-head target-rollout training reaches at least 0.75 accepted tokens per draft on held-out contexts and is within 10% of the multi-head Medusa accepted-prefix metric while using fewer or equal trainable parameters.
- Stop condition: Stop if after a calibrated bounded run the single-head accepted-prefix metric remains below 0.5 tokens per draft or trails the parameter-matched multi-head baseline by more than 25%.

## Evidence references

- Artifact root: `<local-path>/projects/frozen-backbone-medusa-style-single-head-spec-decoding-19cafab472b5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
