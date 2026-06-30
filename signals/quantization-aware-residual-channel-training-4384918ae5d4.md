# Quantization-Aware Residual Channel Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantization-aware-residual-channel-training-4384918ae5d4`
Run ID: `quantization-aware-residual-channel-training-4384918ae5d4-20260601T070812133064+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8740107b585d

## What looked useful

Plain QAT matched or exceeded residual-channel QAT accuracy at 4-bit and residual-channel QAT improved 3-bit loss but not accuracy consistently. This argues against the simplest fixed residual-channel formulation as a standalone research result.

## Boundaries and scale limits

Synthetic MLP only; five seeds; 6000 train and 2000 validation samples; no transformer, real dataset, activation quantization, integer kernel, optimizer-state quantization, latency, or full-scale validation.

## Claim scope

A fixed 10% activation-selected high-precision residual channel path in the first layer of a fake-quantized synthetic teacher-student MLP did not robustly improve validation accuracy over plain low-bit QAT. It showed only a small 3-bit validation-loss improvement.

## Why it stopped

Proxy/local evidence is mixed and insufficient for a paper: residual channels did not produce a robust accuracy gain over plain QAT, and the only positive signal was a small 3-bit loss reduction.

## Recommended next action

Stop this formulation as no-paper evidence; if continuing, run a bounded deepen test with learned/per-layer residual channel selection on a small real sequence or vision benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned residual channel selection for low-bit QAT on a small real benchmark
- Success threshold: Residual-channel QAT improves validation accuracy by at least 1 percentage point or validation loss/perplexity by at least 2% over plain QAT, with improvement in at least 4 of 5 paired seeds at matched residual budget.
- Stop condition: Stop if learned/per-layer residual selection fails to beat plain QAT by the success threshold or if gains vanish after accounting for residual parameter/compute overhead.

## Evidence references

- Artifact root: `<local-path>/projects/quantization-aware-residual-channel-training-4384918ae5d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
