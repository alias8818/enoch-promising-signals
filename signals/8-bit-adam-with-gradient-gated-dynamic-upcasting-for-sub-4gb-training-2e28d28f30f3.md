# 8-bit Adam with gradient-gated dynamic upcasting for sub-4GB training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `8-bit-adam-with-gradient-gated-dynamic-upcasting-for-sub-4gb-training-2e28d28f30f3`
Run ID: `8-bit-adam-with-gradient-gated-dynamic-upcasting-for-sub-4gb-training-2e28d28f30f3-20260629T173759627195+0000`

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

- Provider-backed Research Facility batch: z-ai/glm-5.2: enoch://research-facility/provider/z-ai/glm-5.2/9e7c6374ebc0

## What looked useful

Optimizer-state memory fell to 25.6% of fp32 AdamW for pure blockwise int8 and about 30.1% for a capped gated variant, but training collapsed to NaN for the gated optimizer in 250-step bounded runs. At lr 0.0002, pure 8-bit stayed finite but had much worse loss than AdamW, while low-threshold gated upcasting still collapsed despite only 4.3% active upcast blocks.

## Boundaries and scale limits

No GPT-2-small-class or LLM training was run; throughput was not evaluated with fused production kernels; persistent optimizer-state bytes were estimated from tensors in the harness. The result is an early falsification of this specific mechanism, not a universal rejection of all 8-bit Adam optimizers.

## Claim scope

Bounded local PyTorch mechanism test on a tiny CUDA MLP teacher-label classification task: naive blockwise int8 AdamW plus gradient-ratio-gated fp32 moment overlays did not preserve AdamW-like convergence while keeping optimizer state under the target memory budget.

## Why it stopped

Bounded proxy and control runs showed early falsification: gradient-gated fp32 overlays alone did not prevent NaN collapse or close the convergence gap to AdamW, even when memory stayed below the target.

## Recommended next action

Stop this mechanism as a paper path; any future work should first solve stable second-moment quantization with floors/clipping or a different quantizer before re-testing dynamic upcasting.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adam-with-gradient-gated-dynamic-upcasting-for-sub-4gb-training-2e28d28f30f3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
