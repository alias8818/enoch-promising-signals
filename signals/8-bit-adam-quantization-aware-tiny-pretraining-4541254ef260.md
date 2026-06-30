# 8-bit Adam quantization-aware tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adam-quantization-aware-tiny-pretraining-4541254ef260`
Run ID: `8-bit-adam-quantization-aware-tiny-pretraining-4541254ef260-20260603T211813624052+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae55cc497071

## What looked useful

Deterministic 8-bit AdamW state storage is a viable tiny-pretraining control, but naive stochastic-rounding quantization awareness can destabilize training at lr=3e-4, diverging on 1 of 3 seeds. Lowering lr to 1e-4 stabilized all tested 8-bit seeds, suggesting a stability-margin issue rather than an execution blocker.

## Boundaries and scale limits

Synthetic data only; 300-step tiny model only; no GPT-2-small-class, real-token corpus, long-run, fused optimizer, or production throughput validation. The Python 8-bit optimizer is memory-oriented and slower than PyTorch AdamW in this run.

## Claim scope

On a 636k-parameter synthetic Markov-token tiny causal-LM pretraining task for 300 GB10 GPU steps across 3 seeds, deterministic blockwise 8-bit AdamW state storage matched FP32 AdamW eval loss within 0.0006 while using about 25% of optimizer-state memory; the tested stochastic-rounding quantization-aware variant was not robust at the baseline learning rate.

## Why it stopped

The direct tiny synthetic test produced mixed evidence: deterministic 8-bit state storage worked, but the tested quantization-aware stochastic-rounding variant had a reproducible seed-level divergence at the baseline learning rate. This is not full validation and not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is to test a variance-controlled quantization-aware 8-bit Adam variant against FP32 and deterministic 8-bit controls on a real-token small model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Variance-controlled quantization-aware 8-bit Adam on small real-token pretraining
- Success threshold: Quantization-aware 8-bit AdamW completes all seeds without divergence, uses no more than 30% of FP32 optimizer-state memory, and has mean eval loss within 0.02 of FP32 and no worse than deterministic 8-bit AdamW.
- Stop condition: Stop as negative if the quantization-aware variant diverges on any seed at the FP32 baseline learning rate or requires a materially lower learning rate that leaves it worse than deterministic 8-bit AdamW.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adam-quantization-aware-tiny-pretraining-4541254ef260`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
