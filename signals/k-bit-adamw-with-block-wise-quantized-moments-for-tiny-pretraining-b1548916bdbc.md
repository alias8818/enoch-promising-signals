# K-bit AdamW with block-wise quantized moments for tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `k-bit-adamw-with-block-wise-quantized-moments-for-tiny-pretraining-b1548916bdbc`
Run ID: `k-bit-adamw-with-block-wise-quantized-moments-for-tiny-pretraining-b1548916bdbc-20260621T043052599321+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2d8d3d5cbd65

## What looked useful

q8 block-wise moment quantization matched fp32 AdamW closely (mean final validation loss 0.3246 vs 0.3228, +0.0018) with estimated optimizer-state memory 25.8% of fp32. q6 degraded (+0.1565 validation loss), while q4 and q2 failed badly (validation loss around 26 and 25), providing an early falsification of naive low-bit affine block-wise moment quantization for this setup.

## Boundaries and scale limits

No Transformer/GPT-2-scale model, no real tokenized dataset, no GPU/fused optimizer, no true packed runtime implementation, and no long-horizon pretraining. Sub-8-bit memory is estimated as bit-packed payload plus fp32 block metadata while the prototype uses NumPy uint8 buffers.

## Claim scope

Bounded NumPy tiny-pretraining probe: a small character-level neural LM trained for 600 steps over 3 seeds with AdamW moments stored as fp32 or block-wise affine k-bit quantized states.

## Why it stopped

Proxy-scale optimizer evidence is sufficient to reject the broad naive k-bit claim for q4/q2 here, but it is not full validation of q8 or any transformer-scale optimizer.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded action is to test a stabilized q4 design such as log-domain second moments or error-feedback residuals on the same tiny LM before any larger training.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stabilized 4-bit block-wise AdamW moments on the same tiny LM
- Success threshold: Mean final validation loss delta versus fp32 AdamW <= 0.05 over 3 seeds, no divergent seed, and estimated optimizer-state memory ratio < 0.15.
- Stop condition: Stop if q4 validation loss delta remains > 0.20 after two stabilization variants or if moment quantization errors show order-of-magnitude blow-up similar to this run.

## Evidence references

- Artifact root: `<local-path>/projects/k-bit-adamw-with-block-wise-quantized-moments-for-tiny-pretraining-b1548916bdbc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
