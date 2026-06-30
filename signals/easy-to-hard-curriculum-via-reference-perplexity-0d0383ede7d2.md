# Easy-to-Hard Curriculum via Reference Perplexity

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `easy-to-hard-curriculum-via-reference-perplexity-0d0383ede7d2`
Run ID: `easy-to-hard-curriculum-via-reference-perplexity-0d0383ede7d2-20260613T150201971706+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ee0ff0d24823

## What looked useful

Reference perplexity cleanly separated generated hard from easy examples in all 30 seeds, but reference easy-to-hard ordering had worse final validation NLL than random in every seed: mean delta +0.144188 NLL, 95% bootstrap CI [+0.132475, +0.156332], where positive favors random.

## Boundaries and scale limits

No real corpus, no transformer, no tokenizer or batching effects, no large-scale pretraining. The result is an early proxy falsification of the strict sorted curriculum mechanism, not a universal rejection of reference-perplexity curricula.

## Claim scope

Bounded synthetic character-language proxy with a fixed trigram reference scorer and online bigram softmax learner. Strict easy-to-hard ordering by reference perplexity did not improve fixed-budget validation NLL versus random/control orderings.

## Why it stopped

A bounded CPU proxy produced an early negative result for strict easy-to-hard reference-perplexity ordering; this is not a full validation, but it is enough to avoid paper-positive claims from this run.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test mixed or annealed reference-perplexity schedules against strict sorting and random on the same proxy before any real-corpus transformer run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Annealed Reference-Perplexity Curriculum Versus Strict Sorting
- Success threshold: Annealed reference-perplexity schedule beats random by at least 0.03 final validation NLL with a 95% paired bootstrap CI entirely below 0, and does not increase hard-regime validation NLL.
- Stop condition: Stop if annealed schedules fail to beat random under the paired threshold or if any gain appears only in easy-regime validation while hard-regime NLL worsens.

## Evidence references

- Artifact root: `<local-path>/projects/easy-to-hard-curriculum-via-reference-perplexity-0d0383ede7d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
