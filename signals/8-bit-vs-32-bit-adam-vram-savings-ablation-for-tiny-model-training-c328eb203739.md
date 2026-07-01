# 8-bit vs 32-bit Adam: VRAM Savings Ablation for Tiny Model Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-vs-32-bit-adam-vram-savings-ablation-for-tiny-model-training-c328eb203739`
Run ID: `8-bit-vs-32-bit-adam-vram-savings-ablation-for-tiny-model-training-c328eb203739-20260613T192136034952+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/5d0558a2f703

## What looked useful

8-bit AdamW materially shrinks optimizer state for tiny transformer training, but tiny-model peak VRAM savings are much smaller than optimizer-state savings and shrink further when activation memory grows with batch size.

## Boundaries and scale limits

Synthetic random-token data, 20-step runs, fp32 training, one GB10 system, bitsandbytes 0.49.2, PyTorch 2.12.0+cu130, and model sizes below GPT-2-small. Results measure memory mechanics, not convergence or final model quality.

## Claim scope

On this GB10 worker, short synthetic micro-to-medium transformer training runs with 0.67M to 13.84M parameters showed bitsandbytes AdamW8bit reduced optimizer-state memory by about 74%, while end-to-end CUDA peak allocated memory fell by only 2.2% to 15.5% depending on model and batch size.

## Why it stopped

The result is a bounded synthetic memory-mechanics ablation, not full validation; it supports a practical caveat rather than a paper-ready claim.

## Recommended next action

Stop this run as no-paper useful signal; a bounded deepen follow-up should repeat the ablation on a GPT-2-small-class real-data workload with mixed precision and fixed convergence checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class real-data 8-bit AdamW peak-memory and convergence ablation
- Success threshold: AdamW8bit reaches within 2% of AdamW32 validation loss over the fixed sequence-item budget while reducing optimizer-state memory by at least 65% and documenting total peak VRAM savings for each batch setting.
- Stop condition: Stop if AdamW8bit fails to run correctly on the target workload, diverges relative to AdamW32, or total peak VRAM savings remain below 5% in all tested realistic settings.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-vs-32-bit-adam-vram-savings-ablation-for-tiny-model-training-c328eb203739`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
