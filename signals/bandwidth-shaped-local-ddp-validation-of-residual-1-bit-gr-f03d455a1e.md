# Bandwidth-shaped local DDP validation of residual 1-bit gradients

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bandwidth-shaped-local-ddp-validation-of-residual-1-bit-gr-f03d455a1e`
Run ID: `bandwidth-shaped-local-ddp-validation-of-residual-1-bit-gr-f03d455a1e-20260522T161304426363+0000`

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

- Parent run decision: Residual-Compensated 1-bit Gradients for Home Distributed Training: enoch://control-plane/projects/residual-compensated-1-bit-gradients-for-home-distributed-training-f1824475b741/runs/residual-compensated-1-bit-gradients-for-home-distributed-training-f1824475b741-20260522T150955082830+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bd4403e6afb2

## What looked useful

On the harder 3-seed controlled task, dense DDP reached 0.9671 mean validation accuracy. Bandwidth-shaped residual 1-bit at 10% active coordinates reached 0.9668 mean validation accuracy, -0.03 percentage points versus dense, with 5.0% of dense estimated payload. The 5% active-coordinate stress run reached 0.9666, -0.05 percentage points, with 2.5% payload.

## Boundaries and scale limits

Synthetic MLP task only; 2 local CPU ranks; payload is estimated and excludes protocol/framework headers; no NCCL/GPU communication hook, multi-node network, larger worker count, or real dataset/model validation.

## Claim scope

In a two-rank localhost torch.distributed Gloo synthetic classification test, residual error-feedback 1-bit gradient synchronization with top-|gradient| bandwidth shaping preserved validation accuracy relative to dense FP32 gradient averaging while reducing estimated gradient payload.

## Why it stopped

Tier 1 controlled small direct test met the useful-signal threshold, but evidence is synthetic/local and not enough for a paper.

## Recommended next action

Run a bounded real-dataset DDP communication-hook validation on CIFAR-10 or a small language-model task with dense, full residual 1-bit, 10% bandwidth-shaped residual 1-bit, and error-feedback-off controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-dataset DDP hook validation of bandwidth-shaped residual 1-bit gradients
- Success threshold: 10% active-coordinate residual 1-bit must finish within 2 validation percentage points of dense DDP across three seeds, use no more than 10% estimated gradient payload, and avoid monotonic residual-norm growth in the final third of training.
- Stop condition: Stop if 10% active-coordinate residual 1-bit is more than 2 validation percentage points below dense on at least two seeds, or if error-feedback-off matches error-feedback-on while residual norms grow, indicating the proposed residual mechanism is not carrying the effect.

## Evidence references

- Artifact root: `<local-path>/projects/bandwidth-shaped-local-ddp-validation-of-residual-1-bit-gr-f03d455a1e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
