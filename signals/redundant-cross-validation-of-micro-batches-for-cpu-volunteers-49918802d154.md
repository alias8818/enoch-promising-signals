# Redundant Cross-Validation of Micro-Batches for CPU Volunteers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `redundant-cross-validation-of-micro-batches-for-cpu-volunteers-49918802d154`
Run ID: `redundant-cross-validation-of-micro-batches-for-cpu-volunteers-49918802d154-20260524T055844955537+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/27bbaca74165

## What looked useful

Redundant micro-batch cross-validation is useful for non-colluding fault detection and single-fault correction, but must be paired with randomized assignment, identity/reputation controls, hidden gold work, or trusted recomputation to handle correlated faults and collusion.

## Boundaries and scale limits

Tested locally with one standard-library Python process, synthetic logistic-regression gradients, 2000 trials per main condition, 48 main conditions, and injected faults. Not tested on real volunteer hosts, heterogeneous CPUs/compilers, real networks, colluding identities, or end-to-end model training convergence.

## Claim scope

In a deterministic synthetic CPU micro-batch gradient workload, duplicate redundant execution detects non-colluding mismatched volunteer outputs and triple replication corrects most isolated faults, but neither is sufficient as a standalone trust mechanism against correlated or colluding wrong outputs.

## Why it stopped

Local direct simulation supports the mechanism only under non-colluding faults and exposes a standalone failure mode under correlated faults/collusion, so the evidence is useful but not paper-positive.

## Recommended next action

Stop this run as no-paper useful signal; a bounded next test should implement a multi-process or multi-host prototype with randomized assignment and hidden gold micro-batches before considering larger validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prototype Volunteer Micro-Batch Validation with Gold Work and Randomized Assignment
- Success threshold: At 10% faulty volunteers including colluding pairs, accepted-corrupt rate below 1%, false rejection on clean work below 1%, and effective accepted throughput at least 40% of unchecked single execution.
- Stop condition: Stop if accepted-corrupt rate remains above 5% under collusion after adding gold work and randomized assignment, or if validation overhead reduces accepted throughput below 25% of unchecked execution in the bounded prototype.

## Evidence references

- Artifact root: `<local-path>/projects/redundant-cross-validation-of-micro-batches-for-cpu-volunteers-49918802d154`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
