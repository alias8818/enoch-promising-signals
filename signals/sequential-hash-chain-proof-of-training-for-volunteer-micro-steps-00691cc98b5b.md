# Sequential Hash-Chain Proof-of-Training for Volunteer Micro-Steps

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sequential-hash-chain-proof-of-training-for-volunteer-micro-steps-00691cc98b5b`
Run ID: `sequential-hash-chain-proof-of-training-for-volunteer-micro-steps-00691cc98b5b-20260526T055214555515+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fcaeefd6eeab

## What looked useful

Chain-only verification took about 0.0019 s for 600 records while semantic verification cost approximately a full training replay. Truncation and forged rehashed suffixes were accepted without a terminal commitment, and forged updates required semantic recomputation to reject.

## Boundaries and scale limits

Tested only synthetic deterministic logistic-regression updates up to 600 steps, batch size 32, and 65,536 parameters on one CPU host. No distributed volunteers, neural-network training, privacy constraints, external notarization service, or adaptive adversary was tested.

## Claim scope

On a deterministic CPU logistic-regression micro-step harness, a sequential per-step hash chain provides cheap tamper-evident ordering and progress only when a terminal hash is independently committed; it does not by itself prove semantic training correctness.

## Why it stopped

Proxy evidence supports hash-chain ledger utility but early-falsifies the stronger standalone proof-of-training claim; full validation would need a client/server audit prototype rather than more local hash-chain benchmarking.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should add random audit challenges to measure how much recomputation is needed to deter forged volunteer micro-steps.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Random Audit Challenges for Hash-Chain Volunteer Training Logs
- Success threshold: Detect at least 95% of forged or skipped micro-step traces at an audit rate that costs under 20% of full semantic replay on a small neural or logistic workload.
- Stop condition: Stop if attacks can keep acceptance above 20% while saving at least 25% prover compute under audit rates that are cheaper than full replay.

## Evidence references

- Artifact root: `<local-path>/projects/sequential-hash-chain-proof-of-training-for-volunteer-micro-steps-00691cc98b5b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
