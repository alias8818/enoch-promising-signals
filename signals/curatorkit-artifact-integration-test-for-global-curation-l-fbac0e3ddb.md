# CuratorKIT artifact integration test for global curation ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `87`
Project ID: `curatorkit-artifact-integration-test-for-global-curation-l-fbac0e3ddb`
Run ID: `curatorkit-artifact-integration-test-for-global-curation-l-fbac0e3ddb-20260629T074039557656+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `87`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 12}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- external source URL present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Auditable post-training curation ledger inspired by CuratorKIT: enoch://control-plane/projects/curatorkit-auditable-curation-ledger-20260628/runs/curatorkit-auditable-curation-ledger-20260628-20260629T065916906815+0000
- Exa/arXiv frontier AI scout shortlist: frontier-ai-scout-exa-arxiv-20260628
- Linear ALI-207 frontier research issue: linear-ALI-207
- Linear ALI-208 frontier research issue: linear-ALI-208
- Auditable post-training curation ledger inspired by CuratorKIT: https://arxiv.org/abs/2606.21631v1

## What looked useful

The prototype accepted a valid 120-entry synthetic ledger with zero replay errors and rejected all three negative controls: tampered artifact payload, broken previous hash, and conflicting duplicate artifact ID.

## Boundaries and scale limits

No upstream CuratorKIT schema, SDK, API, repository, production ledger endpoint, or real curator dataset was provided. The global behavior is simulated locally with synthetic curators/regions and does not prove compatibility with an existing CuratorKIT or global ledger deployment.

## Claim scope

A dependency-free local harness over 120 synthetic CuratorKIT-style artifacts supports a minimal ledger integration contract: canonical artifact hashing, append-only hash chaining, deterministic replay, tamper rejection, broken-chain rejection, and divergent duplicate-artifact rejection.

## Why it stopped

Local synthetic proxy evidence supports the mechanism but is insufficient for paper-positive validation of real CuratorKIT/global-ledger integration.

## Recommended next action

Stop this run as a no-paper useful signal; the next concrete step is a bounded conformance test using a real CuratorKIT artifact schema or SDK plus the same tamper/conflict controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CuratorKIT schema-backed ledger conformance test
- Success threshold: At least 100 schema-valid CuratorKIT artifacts ingest and replay deterministically with zero valid-ledger errors, while tamper, broken-chain, and duplicate-conflict controls are all rejected.
- Stop condition: Stop as unsupported if the real schema lacks stable artifact identity, canonicalizable payloads, or provenance fields needed for deterministic content addressing and replay.

## Evidence references

- Artifact root: `<local-path>/projects/curatorkit-artifact-integration-test-for-global-curation-l-fbac0e3ddb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
