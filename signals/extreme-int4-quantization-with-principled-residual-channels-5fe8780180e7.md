# Extreme INT4 Quantization with Principled Residual Channels

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `extreme-int4-quantization-with-principled-residual-channels-5fe8780180e7`
Run ID: `extreme-int4-quantization-with-principled-residual-channels-5fe8780180e7-20260605T210208292221+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/87c976834bf7

## What looked useful

Activation-aware residual channel selection recovered 14.6%, 15.0%, and 21.8% of no-residual INT4 NLL damage at 0.5%, 1%, and 2% residual budgets respectively; weight-norm recovered 4.3%, 7.0%, and 8.2%, while random recovered at most 2.7%.

## Boundaries and scale limits

Single model family member, one dataset, 64 calibration sequences, 128 eval sequences, no packed INT4 kernels, no serving latency or memory-bandwidth measurement, no robustness over calibration seeds or larger models.

## Claim scope

On GPT-2 small evaluated on 128 WikiText-2 test sequences, activation-aware selection of 0.5-2% residual full-precision projection output channels consistently recovers more INT4 post-training quantization loss than random or weight-norm residual selection.

## Why it stopped

This worker produced a bounded GPT-2/WikiText-2 quality signal, but not deployable INT4 memory/latency evidence or robustness sufficient for paper-positive closure.

## Recommended next action

Run a bounded deepen follow-up with packed or memory-faithful INT4 implementation, repeated calibration seeds, and at least two model/dataset pairs before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed INT4 Residual-Channel Validation Across Seeds and Models
- Success threshold: Activation-error selection recovers at least 10% more no-residual INT4 NLL damage than weight-norm selection on average while preserving an actual packed-model memory advantage over FP16.
- Stop condition: Stop if activation-error selection fails to beat weight-norm by 5% relative recovery on two model/dataset pairs or if packed residual bookkeeping erases the memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-int4-quantization-with-principled-residual-channels-5fe8780180e7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
