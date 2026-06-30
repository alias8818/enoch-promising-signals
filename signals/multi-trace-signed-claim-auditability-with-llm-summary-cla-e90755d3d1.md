# Multi-trace signed-claim auditability with LLM summary claims

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `multi-trace-signed-claim-auditability-with-llm-summary-cla-e90755d3d1`
Run ID: `multi-trace-signed-claim-auditability-with-llm-summary-cla-e90755d3d1-20260628T172554611511+0000`

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
- Parent run decision: Real Trace Signed-Claim Auditability Benchmark: enoch://control-plane/projects/real-trace-signed-claim-auditability-benchmark-ed428643ac/runs/real-trace-signed-claim-auditability-benchmark-ed428643ac-20260628T170411685589+0000

## What looked useful

Multi-trace signed evidence references are a useful auditability mechanism for LLM-style summary claims in a bounded synthetic probe: signed_multi had 1.000 attack detection and 0.000 false rejects, while signed_single false-accepted 0.400 of attack rows and unsigned_multi false-accepted 0.253.

## Boundaries and scale limits

Synthetic template summaries only; local HMAC signatures rather than production public-key signing; no live LLM summaries, human adjudication, real operator traces, redaction noise, or adversarial natural-language paraphrases.

## Claim scope

In a deterministic synthetic corpus of 120 tasks and 2,880 audit rows, multi-trace signed claim envelopes detected all injected tampering, under-evidence, unsupported-value, and cross-run evidence cases while text-only, unsigned multi-trace, and signed single-trace controls had false accepts.

## Why it stopped

Proxy-only synthetic validation is insufficient for a paper-positive claim, even though it supports the mechanism.

## Recommended next action

Stop this run as synthetic useful-signal evidence; next run should test real LLM-generated summaries against the same signed multi-trace audit protocol with human support labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-generated signed summary claims on realistic traces
- Success threshold: At least 0.95 attack detection, at most 0.05 false accepts, at most 0.10 false rejects on benign supported LLM-generated claims, and at least 0.90 complete evidence-reference coverage.
- Stop condition: Stop if LLM-generated claims cannot produce complete evidence references above 0.80 coverage or if benign false rejects exceed 0.20 after one prompt/schema refinement.

## Evidence references

- Artifact root: `<local-path>/projects/multi-trace-signed-claim-auditability-with-llm-summary-cla-e90755d3d1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
