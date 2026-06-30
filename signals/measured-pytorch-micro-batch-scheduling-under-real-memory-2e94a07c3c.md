# Measured PyTorch micro-batch scheduling under real memory pressure

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `measured-pytorch-micro-batch-scheduling-under-real-memory-2e94a07c3c`
Run ID: `measured-pytorch-micro-batch-scheduling-under-real-memory-2e94a07c3c-20260614T014040947231+0000`

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

- Parent run decision: Memory-aware micro-batch scheduler under VRAM cap: enoch://control-plane/projects/memory-aware-micro-batch-scheduler-under-vram-cap-dbb1bcd0ee11/runs/memory-aware-micro-batch-scheduler-under-vram-cap-dbb1bcd0ee11-20260614T013018971263+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/43a89d19a40a

## What looked useful

Real CUDA/UMA pressure shifted the calibrated maximum micro-batch from 64 to 32. Fixed micro-batch 64 OOMed under pressure, fixed micro-batch 32 completed at 33.84 samples/s, and adaptive scheduling completed at 32.68 samples/s after two caught OOM events.

## Boundaries and scale limits

Single host, single process, synthetic model and payload, 192 samples, controlled tensor pressure, safety allocator cap after pressure allocation, no real colocated workload, no distributed or long-duration training.

## Claim scope

On one GB10 host with PyTorch 2.12 CUDA, a synthetic CUDA training workload under 77 GiB of real tensor memory pressure showed that a reactive halve-on-OOM micro-batch scheduler completed work when the no-pressure fixed micro-batch failed, and ran within 10% throughput of the pressure-calibrated conservative fixed micro-batch.

## Why it stopped

Tier 1 direct mechanism support was obtained, but the evidence is synthetic, local, and safety-capped, so it is not paper-positive.

## Recommended next action

Run a bounded deepen test comparing reactive OOM-halving with a memory-telemetry predictive scheduler under time-varying pressure from a separate CUDA process.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Predictive PyTorch micro-batch scheduling under time-varying CUDA pressure
- Success threshold: Predictive scheduler completes all samples with zero caught OOM events and throughput at least 95% of the best completing policy across at least three pressure traces.
- Stop condition: Stop if predictive scheduling either OOMs under any trace or is more than 10% slower than reactive scheduling on two or more traces.

## Evidence references

- Artifact root: `<local-path>/projects/measured-pytorch-micro-batch-scheduling-under-real-memory-2e94a07c3c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
