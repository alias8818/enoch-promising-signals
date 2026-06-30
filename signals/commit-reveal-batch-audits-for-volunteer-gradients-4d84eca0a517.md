# Commit-Reveal Batch Audits for Volunteer Gradients

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `commit-reveal-batch-audits-for-volunteer-gradients-4d84eca0a517`
Run ID: `commit-reveal-batch-audits-for-volunteer-gradients-4d84eca0a517-20260521T232750813796+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f075905c6213

## What looked useful

Commit-reveal is a viable binding primitive, but simple random whole-batch audits have a poor tradeoff: sparse adversaries require auditing a large batch fraction for high detection confidence, while successful detection discards large amounts of honest gradient work. For example, n=512 with 1% malicious workers needs k=201 audits for 95% detection; k=32 detects only 32.24% and still discards 163.13 honest gradients in expectation under whole-batch rejection.

## Boundaries and scale limits

No real model training, non-IID volunteer data, adaptive adversary, network protocol, production serialization, stake/slashing, or reputation system was tested. Monte Carlo rounds were intentionally bounded to 50 for poison scale 4 and 30 for poison scale 10; detection conclusions rely primarily on exact hypergeometric formulas.

## Claim scope

Synthetic volunteer-gradient rounds with SHA-256 commit-reveal binding, exact random audit detection formulas, n in {32,128,512}, audit k in {1,2,4,8,16,32}, 64-dimensional gradients, sign-flip poison scales 4 and 10, and whole-batch rejection compared against no audit, sampled removal, and full audit controls.

## Why it stopped

Bounded synthetic and analytic evidence produced a useful early falsification of the simple batch-reject audit policy, not a full validation of volunteer-gradient training security.

## Recommended next action

Do not write a paper on simple commit-reveal whole-batch rejection; run a bounded follow-up that combines commit-reveal with per-worker quarantine or robust aggregation on a small real training benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commit-Reveal Quarantine Audits with Robust Aggregation on a Small Federated Benchmark
- Success threshold: At the same audit budget, quarantine plus robust aggregation keeps final validation accuracy within 2 percentage points of full audit and reduces accepted malicious-gradient mass by at least 70% versus no audit while discarding under 20% of honest gradients.
- Stop condition: Stop if quarantine plus robust aggregation fails to beat whole-batch rejection on both validation accuracy and honest-gradient discard in two of three seeds, or if the workload would exceed the local short-run CPU/GPU budget.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-batch-audits-for-volunteer-gradients-4d84eca0a517`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
