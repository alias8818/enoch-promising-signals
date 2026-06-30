# Real-corpus DSIR-lite confirmation for tiny target-domain pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-corpus-dsir-lite-confirmation-for-tiny-target-domain-6ed220a78a`
Run ID: `real-corpus-dsir-lite-confirmation-for-tiny-target-domain-6ed220a78a-20260613T125651841814+0000`

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

- Parent run decision: Importance Resampling Lite (DSIR) for Tiny Pretraining: enoch://control-plane/projects/importance-resampling-lite-dsir-for-tiny-pretraining-faf1cbafc9c9/runs/importance-resampling-lite-dsir-for-tiny-pretraining-faf1cbafc9c9-20260613T123650646193+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3c2469b6e979

## What looked useful

DSIR-lite strongly enriched target-domain documents but did not improve tiny target-domain LM pretraining over random. In the final equal-token fairness pass, DSIR-lite selected 60.00% target documents versus a 5.03% target pool, but final held-out target NLL was worse than random: DSIR-lite 6.7149 vs random 6.3880 over three seeds.

## Boundaries and scale limits

Single corpus, single target category, tiny LSTM, short training, unigram selector, and three random seeds; not a full DSIR or GPT-2-scale validation.

## Claim scope

Tier 1 real-corpus test on 20 Newsgroups sci.space with 32 target seed documents, DSIR-lite unigram selection, tiny LSTM pretraining, equal target fine-tuning, and held-out target-domain NLL.

## Why it stopped

Controlled small direct real-corpus test falsified the expected DSIR-lite over random improvement under equal token budgets; this is not a full validation, but it is sufficient to reject the Tier 1 confirmation.

## Recommended next action

Stop this confirmation as no-paper negative/useful-signal evidence; only reopen with a bounded medium transformer/category-sweep test that directly checks whether the negative LSTM result is architecture- or category-specific.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium transformer/category sweep for DSIR-lite target-domain pretraining
- Success threshold: DSIR-lite must beat random by at least 0.05 held-out target NLL on mean across categories and seeds, with no more than one category showing a negative effect.
- Stop condition: Stop if DSIR-lite fails to beat random mean held-out target NLL in two categories after matched token budgets and identical training steps.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-dsir-lite-confirmation-for-tiny-target-domain-6ed220a78a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
