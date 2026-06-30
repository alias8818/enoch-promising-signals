# Home CPU fine-tuning: 2-bit base + 4-bit residual adapter

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `home-cpu-fine-tuning-2-bit-base-4-bit-residual-adapter-14a636b63b6b`
Run ID: `home-cpu-fine-tuning-2-bit-base-4-bit-residual-adapter-14a636b63b6b-20260619T182502865378+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/38572eb15e20

## What looked useful

Across 3 seeds, frozen 2-bit base MSE averaged 0.9581; the 4-bit full-rank residual adapter averaged 0.0327 MSE and closed 96.6% of the base error, while float LoRA rank-16 closed 13.6%. Main runs took 14.3-21.0 seconds and about 75 MiB RSS.

## Boundaries and scale limits

No transformer, tokenizer, real language modeling dataset, GPT-2-small-class baseline, integer-only optimizer, or multi-hardware home CPU study was run. The residual adapter is full-rank and same-shape, so inference storage is 2-bit base plus 4-bit residual.

## Claim scope

In a synthetic linear regression proxy on this local CPU worker, a frozen signed-symmetric 2-bit base plus a full-rank 4-bit residual adapter trained with an fp32 shadow recovered most of the 2-bit quantization/pretrain error.

## Why it stopped

Closed as no-paper useful signal: the result is a reproducible proxy mechanism, not direct evidence for practical LLM fine-tuning.

## Recommended next action

Run a bounded GPT-2-small-class or smaller transformer language-model follow-up comparing 2-bit base plus 4-bit residual against LoRA/QLoRA-style baselines with matched storage and train-state accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer validation of 2-bit base plus 4-bit residual adapters
- Success threshold: At equal or explicitly accounted storage/train-state budget, the 4-bit residual adapter should recover at least 50% of the validation-loss gap between frozen 2-bit base and a float adapter/full fine-tune control without exceeding a bounded home-CPU memory budget.
- Stop condition: Stop if the 4-bit residual recovers less than 25% of the validation-loss gap in a calibrated small-transformer run or if CPU wall-clock/memory exceeds the local deployment budget before producing interpretable validation metrics.

## Evidence references

- Artifact root: `<local-path>/projects/home-cpu-fine-tuning-2-bit-base-4-bit-residual-adapter-14a636b63b6b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
