# Trace Replay Validation for Agent Evidence Ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-replay-validation-for-agent-evidence-ledgers-df1f7a6569`
Run ID: `trace-replay-validation-for-agent-evidence-ledgers-df1f7a6569-20260524T013758531131+0000`

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

- Parent run decision: Agent Evidence Ledger for Tool-Use Reliability: enoch://control-plane/projects/agent-evidence-ledger-for-tool-use-reliability-f699e49cb406/runs/agent-evidence-ledger-for-tool-use-reliability-f699e49cb406-20260524T011853968704+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c67014ae553a

## What looked useful

Tier 1 evidence supports the mechanism that replay-capable evidence ledgers catch corruption classes that final-answer/action logs can miss, with 16.73x small-trace byte overhead and sub-millisecond replay time in this harness.

## Boundaries and scale limits

Synthetic deterministic traces only; no real LLM calls, external tools, asynchronous execution, long contexts, schema migrations, production persistence, or adversarial trusted-root compromise were tested.

## Claim scope

In a 100-case deterministic synthetic agent-trace harness, a content-addressed evidence ledger with per-step output hashes and a hash chain validated all clean traces and detected all injected output, missing-observation, and input-fixture corruptions; a minimal action/final-answer log missed 27% of input-tamper cases.

## Why it stopped

The controlled Tier 1 direct test met its scoped thresholds, but the evidence is synthetic and mechanism-level rather than publication-grade validation.

## Recommended next action

Run a bounded deepen test on real agent workflow traces with persisted prompts, model metadata, tool IO, and injected corruptions before any paper gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay Validation on Real Agent Workflow Ledgers
- Success threshold: >=95% clean replay validation and >=95% detection of injected corruptions, with all nondeterministic failures categorized rather than silently accepted.
- Stop condition: Stop if real traces cannot be replayed because required prompt/tool/model evidence is unavailable, or if clean replay validation falls below 80% after schema fixes.

## Evidence references

- Artifact root: `<local-path>/projects/trace-replay-validation-for-agent-evidence-ledgers-df1f7a6569`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
