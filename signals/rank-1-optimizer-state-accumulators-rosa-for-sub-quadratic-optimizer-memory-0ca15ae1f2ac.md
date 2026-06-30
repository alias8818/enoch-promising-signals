# Rank-1 Optimizer State Accumulators (ROSA) for Sub-Quadratic Optimizer Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `rank-1-optimizer-state-accumulators-rosa-for-sub-quadratic-optimizer-memory-0ca15ae1f2ac`
Run ID: `rank-1-optimizer-state-accumulators-rosa-for-sub-quadratic-optimizer-memory-0ca15ae1f2ac-20260520T111109951590+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4bf726152d4b

## What looked useful

The mechanism is practically viable as an Adafactor-style memory reducer in bounded probes, but the rank-1 reconstructed second moment is not a close estimator of dense Adam v (relative Frobenius error about 0.79-0.91), and the idea is not novel enough for a paper as specified.

## Boundaries and scale limits

Synthetic quadratic matrix objectives only; no neural network training, no first-moment state, no AdamW comparison, no stochastic minibatches, no mixed precision, and no large-model validation. The tested row/column factored second-moment mechanism overlaps directly with Adafactor prior art.

## Claim scope

A row/column rank-1 second-moment accumulator for square matrix parameters reduced v-only optimizer state by 128x at n=256 and 256x at n=512 in deterministic NumPy quadratic probes, while matching or beating dense v-only Adam's best swept final loss on the tested synthetic objectives.

## Why it stopped

No-paper useful signal: the local mechanism test is positive, but the core row/column factored second-moment accumulator is already established by Adafactor and the evidence is synthetic/proxy-only rather than direct model-training validation.

## Recommended next action

Stop this ROSA formulation as a paper candidate unless a clearly distinct mechanism beyond Adafactor is specified; otherwise use these artifacts as a bounded baseline/probe for future memory-efficient optimizer work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Distinguish ROSA from Adafactor on Small Transformer Training
- Success threshold: ROSA must match Adafactor validation loss within 2% and beat AdamW optimizer-state memory by at least 2x, or beat Adafactor validation loss by at least 3% at comparable memory, across at least 3 seeds.
- Stop condition: Stop if ROSA is algorithmically equivalent to Adafactor, or if it fails to match Adafactor within 2% validation loss under the matched tuning budget.

## Evidence references

- Artifact root: `<local-path>/projects/rank-1-optimizer-state-accumulators-rosa-for-sub-quadratic-optimizer-memory-0ca15ae1f2ac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
