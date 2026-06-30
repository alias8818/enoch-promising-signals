# API-backed tiny-agent replay drift ledger validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `api-backed-tiny-agent-replay-drift-ledger-validation-8de7c33aa1`
Run ID: `api-backed-tiny-agent-replay-drift-ledger-validation-8de7c33aa1-20260528T215020999164+0000`

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

- Parent run decision: Deterministic evidence ledger for tiny agent reliability: enoch://control-plane/projects/deterministic-evidence-ledger-for-tiny-agent-reliability-9329e525f021/runs/deterministic-evidence-ledger-for-tiny-agent-reliability-9329e525f021-20260528T154250896752+0000
- Parent run decision: Deterministic evidence ledgers on real tiny-agent workflows with replay drift: enoch://control-plane/projects/deterministic-evidence-ledgers-on-real-tiny-agent-workflow-285feb4a25/runs/deterministic-evidence-ledgers-on-real-tiny-agent-workflow-285feb4a25-20260528T180510922843+0000

## What looked useful

Across 100 deterministic tasks and 600 replay cases per validator, the full ledger achieved 400/400 material drift detection, 0/200 benign false positives, and 400/400 material localization. Output-only and raw-transcript baselines each detected 300/400 material cases; raw transcript also produced 100/200 benign false positives. Ablations failed in the expected component-specific ways.

## Boundaries and scale limits

Local deterministic API, arithmetic two-step tiny-agent traces, controlled injected drift, no live LLM provider, no streaming, no retries, no long multi-tool traces, and no naturally occurring provider/model drift.

## Claim scope

In a controlled local HTTP API tiny-agent harness with fixed seeds and injected replay drift, a normalized request/semantic-response/tool/state hash-chain ledger detected and localized all tested material drift while avoiding benign wording-drift false positives.

## Why it stopped

No-paper closure: the run provides controlled mechanism support with a real HTTP boundary, fixed seeds, ablations, and baselines, but the evidence is synthetic and not enough for publication readiness.

## Recommended next action

Run the same metric suite against a live or open-weight LLM HTTP API with fixed prompts, retries/streaming controls, and at least 100 multi-tool traces before considering any paper-positive claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live or open-weight LLM API replay drift ledger validation
- Success threshold: Full ledger material detection >= 0.95, benign false-positive rate <= 0.05, localization >= 0.90, and a statistically clear improvement over output-only and raw-transcript baselines on at least two drift classes.
- Stop condition: Stop negative if the full ledger misses more than 5% of material drift, exceeds 5% benign false positives, or fails to outperform both baselines on real API traces.

## Evidence references

- Artifact root: `<local-path>/projects/api-backed-tiny-agent-replay-drift-ledger-validation-8de7c33aa1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
