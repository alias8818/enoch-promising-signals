# LangGraph evidence-ledger rollback on noisy natural-language contradiction traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `langgraph-evidence-ledger-rollback-on-noisy-natural-langua-f4e90b6a1d`
Run ID: `langgraph-evidence-ledger-rollback-on-noisy-natural-langua-f4e90b6a1d-20260522T021912930465+0000`

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

- Parent run decision: Evidence-ledger agent with rollback on contradiction: enoch://control-plane/projects/evidence-ledger-agent-with-rollback-on-contradiction-b6f89c47dc66/runs/evidence-ledger-agent-with-rollback-on-contradiction-b6f89c47dc66-20260521T220804590367+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1d33469bb5d9

## What looked useful

Evidence-gated rollback reduced mean active-ledger conflict rate from 0.6238 to 0.0000 and raised strict accuracy from 0.3762 to 1.0000. Naive rollback also removed conflicts but dropped to 0.9373 strict accuracy because low-confidence rumors caused over-rollback.

## Boundaries and scale limits

Validated on 1000 synthetic traces of 50 events with deterministic regex claim extraction over a small entity-attribute domain; no real traces, LLM/NLI extraction, persistence backend, concurrent execution, or production checkpoint recovery were tested.

## Claim scope

In a controlled synthetic natural-language trace setting using actual LangGraph StateGraph execution, an evidence-gated rollback ledger eliminated active contradictions and improved strict final ledger accuracy versus append-only and naive rollback controls.

## Why it stopped

Tier 1 direct controlled test completed; mechanism support is useful but synthetic/template-bound and not publication-grade.

## Recommended next action

Run a bounded deepen test with LLM/NLI claim extraction on adversarial paraphrase traces plus checkpoint replay before considering paper scope.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM/NLI evidence-ledger rollback on adversarial paraphrase contradiction traces
- Success threshold: Rollback conflict rate <= 0.05, strict accuracy at least 15 percentage points above append-only and 5 percentage points above naive rollback, extractor claim F1 >= 0.85, and checkpoint replay metrics exactly match uninterrupted execution.
- Stop condition: Stop if extractor claim F1 is below 0.85 or if rollback fails to improve strict accuracy by at least 5 percentage points versus both controls.

## Evidence references

- Artifact root: `<local-path>/projects/langgraph-evidence-ledger-rollback-on-noisy-natural-langua-f4e90b6a1d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
