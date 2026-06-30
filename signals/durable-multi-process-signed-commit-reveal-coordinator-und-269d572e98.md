# Durable multi-process signed commit/reveal coordinator under crash and network faults

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `durable-multi-process-signed-commit-reveal-coordinator-und-269d572e98`
Run ID: `durable-multi-process-signed-commit-reveal-coordinator-und-269d572e98-20260620T195001643538+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Production-signature asynchronous commit/reveal coordinator test: enoch://control-plane/projects/production-signature-asynchronous-commit-reveal-coordinato-517e0f5061/runs/production-signature-asynchronous-commit-reveal-coordinato-517e0f5061-20260620T191202506822+0000
- Parent run decision: Signed trace-driven commit-reveal volunteer update prototype: enoch://control-plane/projects/signed-trace-driven-commit-reveal-volunteer-update-prototy-ad64935ae6/runs/signed-trace-driven-commit-reveal-volunteer-update-prototy-ad64935ae6-20260620T184132127639+0000

## What looked useful

Across 80 trials per config, durable_signed completed 56/80 with 0/80 safety violations; volatile_signed_baseline completed 31/80 with 0/80 safety violations; durable_unsigned_ablation completed 57/80 but had 44/80 forged-finalization safety violations. Durable logging improved liveness over volatile state and signatures were necessary for safety, but durable_signed still timed out in 24/80 trials.

## Boundaries and scale limits

Not a production distributed-system validation: no multi-host network, no disk corruption, no public-key infrastructure, no long soak, no datacenter-scale process count, and Python queues model network faults.

## Claim scope

Bounded local Python multiprocessing fault-injection harness with 5 participant processes, one coordinator process, HMAC-signed commit/reveal messages, durable JSONL fsync ledger, two coordinator SIGKILL/restarts per trial, 5% message drops, random delays, duplicates, and forged adversarial commit/reveal traffic.

## Why it stopped

No-paper useful signal: mechanism support was demonstrated, but the 70% durable-signed completion rate under repeated crash/drop faults is not strong enough for a robustness claim.

## Recommended next action

Run a bounded deepen follow-up that adds coordinator ACK/phase retransmission and requires at least 95% completion with zero safety violations under the same crash/drop/adversary schedule.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: ACK-driven durable signed commit/reveal recovery under repeated coordinator crashes
- Success threshold: At least 95% completion and 0 safety violations for the ACK/phase retransmission durable-signed coordinator, with a statistically visible liveness improvement over the current 70% durable_signed result.
- Stop condition: Stop if safety violations appear, if completion remains below 90% after ACK/phase retransmission, or if failures show the same all-commits/no-reveals pattern in more than 10% of trials.

## Evidence references

- Artifact root: `<local-path>/projects/durable-multi-process-signed-commit-reveal-coordinator-und-269d572e98`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
