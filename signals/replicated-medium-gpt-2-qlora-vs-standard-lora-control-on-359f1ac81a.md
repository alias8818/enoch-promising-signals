# Replicated medium GPT-2 QLoRA vs standard LoRA control on GB10

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `replicated-medium-gpt-2-qlora-vs-standard-lora-control-on-359f1ac81a`
Run ID: `replicated-medium-gpt-2-qlora-vs-standard-lora-control-on-359f1ac81a-20260605T172005502730+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: 4-bit Quantized Training with LoRA on GB10: enoch://control-plane/projects/4-bit-quantized-training-with-lora-on-gb10-8cf1e30d1921/runs/4-bit-quantized-training-with-lora-on-gb10-8cf1e30d1921-20260605T105530274318+0000
- Parent run decision: GPT-2-small-class QLoRA validation on GB10 with real data: enoch://control-plane/projects/gpt-2-small-class-qlora-validation-on-gb10-with-real-data-a5545ed12b/runs/gpt-2-small-class-qlora-validation-on-gb10-with-real-data-a5545ed12b-20260605T143755321491+0000

## What looked useful

Both LoRA and QLoRA improved over frozen GPT-2 medium. Standard LoRA had consistently lower final validation loss than QLoRA across three seeds (2.9777 vs 2.9994 mean loss), while QLoRA reduced peak CUDA allocation (0.764 GiB vs 0.975 GiB) but trained slower (2849 vs 3557 tokens/s).

## Boundaries and scale limits

Not a full convergence study; only one dataset, one adapter rank, one learning rate, one sequence length, and one 100-update token budget were tested. No downstream tasks or memory-pressure boundary cases were evaluated.

## Claim scope

GPT-2 medium on WikiText-2 raw, seq_len 256, rank-8 adapters targeting c_attn/c_proj/c_fc, bf16 standard LoRA versus NF4 QLoRA, 100 optimizer updates, seeds 1-3, evaluated on 65,536 validation tokens on GB10.

## Why it stopped

Medium confirmation found a consistent memory-saving but slower and slightly worse-validation-loss QLoRA tradeoff versus standard LoRA, not a paper-positive advantage.

## Recommended next action

Stop this follow-up as no-paper useful evidence; use these artifacts to decide whether a separate longer convergence study is worth running.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/replicated-medium-gpt-2-qlora-vs-standard-lora-control-on-359f1ac81a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
