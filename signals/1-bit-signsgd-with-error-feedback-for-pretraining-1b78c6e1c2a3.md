# 1-bit SignSGD with Error Feedback for Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-signsgd-with-error-feedback-for-pretraining-1b78c6e1c2a3`
Run ID: `1-bit-signsgd-with-error-feedback-for-pretraining-1b78c6e1c2a3-20260621T102753787565+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/e2df2029c8a7

## What looked useful

Error feedback was not inert: high-precision three-seed final validation loss improved from 2.4221 for mean-scaled signSGD to 2.3882 for EF mean-scaled signSGD. The same run showed AdamW at 2.1107 and tuned raw signSGD at 2.0654, so the broader pretraining viability claim remains unsupported.

## Boundaries and scale limits

Single GB10 GPU, single-process optimizer simulation, Tiny Shakespeare character modeling, three seeds, bounded learning-rate calibration, no distributed all-reduce, no BPE/token-level corpus, no GPT-2-small or larger validation, no 1B-parameter pretraining.

## Claim scope

On a 624k-parameter character-level GPT trained for 600 steps on Tiny Shakespeare, error-feedback mean-scaled 1-bit signSGD trains stably and slightly improves over mean-scaled signSGD without error feedback, but does not beat AdamW or tuned raw signSGD.

## Why it stopped

Proxy evidence is mixed: EF improves a faithful mean-scaled 1-bit compressor slightly, but the result is small-scale and weaker than AdamW and tuned raw signSGD, so it is not a full validation or paper-positive result.

## Recommended next action

Stop this run as no-paper useful signal; a bounded deepen follow-up should test EF 1-bit compression with a larger LR sweep, warmup/momentum variants, and a GPT-2-small-class BPE language-model proxy before any distributed or 1B-scale claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tuned EF 1-bit compression on GPT-2-small-class BPE language modeling
- Success threshold: EF mean-scaled signSGD should reduce validation loss versus no-EF mean-scaled signSGD by at least 0.05 or close at least half of the gap to AdamW without instability at the same token budget.
- Stop condition: Stop if EF remains within 0.02 validation loss of no-EF mean-scaled signSGD across calibrated settings or remains more than 0.15 validation loss worse than AdamW after matched token budgets.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-signsgd-with-error-feedback-for-pretraining-1b78c6e1c2a3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
