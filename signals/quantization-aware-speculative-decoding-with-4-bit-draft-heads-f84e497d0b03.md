# Quantization-aware speculative decoding with 4-bit draft heads

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantization-aware-speculative-decoding-with-4-bit-draft-heads-f84e497d0b03`
Run ID: `quantization-aware-speculative-decoding-with-4-bit-draft-heads-f84e497d0b03-20260605T110351893752+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/4be1fc6fa736

## What looked useful

FP-then-QAT fine-tuning improved mean int4 acceptance from 0.3202 PTQ to 0.5099 at the best tested QAT LR, and exceeded a matched 1200-step FP/PTQ control by mean +0.1815 acceptance across five seeds. QAT from scratch was consistently negative, mean -0.0294 acceptance vs PTQ.

## Boundaries and scale limits

Test used synthetic hidden states and low-rank-plus-noise teacher logits with vocab=4096, hidden=256, train_n=8192, val_n=2048, five seeds, and no real autoregressive LM or serving kernel. It is not evidence for 7B-class models or end-to-end speedup.

## Claim scope

Synthetic teacher-head evidence: a 4-bit grouped fake-quant draft head trained by FP pretraining followed by short QAT fine-tuning preserves the speculative acceptance proxy substantially better than PTQ, while QAT from random initialization is worse than PTQ.

## Why it stopped

Closed as no-paper useful signal because the evidence is controlled synthetic/proxy evidence, not real LM speculative decoding or end-to-end throughput validation.

## Recommended next action

Run a bounded direct-evidence follow-up on pretrained GPT-2-small hidden states, comparing PTQ vs FP-then-QAT-finetuned 4-bit draft heads on true multi-token speculative acceptance before considering larger model scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2 small validation of FP-then-QAT 4-bit draft heads
- Success threshold: FP-then-QAT int4 draft head improves true mean speculative acceptance by at least +0.05 absolute over equal-total-step FP/PTQ on GPT-2-small held-out text without reducing top-1 match or increasing KL versus PTQ.
- Stop condition: Stop as negative if FP-then-QAT fails to beat equal-total-step FP/PTQ by +0.02 absolute acceptance on two seeds or if gains disappear under sequential draft lengths greater than 1.

## Evidence references

- Artifact root: `<local-path>/projects/quantization-aware-speculative-decoding-with-4-bit-draft-heads-f84e497d0b03`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
