# Auditable post-training curation ledger inspired by CuratorKIT

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `100`
Project ID: `curatorkit-auditable-curation-ledger-20260628`
Run ID: `curatorkit-auditable-curation-ledger-20260628-20260629T065916906815+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `100`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 12}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- external source URL present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Exa/arXiv frontier AI scout shortlist: frontier-ai-scout-exa-arxiv-20260628
- Linear ALI-207 frontier research issue: linear-ALI-207
- Linear ALI-208 frontier research issue: linear-ALI-208
- Auditable post-training curation ledger inspired by CuratorKIT: https://arxiv.org/abs/2606.21631v1

## What looked useful

A global auditable curation ledger provides concrete extra integrity coverage over per-sample provenance in synthetic post-training curation traces, with about 1.42x serialized size overhead and 8.85 s full verification time for 204,946 events on one CPU process.

## Boundaries and scale limits

No real CuratorKIT integration, real LLM generation, production dataset, signed transparency log, concurrent writer, or adversarial key-management validation was performed. Verification used a naive Merkle recomputation implementation and should not be treated as optimized throughput evidence.

## Claim scope

Dependency-free synthetic curation traces up to 50,000 samples / 204,946 events show that adding a global append-only hash chain and Merkle checkpoints to per-sample provenance detects rejected-sample deletion and cross-sample event reordering that per-sample chains alone do not detect.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only, even though the scoped mechanism was supported.

## Recommended next action

Run a bounded direct integration test that emits the same ledger from actual CuratorKIT pipeline outputs and validates it against real manifest, rejected.jsonl, dataset card, and checksum artifacts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CuratorKIT artifact integration test for global curation ledger
- Success threshold: On at least one reproducible public CuratorKIT-style run with 1,000 or more samples, untampered artifacts verify cleanly and all four predefined tamper classes are detected with less than 2x serialized metadata overhead and less than 60 seconds verification time.
- Stop condition: Stop if CuratorKIT cannot be installed/run locally on a public dataset within the worker budget, or if ledger emission cannot be mapped to its artifacts without changing CuratorKIT internals.

## Evidence references

- Artifact root: `<local-path>/projects/curatorkit-auditable-curation-ledger-20260628`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
