# Layer-Shared LoRA for Tiny-VRAM Domain Adaptation on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layer-shared-lora-for-tiny-vram-domain-adaptation-on-cpu-dbe318154cf2`
Run ID: `layer-shared-lora-for-tiny-vram-domain-adaptation-on-cpu-dbe318154cf2-20260629T072004395320+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d1376a4c5689

## What looked useful

Shared LoRA improved target loss over no adapter by 0.6485 and achieved 0.7692 mean target accuracy with 384 trainable parameters, compared with 0.8182 accuracy for independent per-layer LoRA with 1536 trainable parameters. The memory mechanism is supported, but there is a measurable quality cost.

## Boundaries and scale limits

Synthetic classification only; no real language-model corpus, no CUDA VRAM measurement, no heterogeneous transformer projection sharing, and no rank-matched per-layer control beyond the same-rank independent LoRA baseline.

## Claim scope

On a five-seed NumPy synthetic rotated-domain classifier proxy with four same-width frozen residual layers, one rank-4 LoRA matrix pair shared across layers reduced trainable parameters and estimated FP32 Adam trainable-plus-state memory by 4.0x while retaining substantial target-domain adaptation versus no adapter, but it underperformed independent per-layer LoRA.

## Why it stopped

Closed as no-paper useful signal because the local evidence is a synthetic CPU proxy that supports the memory/adaptation mechanism but is not direct full validation of tiny-VRAM language-model domain adaptation.

## Recommended next action

Run a bounded small transformer language-model follow-up with real token data, measured device or process memory, and a rank-reduced per-layer LoRA control before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM Layer-Shared LoRA Memory-Quality Tradeoff
- Success threshold: Layer-shared LoRA uses at least 3x less optimizer-state memory than independent per-layer LoRA and recovers at least 80% of its validation-loss improvement over no adapter while beating a parameter-matched rank-reduced per-layer control.
- Stop condition: Stop if shared LoRA fails to improve validation loss over no adapter, fails to beat the parameter-matched control, or loses more than 20% of the independent per-layer LoRA improvement under the memory budget.

## Evidence references

- Artifact root: `<local-path>/projects/layer-shared-lora-for-tiny-vram-domain-adaptation-on-cpu-dbe318154cf2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
