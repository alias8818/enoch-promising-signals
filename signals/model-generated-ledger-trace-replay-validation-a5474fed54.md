# Model-Generated Ledger Trace-Replay Validation

Status: `useful_signal`
Project ID: `model-generated-ledger-trace-replay-validation-a5474fed54`
Run ID: `model-generated-ledger-trace-replay-validation-a5474fed54-20260515T182302603508+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Model-Generated Ledger Trace-Replay Validation: internal_generated:model-generated-ledger-trace-replay-validation-a5474fed54

## What looked useful

Trace replay achieved 100% invalid detection and 100% valid acceptance on the synthetic benchmark, versus 33.3% invalid detection for double-entry and final-balance baselines; ablations showed event contracts, references, and resource checks each contributed coverage.

## Boundaries and scale limits

No real LLM-generated ledger traces were evaluated. The test uses a closed-world event schema, synthetic corruptions, 10 fixed seeds, 3,000 valid traces, and 3,000 invalid traces of length 60.

## Claim scope

In a deterministic synthetic benchmark of model-like ledger trace corruptions, replay validation against event contracts, references, and resource state detected balanced semantic errors that schema, double-entry, and final-balance baselines missed.

## Why it stopped

Tier 2 synthetic evidence supports the mechanism but is not paper-positive evidence for real model-generated ledger traces.

## Recommended next action

Evaluate the same validators on an adjudicated corpus of actual LLM-generated ledger traces from at least two model families before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-Generated Ledger Trace-Replay Benchmark
- Success threshold: Replay improves invalid detection by at least 25 percentage points over the best real baseline with bootstrap 95% CI lower bound above 10 points and valid acceptance at least 95%.
- Stop condition: Stop if replay improves invalid detection by less than 10 percentage points over the best baseline or rejects more than 10% of adjudicated valid traces.

## Evidence references

- Artifact root: `<local-path>/projects/model-generated-ledger-trace-replay-validation-a5474fed54`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
