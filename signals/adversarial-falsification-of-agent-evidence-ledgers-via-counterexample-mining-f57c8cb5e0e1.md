# Adversarial Falsification of Agent Evidence Ledgers via Counterexample Mining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adversarial-falsification-of-agent-evidence-ledgers-via-counterexample-mining-f57c8cb5e0e1`
Run ID: `adversarial-falsification-of-agent-evidence-ledgers-via-counterexample-mining-f57c8cb5e0e1-20260517T132557765206+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/536f48d17d5a

## What looked useful

The run provides a reproducible counterexample template showing that source integrity and rationale token checks do not guarantee claim truth when verifier policies omit task-level semantic replay.

## Boundaries and scale limits

Tested only on 5000 synthetic arithmetic tasks with deterministic records and simple verifier policies; no real agent traces, natural-language entailment, multi-step tool use, or production append-only ledger implementation was evaluated.

## Claim scope

In a deterministic synthetic arithmetic-ledger benchmark, mined false claims can pass schema, provenance-hash, and lexical-rationale evidence-ledger checks while being rejected by semantic replay.

## Why it stopped

Proxy/synthetic useful signal only: the mechanism is demonstrated locally, but broad scientific closure needs real ledger traces or a realistic ledger implementation.

## Recommended next action

Run a bounded direct follow-up on realistic tool-use or agent evidence ledgers with mined false claims, semantic replay, and entailment-model verifier baselines; stop this run as no-paper synthetic useful signal.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Counterexample Mining on Realistic Agent Evidence Ledgers
- Success threshold: On at least 500 realistic ledger instances, mined false claims achieve at least 25 percentage points higher false acceptance than random corruptions under a non-semantic verifier, while semantic replay or entailment baselines reject at least 90% of mined false claims without rejecting more than 5% of clean ledgers.
- Stop condition: Stop as negative if mined false claims do not materially outperform random corruption or if realistic ledgers already include semantic replay that rejects at least 95% of mined false claims.

## Evidence references

- Artifact root: `<local-path>/projects/adversarial-falsification-of-agent-evidence-ledgers-via-counterexample-mining-f57c8cb5e0e1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
