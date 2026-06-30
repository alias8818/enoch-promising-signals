# Evidence-ledger rollback for CPU tool-use agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-rollback-for-cpu-tool-use-agents-9fd73d2075d8`
Run ID: `evidence-ledger-rollback-for-cpu-tool-use-agents-9fd73d2075d8-20260522T113007465813+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/10b0868b9e9f

## What looked useful

Rollback reduced invalid live side effects from 37.34% to 0.00% at 20% stale evidence when all early actions were rollbackable, and to 18.47% when 50% of early actions were irreversible. A validate-first control also achieved 0.00% invalid side effects, so rollback needs a latency/deadline setting where waiting for authoritative evidence has measurable utility cost.

## Boundaries and scale limits

Synthetic order-fulfillment state machine only; no real LLM planner, no real shell/file/network tools, no concurrency, no external latency, and no full compensation semantics for irreversible side effects.

## Claim scope

In a deterministic synthetic CPU tool-use workflow with stale cached observations followed by authoritative observations, evidence-dependency rollback eliminates invalid live side effects when early actions are rollbackable, and partially reduces them when only some early actions are rollbackable.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only and the validate-first control dominates unless a real latency or deadline utility is shown.

## Recommended next action

Run a bounded real-agent deepen test with reversible file/database tools, injected stale observations, and a deadline/latency utility that makes early commit valuable relative to validate-first.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU tool-use rollback under deadline utility
- Success threshold: Rollback must reduce invalid live side effects by at least 50% versus no-rollback while achieving higher utility-adjusted correctness than validate-first across at least three stale-observation rates.
- Stop condition: Stop if rollback fails to beat validate-first on utility-adjusted correctness or cannot reduce invalid live side effects by 50% in the reversible-tool setting.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-for-cpu-tool-use-agents-9fd73d2075d8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
