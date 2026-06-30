# Gradient-norm coreset selection for tiny CPU pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `gradient-norm-coreset-selection-for-tiny-cpu-pretraining-df5e5b88b9e9`
Run ID: `gradient-norm-coreset-selection-for-tiny-cpu-pretraining-df5e5b88b9e9-20260528T134621073809+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c8ad9af5b056

## What looked useful

Gradient-norm scores were highly correlated with scoring loss (r = 0.925 and 0.881), and top-gradient subsets were much worse than random: +2.2116 validation loss at 20% subset and +1.6314 at 50% subset. Raw gradient-norm selection appears to overselect hard/outlier contexts rather than representative pretraining data in this proxy.

## Boundaries and scale limits

Tested 6,000 character-context examples, a small MLP rather than a transformer, character tokens rather than subword tokens, one public text corpus, two subset-budget settings, and short CPU-only training runs. This does not validate behavior for GPT-2-small-class or larger transformer pretraining.

## Claim scope

Naive top per-example gradient-norm coreset selection from a shared warmup checkpoint did not improve and substantially worsened validation loss versus random equal-budget subset selection for a NumPy tiny character next-token MLP trained on fixed-context tiny Shakespeare examples.

## Why it stopped

Bounded proxy/direct-small-model falsification: the exact tested method consistently underperformed random selection by large margins, so the result is no-paper useful negative evidence rather than full-scale validation.

## Recommended next action

Stop the naive high-gradient-norm coreset idea for tiny CPU pretraining unless a future run adds an explicit diversity or token-coverage constraint and tests a direct tiny transformer baseline.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-coreset-selection-for-tiny-cpu-pretraining-df5e5b88b9e9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
