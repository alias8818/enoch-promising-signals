# LoRA pretraining with 4-bit moments on low-rank deltas only

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `lora-pretraining-with-4-bit-moments-on-low-rank-deltas-only-a2dff72825b9`
Run ID: `lora-pretraining-with-4-bit-moments-on-low-rank-deltas-only-a2dff72825b9-20260611T043426255779+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9ad90487fc08

## What looked useful

FP32 AdamW converged on all 3 seeds with mean final eval loss 2.4795, while the matched-LR 4-bit moment variant produced NaN/Inf on all 3 seeds despite about 7.95x lower estimated optimizer-state bytes. Lower learning rates did not recover comparable behavior.

## Boundaries and scale limits

Toy synthetic next-token task, 28,928 trainable LoRA parameters, 160 training steps, three seeds, no real corpus, no long-horizon LLM pretraining, and no packed int4 performance kernel.

## Claim scope

In a frozen tiny-transformer LoRA-only synthetic pretraining probe, naive per-tensor symmetric 4-bit quantization of Adam first and second moments for low-rank LoRA tensors reduced optimizer-state bytes but did not preserve training behavior and diverged across matched seeds.

## Why it stopped

Proxy early falsification: the direct toy LoRA-only optimizer test showed memory savings but unstable or worsening loss for the naive 4-bit moment implementation, so it is not paper-ready and should not be scaled unchanged.

## Recommended next action

Stop this run as a proxy early falsification of the naive/drop-in 4-bit moment approach; test a blockwise or otherwise stabilized 4-bit moment quantizer in a bounded follow-up before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stabilized 4-bit Adam moments for LoRA-only pretraining
- Success threshold: No NaN/Inf across 3 seeds and mean final eval loss within 5% of FP32 AdamW while retaining at least 4x estimated optimizer-state memory reduction.
- Stop condition: Stop if stabilized 4-bit moments still diverge on any seed or mean final eval loss is more than 20% worse than FP32 AdamW after basic LR tuning.

## Evidence references

- Artifact root: `<local-path>/projects/lora-pretraining-with-4-bit-moments-on-low-rank-deltas-only-a2dff72825b9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
