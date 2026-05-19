# GPT-2-small-class detached residual-split Q3 W+A validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `gpt-2-small-class-detached-residual-split-q3-w-a-validatio-d08e69867d`
Run ID: `gpt-2-small-class-detached-residual-split-q3-w-a-validatio-d08e69867d-20260516T182252714824+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: GPT-2-small-class detached residual-split Q3 W+A validation: internal_generated:gpt-2-small-class-detached-residual-split-q3-w-a-validatio-d08e69867d

## What looked useful

At step 450, mean validation loss over three seeds was dense 6.3599, Q3 W-only 6.3760, plain Q3 W+A 6.3978, and detached residual-split Q3 W+A 6.3703. Detached residual-split improved over plain Q3 W+A by 0.0275 loss, recovered 72.6% of the plain Q3 W+A degradation, and was 0.0057 loss better than Q3 W-only on mean. A seed-11 naive residual-split ablation at step 300 was much worse at 7.4408 loss.

## Boundaries and scale limits

This was GPT-2-small-class architecture and tokenizer, but not pretrained GPT-2-small, not a long schedule, not a large corpus, not downstream evaluation, not packed low-bit kernels, and not real deployment memory-compression validation. Naive residual-split was only checked for one seed through 300 steps.

## Claim scope

On a 123.8M-parameter GPT-2-small-class causal transformer trained from scratch on WikiText-2 with GPT-2 BPE for 450 steps over seeds 11, 22, and 33, detached residual-split Q3 W+A reduced validation loss versus plain Q3 W+A and met the inherited threshold by recovering 72.6% of the plain Q3 W+A degradation relative to dense while staying within 0.03 loss of Q3 weight-only.

## Why it stopped

Bounded local Tier 3 validation produced a useful direct GPT-2-small-class signal that met the scoped success threshold, but it remains no-paper evidence because it is short from-scratch fake-quant training rather than pretrained, long-schedule, deployment-kernel, or broad-corpus validation.

## Recommended next action

Run a final depth-4 robustness follow-up on pretrained GPT-2-small or a longer WikiText/OpenWebText schedule with bootstrap confidence intervals and a fuller naive-detach ablation; stop after that unless it is paper-ready.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2-small detached residual-split Q3 W+A robustness validation
- Success threshold: Detached residual-split Q3 W+A must recover at least 60% of the plain Q3 W+A perplexity or validation-loss degradation relative to dense, stay within 0.03 loss of Q3 weight-only, and beat plain Q3 W+A under confidence intervals or all fixed seeds.
- Stop condition: Stop if detached residual-split fails to beat plain Q3 W+A under the direct pretrained/fine-tuning metric, if it is more than 0.05 loss worse than Q3 weight-only, or if the depth-4 run still cannot support a paper-ready claim.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-detached-residual-split-q3-w-a-validatio-d08e69867d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
