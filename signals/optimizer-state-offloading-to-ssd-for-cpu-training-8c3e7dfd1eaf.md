# Optimizer State Offloading to SSD for CPU Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `optimizer-state-offloading-to-ssd-for-cpu-training-8c3e7dfd1eaf`
Run ID: `optimizer-state-offloading-to-ssd-for-cpu-training-8c3e7dfd1eaf-20260629T045231752861+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4a5ef7e4f0eb

## What looked useful

Naive persistent whole-file memmap did not reduce process RSS after all optimizer pages were touched, but streaming chunk-level memmap reduced max RSS from 768.8 MB to 302.9 MB at 2.47x optimizer-update slowdown on the 60M-parameter proxy.

## Boundaries and scale limits

Not end-to-end model training; no autograd, data pipeline, validation metric, convergence study, asynchronous NVMe scheduling, or multi-GB/full-model scale. Project filesystem free space limited the state size to a sub-GB test.

## Claim scope

Bounded local CPU proxy: for a 60M-parameter synthetic Adam optimizer update, streaming shard-level SSD-backed memmap state reduced process max RSS by 60.6% versus RAM-resident Adam state while preserving identical update checksums and proxy loss.

## Why it stopped

No-paper useful signal only: this run isolates optimizer-state update mechanics and includes an early negative result for naive persistent memmap, but it is not direct full CPU training validation.

## Recommended next action

Run a bounded end-to-end CPU training follow-up on a real model where Adam state is a major memory component, comparing RAM Adam with streaming SSD-state Adam on convergence, wall-clock, RSS, and validation loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU training with streaming SSD-backed Adam state
- Success threshold: Streaming SSD-state Adam reduces max RSS by >=40% versus RAM Adam, reaches validation loss within 2% relative of RAM Adam, and has <=3x end-to-end wall-clock slowdown on the bounded workload.
- Stop condition: Stop if streaming SSD-state Adam fails to reduce max RSS by 25%, exceeds 4x wall-clock slowdown before convergence, or diverges while RAM Adam converges under the same seed and hyperparameters.

## Evidence references

- Artifact root: `<local-path>/projects/optimizer-state-offloading-to-ssd-for-cpu-training-8c3e7dfd1eaf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
