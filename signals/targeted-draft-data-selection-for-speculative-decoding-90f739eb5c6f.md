# Targeted Draft Data Selection for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `targeted-draft-data-selection-for-speculative-decoding-90f739eb5c6f`
Run ID: `targeted-draft-data-selection-for-speculative-decoding-90f739eb5c6f-20260604T111643920661+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 10, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- weak evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0c356b85ef28

## What looked useful

Across 4 synthetic domains, 3 seeds, and draft budgets of 25, 50, 100, 200, and 400 docs, targeted same-domain draft data beat random mixed and off-domain-only controls in all 60 paired comparisons. At 200 draft docs, mean overlap was 0.8902 for targeted, 0.5432 for random mixed, and 0.6620 for off-domain-only; the gamma=4 accepted-proposal proxy was 3.0161 versus 1.0886 and 1.5826.

## Boundaries and scale limits

Synthetic corpus only; smoothed bigram language models only; no neural draft model training, no real-corpus acceptance traces, no wall-clock speculative decoding throughput, and no large-model serving validation.

## Claim scope

In a deterministic synthetic topical-corpus word-bigram proxy, selecting draft training data from the target domain increases target/draft next-token distribution overlap, the one-step speculative decoding acceptance quantity, versus same-budget random mixed or off-domain draft data.

## Why it stopped

Proxy-only early positive mechanism signal on synthetic data; not a full validation and not sufficient for paper-positive closure.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should test the same selection strategies with a real corpus and a small neural draft/target pair, measuring exact speculative acceptance and wall-clock throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus neural draft data selection for speculative decoding acceptance
- Success threshold: Target-domain selected draft data improves exact acceptance by at least 10 percentage points or decoding throughput by at least 15% over random mixed selection in both tested domains, without worse target-model output likelihood under exact speculative sampling.
- Stop condition: Stop if targeted selection fails to beat random mixed selection on exact acceptance in either domain, or if throughput gains vanish after including draft-model cost.

## Evidence references

- Artifact root: `<local-path>/projects/targeted-draft-data-selection-for-speculative-decoding-90f739eb5c6f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
