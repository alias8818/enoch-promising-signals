# Perplexity-Threshold Data Filter Ladder for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-threshold-data-filter-ladder-for-tiny-pretraining-b40410baf0ed`
Run ID: `perplexity-threshold-data-filter-ladder-for-tiny-pretraining-b40410baf0ed-20260621T152900937113+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7e6ee64797e2

## What looked useful

Filtering by teacher perplexity reduced mean clean validation BPC from 0.5586 for all-data to 0.4607 for median-threshold filtering. The ladder also beat all-data at 0.4915 BPC, but was worse than median-threshold filtering and reintroduced about 11.4% noisy documents.

## Boundaries and scale limits

Synthetic generated corpus, character 5-gram teacher/student models, five seeds, CPU-only 8-second run. No neural optimizer dynamics, real web-corpus distribution, tokenizer effects, downstream task transfer, or large-scale pretraining were tested.

## Claim scope

On a synthetic clean/noisy character-LM proxy, teacher perplexity filtering improves equal-token-budget tiny language-model validation loss over all-data training, but the staged q25/q50/q75 ladder does not beat a simpler median-threshold filter.

## Why it stopped

Proxy evidence supports perplexity filtering but not the ladder-specific advantage; this is early bounded evidence, not full validation.

## Recommended next action

Stop this run as no-paper useful signal; if deepening, run a small neural LM on a real mixed-quality corpus with ladder, tuned one-shot thresholds, and all-data controls under matched tokens and seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural Tiny-LM Perplexity Filter Ladder on Real Mixed-Quality Text
- Success threshold: Ladder mean held-out loss is at least 2% lower than the best one-shot threshold control and wins on at least 3 of 3 seeds under matched token budget.
- Stop condition: Stop if ladder fails to beat the best one-shot threshold control or if the run would exceed local CPU budget without GPU/model-hardware justification.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-threshold-data-filter-ladder-for-tiny-pretraining-b40410baf0ed`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
