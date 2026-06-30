# Curriculum data selection for tiny CPU pretraining of GPT-2-small class

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `curriculum-data-selection-for-tiny-cpu-pretraining-of-gpt-2-small-class-9839903b3584`
Run ID: `curriculum-data-selection-for-tiny-cpu-pretraining-of-gpt-2-small-class-9839903b3584-20260622T012514534673+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f2f77c424514

## What looked useful

Quality-diversity selection beat random in all seeds, quality-only was mixed and slightly worse on average, and low-quality/noisy selection collapsed. This suggests diversity constraints may be necessary when scalar quality scores over-select easy domains.

## Boundaries and scale limits

Proxy-only CPU experiment; no GPT-2-small-class transformer, no real corpus shards, no BPE tokenization, no downstream tasks, and no long training horizon. Evidence tests data-selection mechanics rather than full pretraining performance.

## Claim scope

In a synthetic mixed-quality corpus with balanced clean validation, a simple quality-plus-diversity selector improved an order-4 byte-level causal n-gram LM over random selection by 0.0203 bits/byte on average across 8 seeds, with 8/8 paired wins under the same 55k-byte budget.

## Why it stopped

No-paper closure: the run produced a reproducible proxy useful signal, but not direct GPT-2-small-class pretraining evidence.

## Recommended next action

Run a direct small-transformer follow-up on real corpus shards with the same random, quality-only, quality-diversity, and low-quality controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer validation of quality-diversity curriculum selection on real corpus shards
- Success threshold: Quality-diversity must beat random and quality-only on final clean validation loss in at least 4/5 seeds with no worse than matched-token compute, and the effect must persist after an early-training checkpoint.
- Stop condition: Stop if quality-diversity fails to beat random in at least 3/5 seeds, or if the observed gain is below 0.5% relative validation-loss improvement with overlapping loss curves.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-data-selection-for-tiny-cpu-pretraining-of-gpt-2-small-class-9839903b3584`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
