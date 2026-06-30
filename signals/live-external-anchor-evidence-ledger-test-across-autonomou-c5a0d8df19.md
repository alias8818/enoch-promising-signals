# Live external-anchor evidence ledger test across autonomous GPU worker jobs

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-external-anchor-evidence-ledger-test-across-autonomou-c5a0d8df19`
Run ID: `live-external-anchor-evidence-ledger-test-across-autonomou-c5a0d8df19-20260605T192835282308+0000`

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

- Parent run decision: Evidence ledger bounded test for GPU worker agent reliability: enoch://control-plane/projects/evidence-ledger-bounded-test-for-gpu-worker-agent-reliability-88e1b7f0e129/runs/evidence-ledger-bounded-test-for-gpu-worker-agent-reliability-88e1b7f0e129-20260605T164338244847+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/c229376e617b

## What looked useful

Clean three-entry ledger verification passed with external rechecks, independent re-verification passed, and controlled artifact and anchor mutations failed verification for the expected reasons.

## Boundaries and scale limits

Only three local workers, one host, one external anchor provider, short runtime, simple retry handling, no hardware signing, no multi-machine orchestration, no adversarial worker model, and no long-duration durability test.

## Claim scope

A local Tier 1 controlled test with three independent Python subprocess GPU workers on NVIDIA GB10 showed that CUDA job artifacts can be chained into a live Bitcoin-block-anchored evidence ledger and that clean verification plus artifact/anchor mutation detection works.

## Why it stopped

Tier 1 mechanism support was obtained, but the evidence is small local no-paper evidence rather than publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up with 20-50 autonomous GPU worker jobs, two independent external anchor providers, and clean-checkout verifier replay before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-anchor replay validation for autonomous GPU worker evidence ledgers
- Success threshold: Clean replay verifies all entries and both anchor providers for at least 95% of jobs without manual repair, and all predeclared mutation controls are detected.
- Stop condition: Stop if clean replay fails for more than 5% of jobs, either anchor provider cannot be independently rechecked, or any predeclared mutation control passes verification.

## Evidence references

- Artifact root: `<local-path>/projects/live-external-anchor-evidence-ledger-test-across-autonomou-c5a0d8df19`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
