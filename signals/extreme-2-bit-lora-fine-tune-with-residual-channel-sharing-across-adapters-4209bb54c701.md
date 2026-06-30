# Extreme 2-bit LoRA Fine-tune with Residual Channel Sharing Across Adapters

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `extreme-2-bit-lora-fine-tune-with-residual-channel-sharing-across-adapters-4209bb54c701`
Run ID: `extreme-2-bit-lora-fine-tune-with-residual-channel-sharing-across-adapters-4209bb54c701-20260621T120757829783+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2f909791b33b

## What looked useful

Across 5 seeds in the shared-structure probe, q2_rcs reached mean validation NRMSE 0.705943 versus 0.775098 for q2_lora and 0.859734 for q2_lora_wide. In a no-shared ablation, q2_rcs no longer beat plain q2_lora, suggesting the gain is conditional on real cross-adapter shared residual structure.

## Boundaries and scale limits

No transformer, language-model, instruction-tuning, real dataset, serialization, or deployment validation was run. The result is a mechanism probe only and does not establish broad LLM fine-tuning viability.

## Claim scope

In a synthetic multi-task linear adaptation setting with known shared low-rank residual structure, 2-bit LoRA plus shared residual channels reduced held-out NRMSE versus plain same-rank 2-bit LoRA and a wider private-rank 2-bit LoRA control.

## Why it stopped

Closed as no-paper useful signal because current evidence is synthetic/proxy-only and not direct transformer fine-tuning evidence.

## Recommended next action

Run a bounded GPT-2-small-class multi-task fine-tuning follow-up with the same controls, adapter-subspace diagnostics, and quantized serialization/reload checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small 2-bit residual-channel-sharing LoRA validation
- Success threshold: q2_rcs improves validation loss or task metric over plain q2_lora by at least 3% relative and matches or beats the wider private-rank 2-bit control while using fewer storage bits, across at least 3 seeds.
- Stop condition: Stop if q2_rcs fails to beat plain q2_lora on mean validation quality, if gains disappear after quantized reload, or if measured adapter deltas show no shared subspace to exploit.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-2-bit-lora-fine-tune-with-residual-channel-sharing-across-adapters-4209bb54c701`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
