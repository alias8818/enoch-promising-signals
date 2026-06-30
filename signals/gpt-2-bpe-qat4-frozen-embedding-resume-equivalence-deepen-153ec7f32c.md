# GPT-2 BPE QAT4 frozen-embedding resume-equivalence deepen test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `100`
Project ID: `gpt-2-bpe-qat4-frozen-embedding-resume-equivalence-deepen-153ec7f32c`
Run ID: `gpt-2-bpe-qat4-frozen-embedding-resume-equivalence-deepen-153ec7f32c-20260523T212803441800+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `100`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: GPT-2-small frozen-embedding QAT4 fine-tuning confirmation: enoch://control-plane/projects/gpt-2-small-frozen-embedding-qat4-fine-tuning-confirmation-dd084bb59d/runs/gpt-2-small-frozen-embedding-qat4-fine-tuning-confirmation-dd084bb59d-20260523T205351593666+0000
- Parent run decision: Longer GPT-2-small frozen-embedding QAT4 convergence and checkpoint persistence test: enoch://control-plane/projects/longer-gpt-2-small-frozen-embedding-qat4-convergence-and-c-dc95aca8cf/runs/longer-gpt-2-small-frozen-embedding-qat4-convergence-and-c-dc95aca8cf-20260523T210401191760+0000

## What looked useful

Across 16 FP32/QAT4 and frozen/trainable condition-seed cells, uninterrupted versus stop/resume training matched exactly on loss trace, final parameters, logits, and AdamW optimizer state. Frozen token embeddings had zero drift, trainable controls had nonzero drift, and missing-optimizer/reset-cursor ablations produced clear divergence.

## Boundaries and scale limits

This did not train GPT-2-small/124M or larger, did not use WebText/OpenWebText-scale data, and did not validate a production packed-int4 QAT/deployment stack. The model used a small 4-layer, 96-dim transformer with an untied output head.

## Claim scope

In a deterministic small GPT-style causal transformer trained on GPT-2 BPE token streams, fake symmetric 4-bit QAT with frozen token embeddings is exactly checkpoint/resume equivalent across 4 seeds and 720-step runs when model, optimizer, dataloader cursor, and RNG states are serialized.

## Why it stopped

The scoped implementation-level hypothesis was supported, but the evidence is small-model/local-data/fake-QAT only and is not sufficient for publication-grade GPT-2 BPE QAT4 frozen-embedding resume-equivalence claims.

## Recommended next action

Stop as no-paper useful-signal evidence; a bounded next deepen test should use an actual GPT-2-small-class Hugging Face model or architecture-parity implementation with a real OpenWebText/WebText-style shard and the same exact resume-equivalence metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class QAT4 frozen-embedding resume-equivalence on real text shard
- Success threshold: All seeds in the QAT4 frozen target and FP32 baseline have max loss, parameter, logit, and optimizer-state absolute differences equal to 0.0 or a predeclared deterministic-kernel tolerance no larger than 1e-7, while missing-state ablations diverge by at least 1e-3 in parameters or logits.
- Stop condition: Stop if any target seed exceeds the equivalence tolerance after verifying serialization correctness, or if the architecture/data scale cannot run with checkpointed partial artifacts inside the bounded validation budget.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-bpe-qat4-frozen-embedding-resume-equivalence-deepen-153ec7f32c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
