# Real-agent trace validation for local evidence-ledger policy verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-trace-validation-for-local-evidence-ledger-poli-b9a003676d`
Run ID: `real-agent-trace-validation-for-local-evidence-ledger-poli-b9a003676d-20260529T010331547459+0000`

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

- Parent run decision: Small-agent evidence ledger with local policy verifier: enoch://control-plane/projects/small-agent-evidence-ledger-with-local-policy-verifier-e1aa4e5ce2e1/runs/small-agent-evidence-ledger-with-local-policy-verifier-e1aa4e5ce2e1-20260528T215021459416+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0390c3e9c4a0

## What looked useful

The Tier 1 direct test passed: baseline real-trace replay had no findings and all three negative controls were detected, supporting the mechanism but not publication readiness.

## Boundaries and scale limits

Single project-local trace, simple command/artifact/schema policies, local post-hoc controls, no adversarial trace-capture threat model, no multi-agent or production deployment corpus.

## Claim scope

A single local real Codex agent JSONL trace can be normalized into a SHA-256 hash-chained evidence ledger, replayed deterministically against a small local policy, and used to detect three injected tamper or policy-violation controls.

## Why it stopped

No-paper closure: the local mechanism is supported, but this is a small Tier 1 validation rather than broad or publication-grade evidence.

## Recommended next action

Run a bounded deepen follow-up on at least 50 independent real-agent traces with predeclared policies and adversarial bypass attempts before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus-scale real-agent evidence-ledger replay with adversarial bypass controls
- Success threshold: Ledger replay succeeds on at least 95% of valid traces, detects 100% of injected tamper controls, and reduces unresolved manual-review items by at least 30% versus raw JSONL review without introducing false passes on forbidden-command controls.
- Stop condition: Stop if valid trace replay falls below 90%, any injected tamper control class repeatedly escapes detection, or policy replay becomes nondeterministic across repeated runs.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-trace-validation-for-local-evidence-ledger-poli-b9a003676d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
