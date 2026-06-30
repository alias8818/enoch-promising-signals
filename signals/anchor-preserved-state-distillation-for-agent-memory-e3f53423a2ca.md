# Anchor-Preserved State Distillation for Agent Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-preserved-state-distillation-for-agent-memory-e3f53423a2ca`
Run ID: `anchor-preserved-state-distillation-for-agent-memory-e3f53423a2ca-20260601T081912069857+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/51f0628e9d71

## What looked useful

Teacher anchor probes reached 1.000 accuracy. Anchor-preserved distillation improved compressed anchor accuracy by +0.157, +0.279, and +0.456 at bottlenecks 4, 8, and 16 respectively, with positive anchor gains in every seed. It also reduced action accuracy by -0.075, -0.175, and -0.202 and increased normalized MSE, showing a real preservation-versus-behavior tradeoff.

## Boundaries and scale limits

Only synthetic states were tested; no real LLM hidden states, transcript memories, tool-agent traces, long-context tasks, or GPT-2-small-class model training were evaluated. The result is a mechanism probe, not a full validation of agent memory distillation.

## Claim scope

In a synthetic vector-state proxy for agent memory, adding a fixed-probe anchor-preservation loss to bottleneck state distillation improves anchored-fact recall over reconstruction-only distillation across 4 seeds and bottlenecks 4, 8, and 16, but it degrades synthetic action fidelity and reconstruction error.

## Why it stopped

Synthetic proxy produced a useful mechanism signal but also a consistent action-fidelity regression, so this is no-paper evidence rather than publication-grade validation.

## Recommended next action

Run a bounded deepen experiment adding behavior-preserving distillation or a Pareto loss sweep, and continue only if anchor recall improves while action accuracy drops by less than 5 percentage points.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Behavior-Preserving Anchor State Distillation
- Success threshold: Mean anchor accuracy improves by at least 0.15 absolute over baseline across four seeds while mean action accuracy is no more than 0.05 absolute below baseline.
- Stop condition: Stop if every behavior-preserving setting either improves anchor accuracy by less than 0.10 absolute or loses more than 0.05 absolute action accuracy versus baseline.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserved-state-distillation-for-agent-memory-e3f53423a2ca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
