# Larger open-ended real-LLM validation of LangGraph evidence-ledger rollback

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `larger-open-ended-real-llm-validation-of-langgraph-evidenc-2c8477dfd7`
Run ID: `larger-open-ended-real-llm-validation-of-langgraph-evidenc-2c8477dfd7-20260527T011447002406+0000`

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

- Parent run decision: Evidence-ledger rollback in a real tool-using LLM agent harness: enoch://control-plane/projects/evidence-ledger-rollback-in-a-real-tool-using-llm-agent-ha-200d93d7b9/runs/evidence-ledger-rollback-in-a-real-tool-using-llm-agent-ha-200d93d7b9-20260524T202539682932+0000
- Parent run decision: Evidence-ledger rollback in a real LLM LangGraph agent loop: enoch://control-plane/projects/evidence-ledger-rollback-in-a-real-llm-langgraph-agent-loo-7971f2d1ac/runs/evidence-ledger-rollback-in-a-real-llm-langgraph-agent-loo-7971f2d1ac-20260524T203646329277+0000

## What looked useful

Across 60 real-model LangGraph runs, rollback achieved 95% accuracy and 0% stale-use, while append-only achieved 0% accuracy and 100% stale-use and verifier-without-rollback achieved 5% accuracy and 90% stale-use.

## Boundaries and scale limits

One local 0.5B instruction model, synthetic evidence-conflict tasks, in-memory LangGraph state, no autonomous tool-call planning, no durable checkpoint/replay crash recovery, and one adversarial evidence ordering with six stale cached claims after the live claim.

## Claim scope

In a controlled 20-case fixed-seed LangGraph stress test using Qwen/Qwen2.5-0.5B-Instruct open-ended generation, physical rollback of verifier-invalidated stale evidence reduced stale-evidence use versus append-only and verifier-without-rollback conditions.

## Why it stopped

Bounded direct validation completed and supports the mechanism, but the scope is too narrow for publication readiness.

## Recommended next action

Run one final depth-4 robustness follow-up across evidence orderings, prompt variants, and at least two locally cached instruction models before considering any paper-oriented claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robustness sweep for open-ended LangGraph evidence-ledger rollback
- Success threshold: Rollback improves accuracy by at least 0.20 and reduces stale-use by at least 0.20 versus verifier-without-rollback in every tested ordering-template family, without increasing parse failures above 0.10.
- Stop condition: Stop if rollback fails the threshold in any ordering-template family or if the second model cannot run within the calibrated CPU budget.

## Evidence references

- Artifact root: `<local-path>/projects/larger-open-ended-real-llm-validation-of-langgraph-evidenc-2c8477dfd7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
