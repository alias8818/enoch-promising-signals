# Evidence-ledger rollback on real small local tool-agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-rollback-on-real-small-local-tool-agent-tr-bc95ba8933`
Run ID: `evidence-ledger-rollback-on-real-small-local-tool-agent-tr-bc95ba8933-20260605T060340997659+0000`

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

- Parent run decision: Evidence-Ledger Rollback for Small Local Agents: enoch://control-plane/projects/evidence-ledger-rollback-for-small-local-agents-de053873248b/runs/evidence-ledger-rollback-for-small-local-agents-de053873248b-20260605T021944513018+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/47a251bb1026

## What looked useful

The Tier 1 direct test passed: ledger_safe_rate was 1.0, baseline_error_rate was 1.0, drift rollback was 3/3, and failed-evidence rejection was 1/1 on real local shell command traces.

## Boundaries and scale limits

Small deterministic harness only: four scenarios, one-evidence/one-claim dependencies, structured claims, local filesystem tools, no diverse LLM-agent corpus, no long sessions, no concurrent tools, and no natural-language claim extraction evaluation.

## Claim scope

On four controlled local shell-backed tool-agent scenarios with mutable or failed evidence, an explicit evidence ledger with dependency validation rolled back or rejected all stale/unsupported dependent claims while a no-rollback scratchpad baseline retained all bad claims.

## Why it stopped

Tier 1 mechanism support was achieved, but the controlled trace-only evidence is not publication-grade and should close as no-paper useful signal.

## Recommended next action

Run a bounded deepen follow-up on at least 20 existing local Codex/LangGraph-style traces with natural-language claim-to-evidence mapping, stale-claim prevention, and false rollback rate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger rollback on existing natural-language local agent traces
- Success threshold: Catch at least 80% of injected stale-evidence claims and keep false rollbacks at or below 10% on unchanged controls across at least 20 real local traces.
- Stop condition: Stop if claim-to-evidence extraction cannot map at least 50% of candidate claims or if false rollback rate exceeds 25% after the first 10 traces.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-on-real-small-local-tool-agent-tr-bc95ba8933`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
