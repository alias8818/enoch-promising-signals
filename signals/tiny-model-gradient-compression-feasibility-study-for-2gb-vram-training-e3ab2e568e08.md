# Tiny Model Gradient Compression: Feasibility Study for 2GB VRAM Training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `tiny-model-gradient-compression-feasibility-study-for-2gb-vram-training-e3ab2e568e08`
Run ID: `tiny-model-gradient-compression-feasibility-study-for-2gb-vram-training-e3ab2e568e08-20260607T062155252497+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/8b1a34cc0646

## What looked useful

Int8 gradient storage preserved short synthetic SGD loss movement and reduced end allocation by 10.09 MB on a 5.29M parameter model and 44.27 MB on a 23.21M parameter model, but peak allocation stayed identical at 146.67 MB and 226.57 MB respectively. The bottleneck for 2 GiB feasibility is peak backward/activation/optimizer memory, not post-backward retained gradients alone.

## Boundaries and scale limits

The run used synthetic data, 5.29M and 23.21M parameter transformer probes, BF16 SGD, GB10 CUDA allocator measurements, and an analytical 2 GiB persistent-state model. It did not enforce a physical 2 GiB GPU limit, run AdamW end to end with compressed gradients, or test fused/custom backward kernels that compress before the measured peak.

## Claim scope

On two synthetic BF16 tiny-transformer CUDA probes, post-accumulation int8 gradient storage reduced retained gradient memory but did not reduce peak training allocation, so it is not a standalone method for fitting otherwise-OOM training runs into a 2 GiB VRAM peak budget.

## Why it stopped

Proxy/early falsification rather than full validation: real CUDA probes showed no peak-memory reduction from post-accumulation int8 gradient storage, which is the required success condition for 2 GiB VRAM training feasibility.

## Recommended next action

Stop this standalone gradient-compression line as no-paper evidence; a bounded follow-up should test a complete 2 GiB recipe focused on activation checkpointing plus optimizer-state compression under an enforced CUDA memory cap.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: 2 GiB Tiny Transformer Training Recipe with Activation and Optimizer-State Compression
- Success threshold: The combined recipe trains at least one model/batch/sequence setting that the dense baseline OOMs under the 2 GiB cap, with stable loss over at least 100 synthetic or real-data steps and explicit peak-memory telemetry below 2 GiB.
- Stop condition: Stop if activation/optimizer compression does not move the OOM boundary under the 2 GiB cap or if the only remaining gain requires datacenter-scale resources rather than local bounded testing.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-model-gradient-compression-feasibility-study-for-2gb-vram-training-e3ab2e568e08`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
