# Authenticated multi-agent full-family local trap panel

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `authenticated-multi-agent-full-family-local-trap-panel-e7da28ac73`
Run ID: `authenticated-multi-agent-full-family-local-trap-panel-e7da28ac73-20260612T105257258923+0000`

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

- Parent run decision: Trace real coding agents on the local adversarial trap suite: enoch://control-plane/projects/trace-real-coding-agents-on-the-local-adversarial-trap-sui-1cf5bfb742/runs/trace-real-coding-agents-on-the-local-adversarial-trap-sui-1cf5bfb742-20260612T103705470968+0000
- Parent run decision: Local Adversarial Agent Trap Benchmark: enoch://control-plane/projects/local-adversarial-agent-trap-benchmark-d06b8db45e8b/runs/local-adversarial-agent-trap-benchmark-d06b8db45e8b-20260611T142000338387+0000

## What looked useful

Across 40 paired seeds and 700,000 simulated episodes, altp_full leak rate was 0.0164 versus 1.0000 open_panel, 0.6208 shared_token, and 0.0753 RBAC; attack detection was 0.8546 versus 0.0000 for the three baselines. Ablations showed traps mainly improve detection/incident cost and family binding prevents leaks.

## Boundaries and scale limits

Synthetic simulator only; no LLM agents, real credential stores, OS sandboxing, UI surfaces, persistent adversarial adaptation, or deployed authentication service were tested.

## Claim scope

In a fixed-seed protocol-level simulator of family-partitioned multi-agent panel access, a full authenticated local trap panel reduced cross-family secret leaks versus open access, shared-token access, and RBAC, while local traps improved detection and family binding drove leak prevention.

## Why it stopped

No paper now: this is a medium synthetic protocol confirmation with fixed seeds, baselines, and ablations, but it does not directly validate real authenticated multi-agent systems.

## Recommended next action

Run a bounded local LLM-in-the-loop follow-up with real tool descriptors and a concrete trap-panel implementation to test whether the simulator mechanism survives realistic agent routing and adversarial prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop validation of family-local authenticated trap panels
- Success threshold: Compared with RBAC-only, the local trap panel should improve attack detection by at least 30 percentage points without increasing leak rate and with benign task success no more than 3 percentage points lower.
- Stop condition: Stop if task success drops below 90%, leak rate is not lower than RBAC-only, or trap detection improves by less than 10 percentage points over the global-trap control.

## Evidence references

- Artifact root: `<local-path>/projects/authenticated-multi-agent-full-family-local-trap-panel-e7da28ac73`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
