# Queue-Based Data Selection with Batch-Adaptive Sampling for Tiny Local Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `queue-based-data-selection-with-batch-adaptive-sampling-for-tiny-local-pretraining-f1d07e2a3f7e`
Run ID: `queue-based-data-selection-with-batch-adaptive-sampling-for-tiny-local-pretraining-f1d07e2a3f7e-20260607T002405355468+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/63bd8534a579

## What looked useful

QBAS reached 0.9307 +/- 0.0818 clean validation loss versus 2.0237 +/- 0.0082 for uniform and 2.0858 +/- 0.0112 for high-loss queue at 1500 steps. It reduced selected noise from about 57.9% under uniform to 5.6% and increased hard clean examples from 12.0% to 39.6%. Naive high-loss queuing over-sampled noise at 68.3% and underperformed uniform.

## Boundaries and scale limits

Synthetic 64-token vocabulary, 32-token sequences, 2-layer 96-wide transformer, 1500 training steps, 5 seeds, one GB10 GPU. QBAS used synthetic domain IDs for batch quotas; no real text corpus, tokenizer, large model, long training run, or metadata-free production setting was tested.

## Claim scope

In a synthetic tiny causal-LM pretraining proxy with a noisy mixed pool and clean validation target, a metadata-aware queue-based sampler using mid-loss/progress scoring plus batch-adaptive hard-clean allocation improved clean validation loss over uniform sampling and naive high-loss priority.

## Why it stopped

Closed as no-paper useful signal because evidence is controlled synthetic proxy evidence, not direct real-corpus or large-scale pretraining validation.

## Recommended next action

Run a bounded deepen follow-up on a small real corpus with clean/noisy source metadata and a metadata-free or metadata-limited QBAS variant before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus metadata-limited QBAS for tiny causal-LM pretraining
- Success threshold: QBAS improves clean validation loss by at least 10% relative to uniform and does not increase noisy-source exposure above uniform after matched token budget.
- Stop condition: Stop if QBAS fails to beat uniform on mean clean validation loss across 3 seeds or if gains require explicit labels unavailable in the target deployment.

## Evidence references

- Artifact root: `<local-path>/projects/queue-based-data-selection-with-batch-adaptive-sampling-for-tiny-local-pretraining-f1d07e2a3f7e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
