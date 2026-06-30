# 8-bit GaLore with selective optimizer offload for tiny-VRAM training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-galore-with-selective-optimizer-offload-for-tiny-vram-training-f5cd4b218773`
Run ID: `8-bit-galore-with-selective-optimizer-offload-for-tiny-vram-training-f5cd4b218773-20260531T205911401962+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e8771661c28c

## What looked useful

Rank-16 offloaded GaLore8 used 912,664 B combined CUDA optimizer/projector state, 2.7% of AdamW32 optimizer state, but loss worsened by +0.0118 while AdamW32 improved by -0.4010. Rank-64 offload used 10.3% of AdamW32 state with the same stalled loss. FP32 GaLore at rank 64 also stalled at the AdamW learning rate, and a higher-LR 8-bit offload probe failed with CUDA SVD non-convergence.

## Boundaries and scale limits

Tested only a 16.9 MB parameter proxy for 40-step synthetic-token runs on GB10 UMA. No real tiny-VRAM hard cap, real text corpus, GPT-2-small-class baseline, long convergence run, distributed training, or official/tuned GaLore package reproduction was performed.

## Claim scope

On a deterministic small-transformer CUDA proxy, 8-bit low-rank GaLore-style optimizer states with selective CPU offload greatly reduce persistent CUDA optimizer-state memory, but the tested implementation does not preserve AdamW-like short-run loss improvement and shows instability at a higher learning rate.

## Why it stopped

Proxy evidence shows the memory mechanism works, but the combined optimizer/offload path failed to match AdamW short-run learning and showed an SVD convergence failure at higher LR; this is not full-scale validation.

## Recommended next action

Stop this run as an early proxy falsification of the drop-in training claim; the next bounded action is to test a numerically safer official/tuned GaLore variant with per-row or block quantization before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Numerically stable 8-bit GaLore offload with tuned projection and block quantization
- Success threshold: GaLore8 offload uses no more than 15% of AdamW32 combined CUDA optimizer/projector state, completes without nonfinite/SVD failures, and achieves at least 80% of AdamW32 loss reduction on the 40-step proxy and a 200-step confirmation.
- Stop condition: Stop if tuned GaLore32 still achieves less than 50% of AdamW32 loss reduction or if the 8-bit offloaded path produces any repeatable nonfinite/SVD failure under the predeclared stable settings.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-galore-with-selective-optimizer-offload-for-tiny-vram-training-f5cd4b218773`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
