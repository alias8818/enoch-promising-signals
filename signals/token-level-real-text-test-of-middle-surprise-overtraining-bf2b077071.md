# Token-level real-text test of middle-surprise overtraining robustness

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `token-level-real-text-test-of-middle-surprise-overtraining-bf2b077071`
Run ID: `token-level-real-text-test-of-middle-surprise-overtraining-bf2b077071-20260520T041606734620+0000`

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

- Parent run decision: Middle-surprise filtering for tiny neural LM pretraining: enoch://control-plane/projects/middle-surprise-filtering-for-tiny-neural-lm-pretraining-7a17cd0d86/runs/middle-surprise-filtering-for-tiny-neural-lm-pretraining-7a17cd0d86-20260520T034927445434+0000
- Parent run decision: Real-text tiny transformer test of middle-surprise filtering: enoch://control-plane/projects/real-text-tiny-transformer-test-of-middle-surprise-filteri-42a4a54316/runs/real-text-tiny-transformer-test-of-middle-surprise-filteri-42a4a54316-20260520T035456616350+0000

## What looked useful

Middle-surprise filtering reduced mean final-minus-best validation overfit gap versus random by 0.0944 nats overall and won 2/3 paired seeds, but low-surprise filtering had the best filtered overfit gap overall (3.8166 vs 4.1906 for middle) and on middle-surprise validation tokens (4.8847 vs 5.2116).

## Boundaries and scale limits

Single small real-text corpus, compact observed GPT-2 BPE vocabulary, token-bigram pilot scorer, 3.81M parameter model, three filtered seeds, one full-data seed; not GPT-2-small-class or broad-corpus evidence.

## Claim scope

On Tiny Shakespeare with GPT-2 BPE tokenization, a 3.81M parameter decoder-only transformer, token-bigram surprise scoring, and 3200-step fixed-budget overtraining, middle-surprise filtering is modestly more robust than random and high-surprise filtering but not more robust than low-surprise filtering.

## Why it stopped

Direct bounded token-level validation produced a mixed-negative result: middle beats random/high modestly but fails the stated threshold because low-surprise is the stronger equal-token overtraining-robustness control.

## Recommended next action

Stop treating middle-surprise overtraining robustness as supported; if continuing, branch to test whether low-surprise robustness is a duplicate/easy-token artifact under diversity-matched controls.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Diversity-matched test of low-surprise overtraining robustness
- Success threshold: Low-surprise robustness is considered an artifact if diversity-matched low no longer beats middle and random by at least 0.05 nats mean final-minus-best overall gap across three seeds; it is considered a real branch signal if low still beats both by at least 0.05 nats and wins at least 2/3 paired seeds.
- Stop condition: Stop after the diversity-matched three-seed grid if low no longer beats both controls or if full-data remains the only robust condition and all filtered differences are under 0.05 nats.

## Evidence references

- Artifact root: `<local-path>/projects/token-level-real-text-test-of-middle-surprise-overtraining-bf2b077071`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
