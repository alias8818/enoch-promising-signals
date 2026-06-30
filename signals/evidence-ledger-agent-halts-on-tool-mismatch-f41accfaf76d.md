# Evidence-ledger agent halts on tool mismatch

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-halts-on-tool-mismatch-f41accfaf76d`
Run ID: `evidence-ledger-agent-halts-on-tool-mismatch-f41accfaf76d-20260523T171727295488+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3ba0aaaf3c26

## What looked useful

Across 20,000 randomized trials, the unguarded baseline executed 12,015 mismatched observed tool calls, while the evidence-ledger guard executed zero mismatched calls, had zero mismatch misses, zero false halts on 7,985 matched calls, and zero ledger hash-chain failures.

## Boundaries and scale limits

20,000 synthetic single-process trials only; no real LangGraph runtime, no LLM-generated trace corpus, no concurrent or streaming tool calls, no production tool stack, and no human review workflow.

## Claim scope

In a local synthetic Python agent harness with flat tool schemas, an append-only evidence ledger plus pre-dispatch guard halted all generated tool-name and argument-schema mismatches before simulated tool side effects while allowing matched calls.

## Why it stopped

Closed as no-paper useful signal: this run directly supports the local synthetic mechanism but does not provide real-runtime or model-trace evidence.

## Recommended next action

Run a bounded LangGraph replay follow-up around real tool nodes with injected tool-name/schema mismatches and clean traces before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LangGraph replay validation for evidence-ledger tool mismatch halts
- Success threshold: Zero mismatched tool side effects, zero undetected injected mismatches, false halt rate no greater than 0.1% on clean traces, and median guard overhead below 5 ms per tool call.
- Stop condition: Stop if any injected mismatch causes a side effect, if false halt rate exceeds 0.1% after schema fixes, or if integration requires private/external traces unavailable to the worker.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-halts-on-tool-mismatch-f41accfaf76d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
