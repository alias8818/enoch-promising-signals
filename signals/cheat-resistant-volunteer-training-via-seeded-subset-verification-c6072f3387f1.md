# Cheat-Resistant Volunteer Training via Seeded Subset Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cheat-resistant-volunteer-training-via-seeded-subset-verification-c6072f3387f1`
Run ID: `cheat-resistant-volunteer-training-via-seeded-subset-verification-c6072f3387f1-20260629T231552124765+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/73e1919ed312

## What looked useful

Across 108 parameterized policy cases, hidden subset audits deterred shortcutting in 53 subset cases, predictable audits deterred in 0 cases, and representative Monte Carlo pass rates matched analytic probabilities.

## Boundaries and scale limits

No real volunteer deployment, no repeated-session seed leakage, no collusion model, no human behavior measurements, and no operational seed-bank cost model were tested.

## Claim scope

In a transparent analytic and Monte Carlo proxy model, hidden seeded-subset verification can deter utility-maximizing shortcutting with materially less review effort than full seed verification, while predictable audits fail to deter shortcutting.

## Why it stopped

Proxy-only useful signal; not direct or publication-grade evidence.

## Recommended next action

Run a bounded deepen follow-up that adds repeated attempts, seed leakage/adaptive attackers, and honest-user false-failure constraints before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Repeated-Attempt Seed Leakage Stress Test for Hidden Subset Verification
- Success threshold: At least 50% lower optimal shortcut rate than no verification, at most 40% of full verification effort, and honest false-failure rate below 5% in the tested parameter range.
- Stop condition: Stop if any adaptive leakage setting with realistic rotation cost drives optimal shortcut rate above 0.5 or honest false-failure above 10% at 40% review effort.

## Evidence references

- Artifact root: `<local-path>/projects/cheat-resistant-volunteer-training-via-seeded-subset-verification-c6072f3387f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
