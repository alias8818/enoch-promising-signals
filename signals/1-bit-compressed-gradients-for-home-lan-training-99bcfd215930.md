# 1-bit Compressed Gradients for Home LAN Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-compressed-gradients-for-home-lan-training-99bcfd215930`
Run ID: `1-bit-compressed-gradients-for-home-lan-training-99bcfd215930-20260605T004939718521+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/f39d9fa0999d

## What looked useful

Error feedback is the necessary mechanism for this idea: plain 1-bit sign exchange saved bandwidth but hurt convergence, while sign plus error feedback retained most dense-baseline behavior at the same modeled 32x payload reduction.

## Boundaries and scale limits

No real LAN transport, no separate machines, no NCCL/TCP timing, no real dataset/model, no long-run persistence, and no adaptive optimizer validation were tested.

## Claim scope

In a CUDA-backed virtual four-worker synthetic MLP training setup with non-IID batches, packed 1-bit sign gradients with error feedback reduced modeled LAN payload by about 32x and approximately preserved dense gradient averaging on one noisy task while losing 0.035 mean accuracy on a cleaner confirmation task; plain sign-only compression degraded accuracy.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic and virtual-worker only; it supports a mechanism to test next, not a publication-grade validation of home-LAN training.

## Recommended next action

Run a bounded two-machine home-LAN experiment with packed sign+error-feedback gradients, dense DDP control, measured step time, measured payload, and a real small model/dataset.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two-machine LAN validation of packed sign gradients with error feedback
- Success threshold: sign_ef achieves at least 20 percent lower communication-dominated step time than dense DDP and final validation accuracy within 5 percentage points of dense after the same number of optimizer steps.
- Stop condition: Stop if sign_ef is slower end-to-end than dense after packing overhead or loses more than 5 percentage points validation accuracy in two repeated runs.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-compressed-gradients-for-home-lan-training-99bcfd215930`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
