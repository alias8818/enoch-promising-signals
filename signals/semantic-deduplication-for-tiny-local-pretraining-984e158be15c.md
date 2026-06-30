# Semantic deduplication for tiny local pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `semantic-deduplication-for-tiny-local-pretraining-984e158be15c`
Run ID: `semantic-deduplication-for-tiny-local-pretraining-984e158be15c-20260523T120614625129+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/866ca2adf2db

## What looked useful

Perfect semantic-cluster dedup removed paraphrase diversity and produced worse held-out NLL than no dedup and exact dedup: +0.855 same-fact NLL and +0.790 new-fact NLL versus no dedup over five repeats.

## Boundaries and scale limits

Synthetic data only; tiny GRU only; no learned embedding deduper, real web corpus, tokenizer ablation, transformer baseline, or long/full-scale pretraining was tested.

## Claim scope

On a controlled synthetic paraphrase corpus, one-representative oracle semantic deduplication worsened held-out language-model NLL for a tiny word-level GRU trained from scratch under a fixed 240-update budget.

## Why it stopped

Proxy early falsification: oracle one-representative semantic dedup hurt the direct tiny-LM validation metric in the bounded synthetic setting, so the broad idea is not paper-ready without a different policy or real-corpus evidence.

## Recommended next action

Stop this as a no-paper useful signal; if continuing, test diversity-preserving semantic dedup that keeps multiple lexical representatives per cluster on a small real corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Diversity-preserving semantic dedup for tiny LM pretraining
- Success threshold: Diversity-preserving semantic dedup improves held-out NLL by at least 0.10 over exact dedup and no dedup across at least three seeds without reducing unique semantic cluster coverage.
- Stop condition: Stop if all diversity-preserving variants are within 0.05 NLL of exact dedup/no dedup or are worse on held-out NLL across three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-deduplication-for-tiny-local-pretraining-984e158be15c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
