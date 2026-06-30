# Real Trace Signed-Claim Auditability Benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-signed-claim-auditability-benchmark-ed428643ac`
Run ID: `real-trace-signed-claim-auditability-benchmark-ed428643ac-20260628T170411685589+0000`

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

- Parent run decision: Signed Claim System with Evidence Strength Markers: enoch://control-plane/projects/signed-claim-system-with-evidence-strength-markers-86e8ed094d7e/runs/signed-claim-system-with-evidence-strength-markers-86e8ed094d7e-20260628T164810515669+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/deb7aa3d971c

## What looked useful

Signed evidence-bound claims gave machine-checkable auditability in the bounded trace benchmark: supported accept rate 1.000, unsupported reject rate 1.000, tamper reject rate 1.000, while unsigned claims had 0.000 evidence binding.

## Boundaries and scale limits

Single trace, 54 events, 12 templated claims, 4 unsupported controls, 3 tamper controls; no LLM-generated summaries, no human-labeled corpus, and no multi-project trace diversity.

## Claim scope

On one frozen local Codex JSONL worker trace, deterministic signed claims with evidence IDs, evidence hashes, HMAC signatures, and hand-coded predicates accepted all supported controls and rejected all unsupported and tampered controls.

## Why it stopped

Bounded one-trace mechanism evidence supports the auditability design but is not publication-grade direct evidence for broad real-world signed-claim auditability.

## Recommended next action

Stop this run as a no-paper useful signal; next run should deepen with at least 20 real traces, LLM-generated summaries, human support labels, and unsigned/source-linked/signed baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-trace signed-claim auditability with LLM summary claims
- Success threshold: Signed claims reject at least 90% of unsupported or tampered claims and accept at least 90% of supported claims, with at least a 30 percentage point unsupported-reject improvement over unsigned summaries.
- Stop condition: Stop if signed claims accept more than 20% of unsupported claims, reject more than 20% of supported claims, or if trace diversity/human labels cannot be obtained locally.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-signed-claim-auditability-benchmark-ed428643ac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
