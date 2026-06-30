# Speculative Agent Verification via Draft-Verify Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `speculative-agent-verification-via-draft-verify-ledger-2191689b1909`
Run ID: `speculative-agent-verification-via-draft-verify-ledger-2191689b1909-20260523T215343991739+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b49cd735f64b

## What looked useful

DVL produced zero invalid commits across all tested synthetic conditions, while naive and final-only baselines averaged 2.0358 invalid commits per non-clean condition. DVL average task success across non-clean conditions was 0.4771 versus 0.3520 for baselines, but completion degraded when bad drafts were rejected without repair.

## Boundaries and scale limits

Synthetic simulator only; no LLM drafting, real tool side effects, natural-language verifier, distributed concurrency, or external persistence was tested. The run was CPU-only and completed 1000 trials per condition.

## Claim scope

In a deterministic synthetic stateful task environment, per-action draft verification against a ledger of preconditions, evidence requirements, uniqueness checks, and ordering invariants eliminated invalid commits compared with immediate-commit and final-only baselines.

## Why it stopped

Closed as no-paper useful signal: the result is a synthetic mechanism probe, not direct publication-grade validation of speculative agent verification.

## Recommended next action

Run a bounded real LLM tool-agent trace replay with machine-checkable ledger entries and a repair/resample loop before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Draft-Verify Ledger on Real LLM Tool-Agent Traces
- Success threshold: DVL-plus-repair reduces invalid external commits by >=80% relative to immediate commit and keeps task completion >=80% of the immediate-commit baseline with rejected-valid rate <=10%.
- Stop condition: Stop if rejected-valid rate exceeds 20%, completion falls below 60% of baseline, or invalid commit reduction is below 50% on the first 20 labeled tasks.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-agent-verification-via-draft-verify-ledger-2191689b1909`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
