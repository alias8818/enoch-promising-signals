# Domain-Mixture Grid Search for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `domain-mixture-grid-search-for-tiny-pretraining-1adf7361c731`
Run ID: `domain-mixture-grid-search-for-tiny-pretraining-1adf7361c731-20260526T020850934675+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/07c14c56f2fd

## What looked useful

Fine grid search found target-specific mixtures with 6.9% lower NLL than uniform for code-heavy validation and 3.5% lower NLL for prose-heavy validation; balanced validation improved only 0.7% and was not robust across seeds. Single-domain mixtures were poor for all mixed targets.

## Boundaries and scale limits

Synthetic domains and smoothed n-gram LM only; no neural transformer, real corpus, tokenizer, optimizer, downstream task, or large-scale pretraining evidence. Final fine sweep used 288 mixtures, 5 seeds, and 50k training characters per run.

## Claim scope

In a synthetic four-domain, fixed-token, character 6-gram tiny LM proxy, grid-selected mixtures improved held-out next-token NLL over uniform/source-proportional baselines for code-heavy and prose-heavy target distributions, while balanced-target gains were weak and seed-sensitive.

## Why it stopped

Closed as no-paper useful signal because the current result is a synthetic n-gram proxy, not direct transformer pretraining evidence; it supports a bounded follow-up rather than a publication claim.

## Recommended next action

Run a bounded tiny-transformer follow-up on real small domain corpora with fixed token/FLOP budgets and compare grid-selected mixtures against uniform, source-proportional, and target-proportional controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer Domain-Mixture Confirmation on Real Corpora
- Success threshold: Grid-selected mixture improves target-weighted validation loss by at least 2% over both uniform and source-proportional baselines on two non-uniform target distributions, with the same or adjacent mixture family winning in at least 2 of 3 seeds.
- Stop condition: Stop as negative if uniform or source-proportional matches the best grid mixture within 1% on target-weighted validation loss across two target distributions, or if gains only appear in one seed without persistence.

## Evidence references

- Artifact root: `<local-path>/projects/domain-mixture-grid-search-for-tiny-pretraining-1adf7361c731`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
