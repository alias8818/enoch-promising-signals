# Token-budget-matched bucketed accumulation with micro-batch-count cap

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `token-budget-matched-bucketed-accumulation-with-micro-batc-347563ffa5`
Run ID: `token-budget-matched-bucketed-accumulation-with-micro-batc-347563ffa5-20260524T024509368440+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Adaptive Micro-batch Gradient Accumulation on Real Small-LM Fine-tuning: enoch://control-plane/projects/adaptive-micro-batch-gradient-accumulation-on-real-small-l-02732ee228/runs/adaptive-micro-batch-gradient-accumulation-on-real-small-l-02732ee228-20260524T021323841800+0000
- Parent run decision: Length-bucketed adaptive micro-batch accumulation with matched update count: enoch://control-plane/projects/length-bucketed-adaptive-micro-batch-accumulation-with-mat-82a663d1b1/runs/length-bucketed-adaptive-micro-batch-accumulation-with-mat-82a663d1b1-20260524T023343910663+0000

## What looked useful

The mechanism gives a strong systems win: the distribution-preserving bucketed variant improved throughput by 1.92x versus the 8-accum fixed baseline and reduced padding fraction from 0.643 to 0.344. However, final validation loss worsened by 0.300 versus the 8-accum baseline and by 0.113 versus a same-token/update fixed-random control, so the training-quality claim is not supported.

## Boundaries and scale limits

Synthetic data only; single GB10 GPU; small 2.0M-parameter model; 1.5M non-padding training tokens per seed; no real corpus, large-model, distributed, optimizer-retuned, or production dataloader validation.

## Claim scope

On a deterministic synthetic variable-length causal-LM training harness with a 2.0M-parameter model and three fixed seeds, bucketed length-aware token-budget accumulation with an 8 micro-batch cap reduced padding waste and improved actual-token throughput, but did not preserve validation loss versus fixed-random baselines at matched non-padding training tokens.

## Why it stopped

Bounded validation produced a mixed useful signal rather than publication-grade support: throughput and padding metrics improved, but validation loss degraded under matched-token controls.

## Recommended next action

Stop this paper track; if continuing, first test a real-corpus distribution-preserving implementation with optimizer/batch-size retuning and require validation-loss parity before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus distribution-preserving bucketed token accumulation with optimizer retuning
- Success threshold: Validation loss no worse than 0.02 absolute versus the strongest matched-token baseline and at least 1.5x actual-token throughput with padding fraction reduced by at least 0.20 absolute.
- Stop condition: Stop if validation loss remains worse by more than 0.05 after optimizer retuning, or if throughput gain falls below 1.25x against a packed/bucketed baseline.

## Evidence references

- Artifact root: `<local-path>/projects/token-budget-matched-bucketed-accumulation-with-micro-batc-347563ffa5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
