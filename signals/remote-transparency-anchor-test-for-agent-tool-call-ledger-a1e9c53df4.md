# Remote Transparency Anchor Test for Agent Tool-Call Ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `remote-transparency-anchor-test-for-agent-tool-call-ledger-a1e9c53df4`
Run ID: `remote-transparency-anchor-test-for-agent-tool-call-ledger-a1e9c53df4-20260610T183401270122+0000`

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

- Parent run decision: Tamper-Evident Evidence Ledger for Agent Tool Calls: enoch://control-plane/projects/tamper-evident-evidence-ledger-for-agent-tool-calls-0e7eb1d87a2c/runs/tamper-evident-evidence-ledger-for-agent-tool-calls-0e7eb1d87a2c-20260610T170322432710+0000
- Parent run decision: Real Agent Tool-Call Ledger Integration With External Anchors: enoch://control-plane/projects/real-agent-tool-call-ledger-integration-with-external-anch-59ccac4e2d/runs/real-agent-tool-call-ledger-integration-with-external-anch-59ccac4e2d-20260610T174121244278+0000

## What looked useful

Across five fixed seeds and 6,250 adversarial trials spanning edit, delete, insert, truncate, and suffix-rewrite attacks, local checkpoints detected 0% of attacks when local metadata was attacker-rewritable, while all remote-anchor variants detected 100%. Anchor-every-10 added about 4.5% local write time and 7.6% local clean-verify time in the prototype.

## Boundaries and scale limits

The remote transparency log was modeled as an independent append-only artifact rather than a live external service; no network latency, inclusion proof API, service outage, key compromise, colluding log operator, real agent trace, or concurrent writer behavior was tested.

## Claim scope

In deterministic 3,000-entry synthetic agent tool-call ledgers under a local-store compromise model, independent transparency checkpoints detect retroactive ledger rewrites that a local-only checkpoint baseline misses.

## Why it stopped

Mechanism support was observed, but evidence is not paper-positive because the remote anchor was proxied locally and traces were synthetic.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should replace the modeled transparency log with a live HTTP transparency service with inclusion proofs and failure injection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live Transparency Service Validation for Agent Tool-Call Ledger Anchors
- Success threshold: At least 99.9% detection over 10,000 adversarial trials with zero clean-ledger false positives, p95 anchor submission latency below 250 ms on a local HTTP service or documented public-service latency, and bounded failure recovery semantics under injected outages.
- Stop condition: Stop if inclusion-proof verification fails on clean ledgers, if retroactive tampering can be hidden from an uncompromised service, or if p95 anchor latency exceeds 1 second for anchor-every-10 without a viable batching strategy.

## Evidence references

- Artifact root: `<local-path>/projects/remote-transparency-anchor-test-for-agent-tool-call-ledger-a1e9c53df4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
