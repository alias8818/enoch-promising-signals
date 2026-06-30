# GPT-2-small-class QAT4 frozen-embedding resume-equivalence on real text shard

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `83`
Project ID: `gpt-2-small-class-qat4-frozen-embedding-resume-equivalence-a6315890ed`
Run ID: `gpt-2-small-class-qat4-frozen-embedding-resume-equivalence-a6315890ed-20260523T220341327591+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": -10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- supported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Longer GPT-2-small frozen-embedding QAT4 convergence and checkpoint persistence test: enoch://control-plane/projects/longer-gpt-2-small-frozen-embedding-qat4-convergence-and-c-dc95aca8cf/runs/longer-gpt-2-small-frozen-embedding-qat4-convergence-and-c-dc95aca8cf-20260523T210401191760+0000
- Parent run decision: GPT-2 BPE QAT4 frozen-embedding resume-equivalence deepen test: enoch://control-plane/projects/gpt-2-bpe-qat4-frozen-embedding-resume-equivalence-deepen-153ec7f32c/runs/gpt-2-bpe-qat4-frozen-embedding-resume-equivalence-deepen-153ec7f32c-20260523T212803441800+0000

## What looked useful

Across 12 non-ablation condition/seed cells, including the target QAT4 frozen-embedding condition and FP32/trainable controls, uninterrupted and resumed paths matched exactly: max loss, parameter, logit, and optimizer-state differences were all 0.0. Frozen token-embedding drift was 0.0, trainable controls drifted at least 0.0187, and optimizer/cursor ablations broke equality.

## Boundaries and scale limits

Not a broad GPT-2-small paper result: no OpenWebText/WebText-scale corpus, no full convergence, no pretrained Hugging Face GPT-2-small weight parity, no production packed int4 kernels, and no long multi-day robustness run.

## Claim scope

Bounded implementation-level claim: a deterministic GPT-2-small-class custom GPT model using GPT-2 BPE over a Tiny Shakespeare real text shard, fake 4-bit quantized transformer linear weights, frozen token/position embeddings, AdamW, three fixed seeds, 240 steps, and split-step checkpointing is exactly resume-equivalent when model, optimizer, dataloader cursor, and Python/NumPy/PyTorch CPU/CUDA RNG state are serialized.

## Why it stopped

The direct bounded test supports the resume-equivalence mechanism, but the claim remains too scoped and short for Tier-4 paper readiness; follow-up depth is already 4, so no chained follow-up is recommended.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful evidence; use the artifacts only as bounded mechanism support, not as paper-positive GPT-2-small QAT4 validation.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-qat4-frozen-embedding-resume-equivalence-a6315890ed`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
