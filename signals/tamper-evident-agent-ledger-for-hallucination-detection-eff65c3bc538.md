# Tamper-Evident Agent Ledger for Hallucination Detection

Status: `useful_signal`
Project ID: `tamper-evident-agent-ledger-for-hallucination-detection-eff65c3bc538`
Run ID: `tamper-evident-agent-ledger-for-hallucination-detection-eff65c3bc538-20260519T131653798016+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f936603008ce

## What looked useful

Tamper-evident logging is useful for provenance hardening, but hallucination detection comes from verifiable claim-to-evidence bindings rather than from hash chaining alone.

## Boundaries and scale limits

Synthetic evidence table and structured claims only; no real LLM traces, natural-language entailment, retrieval noise, key-management analysis, distributed storage, privacy analysis, or long-running production agent workload.

## Claim scope

In a deterministic synthetic structured-claim setting, a hash-chained HMAC-signed ledger detected all tested post-hoc trace mutations and preserved evidence bindings that enabled exact unsupported-claim detection by a verifier.

## Why it stopped

Synthetic mechanism evidence is useful but insufficient for a paper; it supports provenance integrity, not standalone hallucination detection.

## Recommended next action

Run a bounded real-agent trace study with retrieval/tool outputs and natural-language support labels before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Evidence-Bound Ledger Hallucination Audit
- Success threshold: At least 0.90 tamper detection across realistic trace-edit attacks, no unsupported-claim recall loss versus evidence-bound mutable traces, and less than 10% runtime overhead on a bounded local agent benchmark.
- Stop condition: Stop if evidence linking cannot be made reliable enough for at least 0.70 supported/unsupported label agreement or if ledger overhead exceeds 25% on the bounded benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/tamper-evident-agent-ledger-for-hallucination-detection-eff65c3bc538`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
