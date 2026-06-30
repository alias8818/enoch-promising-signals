# Multi-process crash/recovery validation for anchored evidence ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `multi-process-crash-recovery-validation-for-anchored-evide-8c910db21d`
Run ID: `multi-process-crash-recovery-validation-for-anchored-evide-8c910db21d-20260610T105412020603+0000`

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

- Parent run decision: Append-Only Evidence Ledger with Anchored Quotes for CPU Agents: enoch://control-plane/projects/append-only-evidence-ledger-with-anchored-quotes-for-cpu-agents-1ddaecc2803b/runs/append-only-evidence-ledger-with-anchored-quotes-for-cpu-agents-1ddaecc2803b-20260610T003542330990+0000
- Parent run decision: Real Trace and Concurrency Validation for Anchored Evidence Ledgers: enoch://control-plane/projects/real-trace-and-concurrency-validation-for-anchored-evidenc-25e9602fdd/runs/real-trace-and-concurrency-validation-for-anchored-evidenc-25e9602fdd-20260610T055341936141+0000

## What looked useful

Anchors add measurable evidence-integrity value beyond a hash chain alone: anchored/chain_rewrite detected 6/6 rewrites with 0/6 false accepts, while hash_no_anchor/chain_rewrite detected 0/6 and false-accepted 6/6. Hash chaining detected 6/6 payload tamper cases, while JSONL and SQLite WAL false-accepted 6/6 payload tamper cases. The tradeoff was tail truncation to the latest anchor, with anchored/none losing a mean 4.17 acknowledged records at anchor interval 16.

## Boundaries and scale limits

Six fixed seeds, 72 total medium trials, 6 writer processes, 60 records per writer, SIGKILL process crashes, local filesystem only, local-file anchors, no true power-loss testing, no distributed filesystem testing, no remote immutable anchor service, no throughput scaling study.

## Claim scope

In a local fixed-seed multiprocessing crash/recovery harness, a periodically anchored hash-chain evidence ledger rejected payload tamper and suffix-rewrite faults after writer SIGKILL crashes, while JSONL and SQLite WAL storage baselines accepted tampered records and the unanchored hash-chain ablation accepted recomputed suffix rewrites.

## Why it stopped

Medium local evidence supports the mechanism but remains synthetic/local and lacks power-loss, filesystem, remote-anchor, and scale validation required for a paper claim.

## Recommended next action

Stop short of paper writing; the next bounded deepen test should sweep anchor intervals and add real filesystem fault injection or a remote append-only anchor service to quantify integrity versus acknowledged-tail-loss tradeoffs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor cadence and remote-anchor validation for crash-recovered evidence ledgers
- Success threshold: Across at least 5 fixed seeds per condition, anchored recovery has 0 false accepts for payload tamper and suffix rewrites, detects at least 95% of injected integrity faults, and shows a quantified anchor interval where mean acknowledged-tail loss is below 5 records with less than 2x throughput cost versus SQLite WAL.
- Stop condition: Stop if anchored recovery false-accepts any recomputed suffix rewrite with a valid pre-fault external anchor, or if the lowest-loss anchor cadence costs more than 2x SQLite WAL throughput while still losing more than 5 acknowledged records on average.

## Evidence references

- Artifact root: `<local-path>/projects/multi-process-crash-recovery-validation-for-anchored-evide-8c910db21d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
