# Live gated-versus-ungated CPU-local LLM evidence-ledger harness

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `live-gated-versus-ungated-cpu-local-llm-evidence-ledger-ha-b7898631b5`
Run ID: `live-gated-versus-ungated-cpu-local-llm-evidence-ledger-ha-b7898631b5-20260605T065304023592+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Evidence-ledger gating on real CPU-local LLM tool-use traces: enoch://control-plane/projects/evidence-ledger-gating-on-real-cpu-local-llm-tool-use-trac-7d2b76c35d/runs/evidence-ledger-gating-on-real-cpu-local-llm-tool-use-trac-7d2b76c35d-20260605T023544452860+0000
- Parent run decision: Evidence Ledger Reduces Invalid Tool Calls in CPU Agents: enoch://control-plane/projects/evidence-ledger-reduces-invalid-tool-calls-in-cpu-agents-55648ef1c8f9/runs/evidence-ledger-reduces-invalid-tool-calls-in-cpu-agents-55648ef1c8f9-20260604T213311142654+0000

## What looked useful

The gate is useful as a defensive filter: plain false-accepted 60.0% of cases and ungated ledger false-accepted 86.7%, while gate_no_repair and gate_repair false-accepted 0.0%. It is not a useful answer-producing harness at this scale because gate_repair acceptance was only 6.7% and accepted-correct-over-all-cases was 6.7%, below the 60% acceptance and utility-gain thresholds.

## Boundaries and scale limits

Single 0.5B instruct model, five synthetic-but-file-backed local tasks, deterministic task-specific verifier, one repair attempt, no production traces, no larger local models, no constrained decoder, no human audit study.

## Claim scope

On five controlled local file/code tasks with three fixed seeds using cached CPU-local Qwen2.5-0.5B-Instruct, live evidence-ledger support gating reduced false accepted answers to zero versus ungated baselines, but accepted only 1 of 15 cases.

## Why it stopped

Tier 2 fixed-seed direct benchmark failed the live-gate utility threshold: false accepts were eliminated, but the gate over-blocked and accepted only 1 of 15 cases.

## Recommended next action

Stop this branch as no-paper useful signal; a bounded follow-up should test schema-constrained repair on the same benchmark only if the next controller depth permits it.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Schema-constrained repair for CPU-local evidence-ledger gates
- Success threshold: Schema-constrained repair false_accept_rate = 0.0, accepted_decoy_contamination = 0.0, acceptance_rate >= 0.4, accepted_correct_rate_over_all_cases at least 0.2 above current gate_repair and not below plain by more than 0.1.
- Stop condition: Stop if parse/support failures remain above 50% or if any false accepted answer appears after the gate.

## Evidence references

- Artifact root: `<local-path>/projects/live-gated-versus-ungated-cpu-local-llm-evidence-ledger-ha-b7898631b5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
