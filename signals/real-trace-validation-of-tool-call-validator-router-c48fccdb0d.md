# Real-Trace Validation of Tool-Call Validator Router

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-validation-of-tool-call-validator-router-c48fccdb0d`
Run ID: `real-trace-validation-of-tool-call-validator-router-c48fccdb0d-20260526T152101262702+0000`

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

- Parent run decision: Tool-Call Validator Router for Local Agents: enoch://control-plane/projects/tool-call-validator-router-for-local-agents-f47b621389b4/runs/tool-call-validator-router-for-local-agents-f47b621389b4-20260526T075411001654+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/dfba6690e973

## What looked useful

Schema-aware field validation added measurable routing value over a type-only baseline: invalid recall was 1.0 for the schema router versus 0.3 for the type-only router, while both bypassed the 5,000 valid real records.

## Boundaries and scale limits

The clean records are real local Enoch Codex traces, but malformed records are controlled schema mutations rather than naturally occurring production failures. The test does not cover provider-native function-call payloads, live model generation, adversarial prompts, latency under online serving load, or broader tool schemas.

## Claim scope

In a capped Tier 1 local replay over 5,000 real Codex command-execution trace records plus 50,000 controlled malformed variants derived from those records, a schema-aware router bypassed clean records and routed malformed records to validation with no observed false negatives.

## Why it stopped

Tier 1 mechanism threshold was satisfied, but publication-grade validation would require naturally occurring malformed real traces and broader tool schemas.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next bounded action is to replay the same router against a held-out corpus containing naturally malformed or failed real tool-call payloads, not only controlled mutations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-Out Natural Malformed Tool-Call Router Replay
- Success threshold: Invalid recall of 1.0 on critical malformed records, clean bypass rate >= 0.90, and type-only baseline invalid recall at least 0.10 lower than schema-aware routing on the same held-out corpus.
- Stop condition: Stop if any critical malformed held-out record is bypassed by the schema-aware router, or if clean bypass rate falls below 0.75 after schema corrections.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-validation-of-tool-call-validator-router-c48fccdb0d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
