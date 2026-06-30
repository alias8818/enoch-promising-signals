# TernRes: Ternary Weights with Layer-wise Residual LoRA

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternres-ternary-weights-with-layer-wise-residual-lora-8ed3c865004c`
Run ID: `ternres-ternary-weights-with-layer-wise-residual-lora-8ed3c865004c-20260604T045944712351+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/84a2084c144e

## What looked useful

TernRes is mechanically viable in a bounded local probe: frozen ternary weights plus small residual LoRA adapters restored dense-level accuracy with 2.2% to 8.2% trainable/effective parameter overhead. The signal is mixed because bias-only retraining was also strong, implying this task is highly bias-correctable.

## Boundaries and scale limits

Only a small synthetic MLP task was tested. No real language or vision dataset, no transformer, no GPT-2-small-class baseline, no pretrained-model quantization, no inference throughput measurement, and only 3 random seeds were evaluated. A strong bias-only control recovered 83.6% of the gap, so LoRA-specific novelty is not isolated enough for a paper claim.

## Claim scope

On a deterministic synthetic teacher classification task with small MLP students, frozen post-training ternary weights plus layer-wise residual LoRA adapters can recover nearly all mean held-out accuracy lost by ternarization; rank 1 recovered 96.3% of the dense-to-ternary gap and ranks 4+ matched dense mean accuracy.

## Why it stopped

No-paper useful signal: bounded synthetic evidence supports the mechanism, but the claim is not publication-grade and the bias-only control weakens LoRA-specific novelty.

## Recommended next action

Run a bounded real-task deepen test on a small pretrained or from-scratch transformer/vision model with dense, ternary-only, bias-only, standard LoRA, and TernRes controls before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: TernRes real-task confirmation with bias-only and standard LoRA controls
- Success threshold: TernRes rank <= 4 recovers >=90% of the dense-to-ternary validation degradation and beats bias-only by >=5 absolute accuracy points or equivalent metric across the mean of 3 seeds.
- Stop condition: Stop if TernRes fails to beat bias-only by the threshold on two real-task configurations or if ternary-only degradation is too small to measure a meaningful recovery gap.

## Evidence references

- Artifact root: `<local-path>/projects/ternres-ternary-weights-with-layer-wise-residual-lora-8ed3c865004c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
