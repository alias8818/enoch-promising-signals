# GB10 Adversarial Worker Harness for Volunteer Training Research

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gb10-adversarial-worker-harness-for-volunteer-training-research-a71ec18ce3ad`
Run ID: `gb10-adversarial-worker-harness-for-volunteer-training-research-a71ec18ce3ad-20260610T062441852116+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9adcfa60010b

## What looked useful

A GPU-vectorized adversarial worker harness found two practical signals: too few sentinels for many workers can reject about 90% of honest workers and make gating harmful, while a larger sentinel budget prevents catastrophic failures under high coordinated flip/selective-hard attacks. EM is strongest for random and moderate attacks but inverted at 40% always-flip adversaries in the tested setup.

## Boundaries and scale limits

No real volunteers, no real onboarding/training dynamics, no collusion channels, no incentives, no domain-specific task semantics, and no long-running field deployment. Results are limited to synthetic attacks and should not be treated as full validation of volunteer training defenses.

## Claim scope

Synthetic binary-label volunteer-worker simulation with 512 workers, 8,000 held-out tasks, 9 labels per item, 24 replicates per scenario, three adversary strategies, and three aggregation methods. The harness exposes aggregation failures and sentinel-budget tradeoffs in this local proxy setting.

## Why it stopped

Proxy-only synthetic evidence supports the harness as a useful diagnostic, but it is not direct/full validation of adversarial volunteer training.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same harness with real or high-fidelity agent workers using preregistered adversarial instructions and the same majority, EM, and sentinel-gated controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Worker Study for Sentinel-Budgeted Adversarial Volunteer Training
- Success threshold: Sentinel-weighted aggregation must beat majority vote by at least 10 absolute accuracy points under high coordinated attacks, avoid more than 45% honest-worker rejection at the selected threshold, and avoid the EM inversion failure observed in the synthetic harness.
- Stop condition: Stop if sentinel weighting fails to beat majority vote under coordinated attacks or requires honest-worker rejection above 45% to do so.

## Evidence references

- Artifact root: `<local-path>/projects/gb10-adversarial-worker-harness-for-volunteer-training-research-a71ec18ce3ad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
