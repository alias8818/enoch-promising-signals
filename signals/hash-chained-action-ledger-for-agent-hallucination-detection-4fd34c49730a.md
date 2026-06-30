# Hash-Chained Action Ledger for Agent Hallucination Detection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hash-chained-action-ledger-for-agent-hallucination-detection-4fd34c49730a`
Run ID: `hash-chained-action-ledger-for-agent-hallucination-detection-4fd34c49730a-20260526T115811021715+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b0283eaa9379

## What looked useful

Hash chaining adds detection for deletion, reordering, and replay-prefix attacks that independent per-entry HMACs miss, while retaining sub-0.1 ms mean verification time per synthetic case in this local Python implementation.

## Boundaries and scale limits

Evaluated on 2,000 synthetic traces and 36,000 verification cases with 4-20 actions per trace. No real agent traces, no natural-language claim extraction, no production persistence layer, no external timestamping service, and no compromised-key adversary were tested.

## Claim scope

In deterministic synthetic action traces, a hash-chained ledger with per-entry HMACs and a trusted final anchor detects tested action-level fabrication and tampering attacks, including deletion, insertion, modification, reordering, and prefix replay. It does not by itself detect unconstrained natural-language hallucinations.

## Why it stopped

Synthetic action-ledger evidence supports the narrow mechanism but is not direct evidence for broad agent hallucination detection or paper readiness.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should evaluate ledger-backed structured claim extraction on real or realistic agent transcripts with labeled action-report hallucinations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Ledger-Backed Claim Extraction on Agent Transcripts
- Success threshold: At least 0.90 precision and 0.80 recall for action-report hallucinations on a held-out transcript set, with clear failure taxonomy for unsupported semantic claims.
- Stop condition: Stop if structured claim extraction cannot reliably map at least 80% of action-related summary claims to ledger entries or if false positives exceed 20% on non-hallucinated summaries.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chained-action-ledger-for-agent-hallucination-detection-4fd34c49730a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
