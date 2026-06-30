# Longer multi-dataset GPT-2-small LoRA validation for persisted 8-bit SGDM momentum

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `longer-multi-dataset-gpt-2-small-lora-validation-for-persi-53ef4d6e0f`
Run ID: `longer-multi-dataset-gpt-2-small-lora-validation-for-persi-53ef4d6e0f-20260526T211651257855+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: GPT-2-small LoRA validation for 8-bit SGDM momentum: enoch://control-plane/projects/gpt-2-small-lora-validation-for-8-bit-sgdm-momentum-4c41f1bec2/runs/gpt-2-small-lora-validation-for-8-bit-sgdm-momentum-4c41f1bec2-20260526T015841048628+0000
- Parent run decision: Longer GPT-2-small LoRA persistence test for 8-bit SGDM momentum: enoch://control-plane/projects/longer-gpt-2-small-lora-persistence-test-for-8-bit-sgdm-mo-5c80a550a7/runs/longer-gpt-2-small-lora-persistence-test-for-8-bit-sgdm-mo-5c80a550a7-20260526T145031375379+0000

## What looked useful

After 3000 steps, 8-bit SGDM average validation loss was 3.308724 versus fp32 SGDM 3.308743 and SGD 3.454353. The 8-bit optimizer state was 442560 bytes versus fp32 SGDM 1769472 bytes, a 0.2501 ratio, with about 97.3% of fp32 SGDM throughput in this Python prototype.

## Boundaries and scale limits

One seed, hand-written Python optimizer, LoRA-only GPT-2-small adapters, sequence length 128, 3000 optimizer steps per optimizer, small public text corpora, no AdamW comparison, no fused kernel, and no full pretraining-scale or multi-seed robustness claim.

## Claim scope

Single fixed-seed GPT-2-small LoRA validation on three small text corpora showed persisted per-tensor uint8 SGDM momentum matched fp32 SGDM validation loss while using about one quarter of the optimizer-state bytes, and both momentum variants beat no-momentum SGD.

## Why it stopped

Bounded direct validation supports the mechanism but is not publication-grade because it is single-seed, small-corpus, LoRA-only, and uses a prototype Python optimizer.

## Recommended next action

Do not write a paper from this run; run a bounded multi-seed follow-up with an AdamW LoRA baseline and a production-style/fused 8-bit momentum implementation before considering a scoped paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-seed AdamW-inclusive GPT-2-small LoRA validation for persisted 8-bit SGDM momentum
- Success threshold: 8-bit SGDM mean validation loss within 0.01 of fp32 SGDM across seeds, better than no-momentum SGD, no worse than 0.03 loss behind AdamW, at least 3.5x lower momentum-state bytes than fp32 SGDM, and at least 95% of fp32 SGDM throughput in the optimized implementation.
- Stop condition: Stop if any seed shows persistent divergence or more than 0.03 aggregate validation-loss regression versus fp32 SGDM after matched training tokens, or if optimized 8-bit momentum cannot exceed 90% of fp32 SGDM throughput.

## Evidence references

- Artifact root: `<local-path>/projects/longer-multi-dataset-gpt-2-small-lora-validation-for-persi-53ef4d6e0f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
