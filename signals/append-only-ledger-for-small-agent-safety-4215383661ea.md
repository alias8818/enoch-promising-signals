# Append-Only Ledger for Small Agent Safety

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `append-only-ledger-for-small-agent-safety-4215383661ea`
Run ID: `append-only-ledger-for-small-agent-safety-4215383661ea-20260529T125601002134+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/277f7d0bf68a

## What looked useful

Append-only hash-chain ledgers are useful audit infrastructure for small agents, but unanchored ledgers do not detect suffix truncation and the mechanism does not by itself prevent unsafe runtime actions.

## Boundaries and scale limits

Synthetic tool events only; no live LLM agent integration, no concurrent writers, no crash/restart persistence test, no external anchor service, no adversarial key compromise test, and no online policy-enforcement comparison.

## Claim scope

In a deterministic synthetic small-agent action stream up to 50,000 events, a single-writer HMAC hash-chain JSONL ledger detects post-hoc event modification, deletion, reordering, and forged appends, preserves replayable policy-audit evidence, and detects suffix truncation only when the verifier has an expected final head or count.

## Why it stopped

Synthetic bounded evidence supports audit integrity but not a publication-grade safety claim; it also early-falsifies any strong claim that an unanchored local append-only ledger alone gives complete tamper evidence.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should integrate the ledger with a real small-agent tool loop and compare audit-only logging against online enforcement with external final-head checkpoints.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored ledger with online enforcement in a real small-agent tool loop
- Success threshold: At least 95% reduction in executed policy-violating tool calls versus audit-only logging on the bounded task suite, 100% detection of tested post-hoc tampering including suffix truncation with anchors, and less than 3x wall-clock overhead.
- Stop condition: Stop if ledger integration misses any emitted tool calls, anchored truncation detection fails, or online gating overhead exceeds 3x before reducing executed violations by 95%.

## Evidence references

- Artifact root: `<local-path>/projects/append-only-ledger-for-small-agent-safety-4215383661ea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
