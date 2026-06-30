# Evidence ledger bounded test for GPU worker agent reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-bounded-test-for-gpu-worker-agent-reliability-88e1b7f0e129`
Run ID: `evidence-ledger-bounded-test-for-gpu-worker-agent-reliability-88e1b7f0e129-20260605T164338244847+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/c229376e617b

## What looked useful

The mechanism is useful as a worker reliability control: ledger+anchor audit detected 9/9 bounded independent-anchor faults, while final-artifact-only audit detected 0/9. The compromised-anchor limit was explicitly reproduced.

## Boundaries and scale limits

Single short GPU workload, synthetic perturbations, one host, no live autonomous-agent failure stream, and no external anchor service. A fully consistent ledger rewrite passes when the anchor is also rewritten or non-independent.

## Claim scope

In one bounded GB10/PyTorch workload with synthetic evidence faults, a hash-chained evidence ledger plus an independent anchor detected all tested post-run evidence loss, truncation, reordering, artifact mutation, ledger mutation, and post-anchor rewrite cases that a final-artifact-only check missed.

## Why it stopped

Bounded mechanism evidence is positive, but the run is a short single-job synthetic fault-injection proxy rather than direct publication-grade validation of GPU worker agent reliability.

## Recommended next action

Stop this run as no-paper useful signal; next, run a bounded live fault-injection test across multiple autonomous GPU worker jobs with an external append-only anchor service.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live external-anchor evidence ledger test across autonomous GPU worker jobs
- Success threshold: Ledger audit detects at least 95% of controlled live faults with 0 false positives on clean jobs and less than 5% wall-clock overhead relative to final-artifact-only auditing.
- Stop condition: Stop if the ledger has any unexplained false positive on clean jobs, misses two or more controlled non-anchor-compromise faults, or overhead exceeds 10% after obvious implementation fixes.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-bounded-test-for-gpu-worker-agent-reliability-88e1b7f0e129`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
