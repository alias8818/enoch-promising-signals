# Block-wise Dynamic 8-bit Adam Optimizer States

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `block-wise-dynamic-8-bit-adam-optimizer-states-4d70a273539c`
Run ID: `block-wise-dynamic-8-bit-adam-optimizer-states-4d70a273539c-20260528T124532866170+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8b884c9f8c6f

## What looked useful

Dynamic 8-bit optimizer states are viable as a memory-saving representation in a bounded GPU training probe, but this run did not show block-wise scaling improving training over a simpler global dynamic scale control.

## Boundaries and scale limits

Synthetic task only, tiny transformer only, 220 steps, Python optimizer implementation, no real-corpus pretraining, no long-horizon stability test, no fused CUDA kernel, and no distributed or multi-model validation.

## Claim scope

On a 220-step, 3-seed tiny-transformer synthetic next-token task, dynamic 8-bit AdamW moment states matched AdamW32 early loss while using about 25% of optimizer-state bytes; a separate heterogeneous-tensor probe showed block-wise scales reduce quantization error versus a single global scale.

## Why it stopped

Moderate bounded evidence supports memory savings and the block-wise quantization-error mechanism, but the direct training control did not validate a block-wise advantage; this is not a full validation.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should use a real small language-model workload and require block-wise dynamic states to beat a global dynamic-scale control on loss or stability at the same memory budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-LM validation of block-wise versus global dynamic 8-bit Adam states
- Success threshold: Block-wise dynamic 8-bit Adam reaches validation loss within 1% of AdamW32 and at least 1% better than global dynamic 8-bit Adam in mean validation loss or avoids a reproducible global-scale instability, while using no more than 30% of AdamW32 optimizer-state bytes.
- Stop condition: Stop if global dynamic scaling matches or beats block-wise scaling on validation loss across seeds, or if both 8-bit variants diverge or exceed 30% of AdamW32 state memory.

## Evidence references

- Artifact root: `<local-path>/projects/block-wise-dynamic-8-bit-adam-optimizer-states-4d70a273539c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
