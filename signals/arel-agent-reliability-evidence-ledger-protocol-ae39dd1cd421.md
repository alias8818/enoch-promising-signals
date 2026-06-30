# AREL: Agent Reliability Evidence Ledger Protocol

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `arel-agent-reliability-evidence-ledger-protocol-ae39dd1cd421`
Run ID: `arel-agent-reliability-evidence-ledger-protocol-ae39dd1cd421-20260609T231349658615+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4c3df127b157

## What looked useful

AREL detected 1000/1000 injected faults with 0/200 false rejects; the plain-note baseline detected 0/1000 injected faults with 0/200 false rejects. Mean serialized AREL ledger size was 9.48x the plain-note size.

## Boundaries and scale limits

Synthetic traces only; no production agents, no human audit study, no external artifact store, no multi-agent workflows, no adversarial authors aware of the validator, and no latency measurements in a real agent runtime.

## Claim scope

On deterministic synthetic agent traces, a minimal typed, hash-chained AREL validator detected five injected reliability-evidence fault classes that an unstructured success-token notes baseline missed.

## Why it stopped

Proxy-only synthetic mechanism evidence supports auditability of the protocol invariants but does not validate real-world agent reliability or publication-grade impact.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should replay AREL over real or benchmark agent traces with a blinded human-audit baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: AREL auditability on real benchmark agent traces
- Success threshold: AREL improves unsupported-claim recall by at least 25 percentage points over plain-log human or lexical audit while keeping false rejects below 5% and storage overhead below 20x.
- Stop condition: Stop if trace conversion requires private unavailable data, if false rejects exceed 10% on valid traces, or if recall improves by less than 10 percentage points over the baseline.

## Evidence references

- Artifact root: `<local-path>/projects/arel-agent-reliability-evidence-ledger-protocol-ae39dd1cd421`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
