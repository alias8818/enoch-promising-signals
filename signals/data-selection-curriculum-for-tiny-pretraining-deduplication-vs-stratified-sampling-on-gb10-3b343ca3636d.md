# Data-selection curriculum for tiny pretraining: deduplication vs stratified sampling on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `data-selection-curriculum-for-tiny-pretraining-deduplication-vs-stratified-sampling-on-gb10-3b343ca3636d`
Run ID: `data-selection-curriculum-for-tiny-pretraining-deduplication-vs-stratified-sampling-on-gb10-3b343ca3636d-20260628T193841972255+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b7567edcb0a4

## What looked useful

Controlled 429k-param LM probe over three seeds found exact deduplication consistently beat raw duplicate sampling and naive equal-domain stratification: mean balanced validation loss 1.8856 for dedup vs 2.1490 raw, 3.0940 stratified, and 3.0866 dedup_stratified. Tail loss also favored dedup: 2.3262 vs 2.9590 raw and about 4.40 for stratified variants. The useful mechanism signal is that hard equal-domain balancing can overexpose tiny strata and worsen held-out tail generalization.

## Boundaries and scale limits

Synthetic token corpus; 429,568-parameter Transformer; 1,200 steps per policy; three seeds; exact duplicates only; no real natural-language corpus, near-dedup, larger model, or long schedule validation.

## Claim scope

In a controlled duplicate-heavy, domain-skewed tiny LM pretraining proxy, exact deduplication outperformed raw duplicate sampling and naive equal-domain stratified sampling under equal token budgets.

## Why it stopped

Proxy evidence is consistent but synthetic and small; it supports an early caution about naive stratification, not a full validation of pretraining data-selection curricula.

## Recommended next action

Stop this run as no-paper useful evidence; run a bounded real-corpus follow-up comparing exact dedup against capped or temperature-based stratified sampling before considering scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus capped stratification versus dedup for tiny LM pretraining
- Success threshold: A capped or temperature-stratified policy improves mean balanced validation loss by at least 3% versus dedup-only and does not worsen mean tail loss across three seeds.
- Stop condition: Stop if equal/capped/temperature stratification fails to beat dedup-only on balanced validation loss or worsens tail loss in two of three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/data-selection-curriculum-for-tiny-pretraining-deduplication-vs-stratified-sampling-on-gb10-3b34`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
