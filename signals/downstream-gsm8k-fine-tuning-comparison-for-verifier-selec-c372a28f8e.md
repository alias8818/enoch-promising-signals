# Downstream GSM8K fine-tuning comparison for verifier-selected versus loss-selected traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `downstream-gsm8k-fine-tuning-comparison-for-verifier-selec-c372a28f8e`
Run ID: `downstream-gsm8k-fine-tuning-comparison-for-verifier-selec-c372a28f8e-20260629T103603996879+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Verifier versus token-loss curation on model-generated GSM8K traces: enoch://control-plane/projects/verifier-versus-token-loss-curation-on-model-generated-gsm-36edb4c442/runs/verifier-versus-token-loss-curation-on-model-generated-gsm-36edb4c442-20260629T095549329733+0000
- Parent run decision: Real-trace prefix verifier versus token-loss curation: enoch://control-plane/projects/real-trace-prefix-verifier-versus-token-loss-curation-3b7c767fc2/runs/real-trace-prefix-verifier-versus-token-loss-curation-3b7c767fc2-20260629T084412212920+0000

## What looked useful

Base-model loss selected answer-wrong traces for 91/384 larger-run training examples, while verifier selection chose answer-correct traces. Verifier fine-tuning reached 100% held-out candidate-reranking versus 98.4% for loss-selected, but generation exact match was lower than loss-selected fine-tuning: 4/128 versus 6/128.

## Boundaries and scale limits

Single seed; DistilGPT-2 only; 384 training examples and 128 held-out examples in the largest run; synthetic perturbation candidate pools rather than model-sampled traces; oracle answer verifier rather than trained verifier; short two-epoch fine-tuning.

## Claim scope

On synthetic GSM8K-derived candidate trace pools with DistilGPT-2 fine-tuning, answer-verifier selection creates cleaner selected training traces and better held-out candidate-reranking, but it does not outperform loss-selected traces on held-out generated answer exact match.

## Why it stopped

No-paper useful signal: the selector-alignment mechanism appeared, but the direct downstream generation metric did not support verifier-selected fine-tuning over loss-selected fine-tuning in this bounded local run.

## Recommended next action

Run a bounded follow-up with model-generated trace pools, a non-oracle verifier or verifier proxy, GPT-2-small-class downstream fine-tuning, and at least three seeds; stop unless verifier selection improves generated GSM8K exact match by a predefined margin.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Generated-trace GSM8K verifier-vs-loss selection with GPT-2-small-class fine-tuning
- Success threshold: Verifier-selected fine-tuning beats loss-selected fine-tuning by at least 3 absolute percentage points in generated exact match on a held-out GSM8K subset, with the same direction in at least two of three seeds and no large parse-rate confound.
- Stop condition: Stop if generation exact match remains below 5% for all conditions, if the verifier selector does not improve selected-trace correctness by at least 10 points, or if loss-selected fine-tuning matches or exceeds verifier-selected fine-tuning across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/downstream-gsm8k-fine-tuning-comparison-for-verifier-selec-c372a28f8e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
