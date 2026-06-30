# Tool-Call Validator Router for Local Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tool-call-validator-router-for-local-agents-f47b621389b4`
Run ID: `tool-call-validator-router-for-local-agents-f47b621389b4-20260526T075411001654+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/dfba6690e973

## What looked useful

The validator-router achieved 0.000 mean unsafe execution rate and 1.000 mean valid utility rate across 10 synthetic seeds, while schema-only validation averaged 0.641 unsafe execution rate and 0.818 valid utility rate. Mean router decision latency was 3.08 microseconds.

## Boundaries and scale limits

No real LLM/local-agent traces, adversarial trace generation, production tool adapters, or multi-framework deployment were tested. The benchmark is CPU-only and synthetic, with 10 seeds x 20000 generated calls as the largest persistence check.

## Claim scope

On synthetic local-agent tool-call traces generated from hand-written safe, policy-unsafe, schema-invalid, and repairable cases, a deterministic validator-router reduced unsafe executions versus direct and schema-only baselines while preserving repairable safe-call utility.

## Why it stopped

Closed as no-paper useful synthetic mechanism evidence; the current run is not a full validation because it does not use real agent traces or production tool adapters.

## Recommended next action

Run this exact metric harness on real local-agent traces from at least two agent frameworks, plus adversarially generated tool calls, before considering a bounded paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Validation of Tool-Call Validator Router
- Success threshold: Across real traces, validator-router unsafe execution rate <= 10% of schema-only unsafe execution rate, valid utility rate >= 0.95, and median routing latency < 1 ms.
- Stop condition: Stop if real-trace router utility falls below 0.90 or unsafe execution rate exceeds 0.05 after policy tuning, because the synthetic mechanism would not transfer cleanly.

## Evidence references

- Artifact root: `<local-path>/projects/tool-call-validator-router-for-local-agents-f47b621389b4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
