# GPT-2-medium INT2 RCP versus optimized PTQ baselines across preserve fractions

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `gpt-2-medium-int2-rcp-versus-optimized-ptq-baselines-acros-0372a6fca2`
Run ID: `gpt-2-medium-int2-rcp-versus-optimized-ptq-baselines-acros-0372a6fca2-20260611T125609630398+0000`

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

- Parent run decision: GPT-2-medium INT2 residual channel preservation robustness and storage-normalized baselines: enoch://control-plane/projects/gpt-2-medium-int2-residual-channel-preservation-robustness-ca06202b8f/runs/gpt-2-medium-int2-residual-channel-preservation-robustness-ca06202b8f-20260611T123000477825+0000
- Parent run decision: Medium GPT-2 INT2 Residual Channel Preservation With Realistic Quantization Baselines: enoch://control-plane/projects/medium-gpt-2-int2-residual-channel-preservation-with-reali-672c66cd3f/runs/medium-gpt-2-int2-residual-channel-preservation-with-reali-672c66cd3f-20260611T121052902930+0000

## What looked useful

RCP is useful as a small-fraction channel-preservation mechanism against stronger PTQ baselines, but the effect is non-monotonic and not robust across preserve fractions; increasing preserved fp16 channels to 1/8 degraded the Hessian-grid variant below the no-preserve optimized INT2 baseline.

## Boundaries and scale limits

Single model, single dataset, 128 validation windows, fake quantized fp16 evaluation, no packed INT2 kernels, no latency or memory-bandwidth measurements, and no external GPTQ/AWQ/OmniQuant implementation.

## Claim scope

On GPT-2-medium WikiText-2 validation with fake INT2 target-weight quantization, activation-selected residual channel preservation improves over an optimized activation/Hessian grid-scale INT2 baseline at small preserve fractions 1/64 and 1/32, is marginal at 1/16, and fails at 1/8.

## Why it stopped

Bounded full GPT-2-medium validation found a useful but mixed signal: activation RCP beats optimized PTQ at small preserve fractions, but the across-fractions claim fails at 1/8 and is not paper-positive.

## Recommended next action

Stop paper escalation for this run; if continuing locally, test mask-aware PTQ scale optimization for preserved/non-preserved weights because the current non-monotonic 1/8 result suggests a quantizer-mask interaction rather than a scale-only failure.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Mask-aware PTQ for residual-channel-preserved INT2 GPT-2-medium
- Success threshold: Mask-aware activation RCP must beat no-preserve optimized INT2 by at least 0.5 loss at 1/64 and 1/32, remain no worse than 0.1 loss from no-preserve optimized INT2 at 1/16 and 1/8, and beat top weight-norm same-storage controls at at least three of four preserve fractions.
- Stop condition: Stop if mask-aware RCP still fails to beat no-preserve optimized INT2 at 1/8 or loses to top weight-norm preservation at two or more preserve fractions.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-medium-int2-rcp-versus-optimized-ptq-baselines-acros-0372a6fca2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
