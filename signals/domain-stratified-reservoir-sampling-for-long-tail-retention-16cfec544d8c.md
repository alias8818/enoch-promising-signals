# Domain-Stratified Reservoir Sampling for Long-Tail Retention

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `domain-stratified-reservoir-sampling-for-long-tail-retention-16cfec544d8c`
Run ID: `domain-stratified-reservoir-sampling-for-long-tail-retention-16cfec544d8c-20260521T213204539596+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a7551cd5ba5c

## What looked useful

Equal per-domain quotas eliminated empty retained domains and improved tail-domain accuracy by 1.3 to 3.0 percentage points across the synthetic sweep, with positive seed rates from 0.68 to 0.95. The gain came with macro accuracy losses from 0.4 to 2.3 percentage points, so simple equal stratification is a coverage-tail tradeoff rather than a broad win.

## Boundaries and scale limits

No real continual-learning replay, language-model training, noisy-domain labeling, or production stream was tested. Evidence is CPU-only synthetic proxy evidence, not publication-grade validation.

## Claim scope

Synthetic fixed-buffer long-tail domain streams with known domain labels, 20 domains, Zipf imbalance, ridge classifier trained from retained samples. Equal domain-stratified reservoirs improved tail-domain coverage and tail-domain accuracy versus uniform reservoir sampling, but generally reduced macro/overall accuracy.

## Why it stopped

The local proxy produced a reproducible useful signal but not paper-ready evidence: the mechanism is supported while the broad superiority claim is mixed because equal stratification trades tail retention for macro/overall accuracy.

## Recommended next action

Run a bounded real-domain replay test comparing uniform, equal quotas, square-root quotas, and adaptive quotas; require tail accuracy gain without material macro accuracy loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Domain Quotas for Long-Tail Replay Without Macro Accuracy Loss
- Success threshold: Tail-domain accuracy improves by at least 2 percentage points over uniform while macro accuracy is no worse than 0.5 percentage points below uniform across the primary setting, with the same direction on most seeds.
- Stop condition: Stop if adaptive or square-root quotas cannot beat uniform tail-domain accuracy by 1 percentage point without losing more than 1 percentage point macro accuracy in the first real-domain benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/domain-stratified-reservoir-sampling-for-long-tail-retention-16cfec544d8c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
