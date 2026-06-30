# Curriculum Data Selection for TinyLM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `curriculum-data-selection-for-tinylm-0dfac2dce9eb`
Run ID: `curriculum-data-selection-for-tinylm-0dfac2dce9eb-20260528T135631024722+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/093bcd84ab6e

## What looked useful

Easy-first selection was worse than random in every seed (+0.0346 mean final validation loss), easy-only was strongly worse (+0.2853), and hard-to-easy was slightly better than random in every seed (-0.0126). Researchers should test hard-first/hard-weighted data ordering before assuming easy-to-hard curricula help TinyLMs.

## Boundaries and scale limits

Single small character-level corpus, simple unigram difficulty heuristic, 3 seeds, 800-step budget, no tokenizer-level or multi-corpus validation; not a broad TinyLM curriculum result.

## Claim scope

On Tiny Shakespeare with a 471k-parameter character-level TinyLM trained for 800 steps over 3 seeds, unigram-surprisal easy-to-hard curriculum worsened validation loss versus random, while hard-to-easy produced a small consistent improvement.

## Why it stopped

No-paper useful signal: direct toy-scale evidence falsifies easy-to-hard curriculum in this setup and suggests a small hard-first advantage, but the scale and heuristic are insufficient for publication-grade validation.

## Recommended next action

Run one bounded deepen follow-up with a subword tokenizer, a 2-5M parameter TinyLM, stronger final evaluation, two corpora, and 5-10 seeds to test whether the hard-first advantage persists.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Subword TinyLM hard-first curriculum confirmation
- Success threshold: Hard-to-easy or hard-weighted selection beats random by at least 0.02 final validation loss or 1% relative perplexity on both corpora, with paired improvement in at least 80% of seeds and no worse curve AUC.
- Stop condition: Stop if hard-first fails to beat random on either corpus or if the effect shrinks below 0.01 loss after stronger evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-data-selection-for-tinylm-0dfac2dce9eb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
