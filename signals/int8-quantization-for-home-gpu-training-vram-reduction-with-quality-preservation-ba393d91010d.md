# INT8 Quantization for Home GPU Training: VRAM Reduction with Quality Preservation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-quantization-for-home-gpu-training-vram-reduction-with-quality-preservation-ba393d91010d`
Run ID: `int8-quantization-for-home-gpu-training-vram-reduction-with-quality-preservation-ba393d91010d-20260608T101412625040+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/51028fbb9717

## What looked useful

The mechanism has a real memory-saving signal but is not robust as a naive drop-in replacement: default AdamW hyperparameters diverged to NaN by step 200, while lr=1e-4 and eps=1e-4 stabilized training with about -0.74 percentage-point mean validation accuracy delta and about 72% of AdamW throughput.

## Boundaries and scale limits

Tested only a small synthetic task on one NVIDIA GB10, 1,200 steps per optimizer, three conservative seeds plus one default-hyperparameter failure. No real dataset, LLM, long-run stability, fused kernels, activation quantization, gradient quantization, or established 8-bit optimizer baseline was tested.

## Claim scope

On a bounded synthetic GPU teacher/student classification task, per-tensor INT8 quantization of AdamW first and second moment state reduced optimizer-state bytes by 4x and CUDA peak allocation by about 19.4% under conservative hyperparameters, with a small mean validation accuracy drop versus AdamW.

## Why it stopped

Proxy/local evidence only: the run supports a bounded memory mechanism but also found default-hyperparameter instability and throughput cost, so it is not a full validation of home-GPU INT8 training quality preservation.

## Recommended next action

Stop this run as no-paper useful signal; next, test block-wise INT8 AdamW state against AdamW and an established 8-bit optimizer on a small real next-token language-model workload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Block-wise INT8 AdamW state on a small real language-model training task
- Success threshold: Block-wise INT8 state achieves at least 3.5x optimizer-state byte reduction, at least 15% CUDA peak allocation reduction, no divergence under AdamW-like hyperparameters, and final validation perplexity within 2% of AdamW across three seeds.
- Stop condition: Stop if block-wise INT8 state diverges in two or more seeds under AdamW-like hyperparameters or fails to reduce CUDA peak allocation by at least 10% versus AdamW.

## Evidence references

- Artifact root: `<local-path>/projects/int8-quantization-for-home-gpu-training-vram-reduction-with-quality-preservation-ba393d91010d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
