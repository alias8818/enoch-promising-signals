# Complexity-Ordered vs Random Data Ordering for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `complexity-ordered-vs-random-data-ordering-for-tiny-pretraining-701ac0ecb514`
Run ID: `complexity-ordered-vs-random-data-ordering-for-tiny-pretraining-701ac0ecb514-20260619T064042213430+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b5b380ea115a

## What looked useful

Complexity ordering is direction- and horizon-sensitive in this tiny-pretraining probe: easy-to-hard was consistently worse than random, while hard-to-easy became modestly better than random at 2000 steps on all three seeds and mainly improved harder validation quartiles.

## Boundaries and scale limits

Single small corpus, byte tokenizer, tiny Transformer, three seeds, local GB10 runs only; not GPT-2-small-class, not broad-corpus pretraining, not long-horizon or publication-grade validation.

## Claim scope

In a byte-level tiny Transformer trained on Tiny Shakespeare chunks for 600 and 2000 steps, easy-to-hard complexity ordering did not improve validation loss versus random; hard-to-easy ordering showed a small 2000-step validation-loss gain concentrated in harder validation quartiles after lagging at 600 steps.

## Why it stopped

Evidence is mixed and bounded: it falsifies easy-to-hard as a reliable improvement in this setup but only weakly supports hard-to-easy at tiny scale, so it is not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up comparing random versus hard-to-easy on a broader corpus with a GPT-2-small-class or parameter-matched small decoder and at least five seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard-to-easy complexity ordering on broader small-decoder pretraining
- Success threshold: Hard-to-easy must beat random by at least 0.5% mean final validation loss across paired seeds and improve the hardest validation quartile without increasing overall loss variance materially.
- Stop condition: Stop if hard-to-easy fails to beat random on at least four of five paired seeds or if gains disappear outside Tiny Shakespeare/chunked byte-level data.

## Evidence references

- Artifact root: `<local-path>/projects/complexity-ordered-vs-random-data-ordering-for-tiny-pretraining-701ac0ecb514`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
