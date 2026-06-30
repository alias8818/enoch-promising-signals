# Evidence-ledger constraint on real small LLM tool agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-constraint-on-real-small-llm-tool-agents-d24fd420a8`
Run ID: `evidence-ledger-constraint-on-real-small-llm-tool-agents-d24fd420a8-20260604T153201066653+0000`

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

- Parent run decision: Evidence-Ledger Constraint for Small Tool Agents: enoch://control-plane/projects/evidence-ledger-constraint-for-small-tool-agents-3d6795ec11d2/runs/evidence-ledger-constraint-for-small-tool-agents-3d6795ec11d2-20260604T102629225546+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7c5b6c075e7f

## What looked useful

Evidence-ledger enforcement converted misgrounded cited answers into abstentions/blocks: false-accept rate fell from 1.0 in plain and unconstrained ledger variants to 0.0 in the constrained variant, but acceptance rate was also 0.0 and accepted-answer correctness was 0.0.

## Boundaries and scale limits

Single cached 0.5B local instruct model, one prompt family, one repair attempt, five benchmark tasks, CPU-only inference, and task-specific deterministic support checks; no long-horizon agents, production traces, human audit-time study, or larger model sweep.

## Claim scope

On five controlled local file/code QA tasks with Qwen/Qwen2.5-0.5B-Instruct, a verifier-constrained evidence-ledger loop eliminated false accepted answers by blocking unsupported outputs, but accepted no correct final answers and failed the Tier 1 success threshold.

## Why it stopped

The controlled direct test failed the success threshold: the constraint blocked all unsupported outputs but did not produce any accepted correct answers.

## Recommended next action

Stop this run as no-paper useful negative evidence; the next bounded test should use a stronger local small model or improved multi-turn repair protocol and require acceptance_rate >= 0.6 with false_accept_rate = 0.0 on the same tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stronger local repair loop for constrained evidence-ledger agents
- Success threshold: constrained accepted-answer correctness >= 0.8, false-accept rate = 0.0, accepted decoy contamination = 0.0, acceptance rate >= 0.6, and correctness gain vs unconstrained ledger >= 0.4
- Stop condition: Stop if the stronger repair loop still accepts fewer than 3 of 5 tasks or introduces any false accepted answer on the controlled benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-constraint-on-real-small-llm-tool-agents-d24fd420a8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
