# Real-trace evidence ledger verification benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-evidence-ledger-verification-benchmark-b2c095091a`
Run ID: `real-trace-evidence-ledger-verification-benchmark-b2c095091a-20260608T160712229530+0000`

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

- Parent run decision: Structured Evidence Ledger for Tool-Calling Agent Verification: enoch://control-plane/projects/structured-evidence-ledger-for-tool-calling-agent-verification-087281e9277e/runs/structured-evidence-ledger-for-tool-calling-agent-verification-087281e9277e-20260608T131521298205+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0fbedae6cd8d

## What looked useful

Tier 1 controlled direct test met its threshold: clean verification succeeded; byte flip, line deletion, line duplication, adjacent reorder, tail truncation, and forged append were all detected and first-error localized. Whole-file SHA-256 also detected all tampering but provided no localization.

## Boundaries and scale limits

Single small real trace, 30 JSONL lines and 43,539 bytes; six deterministic tamper modes; no multi-source corpus, long trace, adversarial ledger-forgery model, signed timestamping, append-only storage, or production custody validation.

## Claim scope

A hash-chained evidence ledger built over exact bytes of one real Enoch/Codex JSONL worker trace verified the clean trace and detected plus localized six controlled tamper variants.

## Why it stopped

No-paper closure: bounded Tier 1 mechanism support is useful but too narrow for publication readiness.

## Recommended next action

Run a bounded deepen follow-up on at least five independent real trace files with larger event counts and an adversarial mutation suite before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-trace adversarial evidence ledger verification benchmark
- Success threshold: Clean false-positive rate 0%; tamper detection rate 100%; first-error localization rate at least 95%; ledger verifier throughput within 2x of per-line independent hash baseline on the tested corpus.
- Stop condition: Stop if any clean real trace fails verification without explained ledger construction error, any tamper class detection falls below 100%, or localization falls below 95% after implementation bugs are ruled out.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-evidence-ledger-verification-benchmark-b2c095091a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
