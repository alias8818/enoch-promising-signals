# Evidence-ledger gating on real CPU-local LLM tool-use traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-gating-on-real-cpu-local-llm-tool-use-trac-7d2b76c35d`
Run ID: `evidence-ledger-gating-on-real-cpu-local-llm-tool-use-trac-7d2b76c35d-20260605T023544452860+0000`

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

- Parent run decision: Evidence Ledger Reduces Invalid Tool Calls in CPU Agents: enoch://control-plane/projects/evidence-ledger-reduces-invalid-tool-calls-in-cpu-agents-55648ef1c8f9/runs/evidence-ledger-reduces-invalid-tool-calls-in-cpu-agents-55648ef1c8f9-20260604T213311142654+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/78b7f7db23db

## What looked useful

On real CPU-local LLM tool-use traces, the strict evidence-id/hash/exit-code/token gate accepted 120/120 supported claims, rejected 360/360 unsupported corruptions, produced zero false accepts, and detected a controlled ledger tamper.

## Boundaries and scale limits

Test used 240 command evidence entries from 31 local source traces and 480 programmatically generated structured claims. It did not test free-form LLM answers, semantic entailment, organic hallucinations, or live gated-versus-ungated agent behavior.

## Claim scope

A deterministic append-only evidence ledger gate can separate structured supported claims from matched unsupported corruptions over real local Codex/Enoch command-execution traces in a bounded Tier 1 CPU test.

## Why it stopped

Bounded Tier 1 direct mechanism test passed, but evidence is not publication-grade because claims were structured/programmatic and no live LLM agent comparison was performed.

## Recommended next action

Run a live gated-versus-ungated CPU-local LLM tool-use harness where final answers must cite ledger entries, then measure unsupported answer rate and abstention on held-out tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live gated-versus-ungated CPU-local LLM evidence-ledger harness
- Success threshold: At least 50 held-out tasks; gated unsupported final-answer rate at least 50% lower than ungated; gated abstention on answerable tasks no more than 25%; median gate overhead under 250 ms per final answer.
- Stop condition: Stop if the gated harness cannot force evidence citations, if unsupported answer reduction is below 25% after 50 tasks, or if abstention exceeds 40% on answerable tasks.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-gating-on-real-cpu-local-llm-tool-use-trac-7d2b76c35d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
