# Anchored crash-safe hash-chain ledger for small agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchored-crash-safe-hash-chain-ledger-for-small-agents-c2044f2e60`
Run ID: `anchored-crash-safe-hash-chain-ledger-for-small-agents-c2044f2e60-20260603T180313855351+0000`

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

- Parent run decision: Hash-chain evidence ledger for small agents: enoch://control-plane/projects/hash-chain-evidence-ledger-for-small-agents-c7e2f2fe7ca5/runs/hash-chain-evidence-ledger-for-small-agents-c7e2f2fe7ca5-20260602T205920905641+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4174e93ed6b9

## What looked useful

Controlled crash injection covered five append persistence windows and five anchor persistence windows. Safe append recovered a valid prefix in 5/5 cases, anchor writes left a valid no-anchor or matching-anchor state in 5/5 cases, truncation and tampering were rejected, and a naive JSON-lines baseline produced a torn unreadable record under a mid-line crash.

## Boundaries and scale limits

Single-process local filesystem test only; no true power-loss testing, no hardware write-cache fault model, no concurrent writers, no remote public anchoring, and no large-ledger throughput evaluation.

## Claim scope

A small Python reference ledger using hash-chained whole-snapshot records, temp-write, file fsync, atomic replace, directory fsync, and separate anchors recovered to a prefix-valid chain across all modeled process-crash append windows and detected truncation/tampering relative to the anchor in a local controlled test.

## Why it stopped

Tier 1 controlled direct process-crash evidence supports the mechanism but is not publication-grade and does not validate power-loss or independent anchoring assumptions.

## Recommended next action

Run a bounded VM power-cut and filesystem matrix test to determine whether the same prefix-valid and anchor-detection results hold under realistic crash consistency rather than only process termination.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: VM power-cut crash matrix for anchored hash-chain ledger
- Success threshold: Across at least 100 randomized power-cut trials per filesystem/configuration, every recovered safe ledger is a valid prefix and every existing anchor matches the anchored ledger state; the naive baseline must fail in at least one crash scenario.
- Stop condition: Stop early if any safe-ledger recovery yields unreadable JSON, a broken hash chain, or an anchor that incorrectly accepts truncation/tampering.

## Evidence references

- Artifact root: `<local-path>/projects/anchored-crash-safe-hash-chain-ledger-for-small-agents-c2044f2e60`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
