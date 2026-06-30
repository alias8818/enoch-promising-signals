# Structured Evidence Ledger for Tool-Calling Agent Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `structured-evidence-ledger-for-tool-calling-agent-verification-087281e9277e`
Run ID: `structured-evidence-ledger-for-tool-calling-agent-verification-087281e9277e-20260608T131521298205+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0fbedae6cd8d

## What looked useful

Ledger verifier achieved 1.000 accuracy and 0.000 false accept rate; transcript heuristic achieved 0.500 accuracy and 0.600 false accept rate on the same generated episodes. The useful mechanism is explicit evidence IDs, observation hashes, entry ordering, allowed-tool checks, and required claim fragments.

## Boundaries and scale limits

Synthetic single-tool episodes only; no live LLM agent traces, no multi-hop workflows, no adversarial natural-language paraphrases, no human or LLM judge baseline, and no production integration.

## Claim scope

On a deterministic synthetic benchmark of 6,000 single-tool episodes, a typed hash-linked evidence ledger caught generated verification failures involving tampered observations, unsupported claims, missing citations, stale evidence, and disallowed tools, while a stronger plain transcript heuristic missed the attacks requiring structured evidence semantics.

## Why it stopped

No-paper closure because the positive signal is from a synthetic proxy rather than direct real-agent verification evidence.

## Recommended next action

Run a bounded direct benchmark on at least 200 recorded or semi-real multi-step tool-calling traces with independent labels and a strong transcript or LLM-judge baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace evidence ledger verification benchmark
- Success threshold: At least 30% relative reduction in false accept rate versus the strongest baseline without more than 10% absolute increase in false reject rate.
- Stop condition: Stop if ledger instrumentation cannot be applied to real or semi-real traces without changing task semantics, or if false accept reduction is under 10% relative on the first 100 labeled traces.

## Evidence references

- Artifact root: `<local-path>/projects/structured-evidence-ledger-for-tool-calling-agent-verification-087281e9277e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
