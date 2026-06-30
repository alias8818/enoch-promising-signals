# Cross-Layer Shared LoRA for Memory-Efficient Fine-tuning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cross-layer-shared-lora-for-memory-efficient-fine-tuning-b433e4743ddd`
Run ID: `cross-layer-shared-lora-for-memory-efficient-fine-tuning-b433e4743ddd-20260528T023621568226+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/92d48f0d7ada

## What looked useful

Shared rank-4 LoRA used 5,376 trainable parameters versus 21,504 for independent rank-4 and reduced target loss from 11.6546 to 0.1181, but independent rank-4 reached 0.0096 and a parameter-matched independent rank-1 control reached 0.1013. The mechanism works as compression, but this run does not show it is better than lowering ordinary LoRA rank at the same trainable-state budget.

## Boundaries and scale limits

Evidence is limited to a 4-layer 96-wide synthetic modular next-token task, two seeds, rank-4 sharing across four layers, and estimated optimizer-state memory from trainable parameters. It is not evidence for GPT-2-small-class or larger LLM fine-tuning, natural-language data, instruction tuning, or production memory behavior.

## Claim scope

On a two-seed tiny synthetic CUDA Transformer adaptation task, cross-layer shared LoRA reduced trainable adapter parameters and estimated AdamW trainable state by 4x versus same-rank independent per-layer LoRA, while still adapting the frozen base model to low target loss.

## Why it stopped

Moderate bounded evidence supports the memory-sharing mechanism but leaves the main quality claim mixed because the parameter-matched independent rank-1 control slightly beat shared rank-4 on the synthetic task.

## Recommended next action

Stop this worker run as a no-paper useful signal; the next bounded test should compare shared-rank sweeps against parameter-matched independent LoRA on a real small language-model fine-tuning task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-matched shared LoRA on a GPT-2-small-class language task
- Success threshold: Shared LoRA must be within 2 percent relative validation perplexity of same-rank independent LoRA or clearly beat the parameter-matched independent LoRA control while using no more trainable-state memory.
- Stop condition: Stop if shared LoRA is consistently worse than the parameter-matched independent control by more than 2 percent relative validation perplexity or shows unstable optimization across repeated runs.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-shared-lora-for-memory-efficient-fine-tuning-b433e4743ddd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
