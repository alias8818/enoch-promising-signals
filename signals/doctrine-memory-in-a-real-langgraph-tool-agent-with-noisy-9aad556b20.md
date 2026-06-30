# Doctrine memory in a real LangGraph tool-agent with noisy verifier feedback

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `doctrine-memory-in-a-real-langgraph-tool-agent-with-noisy-9aad556b20`
Run ID: `doctrine-memory-in-a-real-langgraph-tool-agent-with-noisy-9aad556b20-20260630T121903411539+0000`

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

- Parent run decision: Operator-Doctrine Memory for Local Multi-Step Agents: enoch://control-plane/projects/operator-doctrine-memory-for-local-multi-step-agents-601b36059bc0/runs/operator-doctrine-memory-for-local-multi-step-agents-601b36059bc0-20260630T113654057445+0000
- Parent run decision: Automatic Doctrine Memory in a Real Local Tool-Using Agent Harness: enoch://control-plane/projects/automatic-doctrine-memory-in-a-real-local-tool-using-agent-f8c81079a7/runs/automatic-doctrine-memory-in-a-real-local-tool-using-agent-f8c81079a7-20260630T115803663179+0000

## What looked useful

Doctrine beta late accuracy was 0.728, 0.728, 0.726, and 0.685 at verifier noise 0.00, 0.10, 0.25, and 0.35. Margins over no-memory late accuracy were +0.225, +0.225, +0.224, and +0.182. Margins over naive last-positive memory were +0.007 at zero noise and +0.126, +0.213, and +0.274 once feedback was noisy.

## Boundaries and scale limits

34,560 local CPU-only graph episodes; deterministic simulated agent policy; synthetic arithmetic/string/max tools; controlled binary verifier noise; no LLM-backed agent, real benchmark, human labels, or natural verifier failure modes.

## Claim scope

In a synthetic but real LangGraph Python tool-agent loop with ToolNode execution, InMemorySaver checkpointing, four task families, and Bernoulli-flipped verifier feedback, Beta-count doctrine memory improves late-episode tool accuracy over no memory at all tested noise levels and over naive last-positive memory when verifier noise is nonzero.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but is not direct publication-grade validation for real LLM tool agents or realistic verifier noise.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should replace the deterministic policy with an LLM-backed LangGraph ReAct/tool agent on a small real tool-use benchmark while preserving the same noisy-verifier memory ablations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-backed LangGraph doctrine memory under noisy verifier labels
- Success threshold: Doctrine memory improves late-episode accuracy by at least 10 percentage points over both baselines at 10-30% verifier noise without reducing zero-noise performance by more than 3 percentage points.
- Stop condition: Stop if doctrine memory fails to beat either baseline by at least 5 percentage points in a 500-task smoke/medium run or if verifier noise causes persistent incorrect doctrine lock-in in more than one third of task families.

## Evidence references

- Artifact root: `<local-path>/projects/doctrine-memory-in-a-real-langgraph-tool-agent-with-noisy-9aad556b20`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
