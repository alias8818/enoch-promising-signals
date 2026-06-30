# Length-based curriculum vs random order for tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `length-based-curriculum-vs-random-order-for-tiny-pretraining-5b45e21632d3`
Run ID: `length-based-curriculum-vs-random-order-for-tiny-pretraining-5b45e21632d3-20260628T035433655891+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bcfe059b0544

## What looked useful

Random order beat length curriculum on overall validation NLL for 5/5 seeds (mean delta curriculum-random +0.01937), while length curriculum beat random on long-sequence NLL for 5/5 seeds (mean long delta -0.02514).

## Boundaries and scale limits

Synthetic grammar corpus, CPU-only small RNN, 900 train examples per seed, 2 epochs, no transformer, no natural text, no GPT-2-small-class baseline, no large-corpus validation.

## Claim scope

In a 5-seed synthetic tiny NumPy RNN next-token pretraining proxy, length-sorted curriculum did not improve average validation NLL versus random order, but consistently improved long-sequence validation NLL.

## Why it stopped

Bounded proxy produced mixed useful signal but no paper-ready support for the broad length-curriculum hypothesis.

## Recommended next action

Stop this proxy run; run a bounded direct small-transformer follow-up on a real text corpus with random, ascending-length, descending-length, and bucketed-shuffle controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer real-text length ordering control study
- Success threshold: Length-based or bucketed ordering must improve overall validation NLL by at least 1% over random on a majority of paired seeds without degrading short or medium length buckets by more than 1%.
- Stop condition: Stop if random order matches or beats overall validation NLL on at least 4/5 paired seeds, or if gains remain confined to the long bucket while average loss worsens.

## Evidence references

- Artifact root: `<local-path>/projects/length-based-curriculum-vs-random-order-for-tiny-pretraining-5b45e21632d3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
