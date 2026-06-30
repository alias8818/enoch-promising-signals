# Subword Small-Transformer Fake INT8 Pretraining Robustness Check

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `subword-small-transformer-fake-int8-pretraining-robustness-d89d595e97`
Run ID: `subword-small-transformer-fake-int8-pretraining-robustness-d89d595e97-20260608T133022409349+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: INT8 Fake-Quantized Tiny Pretraining: enoch://control-plane/projects/int8-fake-quantized-tiny-pretraining-9c9002f1b922/runs/int8-fake-quantized-tiny-pretraining-9c9002f1b922-20260608T041710545549+0000
- Parent run decision: Real-Corpus Small-Transformer Fake INT8 Pretraining Ablation: enoch://control-plane/projects/real-corpus-small-transformer-fake-int8-pretraining-ablati-dd356b4c89/runs/real-corpus-small-transformer-fake-int8-pretraining-ablati-dd356b4c89-20260608T091105189729+0000

## What looked useful

The matched FP32 baseline clean INT8 penalty was 3.8e-05 loss and stress INT8 penalty was 9.5e-05 loss. Fake-INT8 weight and weight+activation training reduced mean penalties only by about 2e-05 to 6e-05 loss, below practical significance and comparable to seed variation.

## Boundaries and scale limits

Synthetic corpus rather than real BPE text; about 2M parameters rather than GPT-2-small class; 500 optimizer steps per seed/mode; fake INT8 is symmetric per-tensor straight-through quantization for linear weights and residual activations, not a deployment-kernel exact INT8 implementation.

## Claim scope

In a 2M-parameter decoder-only transformer trained for 500 steps on a synthetic subword-style transition grammar across seeds 11, 23, and 37, fake INT8 pretraining ablations did not yield a practically meaningful robustness gain over a matched FP32 baseline because the FP32 model already had near-zero fake-INT8 evaluation loss penalty.

## Why it stopped

Bounded Tier-2 early-to-medium falsification: direct INT8 robustness metrics were measured with fixed seeds, baseline, and ablations, but the FP32 baseline penalty was already near zero, so the observed fake-INT8 gains are not practically meaningful and do not support a paper claim.

## Recommended next action

Stop this follow-up as a no-paper useful signal; only revisit with a real-tokenizer corpus and a deployment-faithful INT8 path that first demonstrates a nontrivial FP32 quantized-eval penalty.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/subword-small-transformer-fake-int8-pretraining-robustness-d89d595e97`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
