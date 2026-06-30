# Cascade Verification for Safer Local Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cascade-verification-for-safer-local-agents-de68e13cb8ba`
Run ID: `cascade-verification-for-safer-local-agents-de68e13cb8ba-20260529T152811405286+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1e8d7bf3cbbd

## What looked useful

Cascade verification caught 24/24 unsafe commands with 1/28 safe false blocks on the fixed benchmark, compared with 23/24 unsafe catches and 1/28 safe false blocks for always-semantic verification. Inline interpreter commands had to be escalated to avoid a scope-check bypass.

## Boundaries and scale limits

No real local-agent traces, no live filesystem sandbox execution, no LLM command generation, and no adversarial mutation suite were used. Cost units are synthetic relative weights, not measured latency.

## Claim scope

On a 52-case synthetic-but-concrete local shell-command benchmark, a static/scope/semantic cascade matched or exceeded the always-semantic verifier's unsafe catch rate while reducing mean relative verification cost from 20.0 to 6.87 cost units and escalating 19.2% of cases.

## Why it stopped

Useful bounded synthetic evidence was produced, but this is not publication-grade validation for real safer local agents.

## Recommended next action

Run a bounded direct-evidence follow-up on recorded or generated local-agent traces with sandbox execution/diff validation and adversarial command mutations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Derived Sandbox Validation for Cascade Verification
- Success threshold: Cascade catches at least 95% of labeled unsafe commands, has no statistically significant increase in safe false blocks versus always-semantic verification, and reduces expensive verifier invocations by at least 50%.
- Stop condition: Stop if cascade misses more than 5% of unsafe commands or if reductions in expensive verifier calls disappear after sandbox/diff validation.

## Evidence references

- Artifact root: `<local-path>/projects/cascade-verification-for-safer-local-agents-de68e13cb8ba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
