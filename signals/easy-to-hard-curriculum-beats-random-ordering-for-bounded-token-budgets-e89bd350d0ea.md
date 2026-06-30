# Easy-to-Hard Curriculum Beats Random Ordering for Bounded Token Budgets

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `easy-to-hard-curriculum-beats-random-ordering-for-bounded-token-budgets-e89bd350d0ea`
Run ID: `easy-to-hard-curriculum-beats-random-ordering-for-bounded-token-budgets-e89bd350d0ea-20260610T223219458579+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/469411b4e18c

## What looked useful

Random interleaving beat strict sorted easy-to-hard in all five paired confirmation seeds on hard exact accuracy, with mean hard exact accuracy 0.084375 for random versus 0.008008 for curriculum and lower held-out loss on every difficulty.

## Boundaries and scale limits

Synthetic arithmetic only; small decoder-only transformer; 5 paired seeds; 1.97M fixed-length input tokens per run in the confirmation setting; not a natural-language, code, large-model, or datacenter-scale validation.

## Claim scope

In a paired small-transformer character-level decimal-addition experiment, strict sorted easy-to-hard ordering under the same fixed input-token budget did not beat random ordering and substantially underperformed it.

## Why it stopped

Direct bounded synthetic evidence falsified the strict sorted easy-to-hard variant rather than supporting a paper-positive claim.

## Recommended next action

Stop this run as a bounded no-paper negative for strict sorted easy-to-hard; next bounded test should evaluate curriculum schedules that retain replay/interleaving against random under the same token budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Interleaved Easy-to-Hard Curriculum Under Fixed Token Budgets
- Success threshold: Interleaved curriculum beats random on hard exact accuracy in at least 4 of 5 paired seeds and improves mean hard exact accuracy by at least 5 percentage points without increasing total input tokens.
- Stop condition: Stop if interleaved curriculum has fewer than 3 paired wins out of 5 or hard exact accuracy remains near floor for both curriculum and random after the calibrated budget.

## Evidence references

- Artifact root: `<local-path>/projects/easy-to-hard-curriculum-beats-random-ordering-for-bounded-token-budgets-e89bd350d0ea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
