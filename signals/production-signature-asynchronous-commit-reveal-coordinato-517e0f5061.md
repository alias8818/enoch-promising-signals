# Production-signature asynchronous commit/reveal coordinator test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `production-signature-asynchronous-commit-reveal-coordinato-517e0f5061`
Run ID: `production-signature-asynchronous-commit-reveal-coordinato-517e0f5061-20260620T191202506822+0000`

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

- Parent run decision: Commit-Reveal Attestation Protocol Test for Volunteer Updates: enoch://control-plane/projects/commit-reveal-attestation-protocol-test-for-volunteer-updates-bd6ace891a46/runs/commit-reveal-attestation-protocol-test-for-volunteer-updates-bd6ace891a46-20260620T181112314424+0000
- Parent run decision: Signed trace-driven commit-reveal volunteer update prototype: enoch://control-plane/projects/signed-trace-driven-commit-reveal-volunteer-update-prototy-ad64935ae6/runs/signed-trace-driven-commit-reveal-volunteer-update-prototy-ad64935ae6-20260620T184132127639+0000

## What looked useful

The mechanism support is clear: immediate publication suffered 96.02% copycat winner rate, unsigned commit/reveal accepted 100% of forged registered-identity attempts, and signed asynchronous commit/reveal had 0% copycat winner rate and 0% forged accept rate across 5,000 seeded rounds. Remaining candidate losses were liveness losses from late honest reveals.

## Boundaries and scale limits

Synthetic single-process simulator only; no production deployment, persistence recovery, multi-node consensus, Byzantine network partitions, key rotation, backpressure, hostile clock skew, or real workload traces were tested.

## Claim scope

In a deterministic local 5,000-round asynchronous coordinator simulation with 32 honest clients, 8 adversarial clients, fixed reveal deadlines, and Ed25519 verification, signed commit/reveal rejected all forged registered-identity reveals and prevented adaptive copycat winners, outperforming immediate publication and unsigned commit/reveal controls on direct safety metrics.

## Why it stopped

Medium local evidence supports the mechanism but is not publication-grade production evidence; the run lacks durable implementation, real deployment traces, and multi-node fault coverage.

## Recommended next action

Stop this run as no-paper useful signal; next bounded deepen test should implement a durable multi-process coordinator with crash/restart persistence and network fault injection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Durable multi-process signed commit/reveal coordinator under crash and network faults
- Success threshold: Across at least 10,000 rounds, signed durable coordinator has 0 forged accepts, 0 adaptive copycat winners, at least 95% honest inclusion before deadline, and deterministic recovery to the same accepted reveal set after injected crashes.
- Stop condition: Stop negative if any forged registered-identity reveal is accepted, any post-commit adaptive copycat winner is accepted, or crash recovery produces divergent accepted reveal sets under fixed seeds.

## Evidence references

- Artifact root: `<local-path>/projects/production-signature-asynchronous-commit-reveal-coordinato-517e0f5061`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
