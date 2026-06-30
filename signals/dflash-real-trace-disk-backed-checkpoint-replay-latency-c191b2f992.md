# DFlash real-trace disk-backed checkpoint replay latency

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `33`
Project ID: `dflash-real-trace-disk-backed-checkpoint-replay-latency-c191b2f992`
Run ID: `dflash-real-trace-disk-backed-checkpoint-replay-latency-c191b2f992-20260520T002932931863+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `33`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: DFlash checkpoint trace replay with measured branch latency: enoch://control-plane/projects/dflash-checkpoint-trace-replay-with-measured-branch-latenc-0947164db6/runs/dflash-checkpoint-trace-replay-with-measured-branch-latenc-0947164db6-20260520T002107041353+0000
- Parent run decision: Real DFlash Trace Replay for Spec Trace Oracle Branch Selection: enoch://control-plane/projects/real-dflash-trace-replay-for-spec-trace-oracle-branch-sele-6f670f66bf/runs/real-dflash-trace-replay-for-spec-trace-oracle-branch-sele-6f670f66bf-20260519T235546563709+0000

## What looked useful

Full eager restore had 0.94 s median total recovery, while lazy demand was 97.80 s and hotset prefetch was 100.09 s over 308 real-trace windows. Lazy replay needed a median 178.43 GiB checkpoint image, about 75.9x the observed checkpoint working set, to break even with full restore.

## Boundaries and scale limits

Trace-driven calibrated model rather than a kernel checkpoint implementation; capped at 4M records and 20 windows per trace; local single-thread random-read model does not include high queue-depth NVMe, application compute overlap, compression, or checkpoint images larger than the observed trace working set.

## Claim scope

On 18 public MSR Cambridge and Tencent CBS oracleGeneral real traces, using calibrated local disk sequential and random-read parameters, lazy disk-backed checkpoint replay and 1% hotset prefetch are slower than eager full checkpoint restore over 100k-request train/replay windows.

## Why it stopped

Bounded real-trace validation falsified the tested threshold/regime: calibrated random fault cost dominated replay and hotset prefetch did not improve p99 or total recovery versus lazy demand.

## Recommended next action

Stop this follow-up as a useful negative result; only revisit if a real implementation targets much larger checkpoint images or parallel low-latency random storage and can test that regime directly.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/dflash-real-trace-disk-backed-checkpoint-replay-latency-c191b2f992`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
