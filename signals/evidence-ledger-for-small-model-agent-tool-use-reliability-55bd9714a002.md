# Evidence ledger for small-model agent tool-use reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-small-model-agent-tool-use-reliability-55bd9714a002`
Run ID: `evidence-ledger-for-small-model-agent-tool-use-reliability-55bd9714a002-20260608T192141825411+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/1d3749dd7343

## What looked useful

On 5,000 paired trusted-tool trials per scenario, ledger success was 1.0000 versus baseline 0.6442 on price ranking and 1.0000 versus baseline 0.7944 on eligibility actions; unsupported decisions fell to 0.0 from 0.7686 and 0.4536 respectively. A 5% source-fault probe showed the boundary condition: the ledger still improved accuracy but faithfully recorded some bad source data.

## Boundaries and scale limits

Evidence is synthetic/proxy-only: no real small LLM inference, natural-language parsing, external tools, long-horizon tasks, or benchmark diversity. The ledger does not solve corrupted source observations; a 5% tool-fault probe reduced ledger success to 0.982 on price ranking and 0.968 on eligibility actions.

## Claim scope

In a bounded synthetic two-scenario proxy, a structured evidence ledger with required-evidence validation reduced noisy small-agent tool-use failures from skipped calls, memory drops, misreads, premature actions, and wrong-tool routes, at the cost of additional tool calls.

## Why it stopped

Synthetic/proxy-only evidence supports the mechanism but is not direct validation of real small-model agent reliability.

## Recommended next action

Stop this run as a no-paper useful synthetic signal; next bounded action is to run the same evidence-ledger protocol with actual small LLM agents on a held-out tool-use benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence ledger validation with real small LLM tool-use agents
- Success threshold: At least one small model shows a paired unsupported-decision reduction of 30% or more and a success-rate gain of 10 percentage points or more, with mean tool-call overhead no greater than 50% and no increase in unsafe actions.
- Stop condition: Stop if ledger overhead exceeds 50% without at least a 10 percentage point success gain, or if unsupported/unsafe decisions do not improve on both tested models.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-model-agent-tool-use-reliability-55bd9714a002`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
