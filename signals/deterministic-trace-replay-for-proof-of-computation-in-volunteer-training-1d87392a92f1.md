# Deterministic Trace Replay for Proof-of-Computation in Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `deterministic-trace-replay-for-proof-of-computation-in-volunteer-training-1d87392a92f1`
Run ID: `deterministic-trace-replay-for-proof-of-computation-in-volunteer-training-1d87392a92f1-20260619T234027269788+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bbf53c67e335

## What looked useful

Full deterministic replay detected skipped update, gradient perturbation, wrong batch, and metadata-only loss tampering at roughly one extra training pass of verifier cost; sampled replay detected state-changing faults but missed metadata-only loss tampering when the affected step was not challenged.

## Boundaries and scale limits

Does not test real volunteer infrastructure, GPU nondeterminism, large-model training, distributed adversaries, checkpoint bandwidth, public verifiability, or cryptographic soundness beyond hash commitments.

## Claim scope

Toy deterministic CPU linear-regression training with public data generation, fixed batch schedule, SHA-256 trace commitments, full replay verification, and 32-of-240 sampled challenges.

## Why it stopped

Proxy/local mechanism result only: deterministic full replay works on the toy workload, but sparse sampled replay is insufficient for a robust proof-of-computation claim and larger real-training validation was not performed.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next bounded work should test a challenge protocol that binds metadata-only claims into verified state or samples metadata with an explicit miss probability target.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Metadata-bound challenge protocol for deterministic training trace replay
- Success threshold: Detect 100% of state-changing faults and achieve <=1% analytic miss probability for single-step metadata-only tampering with verifier cost below 35% of full replay on the same toy workload.
- Stop condition: Stop if metadata-only tamper miss probability remains above 1% at verifier cost >=35% of full replay, because the sampled protocol would not beat straightforward full replay enough to justify added complexity.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-trace-replay-for-proof-of-computation-in-volunteer-training-1d87392a92f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
