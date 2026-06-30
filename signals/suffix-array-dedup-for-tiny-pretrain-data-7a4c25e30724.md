# Suffix Array Dedup for Tiny Pretrain Data

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-dedup-for-tiny-pretrain-data-7a4c25e30724`
Run ID: `suffix-array-dedup-for-tiny-pretrain-data-7a4c25e30724-20260528T180813305949+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/10efd384d24c

## What looked useful

Suffix-array dedup is a sensitive detector of exact long-span duplicates, but naive span deletion has an unfavorable threshold tradeoff on tiny data: min_len 64 reduced leaky overlap 0.732 to 0.460 but retained only 0.236 of leaky bytes and 0.234 of clean bytes; min_len 256 retained 0.993 of clean bytes but left leaky overlap essentially unchanged at 0.731.

## Boundaries and scale limits

Synthetic controlled corpora only; no real web/TinyStories corpus and no neural LM pretraining run. Corpus sizes were around hundreds of KB per condition and the language-model proxy was a smoothed character 4-gram model.

## Claim scope

Controlled tiny-corpus experiments show that naive suffix-array exact-span dedup can remove long duplicate leakage missed by line dedup, but the effective thresholds also remove too much clean text for tiny pretraining data.

## Why it stopped

Proxy/controlled early falsification of the naive suffix-array span-removal hypothesis, not a full validation or full rejection of all suffix-array dedup policies.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should evaluate a less destructive suffix-array policy on a real tiny pretraining corpus with a small neural LM memorization/perplexity check.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Less-destructive suffix-array dedup policy on a real tiny corpus
- Success threshold: Constrained suffix-array dedup retains >=90% of clean bytes, reduces injected held-out 64-gram overlap by >=50% versus raw, beats line dedup on leakage, and does not worsen small neural LM validation loss by more than 2%.
- Stop condition: Stop if constrained suffix-array dedup cannot beat line dedup on leakage at >=90% clean-byte retention or if the neural LM check shows a validation loss regression above 2%.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-dedup-for-tiny-pretrain-data-7a4c25e30724`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
