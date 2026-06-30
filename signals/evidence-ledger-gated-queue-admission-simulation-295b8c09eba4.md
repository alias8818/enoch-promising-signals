# Evidence-Ledger-Gated Queue Admission Simulation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-gated-queue-admission-simulation-295b8c09eba4`
Run ID: `evidence-ledger-gated-queue-admission-simulation-295b8c09eba4-20260620T092704033765+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/65f84ab55b3d

## What looked useful

Ledger gating beat the best tested static evidence threshold in the default scenario by +0.1298 absolute useful-on-time rate and -0.1830 absolute accepted useless-work rate; improvements grew as unreliable/adversarial source fraction increased.

## Boundaries and scale limits

No production scheduler integration, no real workload traces, no adaptive adversaries, no fairness constraints, and no validation beyond local synthetic runs of up to 20,000 jobs x 50 replicates per scenario.

## Claim scope

Synthetic discrete-event queue simulation with repeated source identities, noisy source-dependent evidence quality, burst overload, finite queue capacity, and per-source Bayesian outcome ledger admission. In this scoped simulator, ledger gating improved useful on-time completion and reduced accepted useless work versus FIFO/admit-all and tuned static evidence thresholds.

## Why it stopped

No-paper useful signal: the mechanism is supported in a synthetic proxy, but this is not direct/full validation and is not publication-grade evidence.

## Recommended next action

Run a bounded deepen follow-up adding adaptive submitters and fairness diagnostics before considering real-trace replay or paper drafting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive-source and fairness stress test for evidence-ledger queue admission
- Success threshold: Ledger improves useful-on-time rate by at least +0.05 absolute versus the best tuned static threshold while keeping useful-job rejection disparity between honest high-quality and honest low-history sources below 0.10 absolute.
- Stop condition: Stop if adaptive sources erase the useful-on-time advantage below +0.02 absolute or if fairness disparity exceeds 0.15 absolute in two independent seeded scenario grids.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-gated-queue-admission-simulation-295b8c09eba4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
