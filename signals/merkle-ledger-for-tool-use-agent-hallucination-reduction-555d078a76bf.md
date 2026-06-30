# Merkle Ledger for Tool-Use Agent Hallucination Reduction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `merkle-ledger-for-tool-use-agent-hallucination-reduction-555d078a76bf`
Run ID: `merkle-ledger-for-tool-use-agent-hallucination-reduction-555d078a76bf-20260608T034012373025+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/644b992a27af

## What looked useful

Across 10000 two-lookup trials with 3527 attacked transcripts, the no-ledger baseline accepted corrupted evidence on 0.9997 of attacked trials, while ledger verification detected 1.0 of attacked trials with zero clean rejects; ledger repair reached 1.0 answer accuracy. Scaling from 2 to 128 observations retained 1.0 attack detection per attacked trial with mean repair latency rising from 0.0750 ms to 37.1054 ms.

## Boundaries and scale limits

Synthetic key-value/arithmetic tasks only; no LLM-in-the-loop behavior, real agent traces, prompt injection, concurrent tool streams, or production storage/runtime integration were tested.

## Claim scope

In a deterministic synthetic tool-use pipeline with mutable transcript corruption, Merkle-authenticated tool observation verification detected altered, fabricated, and omitted observations; repair from the canonical event store eliminated accepted corrupted evidence and restored answer accuracy.

## Why it stopped

Bounded synthetic evidence supports the ledger integrity mechanism but is not direct publication-grade evidence for reducing real tool-use agent hallucinations.

## Recommended next action

Stop this run as no-paper useful signal; next run should perform an LLM-in-the-loop corruption benchmark comparing mutable transcript, hash-chain/signed-event, and Merkle-proof conditions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop Merkle tool-ledger corruption benchmark
- Success threshold: At least 30% relative reduction in unsupported tool-grounded claims versus the strongest non-Merkle baseline, no more than 2% false rejects on clean traces, and less than 10% end-to-end latency overhead on a bounded task suite.
- Stop condition: Stop if Merkle verification does not outperform the simpler signed/hash-chain baseline on unsupported claim rate or if false clean rejects exceed 2%.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-ledger-for-tool-use-agent-hallucination-reduction-555d078a76bf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
