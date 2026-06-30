# LangGraph replay validation for evidence-ledger tool mismatch halts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `langgraph-replay-validation-for-evidence-ledger-tool-misma-b61b0d0118`
Run ID: `langgraph-replay-validation-for-evidence-ledger-tool-misma-b61b0d0118-20260523T181114672411+0000`

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

- Parent run decision: Evidence-ledger agent halts on tool mismatch: enoch://control-plane/projects/evidence-ledger-agent-halts-on-tool-mismatch-f41accfaf76d/runs/evidence-ledger-agent-halts-on-tool-mismatch-f41accfaf76d-20260523T171727295488+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3ba0aaaf3c26

## What looked useful

The local harness passed all thresholds: matched replay executed one tool call; tool-name, args, and call-id mismatches each halted with zero tool executions and LangGraph checkpoint histories showed routing to halt.

## Boundaries and scale limits

Tier 1 controlled small direct test only: synthetic tool calls, one graph topology, in-memory checkpoints, no live LLM tool generation, no persistent checkpoint backend, no concurrent replay, and no production evidence-ledger integration.

## Claim scope

In a deterministic LangGraph 1.2.1 StateGraph with an in-memory checkpointer, an evidence-ledger validator that hashes the replayed tool call can route tool-name, args, and call-id mismatches to a halt node before tool execution, while a matched control executes exactly once.

## Why it stopped

No-paper useful signal: the Tier 1 direct test supports the mechanism but is too narrow and synthetic for publication readiness.

## Recommended next action

Run a medium direct follow-up using a persistent LangGraph checkpointer and captured real tool-call message traces to test the same zero-execution invariant under checkpoint resume and concurrent thread ids.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Persistent-checkpoint replay validation for evidence-ledger tool mismatch halts
- Success threshold: Across at least 20 replay cases, 100% of matched controls execute exactly once and 100% of mismatches halt before tool execution, including resumed checkpoints and concurrent thread ids.
- Stop condition: Stop if any mismatch reaches tool execution or if persistent checkpoint replay cannot be made reproducible with local installable dependencies.

## Evidence references

- Artifact root: `<local-path>/projects/langgraph-replay-validation-for-evidence-ledger-tool-misma-b61b0d0118`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
