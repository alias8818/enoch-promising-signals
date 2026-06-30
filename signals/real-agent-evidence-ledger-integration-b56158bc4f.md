# Real Agent Evidence Ledger Integration

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-evidence-ledger-integration-b56158bc4f`
Run ID: `real-agent-evidence-ledger-integration-b56158bc4f-20260605T064255162146+0000`

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

- Parent run decision: Tool Agent Evidence Ledger: enoch://control-plane/projects/tool-agent-evidence-ledger-386cc4fd1cc5/runs/tool-agent-evidence-ledger-386cc4fd1cc5-20260605T022444266171+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/96acb1bd8a94

## What looked useful

Across 2,400 trials per mode, the ledger reduced unsupported plus contradicted claims by 100%, improved exact success from 0.4642 to 0.9233, and added 0.2833 tool calls per task on average. Remaining failures were concentrated in cross-file and derived claims where explicit derived-provenance support was missing.

## Boundaries and scale limits

The run used 24 synthetic controlled tasks, 100 seeds, and a deterministic non-LLM agent policy. It did not test real LLM behavior, external tools, long-horizon memory, adversarial evidence, or broad task distributions.

## Claim scope

In a controlled local file-backed agent harness with deterministic fault injection, an evidence-ledger finalization gate eliminated unsupported and contradicted final claims and improved exact success versus the same agent policy without the gate.

## Why it stopped

No-paper closure: controlled direct mechanism evidence is useful, but the run does not provide publication-grade evidence for real LLM agents.

## Recommended next action

Run a bounded deepen follow-up by integrating the ledger gate into an actual LLM/tool agent on a small public hidden-ground-truth file/API task suite with a citation-only baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM Agent Evidence Ledger Gate on Hidden-Ground-Truth Tool Tasks
- Success threshold: At least 50% reduction in unsupported plus contradicted final claims versus both baselines, exact success no more than 5% below the best baseline, and average tool-call overhead no more than 2.0 calls per task.
- Stop condition: Stop if the ledger fails to reduce unsupported plus contradicted claims by at least 25% on the first 25 tasks or if exact success drops more than 10% versus both baselines.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-evidence-ledger-integration-b56158bc4f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
