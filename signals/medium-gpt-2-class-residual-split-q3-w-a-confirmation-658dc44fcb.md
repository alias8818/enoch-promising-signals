# Medium GPT-2-class residual-split q3 W+A confirmation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-gpt-2-class-residual-split-q3-w-a-confirmation-658dc44fcb`
Run ID: `medium-gpt-2-class-residual-split-q3-w-a-confirmation-658dc44fcb-20260516T180902953231+0000`

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

- Internal Enoch project: Medium GPT-2-class residual-split q3 W+A confirmation: internal_generated:medium-gpt-2-class-residual-split-q3-w-a-confirmation-658dc44fcb

## What looked useful

Corrected detached residual-split Q3 W+A averaged 2.0668 validation loss versus 2.1694 for plain Q3 W+A, 2.0657 for Q3 weight-only, and 2.0457 for dense over three fixed seeds; naive residual-split averaged 2.5959 and is a negative ablation.

## Boundaries and scale limits

Not GPT-2-small parameter count, not GPT-2 tokenizer, not pretrained GPT-2, not long training, not large corpus, and not deployment-kernel validation.

## Claim scope

On a 6-layer 384-wide byte-level causal transformer trained from scratch for 500 steps on WikiText-2, detached residual-split Q3 activation quantization with Q3 weights recovers most of the validation-loss degradation of plain Q3 W+A and nearly matches Q3 weight-only; naive residual-split STE fails.

## Why it stopped

Tier 2 local confirmation produced a useful but implementation-sensitive signal; it is no-paper evidence because the validation is small byte-level WikiText-2 training rather than GPT-2-small-class publication evidence.

## Recommended next action

Run one bounded deepen follow-up using the detached residual-split variant on GPT-2-small-class tokenization/scale or pretrained GPT-2-small evaluation before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class detached residual-split Q3 W+A validation
- Success threshold: Detached residual-split Q3 W+A must improve validation loss by at least 50% of the plain Q3 W+A degradation relative to dense, while staying within 0.03 loss of Q3 W-only on the same setup.
- Stop condition: Stop if detached residual-split fails to beat plain Q3 W+A on at least two of three seeds, or if its mean validation loss remains more than 0.05 above Q3 W-only.

## Evidence references

- Artifact root: `<local-path>/projects/medium-gpt-2-class-residual-split-q3-w-a-confirmation-658dc44fcb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
