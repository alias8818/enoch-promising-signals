# VRAM-Pressure-Triggered Cascade Demotion on GB10 Unified Memory

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `vram-pressure-triggered-cascade-demotion-on-gb10-unified-memory-8021c114bbbd`
Run ID: `vram-pressure-triggered-cascade-demotion-on-gb10-unified-memory-8021c114bbbd-20260610T204351844295+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3d1a388f08f9

## What looked useful

Warmed managed-memory GPU page-touch time stayed linear through 88 GiB in both explicit-prefetch and fault-driven modes; no abrupt demotion threshold was observed. Fault-driven first touch cost was about 1.08-1.23 seconds per newly introduced 8 GiB chunk but did not persist after warming.

## Boundaries and scale limits

Single GB10 host, synthetic sparse page-touch kernel, one process, no full model workload, no pressure below about 19.9 GiB CUDA free headroom, no Nsight/CUPTI migration-counter validation.

## Claim scope

A bounded CUDA managed-memory page-touch probe on one GB10 host did not show cascade-demotion-like warmed latency breakpoints through 88 GiB allocated and about 19.9 GiB CUDA free headroom.

## Why it stopped

The bounded direct probe found no cascade-demotion signature before the safety headroom limit; further pressure would require a separately guarded edge-of-capacity test rather than being claimed from this run.

## Recommended next action

Stop this run as a bounded no-paper negative/useful-signal result; if pursued, run a guarded edge-of-capacity follow-up with CUPTI or Nsight unified-memory migration counters.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Guarded edge-of-capacity GB10 managed-memory migration-counter probe
- Success threshold: A repeated warmed-latency breakpoint greater than 10% over the linear 88 GiB extrapolation, or a corresponding unified-memory migration-counter surge, below 20 GiB CUDA free headroom.
- Stop condition: Stop if guarded edge-of-capacity runs remain linear within 5% residuals or if MemAvailable/CUDA free headroom reaches the safety floor before a breakpoint appears.

## Evidence references

- Artifact root: `<local-path>/projects/vram-pressure-triggered-cascade-demotion-on-gb10-unified-memory-8021c114bbbd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
