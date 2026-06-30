# Quantization-aware LoRA fine-tuning for 4-bit GPT-2

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quantization-aware-lora-fine-tuning-for-4-bit-gpt-2-99a20b647f6c`
Run ID: `quantization-aware-lora-fine-tuning-for-4-bit-gpt-2-99a20b647f6c-20260629T075113311619+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d7b7caee9d55

## What looked useful

Primary six-seed repeat: naive LoRA mean merged 4-bit loss 4.1877, QAT-LoRA 3.8401, QAT minus naive -0.3476; QAT improved 5 of 6 seeds. This supports a bounded mechanism but is not enough for a paper.

## Boundaries and scale limits

Not pretrained GPT-2-small, not natural-language corpus validation, not NF4/bitsandbytes validation, not hardware-kernel validation, and not a long or full-scale fine-tuning run.

## Claim scope

In a tiny GPT-2-style causal transformer on synthetic shifted next-token prediction, rank-4 QAT-LoRA trained with signed 4-bit fake quantization of merged effective weights reduced mean merged 4-bit target cross entropy versus naive LoRA in the primary six-seed repeat.

## Why it stopped

Closed as no-paper useful signal because evidence is a tiny synthetic proxy, not full GPT-2-small validation.

## Recommended next action

Run a direct GPT-2-small or at least pretrained tiny-GPT-2 natural-text follow-up with a true 4-bit backend or faithful NF4 fake quantization before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2-small QAT-LoRA vs naive LoRA under merged 4-bit evaluation
- Success threshold: QAT-LoRA improves merged 4-bit held-out perplexity by at least 3% relative to naive LoRA in the mean and is not worse in more than one seed.
- Stop condition: Stop if QAT-LoRA fails to improve mean merged 4-bit held-out perplexity, if gains disappear under fp-adapter controls, or if memory/runtime exceeds the calibrated local budget without checkpointed partial metrics.

## Evidence references

- Artifact root: `<local-path>/projects/quantization-aware-lora-fine-tuning-for-4-bit-gpt-2-99a20b647f6c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
