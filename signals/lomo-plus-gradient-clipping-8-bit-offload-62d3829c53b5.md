# LOMO-Plus: Gradient Clipping + 8-bit Offload

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `lomo-plus-gradient-clipping-8-bit-offload-62d3829c53b5`
Run ID: `lomo-plus-gradient-clipping-8-bit-offload-62d3829c53b5-20260522T171404920394+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/93f4f84942ac

## What looked useful

Int8 CPU-offloaded momentum plus global clipping matched fp32 clipped momentum within about 1e-5 raw-loss delta over three seeds, reduced GPU peak by 74.4 MiB and GPU optimizer state from 74.4 MiB to 0 MiB, used 18.6 MiB CPU state, and was about 33% slower at this small scale. Without clipping, controlled loss spikes degraded final raw loss from about 6.95 to 10.53 mean.

## Boundaries and scale limits

Proxy-only evidence: PyTorch still materializes gradients, the task is synthetic, runs are 80 steps, model size is far below GPT-2-small, and no real corpus or true fused-backward LOMO implementation was validated.

## Claim scope

On a 19.5M-parameter synthetic tiny Transformer proxy, per-tensor int8 CPU-offloaded momentum with global gradient clipping matched fp32 GPU momentum loss behavior across three seeds while removing measured GPU optimizer-state allocation; clipping prevented controlled loss-spike instability in the same setup.

## Why it stopped

Proxy mechanism produced useful signal but does not directly validate true LOMO, real-data training quality, or large-model memory behavior; therefore it is not paper-ready.

## Recommended next action

Run a true fused-backward LOMO implementation with int8 CPU-offloaded state on a GPT-2-small-class real-data fine-tuning task, comparing against fp32 LOMO and AdamW memory, throughput, and validation loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: True fused-backward LOMO with int8 CPU-offloaded state on real-data GPT-2-small fine-tuning
- Success threshold: Int8-offload fused LOMO validation loss within 1% of fp32 LOMO, at least 20% lower GPU peak memory than fp32 LOMO or AdamW, and no more than 25% throughput penalty on the target local GPU.
- Stop condition: Stop if fused-backward implementation still materializes full gradients, if int8-offload loses more than 1% validation quality versus fp32 LOMO in two independent runs, or if throughput penalty exceeds 50% without a compensating memory win.

## Evidence references

- Artifact root: `<local-path>/projects/lomo-plus-gradient-clipping-8-bit-offload-62d3829c53b5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
