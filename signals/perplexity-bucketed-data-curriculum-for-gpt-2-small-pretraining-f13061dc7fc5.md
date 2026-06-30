# Perplexity-bucketed data curriculum for GPT-2-small pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `perplexity-bucketed-data-curriculum-for-gpt-2-small-pretraining-f13061dc7fc5`
Run ID: `perplexity-bucketed-data-curriculum-for-gpt-2-small-pretraining-f13061dc7fc5-20260621T191432107249+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/41859764a854

## What looked useful

Across five seeds, random order achieved mean validation NLL 4.1512. Easy-to-hard was worse at 4.1944 (+0.0432 NLL), and hard-to-easy was worse at 4.2188 (+0.0676 NLL). Ordered curricula shifted bucket-specific performance but lost overall.

## Boundaries and scale limits

This was not GPT-2-small, did not use a GPT-2 tokenizer, did not use a natural web corpus, and did not test long-horizon pretraining. It is an early proxy falsification of the simplest schedule, not a full validation.

## Claim scope

In a bounded NumPy tiny neural n-gram language-model proxy with synthetic low/mid/high reference-perplexity documents, simple perplexity-ordered curricula did not improve overall validation loss versus random order.

## Why it stopped

Early proxy falsification: the bounded controlled run found no overall advantage for simple perplexity-bucketed ordering over random order, and the evidence is not full GPT-2-small validation.

## Recommended next action

Stop this worker run as a no-paper proxy result; only pursue a follow-up if running a direct GPT-2-small-class real-corpus experiment with matched random-order control is available.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GPT-2-small perplexity-bucket curriculum on a real corpus
- Success threshold: Curriculum must beat random order by at least 0.02 validation NLL overall at matched token budget without worsening any reference-perplexity validation bucket by more than 0.02 NLL at the final checkpoint.
- Stop condition: Stop if strict or bucket-mixed curriculum fails to beat random order overall by 0.02 validation NLL after the planned matched token budget, or if gains appear only by sacrificing one bucket by more than 0.02 NLL.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-bucketed-data-curriculum-for-gpt-2-small-pretraining-f13061dc7fc5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
