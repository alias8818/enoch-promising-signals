# LoRA-Early-Exit Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lora-early-exit-speculative-decoding-bdf39a1e422b`
Run ID: `lora-early-exit-speculative-decoding-bdf39a1e422b-20260515T080511307385+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2cb7be81ce02

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Proxy/early falsification: direct GPT-2/WikiText-2 drafter-quality tests showed LoRA adapters improve early-exit agreement, but an optimistic speculative speed bound stayed below 1.0x for every tested layer/rank.

## Recommended next action

Stop this run as an early proxy falsification of LoRA-hidden-residual early-exit speculative decoding; only revisit with a cache-reuse implementation that can demonstrate draft cost below the naive layer fraction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cache-Reuse Early-Exit Speculative Decode Benchmark
- Success threshold: At least 1.15x wall-clock tokens/second over vanilla target decoding and no correctness failures on the benchmark prompt set.
- Stop condition: Stop if cache reuse cannot reduce measured draft cost below 25% of a full target step or if end-to-end speed remains below 1.05x after one bounded implementation pass.

## Evidence references

- Artifact root: `<local-path>/projects/lora-early-exit-speculative-decoding-bdf39a1e422b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
