# Sparse Gradient Verification Tags via Bucketed Hashing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-gradient-verification-tags-via-bucketed-hashing-55c0db861e91`
Run ID: `sparse-gradient-verification-tags-via-bucketed-hashing-55c0db861e91-20260607T130003116281+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/db9f9c4c51eb

## What looked useful

Bucketed tags can be a cheap random-fault screen, but standalone adversarial verification is structurally unsafe at many practical bucket/table sizes because duplicated coordinate signatures admit exact 2-coordinate tag-preserving edits. Observed duplicate counts matched the birthday estimate d^2 / (2 * B^R * 2^(R-1)).

## Boundaries and scale limits

No real distributed training, optimizer integration, network transport, or private-salt protocol was tested. Random-fault tests used synthetic quantized values and 20,000 trials per grid point. Adaptive scans covered dimensions up to 1,000,000, buckets up to 8192, and up to 4 tables.

## Claim scope

Bounded NumPy simulation of CountSketch-style bucketed verification tags for sparse gradient differences. The tested tags were effective for random quantized sparse faults in small grids, but duplicate multi-table coordinate signatures create exact adaptive 2-sparse null edits unless B^R * 2^(R-1) is large relative to d^2.

## Why it stopped

Bounded local evidence is mixed: random sparse faults were mostly detected, but adaptive duplicate-signature attacks create exact sparse null edits, so the original standalone verification idea is not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is to test a commit-then-private-salt protocol that hides hash/sign assignments until after sparse update commitment.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commit-Then-Salt Sparse Gradient Verification Tags
- Success threshold: Zero adaptive false accepts in at least 10000 commit-then-salt trials at d >= 1000000 with random false-accept upper bound below 0.001 and verifier overhead below 5 percent of sparse update serialization time.
- Stop condition: Stop if the adversary can still construct tag-preserving sparse edits after commitment under the salted protocol, or if verifier overhead exceeds the sparse update serialization baseline by more than 5 percent in the bounded test.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-gradient-verification-tags-via-bucketed-hashing-55c0db861e91`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
