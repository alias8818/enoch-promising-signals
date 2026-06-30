# QAT with Gradient Residual Channels for Home GPUs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `qat-with-gradient-residual-channels-for-home-gpus-b4e1996cb12c`
Run ID: `qat-with-gradient-residual-channels-for-home-gpus-b4e1996cb12c-20260604T153203784978+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/52d33b61574f

## What looked useful

Five-seed medium runs on NVIDIA GB10 showed residual-minus-plain accuracy/loss deltas of -0.00151/+0.00093 at 4-bit gradients and +0.00083/-0.00294 at 2-bit gradients. The mechanism may be useful only under severe gradient quantization, but the effect is small and mixed.

## Boundaries and scale limits

Toy MLP classification only; no GPT-2-small-class transformer, no language modeling perplexity, no production fused low-bit kernels, no optimizer-state quantization, and no long memory-pressure run.

## Claim scope

On a deterministic two-moons MLP proxy with 4-bit fake-quantized weights/activations, per-parameter residual error-feedback gradient channels did not help at 4-bit gradients but gave a small mean loss improvement under 2-bit gradient stress.

## Why it stopped

No-paper proxy closure: the 4-bit direct proxy was negative, and the 2-bit benefit was small, mixed by seed, and not transformer-scale.

## Recommended next action

Run one bounded transformer follow-up on a GPT-2-small-class or parameter-matched character/token language model comparing plain versus residual 2-bit and 4-bit gradient QAT on validation loss/perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer QAT residual-gradient stress test
- Success threshold: Residual QAT beats plain gradient QAT by at least 1% relative validation loss or perplexity at the same bit-width and budget, with no more than 10% wall-clock overhead and no material memory regression.
- Stop condition: Stop if residual QAT fails to beat plain QAT by 0.5% relative validation loss in an early one-seed transformer probe or if runtime projects above the local GB10 budget without checkpointable partial metrics.

## Evidence references

- Artifact root: `<local-path>/projects/qat-with-gradient-residual-channels-for-home-gpus-b4e1996cb12c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
