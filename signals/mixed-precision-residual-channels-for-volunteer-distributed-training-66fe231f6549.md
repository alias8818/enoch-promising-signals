# Mixed Precision Residual Channels for Volunteer Distributed Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `mixed-precision-residual-channels-for-volunteer-distributed-training-66fe231f6549`
Run ID: `mixed-precision-residual-channels-for-volunteer-distributed-training-66fe231f6549-20260608T071735204447+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7841a987ac2c

## What looked useful

4-bit quantized averaging lost about 1.3-1.4 percentage points final accuracy versus fp32, while 4-bit error feedback recovered nearly all of it at equal communication. Adding a top-1% fp16 residual channel increased communication by about 0.83 MB per run and improved final accuracy by only about 0.0006 over error feedback in the 10-seed focused run.

## Boundaries and scale limits

Synthetic classification only; no real volunteer network, no multi-node runtime, no privacy/adversarial setting, no GPT-2-small-class or larger language model, no long-horizon training.

## Claim scope

CUDA toy simulation of volunteer-style distributed MLP training with 8 non-IID workers, 15% dropout, local SGD, quantized update averaging, and fp16 top-1% residual correction channels. Residual/error-feedback state recovered 4-bit convergence loss; explicit fp16 residual transmission did not materially outperform standard error feedback.

## Why it stopped

Proxy/local evidence supports residual error feedback but early-falsifies the extra fp16 residual transmission channel as materially useful over standard error feedback in this bounded simulator; this is not full-scale validation.

## Recommended next action

Stop this as no-paper useful signal; a next bounded deepen test should compare residual-channel designs on a small language-model training task with latency-aware communication accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Latency-aware residual-channel compression on a small language model
- Success threshold: Residual-channel variant improves validation loss or perplexity by at least 1% versus standard error feedback at equal communication or equal wall-clock budget across at least 3 seeds.
- Stop condition: Stop if residual-channel variants do not beat standard error feedback by the success threshold or require more than 15% extra communication for less than 0.5% validation-metric improvement.

## Evidence references

- Artifact root: `<local-path>/projects/mixed-precision-residual-channels-for-volunteer-distributed-training-66fe231f6549`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
