# Multi-anchor durability and tamper-control test for trace evidence ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `multi-anchor-durability-and-tamper-control-test-for-trace-b85e9fbb76`
Run ID: `multi-anchor-durability-and-tamper-control-test-for-trace-b85e9fbb76-20260602T190413498663+0000`

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

- Parent run decision: Real Trace Evidence Ledger with External Anchor Publication: enoch://control-plane/projects/real-trace-evidence-ledger-with-external-anchor-publicatio-79b9732127/runs/real-trace-evidence-ledger-with-external-anchor-publicatio-79b9732127-20260602T155313723073+0000
- Parent run decision: Agent Evidence Ledger via Anchors: enoch://control-plane/projects/agent-evidence-ledger-via-anchors-cd0717334efe/runs/agent-evidence-ledger-via-anchors-cd0717334efe-20260602T102913789033+0000

## What looked useful

Three independent any-conflict anchors improved informed-tamper detection by about 0.31 to 0.32 absolute over the single-anchor baseline across informed rewrite, segment deletion, and segment reorder stress cells, with 0.0 clean false positives in the tested synthetic controls. Majority verification was weaker than any-conflict verification for tamper control.

## Boundaries and scale limits

No real timestamping service, production database, institutional chain-of-custody workflow, legal admissibility process, key-custody process, delayed anchoring, or real trace-evidence data was tested. The result supports the mechanism only within the synthetic threat model.

## Claim scope

Synthetic fixed-seed Monte Carlo trace-evidence ledger simulation: periodic signed anchors over 512-entry hash-chain ledgers, 5 seeds, 125000 trials, single-anchor baseline versus 2-anchor and 3-anchor ablations, clean controls and informed tamper attacks under independent anchor compromise and receipt loss.

## Why it stopped

Useful synthetic Tier 2 mechanism signal, but evidence is not publication-grade because real anchors, real custody workflows, operational failure modes, and non-synthetic data were not tested.

## Recommended next action

Stop paper path for this run; perform a bounded implementation-level replay against a durable ledger database and independent timestamp-anchor services before considering a scoped paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Implementation replay of multi-anchor trace ledger tamper detection
- Success threshold: Three-anchor any-conflict verification preserves at least a 0.20 absolute detection-rate advantage over single-anchor baseline for informed attacks at 0.5 anchor compromise / 0.1 receipt loss, with false_positive_rate <= 0.01 and affected_segment_verifiable_rate >= 0.95.
- Stop condition: Stop if the implemented three-anchor system fails to exceed the single-anchor baseline by 0.10 absolute detection rate under the 0.5 compromise / 0.1 loss condition, or if clean false positives exceed 0.05.

## Evidence references

- Artifact root: `<local-path>/projects/multi-anchor-durability-and-tamper-control-test-for-trace-b85e9fbb76`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
