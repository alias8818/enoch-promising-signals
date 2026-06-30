# Evidence Ledger Reduces Invalid Tool Calls in CPU Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-reduces-invalid-tool-calls-in-cpu-agents-55648ef1c8f9`
Run ID: `evidence-ledger-reduces-invalid-tool-calls-in-cpu-agents-55648ef1c8f9-20260604T213311142654+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/78b7f7db23db

## What looked useful

The mechanism is useful as a guardrail pattern: evidence validation alone prevents invalid tool execution by abstention, while one bounded repair step recovers most completions in the synthetic setting.

## Boundaries and scale limits

Synthetic noisy planner and generated tasks only; no real LLM traces, no production agent framework, no multi-step evolving evidence, and no comparison against schema-only or prompt-only guardrail baselines.

## Claim scope

In a synthetic CPU-only agent benchmark with evidence-grounded entity and attribute tasks, an evidence-ledger gate reduced invalid tool calls reaching the environment from about 30.8% to 0.0%; bounded repair improved task completion relative to pure abstention.

## Why it stopped

No-paper closure: evidence is synthetic/proxy-only, so it supports a mechanism but not a publication-grade claim about real CPU agents.

## Recommended next action

Run a bounded follow-up on real CPU-local LLM agent traces comparing evidence-ledger gating against schema-only and prompt-only controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger gating on real CPU-local LLM tool-use traces
- Success threshold: Evidence-ledger invalid environment call rate is at least 50% lower than schema-only validation, with task success at least 90% of baseline and CPU overhead below 25% excluding model inference variance.
- Stop condition: Stop if real-trace baseline invalid call rate is below 5%, if ledger success falls below 80% of baseline, or if schema-only validation matches ledger invalid-call reduction within 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-reduces-invalid-tool-calls-in-cpu-agents-55648ef1c8f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
