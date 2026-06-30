# Negative-Result Probe: Does Volunteer Compute Actually Help a GB10 Local Run?

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `negative-result-probe-does-volunteer-compute-actually-help-a-gb10-local-run-40b3eee07186`
Run ID: `negative-result-probe-does-volunteer-compute-actually-help-a-gb10-local-run-40b3eee07186-20260621T212634524249+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8e1c1f27a7fb

## What looked useful

Fine-grained volunteer offload is not promising for GB10 dense tensor steps: even a favorable same-host proxy is one to two orders of magnitude slower than the local GPU baseline before adding WAN, straggler, trust, privacy, or validation overhead.

## Boundaries and scale limits

This run used same-host IPC workers rather than real public volunteer machines and tested dense tensor kernels rather than full model training; it does not rule out coarse-grained independent jobs or remote volunteer GPUs with high compute-to-transfer ratios.

## Claim scope

For dense 512-2048 square matmul on this GB10, optimistic same-host CPU offload over multiprocessing IPC is 77-111x slower than local GB10 fp32 GPU execution and 174-398x slower than local fp16 GPU execution.

## Why it stopped

Proxy/early falsification: optimistic same-host IPC offload failed the success threshold by 77-111x versus local fp32 GB10 GPU and 174-398x versus local fp16 GB10 GPU, so real volunteer compute is unlikely to help fine-grained dense tensor steps.

## Recommended next action

Stop this dense-tensor volunteer-offload path as an early proxy falsification; only revisit with a coarse independent workload whose measured compute time dwarfs transfer and validation overhead.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/negative-result-probe-does-volunteer-compute-actually-help-a-gb10-local-run-40b3eee07186`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
