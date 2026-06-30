# Real-Corpus Full-Payload Ledger Replay Consistency

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `73`
Project ID: `real-corpus-full-payload-ledger-replay-consistency-a10aa7b4c0`
Run ID: `real-corpus-full-payload-ledger-replay-consistency-a10aa7b4c0-20260522T195727899448+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `73`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Full-Payload Heterogeneous Ledger Replay Consistency Test: enoch://control-plane/projects/full-payload-heterogeneous-ledger-replay-consistency-test-347d94cd66/runs/full-payload-heterogeneous-ledger-replay-consistency-test-347d94cd66-20260522T194142705711+0000
- Parent run decision: Heterogeneous Real-Ledger Deterministic Replay Corpus Test: enoch://control-plane/projects/heterogeneous-real-ledger-deterministic-replay-corpus-test-1b7b3fccfe/runs/heterogeneous-real-ledger-deterministic-replay-corpus-test-1b7b3fccfe-20260522T101304328718+0000

## What looked useful

Full-payload replay matched 54/54 real selected commit states; latest-snapshot-only matched 3/54; metadata-only matched 0/54; a single-bit corrupted-payload ablation changed 14/54 selected replay states. No selected commit skipped files due to benchmark limits.

## Boundaries and scale limits

The run used three convenience-selected repositories and sampled 18 first-parent commits per repository. It did not test a production ledger, crash recovery, concurrent writes, very large monorepos, broad language ecosystems, binary-heavy corpora, or comprehensive adversarial fault injection. This is mechanism evidence, not Tier-4 paper-readiness replication.

## Claim scope

In a bounded deterministic benchmark over 54 selected commits from three real public Git repositories, an in-memory full-payload append-only ledger replayed full selected file-tree states byte-exactly against Git-derived target digests, with zero replay mismatches.

## Why it stopped

Bounded real-corpus evidence supports the replay mechanism but falls short of the requested Tier-4 paper-readiness threshold; repository count, implementation realism, and robustness coverage are insufficient for publication-grade closure.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful signal; do not chain another follow-up from this run because the controller lineage is already at depth 4.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-full-payload-ledger-replay-consistency-a10aa7b4c0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
