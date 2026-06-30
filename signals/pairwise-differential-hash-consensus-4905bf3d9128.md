# Pairwise Differential Hash Consensus

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `pairwise-differential-hash-consensus-4905bf3d9128`
Run ID: `pairwise-differential-hash-consensus-4905bf3d9128-20260526T123831217467+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1f6642089444

## What looked useful

Pairwise differential hashes localized disagreements but provided no extra consensus power in the tested decision rule: PDHC cluster success exactly matched global hash majority success across all four fault models, while per-chunk majority recovered sparse faults far better. A common-offset counterexample shows differential-only evidence cannot distinguish unanimous correct from unanimous wrong states.

## Boundaries and scale limits

Synthetic local CPU-only evidence only; does not cover production distributed systems, network asynchrony, cryptographic collision economics, or an anchored repair protocol. The main run used 2,000 trials per fault model and completed in 1.51 seconds.

## Claim scope

In a deterministic synthetic replica-state consensus probe with 7 replicas, 64 chunks, sparse independent faults, single faulty replica faults, correlated minority faults, and common-offset faults, pairwise differential hash clustering did not improve consensus success over ordinary whole-state hash majority and is vulnerable to unanimous wrong-state/common-offset ambiguity without an external anchor.

## Why it stopped

Early synthetic falsification of the unanchored consensus-improvement hypothesis, not a full production validation.

## Recommended next action

Stop this as a standalone consensus mechanism; only continue if reframed as an anchored repair/localization protocol and compared against Merkle/per-chunk-majority baselines.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Anchored Differential Hash Repair Protocol
- Success threshold: At least 25% lower repair/localization bandwidth than a Merkle or per-chunk-majority baseline on sparse faults, with zero wrong accepts in common-offset and correlated-minority adversarial tests over at least 10,000 trials.
- Stop condition: Stop if the anchored protocol cannot beat Merkle/per-chunk repair bandwidth by 10% or if any wrong accept occurs under the adversarial common-offset test.

## Evidence references

- Artifact root: `<local-path>/projects/pairwise-differential-hash-consensus-4905bf3d9128`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
