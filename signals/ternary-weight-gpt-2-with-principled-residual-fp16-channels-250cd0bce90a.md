# Ternary Weight GPT-2 with Principled Residual FP16 Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-weight-gpt-2-with-principled-residual-fp16-channels-250cd0bce90a`
Run ID: `ternary-weight-gpt-2-with-principled-residual-fp16-channels-250cd0bce90a-20260523T150005105575+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/34cc41ba48dc

## What looked useful

The mechanism is reproducible in a bounded toy setting: residual FP16 rows reduce ternary quantization damage, and selecting rows by quantization reconstruction error is better than random selection at the same storage budget. At 10% residual rows the loss delta vs dense dropped from 0.3212 to 0.2109, while linear projection weights remained 8.88x compressed vs FP32.

## Boundaries and scale limits

This run did not test pretrained GPT-2-small or larger models, natural-language validation corpora, repeated seeds, training-aware quantization, activation quantization, real ternary/FP16 mixed inference kernels, throughput, or hardware memory-bandwidth gains. Evidence is a local CPU proxy and should not be presented as full GPT-2 validation.

## Claim scope

In a 421k-parameter GPT-2-style causal Transformer trained on a deterministic synthetic token grammar, post-training ternary quantization of linear projections benefits from retaining a small fraction of FP16 residual output channels selected by per-row ternary reconstruction error. Error-selected residual rows reduced the ternary-only validation loss penalty monotonically from 2.8% at 1% rows to 34.3% at 10% rows, and beat random row selection at equal storage.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic tiny-model proxy, not direct GPT-2-scale or natural-language validation.

## Recommended next action

Run the same dense vs ternary-only vs error-selected residual vs random-residual comparison on pretrained GPT-2-small with WikiText-2 or OpenWebText validation before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2-small ternary residual-channel validation on real text
- Success threshold: At one or more residual budgets no larger than 10%, error-selected residual rows should recover at least 25% of the ternary-only loss penalty versus dense and beat random residual rows at equal storage by at least 0.02 validation loss.
- Stop condition: Stop if pretrained GPT-2-small cannot be evaluated locally within the available CPU budget, or if error-selected residual rows do not outperform random rows at equal storage on real text.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-weight-gpt-2-with-principled-residual-fp16-channels-250cd0bce90a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
