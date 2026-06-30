# Task-Attestation via Micro-Benchmarks for Volunteer Compute Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `task-attestation-via-micro-benchmarks-for-volunteer-compute-verification-c19cae55939e`
Run ID: `task-attestation-via-micro-benchmarks-for-volunteer-compute-verification-c19cae55939e-20260605T112634150624+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/5be133f499a0

## What looked useful

At 1% probe density, random skippers computing only 50% of segments were detected in 99.305% of 20,000 synthetic jobs, while a probe-only adversary had 0% detection at every tested probe fraction.

## Boundaries and scale limits

Single-host Python harness; Monte Carlo task layouts; no deployed volunteer network, no heterogeneous clients, no real BOINC integration, no adaptive reverse-engineering exercise, and no proof that probes are indistinguishable from useful work.

## Claim scope

Bounded local CPU proxy showing that secret micro-benchmark probes detect naive and random segment skipping at low nominal overhead, but fail completely when a source-aware adversary can identify and execute only probe segments.

## Why it stopped

Proxy evidence early-falsifies standalone benchmark attestation as full volunteer-compute verification; it remains useful only as a tripwire or reputation signal unless indistinguishability from useful work is demonstrated.

## Recommended next action

Stop this as no-paper useful signal; a concrete next test would embed challenge checks inside a real deterministic workload and evaluate whether a source-aware worker can distinguish or bypass them.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Indistinguishable Challenge Embedding for Volunteer Workloads
- Success threshold: At most 2% overhead, at least 95% detection of workers skipping 50% or more useful work, and no trivial probe-only bypass after source inspection.
- Stop condition: Stop if probes can be isolated and executed independently from useful work with less than 20% of the original compute cost.

## Evidence references

- Artifact root: `<local-path>/projects/task-attestation-via-micro-benchmarks-for-volunteer-compute-verification-c19cae55939e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
