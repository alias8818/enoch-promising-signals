# 2-Bit QAT with Residual Channels on CPU

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `2-bit-qat-with-residual-channels-on-cpu-9d934f764cda`
Run ID: `2-bit-qat-with-residual-channels-on-cpu-9d934f764cda-20260604T233815499346+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/bc4eb80e5e73

## What looked useful

Plain 2-bit QAT averaged 0.959822 final accuracy versus 0.963606 dense. Residual-channel 2-bit averaged 0.960490 at 12.5% FP32 hidden channels and 0.961269 at 25%, but with effective weight bits increasing to 5.75 and 9.5 respectively. Seed-level gains over plain 2-bit changed sign.

## Boundaries and scale limits

Small one-hidden-layer MLP, OptDigits only, weight-only fake quantization, no packed 2-bit CPU kernels, no activation quantization, no transformer/CNN workloads, and no learned residual allocation.

## Claim scope

On a CPU-only NumPy MLP probe using UCI OptDigits, fixed FP32 residual hidden channels inside 2-bit QAT recover only a tiny amount of accuracy over plain 2-bit QAT and do not justify a paper-positive claim.

## Why it stopped

Bounded direct CPU probe found only tiny, seed-unstable residual-channel gains relative to the effective-bit and storage cost; this is not full validation and not paper-positive.

## Recommended next action

Stop this run as a no-paper useful signal; only revisit if testing a larger model with a real packed CPU inference cost model or a learned residual-channel allocation method.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-qat-with-residual-channels-on-cpu-9d934f764cda`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
