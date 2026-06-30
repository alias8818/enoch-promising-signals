# Promotion-Tier Falsification Ladder for Queued Work

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `promotion-tier-falsification-ladder-for-queued-work-869fdcf0bab1`
Run ID: `promotion-tier-falsification-ladder-for-queued-work-869fdcf0bab1-20260610T191438768391+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bc2b9d07cee3

## What looked useful

Across 100 seeds with 20,000 queued items per scenario and equal budget, the score ladder improved mean true accepts versus FIFO in correlated_proxy (279.89 vs 215.59) and rare_positive_correlated (278.64 vs 59.81), but lost badly in weak_proxy (100.81 vs 215.59) and misleading_proxy (1.40 vs 215.59). Tiering alone was not enough: random_ladder was consistently worse than FIFO.

## Boundaries and scale limits

No real Enoch queue traces, human utility labels, live deployment data, nonstationary arrivals, starvation constraints, or model/human reviewer feedback were tested. This is not publication-grade evidence for production queued research work.

## Claim scope

Synthetic queued-work simulation with controlled latent item quality, tier costs, fixed promotion fractions, and known cheap-tier/full-validation correlation. A score-based promotion ladder improves useful acceptances per budget only when cheap proxy tiers are positively correlated with full validation; it is harmful under weak or misleading proxies.

## Why it stopped

Synthetic medium evidence falsifies the broad/unconditional promotion-tier ladder claim while supporting a conditional guardrail; this is proxy evidence, not full validation on real queued work.

## Recommended next action

Stop this run as no-paper useful signal; before any real deployment, run a bounded historical-trace replay or live shadow test that measures cheap-tier/full-validation rank correlation and forced holdout false-suppression rates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Historical Trace Replay for Promotion-Tier Queue Guardrails
- Success threshold: Score ladder improves true accepted items per budget by at least 20% over FIFO while keeping holdout-estimated false suppression of positives below 10% and without materially worsening age/starvation tails.
- Stop condition: Stop if cheap-tier/full-validation rank correlation is nonpositive, if score ladder fails to beat FIFO by 10% in replay, or if holdout false suppression exceeds 20%.

## Evidence references

- Artifact root: `<local-path>/projects/promotion-tier-falsification-ladder-for-queued-work-869fdcf0bab1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
