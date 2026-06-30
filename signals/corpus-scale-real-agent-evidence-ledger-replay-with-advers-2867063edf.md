# Corpus-scale real-agent evidence-ledger replay with adversarial bypass controls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `corpus-scale-real-agent-evidence-ledger-replay-with-advers-2867063edf`
Run ID: `corpus-scale-real-agent-evidence-ledger-replay-with-advers-2867063edf-20260529T024651314689+0000`

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

- Parent run decision: Real-agent trace validation for local evidence-ledger policy verification: enoch://control-plane/projects/real-agent-trace-validation-for-local-evidence-ledger-poli-b9a003676d/runs/real-agent-trace-validation-for-local-evidence-ledger-poli-b9a003676d-20260529T010331547459+0000
- Parent run decision: Small-agent evidence ledger with local policy verifier: enoch://control-plane/projects/small-agent-evidence-ledger-with-local-policy-verifier-e1aa4e5ce2e1/runs/small-agent-evidence-ledger-with-local-policy-verifier-e1aa4e5ce2e1-20260528T215021459416+0000

## What looked useful

Payload inclusion and ordered chaining were necessary controls: payload-free chaining missed most same-type substitutions and many content edits, while order-free hashing missed all adjacent reorder attacks. The result supports the practical mechanism but not a paper-ready novelty claim.

## Boundaries and scale limits

The corpus is local rather than independently public; attacks are deterministic programmatic edits rather than adaptive human/model attacks; verification covers transcript integrity, not semantic correctness of original agent actions; no live tamper-resistant storage or cross-machine root publication was tested.

## Claim scope

On 600 fixed-seed sampled local Enoch/Codex real-agent JSONL traces, a canonical full-payload ordered hash-chain evidence ledger detected 100% of 3,600 deterministic transcript tampering replays with 0% clean false positives, outperforming schema-only, type-sequence, payload-free-chain, and order-free-multiset controls.

## Why it stopped

Tier 2 medium confirmation succeeded for local replay integrity, but evidence is not broad or novel enough for publication because it uses local traces and programmatic attacks only.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should test the same ledger in a live multi-agent harness with externally anchored roots and adaptive bypass attempts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live anchored evidence-ledger replay under adaptive bypass attempts
- Success threshold: Full ledger detects at least 99% of adaptive tamper attempts with under 1% clean false positives and beats every baseline or ablation by at least 15 percentage points on aggregate detection.
- Stop condition: Stop if externally anchored roots cannot be implemented locally, if clean false positives exceed 1%, or if full-ledger detection falls below 99% on any core attack family.

## Evidence references

- Artifact root: `<local-path>/projects/corpus-scale-real-agent-evidence-ledger-replay-with-advers-2867063edf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
