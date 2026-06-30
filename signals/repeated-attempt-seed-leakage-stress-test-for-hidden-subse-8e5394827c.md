# Repeated-Attempt Seed Leakage Stress Test for Hidden Subset Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `repeated-attempt-seed-leakage-stress-test-for-hidden-subse-8e5394827c`
Run ID: `repeated-attempt-seed-leakage-stress-test-for-hidden-subse-8e5394827c-20260629T233616604888+0000`

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

- Parent run decision: Cheat-Resistant Volunteer Training via Seeded Subset Verification: enoch://control-plane/projects/cheat-resistant-volunteer-training-via-seeded-subset-verification-c6072f3387f1/runs/cheat-resistant-volunteer-training-via-seeded-subset-verification-c6072f3387f1-20260629T231552124765+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/73e1919ed312

## What looked useful

Exact hidden-subset score feedback is fragile under repeated attempts: a simple seed-elimination attacker recovered the fixed seed quickly and could then score 1.0 on the hidden subset while covering only 0.03125 of the population. Coarse pass/fail feedback and rotating seeds sharply reduced the tested leakage.

## Boundaries and scale limits

Local CPU-only NumPy simulation; 4096-item universe, 128-item hidden subset, 2^14 candidate seeds, 80 trials, random probes only. No real model training, no production verifier, no large seed space, and no optimized adaptive attacker.

## Claim scope

In a synthetic finite-seed hidden-subset verifier with a fixed reused seed, exact repeated subset-score feedback identified a 2^14-seed verifier seed in 80/80 trials with median 4 attempts; pass/fail threshold feedback did not generally identify the seed within 50 random-probe attempts.

## Why it stopped

The result is a bounded synthetic stress test that supports the exact-score leakage mechanism but is not direct or broad enough for a paper claim.

## Recommended next action

Stop this worker run as no-paper useful signal; next bounded action is an adaptive pass/fail leakage test with larger seed spaces and rounded-score feedback policies.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Pass/Fail and Rounded-Score Leakage for Hidden Subset Verification
- Success threshold: Recover at least 50% of fixed seeds within 100 attempts under one non-exact feedback policy while controls with rotating seeds remain below 5% reusable recovery.
- Stop condition: Stop as negative if adaptive attacks reduce candidate entropy by less than 25% or recover fewer than 10% of seeds within 100 attempts across all non-exact feedback policies.

## Evidence references

- Artifact root: `<local-path>/projects/repeated-attempt-seed-leakage-stress-test-for-hidden-subse-8e5394827c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
