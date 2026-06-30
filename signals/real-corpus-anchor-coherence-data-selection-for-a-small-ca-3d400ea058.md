# Real-corpus anchor-coherence data selection for a small causal LM

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-corpus-anchor-coherence-data-selection-for-a-small-ca-3d400ea058`
Run ID: `real-corpus-anchor-coherence-data-selection-for-a-small-ca-3d400ea058-20260603T204613773756+0000`

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

- Parent run decision: Tiny Pretraining Data Selection by Long-Range Anchor Coherence: enoch://control-plane/projects/tiny-pretraining-data-selection-by-long-range-anchor-coherence-d2315332b5d8/runs/tiny-pretraining-data-selection-by-long-range-anchor-coherence-d2315332b5d8-20260603T143951224373+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/93566c73e35a

## What looked useful

Anchor-high selection beat random by a consistent but tiny mean 0.2149% relative high-anchor NLL and beat anchor-low by about 0.51% relative NLL, while general validation loss was neutral. The score appears to carry a weak mechanism signal but not enough practical effect for the stated threshold.

## Boundaries and scale limits

Byte-level tokenizer, Wikitext-2 only, 640 selected training blocks per condition, 192 high-anchor validation blocks, 550 optimizer steps per model, and sub-1M-parameter models; not evidence about large tokenized corpora, GPT-2-small-class models, or long training runs.

## Claim scope

In a three-seed Tier 1 direct Wikitext-2 test with a 496k-parameter byte-level causal transformer, anchor-coherence-selected training blocks did not reach the preregistered 3% held-out high-anchor NLL improvement over equal-token random selection.

## Why it stopped

Replicated direct Tier 1 validation failed the preregistered threshold in 0/3 seeds; the observed anchor-high gain over random was about 0.21% rather than the required 3%, so this is an early direct falsification of the threshold, not a full-scale validation.

## Recommended next action

Stop this run as a no-paper useful signal; run one bounded medium confirmation with GPT-2-style tokenization, larger real-corpus samples, and multiple random controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium tokenized anchor-coherence confirmation on real corpus
- Success threshold: Mean anchor-high held-out high-anchor NLL at least 1% lower than the random-control mean, no more than 1% worse on general validation NLL, and improvement positive in at least 8 of 9 anchor-high versus random-control comparisons.
- Stop condition: Stop if anchor-high fails to beat the random-control mean by 1% or if general validation NLL degrades by more than 1%.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-anchor-coherence-data-selection-for-a-small-ca-3d400ea058`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
