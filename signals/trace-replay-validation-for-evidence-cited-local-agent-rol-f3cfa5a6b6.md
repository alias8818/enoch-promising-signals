# Trace replay validation for evidence-cited local-agent rollback

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `trace-replay-validation-for-evidence-cited-local-agent-rol-f3cfa5a6b6`
Run ID: `trace-replay-validation-for-evidence-cited-local-agent-rol-f3cfa5a6b6-20260527T223213274669+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Live local-agent rollback with mandatory evidence citations: enoch://control-plane/projects/live-local-agent-rollback-with-mandatory-evidence-citation-fa98b7dfbc/runs/live-local-agent-rollback-with-mandatory-evidence-citation-fa98b7dfbc-20260527T190931120324+0000
- Parent run decision: Evidence-ledger rollback on realistic agent traces: enoch://control-plane/projects/evidence-ledger-rollback-on-realistic-agent-traces-ae5a27b438/runs/evidence-ledger-rollback-on-realistic-agent-traces-ae5a27b438-20260527T171604050258+0000

## What looked useful

Evidence citations add rollback coverage that state hashes alone miss: stale evidence and swapped citations had 0% bad-commit prevention under operation replay and hash-guard replay, while evidence-cited replay reached 100% detection and prevention with 0% false rejects in this simulator.

## Boundaries and scale limits

Synthetic traces only; no real local-agent logs, LLM-generated citations, natural-language evidence ambiguity, external tool side effects, semantic build/test validation, or adversarial hash-forgery model were evaluated.

## Claim scope

In a deterministic synthetic local-agent rollback simulator with fixed seeds, evidence-cited replay detected and repaired injected trace mutation, stale evidence, citation swap, and post-hash tamper faults across 100000 episodes, outperforming operation replay and state-hash-only replay on bad-commit prevention.

## Why it stopped

The mechanism is supported only by synthetic trace validation, not real local-agent rollback traces, so this is not publication-grade evidence.

## Recommended next action

Stop as no-paper useful signal; the next bounded step is to replay captured real local-agent traces with evidence citations and actual file/tool snapshots before making any publication claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay evidence-cited rollback on captured local-agent traces
- Success threshold: At least 95% bad-commit prevention on injected or observed evidence/citation rollback faults, no more than 2% false rejects on clean traces, and a statistically meaningful improvement over both baselines on real trace replay.
- Stop condition: Stop if real traces lack durable evidence citations/checkpoints needed for replay, or if evidence-cited replay fails to beat hash-guard replay on bad-commit prevention without exceeding the false-reject threshold.

## Evidence references

- Artifact root: `<local-path>/projects/trace-replay-validation-for-evidence-cited-local-agent-rol-f3cfa5a6b6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
