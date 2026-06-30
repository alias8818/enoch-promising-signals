# Lane-Pressure Aware Gradient Routing for Home Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lane-pressure-aware-gradient-routing-for-home-training-5fa25802fb0e`
Run ID: `lane-pressure-aware-gradient-routing-for-home-training-5fa25802fb0e-20260529T114532857480+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1e8d7bf3cbbd

## What looked useful

Pressure-aware routing improved transient-pressure makespan by 26.0% over the best static baseline and 68.4% over round-robin, but was 5.9% worse than size-greedy in the stable-lane control. The mechanism appears useful only when lane pressure is real and variable.

## Boundaries and scale limits

Proxy replay only; no integrated optimizer hooks, no real asynchronous device-to-host gradient pipeline, no real NVMe/network/USB pressure source, no GPT-2-small-class end-to-end training throughput, and no convergence measurement.

## Claim scope

On a GB10 bounded replay using gradient shard sizes from a 21M-parameter CUDA model, online lane-pressure aware routing reduced simulated gradient-processing makespan under transient heterogeneous lane pressure, but did not beat static byte balancing when lanes were stable.

## Why it stopped

Proxy replay produced mixed evidence: useful mechanism support under transient pressure, but insufficient direct training evidence and a stable-lane regression versus size-greedy.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement PyTorch backward-hook gradient offload workers and measure end-to-end throughput under real induced CPU/NVMe/network pressure.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated PyTorch Lane-Pressure Gradient Offload Prototype
- Success threshold: At least 10% throughput improvement over the best static baseline under induced pressure, no more than 3% regression in stable-lane control, and unchanged loss trajectory for a short training run.
- Stop condition: Stop if integrated pressure-aware routing fails to beat byte-balanced static routing under induced pressure or adds more than 3% stable-lane overhead after basic tuning.

## Evidence references

- Artifact root: `<local-path>/projects/lane-pressure-aware-gradient-routing-for-home-training-5fa25802fb0e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
