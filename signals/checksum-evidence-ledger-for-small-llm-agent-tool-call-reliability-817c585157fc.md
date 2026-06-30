# Checksum evidence ledger for small LLM agent tool-call reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `checksum-evidence-ledger-for-small-llm-agent-tool-call-reliability-817c585157fc`
Run ID: `checksum-evidence-ledger-for-small-llm-agent-tool-call-reliability-817c585157fc-20260604T165318478806+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/33ebd991a77f

## What looked useful

Anchored receipt checksums are a low-overhead integrity guard for corrupted tool evidence, but self-consistency checks without an anchored original receipt still accepted every forged checksum case.

## Boundaries and scale limits

Synthetic trace-level benchmark only; no real small LLM generations, multi-step agent plans, production tool APIs, adversarial prompt injection, or broad task distribution were tested.

## Claim scope

In a deterministic synthetic one-tool agent trace benchmark with injected evidence corruption, an anchored SHA-256 checksum ledger reduced accepted wrong answers to zero versus 29.757% for no ledger and 20.787% for ID-only validation.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy rather than direct validation of real small LLM agent tool-call reliability.

## Recommended next action

Run a bounded direct small-LLM benchmark comparing no-ledger, ID-only, self-checksum, anchored-checksum, and repair conditions on real tool-use tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-LLM checksum ledger benchmark for tool-call reliability
- Success threshold: Anchored checksum or checksum-plus-repair reduces accepted wrong answers by at least 50% versus ID-only while keeping clean-task false rejects below 5%.
- Stop condition: Stop if real small LLMs cannot reliably emit required receipt fields after two prompt/schema attempts or if clean-task false rejects exceed 20%.

## Evidence references

- Artifact root: `<local-path>/projects/checksum-evidence-ledger-for-small-llm-agent-tool-call-reliability-817c585157fc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
