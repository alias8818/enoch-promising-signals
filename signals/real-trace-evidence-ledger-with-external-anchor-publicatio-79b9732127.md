# Real Trace Evidence Ledger with External Anchor Publication

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-evidence-ledger-with-external-anchor-publicatio-79b9732127`
Run ID: `real-trace-evidence-ledger-with-external-anchor-publicatio-79b9732127-20260602T155313723073+0000`

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

- Parent run decision: Agent Evidence Ledger via Anchors: enoch://control-plane/projects/agent-evidence-ledger-via-anchors-cd0717334efe/runs/agent-evidence-ledger-via-anchors-cd0717334efe-20260602T102913789033+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/18f8c2625857

## What looked useful

The direct Tier 1 mechanism worked: the ledger root d3791e4383593f4b817921e98a4d899bdca81435439db6de1b53652de1d70b91 was timestamped by DigiCert at Jun 2 15:54:59 2026 GMT, and OpenSSL verified the response against the original query with Verification: OK.

## Boundaries and scale limits

Tested only one project workspace, five evidence files, one timestamp authority, and one immediate verification pass. It does not test long-term replay after certificate expiry, multiple independent anchors, adversarial tampering recovery, transparency-log publication, operational governance, or large evidence volumes.

## Claim scope

A small local trace ledger built from five real Enoch project artifacts can produce a deterministic SHA-256 Merkle root and obtain an externally verifiable RFC 3161 timestamp token over that root from a public timestamp authority.

## Why it stopped

Tier 1 direct mechanism support was achieved, but publication readiness would require durability, multi-anchor robustness, tamper-evidence controls, and larger operational traces.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next bounded test is a deepen follow-up that repeats anchoring across at least three independent TSAs or public transparency surfaces and verifies replay after ledger mutation controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-anchor durability and tamper-control test for trace evidence ledgers
- Success threshold: All independent anchors verify the original root, all controlled mutations fail verification or produce a different root, and the full procedure remains reproducible from saved artifacts and logs.
- Stop condition: Stop if fewer than two independent anchors can be obtained without private credentials, if any anchor cannot be replay-verified from saved artifacts, or if a controlled mutation still verifies against the original root.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-evidence-ledger-with-external-anchor-publicatio-79b9732127`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
